#  AudioPolicy
输入输出设备通过mEngine去直接获取device.  
Android音频策略主要是在 frameworks/av/services/audiopolicy/enginedefault/src/Engine.cpp实现的.
通路如下.
```c
frameworks/av/services/audiopolicy/managerdefault/AudioPolicyManager.cpp
void AudioPolicyManager::updateDevicesAndOutputs()
{
    mEngine->updateDeviceSelectionCache();
    mPreviousOutputs = mOutputs;
}
```
```c
frameworks/av/services/audiopolicy/enginedefault/src/Engine.cpp
void Engine::updateDeviceSelectionCache()
{
    for (const auto &iter : getProductStrategies()) {
        const auto& strategy = iter.second;
        auto devices = getDevicesForProductStrategy(strategy->getId());
        mDevicesForStrategies[strategy->getId()] = devices;
        strategy->setDeviceTypes(devices.types());
        strategy->setDeviceAddress(devices.getFirstValidAddress().c_str());
    }
}

DeviceVector Engine::getDevicesForProductStrategy(product_strategy_t strategy) const {
    const SwAudioOutputCollection& outputs = getApmObserver()->getOutputs();

    // Take context into account to remap product strategy before
    // checking preferred device for strategy and applying default routing rules
    strategy = remapStrategyFromContext(strategy, outputs);

    auto legacyStrategy = mLegacyStrategyMap.find(strategy) != end(mLegacyStrategyMap) ?
                          mLegacyStrategyMap.at(strategy) : STRATEGY_NONE;

    DeviceVector availableOutputDevices = getApmObserver()->getAvailableOutputDevices();

    filterOutputDevicesForStrategy(legacyStrategy, availableOutputDevices, outputs);

    // check if this strategy has a preferred device that is available,
    // if yes, give priority to it.
    DeviceVector preferredAvailableDevVec =
            getPreferredAvailableDevicesForProductStrategy(availableOutputDevices, strategy);
    if (!preferredAvailableDevVec.isEmpty()) {
        return preferredAvailableDevVec;
    }

    return getDevicesForStrategyInt(legacyStrategy,
                                    availableOutputDevices,
                                    outputs);
}

DeviceVector Engine::getDevicesForStrategyInt(legacy_strategy strategy,
                                              DeviceVector availableOutputDevices,
                                              const SwAudioOutputCollection &outputs) const
{
    ...
    //另外深入
}

```

有以下策略:
```c
frameworks/services/audiopolicy/enginedefault/src/Engine.h
enum legacy_strategy {
    STRATEGY_NONE = -1,
    STRATEGY_MEDIA,
    STRATEGY_PHONE,
    STRATEGY_SONIFICATION,
    STRATEGY_SONIFICATION_RESPECTFUL,
    STRATEGY_DTMF,
    STRATEGY_ENFORCED_AUDIBLE,
    STRATEGY_TRANSMITTED_THROUGH_SPEAKER,
    STRATEGY_ACCESSIBILITY,
    STRATEGY_REROUTING,
    STRATEGY_CALL_ASSISTANT,
};
```
有以下输出设备:
```c
system/media/audio/include/system/audio-base-utils.h
// TODO: remove audio device combination as it is not allowed to use as bit mask since R.
enum {
    AUDIO_DEVICE_OUT_ALL      = AUDIO_DEVICE_OUT_EARPIECE |
                                AUDIO_DEVICE_OUT_SPEAKER |
...
// Keep the device arrays in order from low to high as they may be needed to do binary search.
// inline constexpr
static CONST_ARRAY audio_devices_t AUDIO_DEVICE_OUT_ALL_ARRAY[] = {
    AUDIO_DEVICE_OUT_EARPIECE,                  // 0x00000001u// 听筒
    AUDIO_DEVICE_OUT_SPEAKER,                   // 0x00000002u// 外放
    AUDIO_DEVICE_OUT_WIRED_HEADSET,             // 0x00000004u// 线控耳机,可以通过耳机控制远端播放、暂停、音量调节等功能的耳机
    AUDIO_DEVICE_OUT_WIRED_HEADPHONE,           // 0x00000008u// 普通耳机,只能听,不能操控播放
    AUDIO_DEVICE_OUT_BLUETOOTH_SCO,             // 0x00000010u// 单声道蓝牙耳机,十进制16
    AUDIO_DEVICE_OUT_BLUETOOTH_SCO_HEADSET,     // 0x00000020u/ 车载免提蓝牙设备,十进制32
    AUDIO_DEVICE_OUT_BLUETOOTH_SCO_CARKIT,      // 0x00000040u// 立体声蓝牙耳机,十进制64
    AUDIO_DEVICE_OUT_BLUETOOTH_A2DP,            // 0x00000080u// 蓝牙耳机
    AUDIO_DEVICE_OUT_BLUETOOTH_A2DP_HEADPHONES, // 0x00000100u// 十进制256
    AUDIO_DEVICE_OUT_BLUETOOTH_A2DP_SPEAKER,    // 0x00000200u// 十进制512
    AUDIO_DEVICE_OUT_HDMI,                      // 0x00000400u, OUT_AUX_DIGITAL// HDMI输出
    AUDIO_DEVICE_OUT_ANLG_DOCK_HEADSET,         // 0x00000800u// 十进制2048
    AUDIO_DEVICE_OUT_DGTL_DOCK_HEADSET,         // 0x00001000u// 十进制4096
    AUDIO_DEVICE_OUT_USB_ACCESSORY,             // 0x00002000u
    AUDIO_DEVICE_OUT_USB_DEVICE,                // 0x00004000u// USB设备
    AUDIO_DEVICE_OUT_REMOTE_SUBMIX,             // 0x00008000u
    AUDIO_DEVICE_OUT_TELEPHONY_TX,              // 0x00010000u
    AUDIO_DEVICE_OUT_LINE,                      // 0x00020000u
    AUDIO_DEVICE_OUT_HDMI_ARC,                  // 0x00040000u
    AUDIO_DEVICE_OUT_HDMI_EARC,                 // 0x00040001u,
    AUDIO_DEVICE_OUT_SPDIF,                     // 0x00080000u
    AUDIO_DEVICE_OUT_FM,                        // 0x00100000u
    AUDIO_DEVICE_OUT_AUX_LINE,                  // 0x00200000u
    AUDIO_DEVICE_OUT_SPEAKER_SAFE,              // 0x00400000u
    AUDIO_DEVICE_OUT_IP,                        // 0x00800000u
    AUDIO_DEVICE_OUT_BUS,                       // 0x01000000u
    AUDIO_DEVICE_OUT_PROXY,                     // 0x02000000u
    AUDIO_DEVICE_OUT_USB_HEADSET,               // 0x04000000u
    AUDIO_DEVICE_OUT_HEARING_AID,               // 0x08000000u
    AUDIO_DEVICE_OUT_ECHO_CANCELLER,            // 0x10000000u
    AUDIO_DEVICE_OUT_BLE_HEADSET,               // 0x20000000u
    AUDIO_DEVICE_OUT_BLE_SPEAKER,               // 0x20000001u
    AUDIO_DEVICE_OUT_BLE_BROADCAST,             // 0x20000002u
    AUDIO_DEVICE_OUT_DEFAULT,                   // 0x40000000u, BIT_DEFAULT
};

```
## 1. 音频输出策略
音频输出策略是在Engine::getDeviceForStrategyInt这个函数里面.  
通过 getFirstDevicesFromTypes 选择, devices.add()可以支持多个设备.
```c
frameworks/av/services/audiopolicy/enginedefault/src/Engine.cpp
@line264
DeviceVector Engine::getDevicesForStrategyInt(legacy_strategy strategy,
                                              DeviceVector availableOutputDevices,
                                              const SwAudioOutputCollection &outputs) const
{
    DeviceVector devices;

    switch (strategy) {
    //播放声音时这里负责选择合适的音频输出策略
    case STRATEGY_TRANSMITTED_THROUGH_SPEAKER:
        devices = availableOutputDevices.getDevicesFromType(AUDIO_DEVICE_OUT_SPEAKER);
        break;

    case STRATEGY_PHONE: {
        ...
        //语音通话的声音输出走这个策略(进行腾讯会议或者打电话通话）
    } break;

    case STRATEGY_SONIFICATION:
    case STRATEGY_ENFORCED_AUDIBLE:
        // strategy STRATEGY_ENFORCED_AUDIBLE uses same routing policy as STRATEGY_SONIFICATION
        // except:
        //   - when in call where it doesn't default to STRATEGY_PHONE behavior
        //   - in countries where not enforced in which case it follows STRATEGY_MEDIA

        ...

        // if SCO headset is connected and we are told to use it, play ringtone over
        // speaker and BT SCO,外放与蓝牙SCO同时播放
        if (!availableOutputDevices.getDevicesFromTypes(getAudioDeviceOutAllScoSet()).isEmpty()) {
            DeviceVector devices2;
            devices2 = availableOutputDevices.getFirstDevicesFromTypes({
                    AUDIO_DEVICE_OUT_BLUETOOTH_SCO_CARKIT, AUDIO_DEVICE_OUT_BLUETOOTH_SCO_HEADSET,
                    AUDIO_DEVICE_OUT_BLUETOOTH_SCO});
            // Use ONLY Bluetooth SCO output when ringing in vibration mode
            if (!((getForceUse(AUDIO_POLICY_FORCE_FOR_SYSTEM) == AUDIO_POLICY_FORCE_SYSTEM_ENFORCED)
                    && (strategy == STRATEGY_ENFORCED_AUDIBLE))) {
                if (getForceUse(AUDIO_POLICY_FORCE_FOR_VIBRATE_RINGING)
                        == AUDIO_POLICY_FORCE_BT_SCO) {
                    if (!devices2.isEmpty()) {
                        devices = devices2;
                        break;
                    }
                }
            }
            // Use both Bluetooth SCO and phone default output when ringing in normal mode
            if (audio_is_bluetooth_out_sco_device(getPreferredDeviceTypeForLegacyStrategy(
                    availableOutputDevices, STRATEGY_PHONE))) {
                if (strategy == STRATEGY_SONIFICATION) {
                    devices.replaceDevicesByType(
                            AUDIO_DEVICE_OUT_SPEAKER,
                            availableOutputDevices.getDevicesFromType(
                                    AUDIO_DEVICE_OUT_SPEAKER_SAFE));
                }
                if (!devices2.isEmpty()) {
                    devices.add(devices2);
                    break;
                }
            }
        }
        // if display-port is connected and being used in voice usecase,
        // play ringtone over speaker and display-port
        if ((strategy == STRATEGY_SONIFICATION) && getDpConnAndAllowedForVoice()) {
             DeviceVector devices2 = availableOutputDevices.getDevicesFromType(
                 AUDIO_DEVICE_OUT_AUX_DIGITAL);
             if (!devices2.isEmpty()) {
               devices.add(devices2);
               break;
             }
        }
        // The second device used for sonification is the same as the device used by media strategy
        FALLTHROUGH_INTENDED;
    ...
    case STRATEGY_MEDIA: {         
        //播放媒体声音时走的策略
        ...
        } break;
 
    case STRATEGY_CALL_ASSISTANT:
        devices = availableOutputDevices.getDevicesFromType(AUDIO_DEVICE_OUT_TELEPHONY_TX);
        break;

    case STRATEGY_NONE:
        // Happens when internal strategies are processed ("rerouting", "patch"...)
        break;

    default:
        ALOGW("%s unknown strategy: %d", __func__, strategy);
        break;
    }

    ...

    ALOGVV("%s strategy %d, device %s", __func__,
           strategy, dumpDeviceTypes(devices.types()).c_str());
    return devices;
}
``` 

## 2. 音频输入策略
音频输入策略是在Engine::getDeviceForInputSource 这个函数里面. 最终是通过 getFirstExistingDevice 去选择.
```c
frameworks/av/services/audiopolicy/enginedefault/src/Engine.cpp
@line520
sp<DeviceDescriptor> Engine::getDeviceForInputSource(audio_source_t inputSource) const
{
    const DeviceVector availableOutputDevices = getApmObserver()->getAvailableOutputDevices();
    const DeviceVector availableInputDevices = getApmObserver()->getAvailableInputDevices();
    const SwAudioOutputCollection &outputs = getApmObserver()->getOutputs();
    DeviceVector availableDevices = availableInputDevices;
    sp<AudioOutputDescriptor> primaryOutput = outputs.getPrimaryOutput();
    DeviceVector availablePrimaryDevices = primaryOutput == nullptr ? DeviceVector()
            : availableInputDevices.getDevicesFromHwModule(primaryOutput->getModuleHandle());
    sp<DeviceDescriptor> device;

    // when a call is active, force device selection to match source VOICE_COMMUNICATION
    // for most other input sources to avoid rerouting call TX audio
    if (isInCall()) {
        switch (inputSource) {
        case AUDIO_SOURCE_DEFAULT:
        case AUDIO_SOURCE_MIC:  //一般会走到这里
        case AUDIO_SOURCE_VOICE_RECOGNITION:
        case AUDIO_SOURCE_UNPROCESSED:
        case AUDIO_SOURCE_HOTWORD:
        case AUDIO_SOURCE_CAMCORDER:
        case AUDIO_SOURCE_VOICE_PERFORMANCE:
        case AUDIO_SOURCE_ULTRASOUND:
            inputSource = AUDIO_SOURCE_VOICE_COMMUNICATION;
            break;
        default:
            break;
        }
    }

    audio_devices_t commDeviceType =
        getPreferredDeviceTypeForLegacyStrategy(availableOutputDevices, STRATEGY_PHONE);

    switch (inputSource) {
    case AUDIO_SOURCE_DEFAULT:
    case AUDIO_SOURCE_MIC:
        if (property_get_bool("vendor.audio.enable.mirrorlink", false)) {
            device = availableDevices.getDevice(
                    AUDIO_DEVICE_IN_REMOTE_SUBMIX, String8(""), AUDIO_FORMAT_DEFAULT);
            if (device != nullptr) break;
        }
        device = availableDevices.getDevice(
                AUDIO_DEVICE_IN_BLUETOOTH_A2DP, String8(""), AUDIO_FORMAT_DEFAULT);
        if (device != nullptr) break;
        if (audio_is_bluetooth_out_sco_device(commDeviceType)) {
            device = availableDevices.getDevice(
                    AUDIO_DEVICE_IN_BLUETOOTH_SCO_HEADSET, String8(""), AUDIO_FORMAT_DEFAULT);
            if (device != nullptr) break;
        }
        device = availableDevices.getFirstExistingDevice({
                AUDIO_DEVICE_IN_WIRED_HEADSET,
                AUDIO_DEVICE_IN_USB_HEADSET, AUDIO_DEVICE_IN_USB_DEVICE,
                AUDIO_DEVICE_IN_BLUETOOTH_BLE, AUDIO_DEVICE_IN_BUILTIN_MIC});
                //从列表里面看出圆孔耳机和USB耳机的优先级是要比 BUILTIN_MIC(麦克风)高
        break;
 
    case AUDIO_SOURCE_VOICE_COMMUNICATION: 
        //进行腾讯会议这类型语音通话类的app进行声音输入时走的策略
        // Allow only use of devices on primary input if in call and HAL does not support routing
        // to voice call path.
        if ((getPhoneState() == AUDIO_MODE_IN_CALL) &&
                (availableOutputDevices.getDevice(AUDIO_DEVICE_OUT_TELEPHONY_TX,
                        String8(""), AUDIO_FORMAT_DEFAULT)) == nullptr) {
            LOG_ALWAYS_FATAL_IF(availablePrimaryDevices.isEmpty(), "Primary devices not found");
            availableDevices = availablePrimaryDevices;
        }

        if (audio_is_bluetooth_out_sco_device(commDeviceType)) {
            // if SCO device is requested but no SCO device is available, fall back to default case
            device = availableDevices.getDevice(
                    AUDIO_DEVICE_IN_BLUETOOTH_SCO_HEADSET, String8(""), AUDIO_FORMAT_DEFAULT);
            if (device != nullptr) {
                break;
            }
        }
        switch (commDeviceType) {
        case AUDIO_DEVICE_OUT_BLE_HEADSET:
            device = availableDevices.getDevice(
                    AUDIO_DEVICE_IN_BLE_HEADSET, String8(""), AUDIO_FORMAT_DEFAULT);
            break;
        case AUDIO_DEVICE_OUT_SPEAKER:
            device = availableDevices.getFirstExistingDevice({
                    AUDIO_DEVICE_IN_BACK_MIC, AUDIO_DEVICE_IN_BUILTIN_MIC,
                    AUDIO_DEVICE_IN_USB_DEVICE, AUDIO_DEVICE_IN_USB_HEADSET});
            break;
        default:    // FORCE_NONE
            device = availableDevices.getFirstExistingDevice({
                    AUDIO_DEVICE_IN_WIRED_HEADSET, AUDIO_DEVICE_IN_USB_HEADSET,
                    AUDIO_DEVICE_IN_USB_DEVICE, AUDIO_DEVICE_IN_BLUETOOTH_BLE,
                    AUDIO_DEVICE_IN_BUILTIN_MIC});
                    //起决定性作用,如果想要修改顺序,调整列表里的设备即可
            break;

        }
        break;

    ...
    return device;
}
```

[AudioOnAndroid](AudioOnAndroid.md)