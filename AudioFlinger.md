# AudioFlinger
```c
AuidoTrack.java → android_media_AudioTrack.cpp → AudioTrack.cpp → AudioFlinger.cpp
AudioRecord.java → android_media_AudioRecord.cpp → AudioRecord.cpp → AudioFlinger.cpp
AuidoSystem.java → android_media_AudioSystem.cpp → AudioSystem.cpp → AudioFlinger.cpp
```
上面三个类的代码走向, 最终都会走向同一个类 AudioFlinger.  
AudioFlinger 是音频管理器,可以把它理解为代理,它代理了音频上层来的所有事物.
AudioFlinger 可以创造真正用于功能的 track 和 recorder.

## AudioFlinger 初始化

首先从 audioserver 开始, audioserver 是放在framework/av/media下面,它只有三个文件 Andoird.bp,audioserver.rc,main_audioserver.cpp,这个模块是开机就开始运行.
audioserver.rc 在开机的时候会被系统的init进程所加载,接着启动audioserver,也就是main_audioserver.cpp,
然后在audioserver的main函数中就启动了AudioFlinger、AudioPolicyService,分别调用了它们的 instantiate()函数.
```c
frameworks/av/services/audioflinger/AudioFlinger.cpp
 
void AudioFlinger::instantiate() {
    sp<IServiceManager> sm(defaultServiceManager());
    sm->addService(String16(IAudioFlinger::DEFAULT_SERVICE_NAME),                      // -------- 1
                   new AudioFlingerServerAdapter(new AudioFlinger()), false,
                   IServiceManager::DUMP_FLAG_PRIORITY_DEFAULT);
}
 
AudioFlinger::AudioFlinger()
    : mMediaLogNotifier(new AudioFlinger::MediaLogNotifier()),
      mPrimaryHardwareDev(NULL),
      mAudioHwDevs(NULL),
      mHardwareStatus(AUDIO_HW_IDLE),
      mMasterVolume(1.0f),
      mMasterMute(false),
      // mNextUniqueId(AUDIO_UNIQUE_ID_USE_MAX),
      mMode(AUDIO_MODE_INVALID),
      mBtNrecIsOff(false),
      mIsLowRamDevice(true),
      mIsDeviceTypeKnown(false),
      mTotalMemory(0),
      mClientSharedHeapSize(kMinimumClientSharedHeapSizeBytes),
      mGlobalEffectEnableTime(0),
      mPatchPanel(this),
      mDeviceEffectManager(this),
      mSystemReady(false)
{
    // Move the audio session unique ID generator start base as time passes to limit risk of
    // generating the same ID again after an audioserver restart.
    // This is important because clients will reuse previously allocated audio session IDs
    // when reconnecting after an audioserver restart and newly allocated IDs may conflict with
    // active clients.
    // Moving the base by 1 for each elapsed second is a good compromise between avoiding overlap
    // between allocation ranges and not reaching wrap around too soon.
    timespec ts{};
    clock_gettime(CLOCK_MONOTONIC, &ts);
    // zero ID has a special meaning, so start allocation at least at AUDIO_UNIQUE_ID_USE_MAX
    uint32_t movingBase = (uint32_t)std::max((long)1, ts.tv_sec);
    // unsigned instead of audio_unique_id_use_t, because ++ operator is unavailable for enum
    for (unsigned use = AUDIO_UNIQUE_ID_USE_UNSPECIFIED; use < AUDIO_UNIQUE_ID_USE_MAX; use++) {
        mNextUniqueIds[use] =
                ((use == AUDIO_UNIQUE_ID_USE_SESSION || use == AUDIO_UNIQUE_ID_USE_CLIENT) ?
                        movingBase : 1) * AUDIO_UNIQUE_ID_USE_MAX;
    }
 
#if 1
    // FIXME See bug 165702394 and bug 168511485
    const bool doLog = false;
#else
    const bool doLog = property_get_bool("ro.test_harness", false);
#endif
    if (doLog) {
        mLogMemoryDealer = new MemoryDealer(kLogMemorySize, "LogWriters",
                MemoryHeapBase::READ_ONLY);
        (void) pthread_once(&sMediaLogOnce, sMediaLogInit);
    }
 
    // reset battery stats.
    // if the audio service has crashed, battery stats could be left
    // in bad state, reset the state upon service start.
    BatteryNotifier::getInstance().noteResetAudio();
 
    mDevicesFactoryHal = DevicesFactoryHalInterface::create();                          //--------  2
    mEffectsFactoryHal = EffectsFactoryHalInterface::create();                          //--------  3
 
    mMediaLogNotifier->run("MediaLogNotifier");
    std::vector<pid_t> halPids;
    mDevicesFactoryHal->getHalPids(&halPids);
    TimeCheck::setAudioHalPids(halPids);
 
    // Notify that we have started (also called when audioserver service restarts)
    mediametrics::LogItem(mMetricsId)
        .set(AMEDIAMETRICS_PROP_EVENT, AMEDIAMETRICS_PROP_EVENT_VALUE_CTOR)
        .record();
}
```
AuidoFlinger 的初始化,先是把自己包装之后加入到了 servicemanager 中,这里主要用于native 层通过binder和AudioFlinger进行数据交换,
然后是初始化了两个很重要的接口, DevicesFactoryHalInterface 和 EffectsFactoryHalInterface,
这两个接口是用于连接HAL层的主要接口类,负责与HAL层的数据交换,这里与HAL层的数据交换同样使用的Binder机制,学名HIDL一种跨进程通信方式.

那先来看下他们做了什么,以 DevicesFactoryHalInterface 为例,窥探一下 DevicesFactoryHalInterface.create 后面的代码
```c
frameworks/av/media/libaudiohal/DevicesFactoryHalInterface.cpp
 
// static
sp<DevicesFactoryHalInterface> DevicesFactoryHalInterface::create() {               //这里create 直接链接到下一个类的函数 createPreferredImpl,传递了两个参数一个是包名另一个是AIDL 的代理类
    using namespace std::string_literals;
    return createPreferredImpl<DevicesFactoryHalInterface>(
            std::make_pair("android.hardware.audio"s, "IDevicesFactory"s),
            std::make_pair("android.hardware.audio.effect"s, "IEffectsFactory"s));
}
```
```c
frameworks/av/media/libaudiohal/FactoryHalHidl.cpp
void* createPreferredImpl(const InterfaceName& iface, const InterfaceName& siblingIface) {          //遍历了一个保存HAL版本的数组,并判断当前处于哪个版本,如果找到有这个版本则创建这个版本的代理接口
    auto findMostRecentVersion = [](const InterfaceName& iface) {
        return std::find_if(detail::sAudioHALVersions.begin(), detail::sAudioHALVersions.end(),     //遍历HAL版本数组
                [&](const auto& v) { return hasHalService(iface.first, v.second, iface.second); });
    };
    auto ifaceVersionIt = findMostRecentVersion(iface);
    auto siblingVersionIt = findMostRecentVersion(siblingIface);
    if (ifaceVersionIt != detail::sAudioHALVersions.end() &&
            siblingVersionIt != detail::sAudioHALVersions.end() &&
            // same major version
            ifaceVersionIt->first.first == siblingVersionIt->first.first) {
        std::string libraryVersion =
                ifaceVersionIt->first >= siblingVersionIt->first ?
                ifaceVersionIt->second : siblingVersionIt->second;
        void* rawInterface;
        if (createHalService(libraryVersion, iface.second, &rawInterface)) {                        //创建对应版本的HAL代理接口
            return rawInterface;
        }
    }
    return nullptr;
}

bool createHalService(const std::string& version, const std::string& interface,
        void** rawInterface) {
    const std::string libName = "libaudiohal@" + version + ".so";   //组装了一个libaudiohal@x.x.so字符串,一个库,x.x就是刚才遍历到的版本储存在sAudioHALVersions中
    const std::string factoryFunctionName = "create" + interface;
    constexpr int dlMode = RTLD_LAZY;
    void* handle = nullptr;
    dlerror(); // clear
    handle = dlopen(libName.c_str(), dlMode);                       //加载库libaudiohal@x.x.so
    if (handle == nullptr) {
        const char* error = dlerror();
        ALOGE("Failed to dlopen %s: %s", libName.c_str(),
                error != nullptr ? error : "unknown error");
        return false;
    }
    void* (*factoryFunction)();
    *(void **)(&factoryFunction) = dlsym(handle, factoryFunctionName.c_str());  //获取库libaudiohal@x.x.so中的 createIDevicesFactory 函数指针
    if (!factoryFunction) {
        const char* error = dlerror();
        ALOGE("Factory function %s not found in library %s: %s",
                factoryFunctionName.c_str(), libName.c_str(),
                error != nullptr ? error : "unknown error");
        dlclose(handle);
        return false;
    }
    *rawInterface = (*factoryFunction)();                                       //调用了 createIDevicesFactory 函数并返回了rawInterface,这个rawInterface最终是要返回到调用 DevicesFactoryHalInterface.create 的地方
    ALOGW_IF(!*rawInterface, "Factory function %s from %s returned nullptr",
            factoryFunctionName.c_str(), libName.c_str());
    return true;
}
```
通过上面几段代码的跟踪和分析,发现 DevicesFactoryHalInterface.create 其实只是去打开了一个libaudiohal@x.x.so的库,并且调用了它的函数 createIDevicesFactory 获取了其返回值,
这个库的源码是在framewrok/av/media/libaudiohal/impl/DevicesFactoryHalHidl.cpp

```c
framewrok/av/media/libaudiohal/impl/DevicesFactoryHalHidl.cpp
extern "C" __attribute__((visibility("default"))) void* createIDevicesFactory() {   //这个函数的调用实际上是构建了DevicesFactoryHalHybrid并且把它返回给了调用者
    auto service = hardware::audio::CPP_VERSION::IDevicesFactory::getService();
    return service ? new DevicesFactoryHalHidl(service) : nullptr;
}

status_t DevicesFactoryHalHidl::openDevice(const char *name, sp<DeviceHalInterface> *device) { //打开HAL层的一些设备,这里设备有几种类型:primary,a2dp,usb,r_submix,stub,我们主要使用的是primary
    auto factories = copyDeviceFactories();
    if (factories.empty()) return NO_INIT;
    status_t status;
    auto hidlId = idFromHal(name, &status);
    if (status != OK) return status;
    Result retval = Result::NOT_INITIALIZED;
    ...
} 
```
## AudioFlinger 实现
上层调用的三步到达AudioFlinger之后做了什么,以 track 为例.

第一步,代码到达了 AudioFlinger.createTrack
```c
frameworks/av/services/audioflinger/AudioFlinger.cpp
status_t AudioFlinger::createTrack(const media::CreateTrackRequest& _input,
                                   media::CreateTrackResponse& _output)
{
    // Local version of VALUE_OR_RETURN, specific to this method's calling conventions.
    CreateTrackInput input = VALUE_OR_RETURN_STATUS(CreateTrackInput::fromAidl(_input));
    CreateTrackOutput output;
 
    sp<PlaybackThread::Track> track;
    sp<TrackHandle> trackHandle;
    sp<Client> client;
    status_t lStatus;
    audio_stream_type_t streamType;
    audio_port_handle_t portId = AUDIO_PORT_HANDLE_NONE;
    std::vector<audio_io_handle_t> secondaryOutputs;
    ...
 
    output.sessionId = sessionId;
    output.outputId = AUDIO_IO_HANDLE_NONE;
    output.selectedDeviceId = input.selectedDeviceId;
    //创建Track,并且保存在了一个数组中,获取Output
    lStatus = AudioSystem::getOutputForAttr(&localAttr, &output.outputId, sessionId, &streamType,
                                            adjAttributionSource, &input.config, input.flags,
                                            &output.selectedDeviceId, &portId, &secondaryOutputs);       
 
 
    ...
 
    {
        Mutex::Autolock _l(mLock);
        PlaybackThread *thread = checkPlaybackThread_l(output.outputId);    //获取playback数组
        if (thread == NULL) {
            ALOGE("no playback thread found for output handle %d", output.outputId);
            lStatus = BAD_VALUE;
            goto Exit;
        }
 
        ...
        ALOGV("createTrack() sessionId: %d", sessionId);
 
        output.sampleRate = input.config.sample_rate;
        output.frameCount = input.frameCount;
        output.notificationFrameCount = input.notificationFrameCount;
        output.flags = input.flags;
        output.streamType = streamType;
 
        track = thread->createTrack_l(client, streamType, localAttr, &output.sampleRate,
                                      input.config.format, input.config.channel_mask,
                                      &output.frameCount, &output.notificationFrameCount,
                                      input.notificationsPerBuffer, input.speed,
                                      input.sharedBuffer, sessionId, &output.flags,
                                      callingPid, adjAttributionSource, input.clientInfo.clientTid,
                                      &lStatus, portId, input.audioTrackCallback);
        LOG_ALWAYS_FATAL_IF((lStatus == NO_ERROR) && (track == 0));
        // we don't abort yet if lStatus != NO_ERROR; there is still work to be done regardless
 
        output.afFrameCount = thread->frameCount();
        output.afSampleRate = thread->sampleRate();
        output.afLatencyMs = thread->latency();
        output.portId = portId;
 
        ...
 
        setAudioHwSyncForSession_l(thread, sessionId);
    }
 
    ...
 
    output.audioTrack = new TrackHandle(track);
    _output = VALUE_OR_FATAL(output.toAidl());
 
Exit:
    if (lStatus != NO_ERROR && output.outputId != AUDIO_IO_HANDLE_NONE) {
        AudioSystem::releaseOutput(portId);
    }
    return lStatus;
}
```
createTrack代码, 根据 input 调用 PlaybackThread 创建 Track,  然后返回 output.  
返回的 audioTrack 不是真的 Track 而是 TrackHandle 代理.  
首先是通过 AudioSystem 中转调用 AudioPolicyInterfaceImpl 中的 getOutputForAttr,  
然后再到 AudioPolicyManager 的 getOutputForAttrInt.
```c
frameworks/av/services/audiopolicy/managerdefault/AudioPolicyManager.cpp
status_t AudioPolicyManager::getOutputForAttrInt(
        audio_attributes_t *resultAttr,
        audio_io_handle_t *output,
        audio_session_t session,
        const audio_attributes_t *attr,
        audio_stream_type_t *stream,
        uid_t uid,
        const audio_config_t *config,
        audio_output_flags_t *flags,
        audio_port_handle_t *selectedDeviceId,
        bool *isRequestedDeviceForExclusiveUse,
        std::vector<sp<AudioPolicyMix>> *secondaryMixes,
        output_type_t *outputType)
{
    DeviceVector outputDevices;
    const audio_port_handle_t requestedPortId = *selectedDeviceId;
    DeviceVector msdDevices = getMsdAudioOutDevices();
    const sp<DeviceDescriptor> requestedDevice =
        mAvailableOutputDevices.getDeviceFromId(requestedPortId);
 
    *outputType = API_OUTPUT_INVALID;
    status_t status = getAudioAttributes(resultAttr, attr, *stream);
    if (status != NO_ERROR) {
        return status;
    }
    if (auto it = mAllowedCapturePolicies.find(uid); it != end(mAllowedCapturePolicies)) {
        resultAttr->flags = static_cast<audio_flags_mask_t>(resultAttr->flags | it->second);
    }
    *stream = mEngine->getStreamTypeForAttributes(*resultAttr);
 
    ALOGV("%s() attributes=%s stream=%s session %d selectedDeviceId %d", __func__,
          toString(*resultAttr).c_str(), toString(*stream).c_str(), session, requestedPortId);
 
    // The primary output is the explicit routing (eg. setPreferredDevice) if specified,
    //       otherwise, fallback to the dynamic policies, if none match, query the engine.
    // Secondary outputs are always found by dynamic policies as the engine do not support them
    sp<AudioPolicyMix> primaryMix;
    status = mPolicyMixes.getOutputForAttr(*resultAttr, uid, *flags, primaryMix, secondaryMixes);
    if (status != OK) {
        return status;
    }
 
    // Explicit routing is higher priority then any dynamic policy primary output
    bool usePrimaryOutputFromPolicyMixes = requestedDevice == nullptr && primaryMix != nullptr;
 
    // FIXME: in case of RENDER policy, the output capabilities should be checked
    if ((usePrimaryOutputFromPolicyMixes
            || (secondaryMixes != nullptr && !secondaryMixes->empty()))
        && !audio_is_linear_pcm(config->format)) {
        ALOGD("%s: rejecting request as dynamic audio policy only support pcm", __func__);
        return BAD_VALUE;
    }
    if (usePrimaryOutputFromPolicyMixes) {
        sp<DeviceDescriptor> deviceDesc =
                mAvailableOutputDevices.getDevice(primaryMix->mDeviceType,
                                                  primaryMix->mDeviceAddress,
                                                  AUDIO_FORMAT_DEFAULT);
        sp<SwAudioOutputDescriptor> policyDesc = primaryMix->getOutput();
        if (deviceDesc != nullptr
                && (policyDesc == nullptr || (policyDesc->mFlags & AUDIO_OUTPUT_FLAG_DIRECT))) {
            audio_io_handle_t newOutput;
            status = openDirectOutput(                                                     //---------------------         1
                    *stream, session, config,
                    (audio_output_flags_t)(*flags | AUDIO_OUTPUT_FLAG_DIRECT),
                    DeviceVector(deviceDesc), &newOutput);
            if (status != NO_ERROR) {
                policyDesc = nullptr;
            } else {
                policyDesc = mOutputs.valueFor(newOutput);
                primaryMix->setOutput(policyDesc);
            }
        }
        if (policyDesc != nullptr) {
            policyDesc->mPolicyMix = primaryMix;
            *output = policyDesc->mIoHandle;
            *selectedDeviceId = deviceDesc != 0 ? deviceDesc->getId() : AUDIO_PORT_HANDLE_NONE;
 
            ALOGV("getOutputForAttr() returns output %d", *output);
            if (resultAttr->usage == AUDIO_USAGE_VIRTUAL_SOURCE) {
                *outputType = API_OUT_MIX_PLAYBACK;
            } else {
                *outputType = API_OUTPUT_LEGACY;
            }
            return NO_ERROR;
        }
    }
    // Virtual sources must always be dynamicaly or explicitly routed
    if (resultAttr->usage == AUDIO_USAGE_VIRTUAL_SOURCE) {
        ALOGW("getOutputForAttr() no policy mix found for usage AUDIO_USAGE_VIRTUAL_SOURCE");
        return BAD_VALUE;
    }
    // explicit routing managed by getDeviceForStrategy in APM is now handled by engine
    // in order to let the choice of the order to future vendor engine
    outputDevices = mEngine->getOutputDevicesForAttributes(*resultAttr, requestedDevice, false);
 
    if ((resultAttr->flags & AUDIO_FLAG_HW_AV_SYNC) != 0) {
        *flags = (audio_output_flags_t)(*flags | AUDIO_OUTPUT_FLAG_HW_AV_SYNC);
    }
 
    // Set incall music only if device was explicitly set, and fallback to the device which is
    // chosen by the engine if not.
    // FIXME: provide a more generic approach which is not device specific and move this back
    // to getOutputForDevice.
    // TODO: Remove check of AUDIO_STREAM_MUSIC once migration is completed on the app side.
    if (outputDevices.onlyContainsDevicesWithType(AUDIO_DEVICE_OUT_TELEPHONY_TX) &&
        (*stream == AUDIO_STREAM_MUSIC  || resultAttr->usage == AUDIO_USAGE_VOICE_COMMUNICATION) &&
        audio_is_linear_pcm(config->format) &&
        isCallAudioAccessible()) {
        if (requestedPortId != AUDIO_PORT_HANDLE_NONE) {
            *flags = (audio_output_flags_t)AUDIO_OUTPUT_FLAG_INCALL_MUSIC;
            *isRequestedDeviceForExclusiveUse = true;
        }
    }
 
    ALOGV("%s() device %s, sampling rate %d, format %#x, channel mask %#x, flags %#x stream %s",
          __func__, outputDevices.toString().c_str(), config->sample_rate, config->format,
          config->channel_mask, *flags, toString(*stream).c_str());
 
    *output = AUDIO_IO_HANDLE_NONE;
    if (!msdDevices.isEmpty()) {
        *output = getOutputForDevices(msdDevices, session, *stream, config, flags);                         //------------   2
        if (*output != AUDIO_IO_HANDLE_NONE && setMsdOutputPatches(&outputDevices) == NO_ERROR) {
            ALOGV("%s() Using MSD devices %s instead of devices %s",
                  __func__, msdDevices.toString().c_str(), outputDevices.toString().c_str());
        } else {
            *output = AUDIO_IO_HANDLE_NONE;
        }
    }
    if (*output == AUDIO_IO_HANDLE_NONE) {
        *output = getOutputForDevices(outputDevices, session, *stream, config,                              //-------------     3
                flags, resultAttr->flags & AUDIO_FLAG_MUTE_HAPTIC);
    }
    if (*output == AUDIO_IO_HANDLE_NONE) {
        return INVALID_OPERATION;
    }
 
    *selectedDeviceId = getFirstDeviceId(outputDevices);
    for (auto &outputDevice : outputDevices) {
        if (outputDevice->getId() == getConfig().getDefaultOutputDevice()->getId()) {
            *selectedDeviceId = outputDevice->getId();
            break;
        }
    }
 
    if (outputDevices.onlyContainsDevicesWithType(AUDIO_DEVICE_OUT_TELEPHONY_TX)) {
        *outputType = API_OUTPUT_TELEPHONY_TX;
    } else {
        *outputType = API_OUTPUT_LEGACY;
    }
 
    ALOGV("%s returns output %d selectedDeviceId %d", __func__, *output, *selectedDeviceId);
 
    return NO_ERROR;
}
```
这段getOutputForAttrInt()代码目的就一个获取 output,上面代码标记的三处分别对应的不同情况,最终都是要用到 openDirectOutput,接着看 openDirectOutput.
```c
frameworks/av/services/audiopolicy/managerdefault/AudioPolicyManager.cpp
status_t AudioPolicyManager::openDirectOutput(audio_stream_type_t stream,
                                              audio_session_t session,
                                              const audio_config_t *config,
                                              audio_output_flags_t flags,
                                              const DeviceVector &devices,
                                              audio_io_handle_t *output) {
 
    *output = AUDIO_IO_HANDLE_NONE;
 
    // skip direct output selection if the request can obviously be attached to a mixed output
    // and not explicitly requested
    if (((flags & AUDIO_OUTPUT_FLAG_DIRECT) == 0) &&
            audio_is_linear_pcm(config->format) && config->sample_rate <= SAMPLE_RATE_HZ_MAX &&
            audio_channel_count_from_out_mask(config->channel_mask) <= 2) {
        return NAME_NOT_FOUND;
    }
 
    // Do not allow offloading or direct if one non offloadable effect is enabled or
    // MasterMono is enabled. This prevents creating an offloaded or direct track
    // and tearing it down immediately after start when audioflinger detects there
    // is an active non offloadable effect.
    // FIXME: We should check the audio session here but we do not have it in this context.
    // This may prevent offloading in rare situations where effects are left active by apps
    // in the background.
    sp<IOProfile> profile;
    if (((flags & (AUDIO_OUTPUT_FLAG_COMPRESS_OFFLOAD | AUDIO_OUTPUT_FLAG_DIRECT)) == 0) ||
            !(mEffects.isNonOffloadableEffectEnabled() || mMasterMono)) {
        profile = getProfileForOutput(
                devices, config->sample_rate, config->format, config->channel_mask,
                flags, true /* directOnly */);
    }
 
    if (profile == nullptr) {
        return NAME_NOT_FOUND;
    }
    if (!(flags & AUDIO_OUTPUT_FLAG_DIRECT) &&
         (profile->getFlags() & AUDIO_OUTPUT_FLAG_DIRECT)) {
        ALOGI("%s rejecting direct profile as was not requested ", __func__);
        profile = nullptr;
        return NAME_NOT_FOUND;
    }                                                                                     
 
    sp<SwAudioOutputDescriptor> outputDesc = nullptr;
    // check if direct output for pcm/track offload or compress offload already exist
    bool directSessionInUse = false;
    bool offloadSessionInUse = false;
    // exclusive outputs for MMAP and Offload are enforced by different session ids.
    if (!(property_get_bool("vendor.audio.offload.multiple.enabled", false) &&
          ((flags & AUDIO_OUTPUT_FLAG_DIRECT) != 0) &&
          (flags & AUDIO_OUTPUT_FLAG_MMAP_NOIRQ) == 0)) {
        for (size_t i = 0; i < mOutputs.size(); i++) {
            sp<SwAudioOutputDescriptor> desc = mOutputs.valueAt(i);
            if (!desc->isDuplicated() && (profile == desc->mProfile)) {
                 outputDesc = desc;
                // reuse direct output if currently open by the same client
                // and configured with same parameters
                if ((config->sample_rate == desc->getSamplingRate()) &&
                    (config->format == desc->getFormat()) &&
                    (config->channel_mask == desc->getChannelMask()) &&
                    (session == desc->mDirectClientSession)) {
                    desc->mDirectOpenCount++;
                    ALOGI("%s reusing direct output %d for session %d", __func__,
                        mOutputs.keyAt(i), session);
                    *output = mOutputs.keyAt(i);
                    return NO_ERROR;
                }
                if (desc->mFlags == AUDIO_OUTPUT_FLAG_DIRECT) {
                    directSessionInUse = true;
                    ALOGV("%s Direct PCM already in use", __func__);
                }
                if (desc->mFlags & AUDIO_OUTPUT_FLAG_COMPRESS_OFFLOAD) {
                    offloadSessionInUse = true;
                    ALOGV("%s Compress Offload already in use", __func__);
                }
            }
        }
        if (outputDesc != nullptr &&
            ((flags == AUDIO_OUTPUT_FLAG_DIRECT && directSessionInUse) ||
            ((flags & AUDIO_OUTPUT_FLAG_COMPRESS_OFFLOAD) && offloadSessionInUse))) {
            if (session != outputDesc->mDirectClientSession) {
                ALOGV("getOutput() do not reuse direct pcm output because current client (%d) "
                      "is not the same as requesting client (%d) for different output conf",
                outputDesc->mDirectClientSession, session);
                return NAME_NOT_FOUND;
            } else {
                ALOGV("%s close previous output on same client session %d ", __func__, session);
                closeOutput(outputDesc->mIoHandle);
            }
        }
    }
    if (!profile->canOpenNewIo()) {
        return NAME_NOT_FOUND;
    }                                                                                                   //上面是处理一些找不到的情况,进行一个过滤
 
    outputDesc = new SwAudioOutputDescriptor(profile, mpClientInterface);                              //---------- 新建一个SwAudioOutputDescriptor,这个是包装output的类
 
    // An MSD patch may be using the only output stream that can service this request. Release
    // all MSD patches to prioritize this request over any active output on MSD.
    releaseMsdOutputPatches(devices);
 
    status_t status = outputDesc->open(config, devices, stream, flags, output);                        //----------真正的打开 output
 
    // only accept an output with the requested parameters
    if (status != NO_ERROR ||
        (config->sample_rate != 0 && config->sample_rate != outputDesc->getSamplingRate()) ||
        (config->format != AUDIO_FORMAT_DEFAULT && config->format != outputDesc->getFormat()) ||
        (config->channel_mask != 0 && config->channel_mask != outputDesc->getChannelMask())) {
        ALOGV("%s failed opening direct output: output %d sample rate %d %d,"
                "format %d %d, channel mask %04x %04x", __func__, *output, config->sample_rate,
                outputDesc->getSamplingRate(), config->format, outputDesc->getFormat(),
                config->channel_mask, outputDesc->getChannelMask());
        if (*output != AUDIO_IO_HANDLE_NONE) {
            outputDesc->close();
        }
        // fall back to mixer output if possible when the direct output could not be open
        if (audio_is_linear_pcm(config->format) &&
                config->sample_rate  <= SAMPLE_RATE_HZ_MAX) {
            return NAME_NOT_FOUND;
        }
        *output = AUDIO_IO_HANDLE_NONE;
        return BAD_VALUE;
    }
    outputDesc->mDirectOpenCount = 1;
    outputDesc->mDirectClientSession = session;
 
    addOutput(*output, outputDesc);
    mPreviousOutputs = mOutputs;
    ALOGV("%s returns new direct output %d", __func__, *output);
    mpClientInterface->onAudioPortListUpdate();
    return NO_ERROR;
}
```
上面新建的 SwAudioOutputDescriptor 调用 open 之后会经过 AudioPolicyClientImpl 到达 Audioflinger 的 openoutput
```c
frameworks/av/services/audioflinger/AudioFlinger.cpp
status_t AudioFlinger::openOutput(const media::OpenOutputRequest& request,
                                media::OpenOutputResponse* response)
{
    audio_module_handle_t module = VALUE_OR_RETURN_STATUS(
            aidl2legacy_int32_t_audio_module_handle_t(request.module));
    audio_config_t config = VALUE_OR_RETURN_STATUS(
            aidl2legacy_AudioConfig_audio_config_t(request.config));
    sp<DeviceDescriptorBase> device = VALUE_OR_RETURN_STATUS(
            aidl2legacy_DeviceDescriptorBase(request.device));
    audio_output_flags_t flags = VALUE_OR_RETURN_STATUS(
            aidl2legacy_int32_t_audio_output_flags_t_mask(request.flags));
 
    audio_io_handle_t output;
    uint32_t latencyMs;
 
    ALOGI("openOutput() this %p, module %d Device %s, SamplingRate %d, Format %#08x, "
              "Channels %#x, flags %#x",
              this, module,
              device->toString().c_str(),
              config.sample_rate,
              config.format,
              config.channel_mask,
              flags);
 
    audio_devices_t deviceType = device->type();
    const String8 address = String8(device->address().c_str());
 
    if (deviceType == AUDIO_DEVICE_NONE) {
        return BAD_VALUE;
    }
 
    Mutex::Autolock _l(mLock);
 
    sp<ThreadBase> thread = openOutput_l(module, &output, &config, deviceType, address, flags);                  //openoutput核心处理
    if (thread != 0) {
        if ((flags & AUDIO_OUTPUT_FLAG_MMAP_NOIRQ) == 0) {
            PlaybackThread *playbackThread = (PlaybackThread *)thread.get();
            latencyMs = playbackThread->latency();
 
            // notify client processes of the new output creation
            playbackThread->ioConfigChanged(AUDIO_OUTPUT_OPENED);
 
            // the first primary output opened designates the primary hw device if no HW module
            // named "primary" was already loaded.
            AutoMutex lock(mHardwareLock);
            if ((mPrimaryHardwareDev == nullptr) && (flags & AUDIO_OUTPUT_FLAG_PRIMARY)) {
                ALOGI("Using module %d as the primary audio interface", module);
                mPrimaryHardwareDev = playbackThread->getOutput()->audioHwDev;
 
                mHardwareStatus = AUDIO_HW_SET_MODE;
                mPrimaryHardwareDev->hwDevice()->setMode(mMode);
                mHardwareStatus = AUDIO_HW_IDLE;
            }
        } else {
            MmapThread *mmapThread = (MmapThread *)thread.get();
            mmapThread->ioConfigChanged(AUDIO_OUTPUT_OPENED);
        }
        response->output = VALUE_OR_RETURN_STATUS(legacy2aidl_audio_io_handle_t_int32_t(output));
        response->config = VALUE_OR_RETURN_STATUS(legacy2aidl_audio_config_t_AudioConfig(config));
        response->latencyMs = VALUE_OR_RETURN_STATUS(convertIntegral<int32_t>(latencyMs));
        response->flags = VALUE_OR_RETURN_STATUS(
                legacy2aidl_audio_output_flags_t_int32_t_mask(flags));
        return NO_ERROR;
    }
 
    return NO_INIT;
}
 
sp<AudioFlinger::ThreadBase> AudioFlinger::openOutput_l(audio_module_handle_t module,
                                                        audio_io_handle_t *output,
                                                        audio_config_t *config,
                                                        audio_devices_t deviceType,
                                                        const String8& address,
                                                        audio_output_flags_t flags)
{
    AudioHwDevice *outHwDev = findSuitableHwDev_l(module, deviceType);                         //寻找并加载对应的HAL层module,也就是链接HAL接口
    if (outHwDev == NULL) {
        return 0;
    }
 
    if (*output == AUDIO_IO_HANDLE_NONE) {
        *output = nextUniqueId(AUDIO_UNIQUE_ID_USE_OUTPUT);
    } else {
        // Audio Policy does not currently request a specific output handle.
        // If this is ever needed, see openInput_l() for example code.
        ALOGE("openOutput_l requested output handle %d is not AUDIO_IO_HANDLE_NONE", *output);
        return 0;
    }
 
    mHardwareStatus = AUDIO_HW_OUTPUT_OPEN;
 
    // FOR TESTING ONLY:
    // This if statement allows overriding the audio policy settings
    // and forcing a specific format or channel mask to the HAL/Sink device for testing.
    if (!(flags & (AUDIO_OUTPUT_FLAG_COMPRESS_OFFLOAD | AUDIO_OUTPUT_FLAG_DIRECT))) {
        // Check only for Normal Mixing mode
        if (kEnableExtendedPrecision) {
            // Specify format (uncomment one below to choose)
            //config->format = AUDIO_FORMAT_PCM_FLOAT;
            //config->format = AUDIO_FORMAT_PCM_24_BIT_PACKED;
            //config->format = AUDIO_FORMAT_PCM_32_BIT;
            //config->format = AUDIO_FORMAT_PCM_8_24_BIT;
            // ALOGV("openOutput_l() upgrading format to %#08x", config->format);
        }
        if (kEnableExtendedChannels) {
            // Specify channel mask (uncomment one below to choose)
            //config->channel_mask = audio_channel_out_mask_from_count(4);  // for USB 4ch
            //config->channel_mask = audio_channel_mask_from_representation_and_bits(
            //        AUDIO_CHANNEL_REPRESENTATION_INDEX, (1 << 4) - 1);  // another 4ch example
        }
    }
 
    AudioStreamOut *outputStream = NULL;
    status_t status = outHwDev->openOutputStream(
            &outputStream,
            *output,
            deviceType,
            flags,
            config,
            address.string());                                          //调用HAL层的 openoutputStream 正式打通和HAL层的通道
 
    mHardwareStatus = AUDIO_HW_IDLE;
 
    if (status == NO_ERROR) {                                           //下面就对应几种情况分别建立了 playbackThread
        if (flags & AUDIO_OUTPUT_FLAG_MMAP_NOIRQ) {
            sp<MmapPlaybackThread> thread =
                    new MmapPlaybackThread(this, *output, outHwDev, outputStream, mSystemReady);                  // -------------    1
            mMmapThreads.add(*output, thread);
            ALOGV("openOutput_l() created mmap playback thread: ID %d thread %p",
                  *output, thread.get());
            return thread;
        } else {
            sp<PlaybackThread> thread;
            if (flags & AUDIO_OUTPUT_FLAG_COMPRESS_OFFLOAD) {
                thread = new OffloadThread(this, outputStream, *output, mSystemReady);                            // --------------    2
                ALOGV("openOutput_l() created offload output: ID %d thread %p",
                      *output, thread.get());
            } else if ((flags & AUDIO_OUTPUT_FLAG_DIRECT)
                    || !isValidPcmSinkFormat(config->format)
                    || !isValidPcmSinkChannelMask(config->channel_mask)) {
                thread = new DirectOutputThread(this, outputStream, *output, mSystemReady);                      // ---------------    3
                ALOGV("openOutput_l() created direct output: ID %d thread %p",
                      *output, thread.get());
            } else {
                thread = new MixerThread(this, outputStream, *output, mSystemReady);                             // ---------------    4
                ALOGV("openOutput_l() created mixer output: ID %d thread %p",
                      *output, thread.get());
            }
            mPlaybackThreads.add(*output, thread);                                                               // 添加到了数组中
            struct audio_patch patch;
            mPatchPanel.notifyStreamOpened(outHwDev, *output, &patch);
            if (thread->isMsdDevice()) {
                thread->setDownStreamPatch(&patch);
            }
            return thread;
        }
    }
 
    return 0;
}
```
mPlaybackThreads 所保存的几种thread 分别有不用的场景应用.  

看完 playbackthread 接着往下看 Track 的创建
```c
frameworks/av/services/audioflinger/Track.cpp
AudioFlinger::PlaybackThread::Track::Track(
            PlaybackThread *thread,
            const sp<Client>& client,
            audio_stream_type_t streamType,
            const audio_attributes_t& attr,
            uint32_t sampleRate,
            audio_format_t format,
            audio_channel_mask_t channelMask,
            size_t frameCount,
            void *buffer,
            size_t bufferSize,
            const sp<IMemory>& sharedBuffer,
            audio_session_t sessionId,
            pid_t creatorPid,
            const AttributionSourceState& attributionSource,
            audio_output_flags_t flags,
            track_type type,
            audio_port_handle_t portId,
            size_t frameCountToBeReady,
            float speed)
    :   TrackBase(thread, client, attr, sampleRate, format, channelMask, frameCount,
                  // TODO: Using unsecurePointer() has some associated security pitfalls
                  //       (see declaration for details).
                  //       Either document why it is safe in this case or address the
                  //       issue (e.g. by copying).
                  (sharedBuffer != 0) ? sharedBuffer->unsecurePointer() : buffer,
                  (sharedBuffer != 0) ? sharedBuffer->size() : bufferSize,
                  sessionId, creatorPid,
                  VALUE_OR_FATAL(aidl2legacy_int32_t_uid_t(attributionSource.uid)), true /*isOut*/,
                  (type == TYPE_PATCH) ? ( buffer == NULL ? ALLOC_LOCAL : ALLOC_NONE) : ALLOC_CBLK,
                  type,
                  portId,
                  std::string(AMEDIAMETRICS_KEY_PREFIX_AUDIO_TRACK) + std::to_string(portId)),                                //调用了父类的构造函数
    mFillingUpStatus(FS_INVALID),
    // mRetryCount initialized later when needed
    mSharedBuffer(sharedBuffer),
    mStreamType(streamType),
    mMainBuffer(thread->sinkBuffer()),
    mAuxBuffer(NULL),
    mAuxEffectId(0), mHasVolumeController(false),
    mFrameMap(16 /* sink-frame-to-track-frame map memory */),
    mVolumeHandler(new media::VolumeHandler(sampleRate)),
    mOpPlayAudioMonitor(OpPlayAudioMonitor::createIfNeeded(attributionSource, attr, id(),
        streamType)),
    // mSinkTimestamp
    mFastIndex(-1),
    mCachedVolume(1.0),
    /* The track might not play immediately after being active, similarly as if its volume was 0.
     * When the track starts playing, its volume will be computed. */
    mFinalVolume(0.f),
    mResumeToStopping(false),
    mFlushHwPending(false),
    mFlags(flags),
    mSpeed(speed)
{                                                                                          //持有了各种状态属性
    // client == 0 implies sharedBuffer == 0
    ALOG_ASSERT(!(client == 0 && sharedBuffer != 0));
 
    ALOGV_IF(sharedBuffer != 0, "%s(%d): sharedBuffer: %p, size: %zu",
            __func__, mId, sharedBuffer->unsecurePointer(), sharedBuffer->size());
 
    if (mCblk == NULL) {
        return;
    }
 
    uid_t uid = VALUE_OR_FATAL(aidl2legacy_int32_t_uid_t(attributionSource.uid));
    if (!thread->isTrackAllowed_l(channelMask, format, sessionId, uid)) {
        ALOGE("%s(%d): no more tracks available", __func__, mId);
        releaseCblk(); // this makes the track invalid.
        return;
    }
 
    if (sharedBuffer == 0) {                                                                          //根据是否有共享内存创建了两个 server代理,和 AudioTrack中的 client 相配对
        mAudioTrackServerProxy = new AudioTrackServerProxy(mCblk, mBuffer, frameCount,
                mFrameSize, !isExternalTrack(), sampleRate);
    } else {
        mAudioTrackServerProxy = new StaticAudioTrackServerProxy(mCblk, mBuffer, frameCount,
                mFrameSize, sampleRate);
    }
    mServerProxy = mAudioTrackServerProxy;
    mServerProxy->setStartThresholdInFrames(frameCountToBeReady); // update the Cblk value
 
    // only allocate a fast track index if we were able to allocate a normal track name
    if (flags & AUDIO_OUTPUT_FLAG_FAST) {
        // FIXME: Not calling framesReadyIsCalledByMultipleThreads() exposes a potential
        // race with setSyncEvent(). However, if we call it, we cannot properly start
        // static fast tracks (SoundPool) immediately after stopping.
        //mAudioTrackServerProxy->framesReadyIsCalledByMultipleThreads();
        ALOG_ASSERT(thread->mFastTrackAvailMask != 0);
        int i = __builtin_ctz(thread->mFastTrackAvailMask);
        ALOG_ASSERT(0 < i && i < (int)FastMixerState::sMaxFastTracks);
        // FIXME This is too eager.  We allocate a fast track index before the
        //       fast track becomes active.  Since fast tracks are a scarce resource,
        //       this means we are potentially denying other more important fast tracks from
        //       being created.  It would be better to allocate the index dynamically.
        mFastIndex = i;
        thread->mFastTrackAvailMask &= ~(1 << i);
    }
 
    mServerLatencySupported = thread->type() == ThreadBase::MIXER
            || thread->type() == ThreadBase::DUPLICATING;
#ifdef TEE_SINK
    mTee.setId(std::string("_") + std::to_string(mThreadIoHandle)
            + "_" + std::to_string(mId) + "_T");
#endif
 
    if (thread->supportsHapticPlayback()) {
        // If the track is attached to haptic playback thread, it is potentially to have
        // HapticGenerator effect, which will generate haptic data, on the track. In that case,
        // external vibration is always created for all tracks attached to haptic playback thread.
        mAudioVibrationController = new AudioVibrationController(this);
        std::string packageName = attributionSource.packageName.has_value() ?
            attributionSource.packageName.value() : "";
        mExternalVibration = new os::ExternalVibration(
                mUid, packageName, mAttr, mAudioVibrationController);
    }
 
    // Once this item is logged by the server, the client can add properties.
    const char * const traits = sharedBuffer == 0 ? "" : "static";
    mTrackMetrics.logConstructor(creatorPid, uid, id(), traits, streamType);
}
```

第二步,play 进行到了 AudioTrak.start 调用了 AudioFlinger侧的 TrackHandle start,这只是一个传递代码真正是到了 Track start(),接看看 Track start 做了什么.
```c
frameworks/av/services/audioflinger/Track.cpp
status_t AudioFlinger::PlaybackThread::Track::start(AudioSystem::sync_event_t event __unused,
                                                    audio_session_t triggerSession __unused)
{
    status_t status = NO_ERROR;
    ALOGV("%s(%d): calling pid %d session %d",
            __func__, mId, IPCThreadState::self()->getCallingPid(), mSessionId);
 
    sp<ThreadBase> thread = mThread.promote();
    if (thread != 0) {
        if (isOffloaded()) {
            Mutex::Autolock _laf(thread->mAudioFlinger->mLock);
            Mutex::Autolock _lth(thread->mLock);
            sp<EffectChain> ec = thread->getEffectChain_l(mSessionId);
            if (thread->mAudioFlinger->isNonOffloadableGlobalEffectEnabled_l() ||
                    (ec != 0 && ec->isNonOffloadableEnabled())) {
                invalidate();
                return PERMISSION_DENIED;
            }
        }
        Mutex::Autolock _lth(thread->mLock);
        track_state state = mState;
        // here the track could be either new, or restarted
        // in both cases "unstop" the track
 
        // initial state-stopping. next state-pausing.
        // What if resume is called ?
 
        if (state == FLUSHED) {
            // avoid underrun glitches when starting after flush
            reset();
        }
 
        // clear mPauseHwPending because of pause (and possibly flush) during underrun.
        mPauseHwPending = false;
        if (state == PAUSED || state == PAUSING) {
            if (mResumeToStopping) {
                // happened we need to resume to STOPPING_1
                mState = TrackBase::STOPPING_1;
                ALOGV("%s(%d): PAUSED => STOPPING_1 on thread %d",
                        __func__, mId, (int)mThreadIoHandle);
            } else {
                mState = TrackBase::RESUMING;
                ALOGV("%s(%d): PAUSED => RESUMING on thread %d",
                        __func__,  mId, (int)mThreadIoHandle);
            }
        } else {
            mState = TrackBase::ACTIVE;
            ALOGV("%s(%d): ? => ACTIVE on thread %d",
                    __func__, mId, (int)mThreadIoHandle);
        }
 
        // states to reset position info for non-offloaded/direct tracks
        if (!isOffloaded() && !isDirect()
                && (state == IDLE || state == STOPPED || state == FLUSHED)) {
            mFrameMap.reset();
        }
        PlaybackThread *playbackThread = (PlaybackThread *)thread.get();                                 //获取playbackThread
        if (isFastTrack()) {
            // refresh fast track underruns on start because that field is never cleared
            // by the fast mixer; furthermore, the same track can be recycled, i.e. start
            // after stop.
            mObservedUnderruns = playbackThread->getFastTrackUnderruns(mFastIndex);                      //这里是监测underrun状态
        }
        status = playbackThread->addTrack_l(this);                                                       //将当前track加入到playbackThread中
        if (status == INVALID_OPERATION || status == PERMISSION_DENIED) {
            triggerEvents(AudioSystem::SYNC_EVENT_PRESENTATION_COMPLETE);
            //  restore previous state if start was rejected by policy manager
            if (status == PERMISSION_DENIED) {
                mState = state;
            }
        }
 
        // Audio timing metrics are computed a few mix cycles after starting.
        {
            mLogStartCountdown = LOG_START_COUNTDOWN;
            mLogStartTimeNs = systemTime();
            mLogStartFrames = mAudioTrackServerProxy->getTimestamp()
                    .mPosition[ExtendedTimestamp::LOCATION_KERNEL];
            mLogLatencyMs = 0.;
        }
 
        if (status == NO_ERROR || status == ALREADY_EXISTS) {
            // for streaming tracks, remove the buffer read stop limit.
            mAudioTrackServerProxy->start();
        }
 
        // track was already in the active list, not a problem
        if (status == ALREADY_EXISTS) {
            status = NO_ERROR;
        } else {
            // Acknowledge any pending flush(), so that subsequent new data isn't discarded.
            // It is usually unsafe to access the server proxy from a binder thread.
            // But in this case we know the mixer thread (whether normal mixer or fast mixer)
            // isn't looking at this track yet:  we still hold the normal mixer thread lock,
            // and for fast tracks the track is not yet in the fast mixer thread's active set.
            // For static tracks, this is used to acknowledge change in position or loop.
            ServerProxy::Buffer buffer;
            buffer.mFrameCount = 1;
            (void) mAudioTrackServerProxy->obtainBuffer(&buffer, true /*ackFlush*/);
        }
    } else {
        status = BAD_VALUE;
    }
    if (status == NO_ERROR) {
        forEachTeePatchTrack([](auto patchTrack) { patchTrack->start(); });
    }
    return status;
}
```
上面的代码我们主要看 playbackThread,播放音频的主要核心线程,playbackThread 是保存在 mPlaybackThreads 数组中,再看看 playbackThread->addTrack_l.
```c
frameworks/av/services/audioflinger/Threads.cpp
@line2713
status_t AudioFlinger::PlaybackThread::addTrack_l(const sp<Track>& track)
{
    status_t status = ALREADY_EXISTS;
 
    if (mActiveTracks.indexOf(track) < 0) {
        // the track is newly added, make sure it fills up all its
        // buffers before playing. This is to ensure the client will
        // effectively get the latency it requested.
        if (track->isExternalTrack()) {
            TrackBase::track_state state = track->mState;
            mLock.unlock();
            status = AudioSystem::startOutput(track->portId());       //调用到了 AudioOutputDescriptor 中,增加了 mPorfile->curActiveCount 的计数
 
            mLock.lock();
            // abort track was stopped/paused while we released the lock
            if (state != track->mState) {
                if (status == NO_ERROR) {
                    mLock.unlock();
                    AudioSystem::stopOutput(track->portId());
                    mLock.lock();
                }
                return INVALID_OPERATION;
            }
            // abort if start is rejected by audio policy manager
            if (status != NO_ERROR) {
                return PERMISSION_DENIED;
            }
#ifdef ADD_BATTERY_DATA
            // to track the speaker usage
            addBatteryData(IMediaPlayerService::kBatteryDataAudioFlingerStart);
#endif
            sendIoConfigEvent_l(AUDIO_CLIENT_STARTED, track->creatorPid(), track->portId());
        }
 
        // set retry count for buffer fill
        if (track->isOffloaded()) {
            if (track->isStopping_1()) {
                track->mRetryCount = kMaxTrackStopRetriesOffload;
            } else {
                track->mRetryCount = kMaxTrackStartupRetriesOffload;
            }
            track->mFillingUpStatus = mStandby ? Track::FS_FILLING : Track::FS_FILLED;
        } else {
            track->mRetryCount = kMaxTrackStartupRetries;
            track->mFillingUpStatus =
                    track->sharedBuffer() != 0 ? Track::FS_FILLED : Track::FS_FILLING;
        }
 
        sp<EffectChain> chain = getEffectChain_l(track->sessionId());
        if (mHapticChannelMask != AUDIO_CHANNEL_NONE
                && ((track->channelMask() & AUDIO_CHANNEL_HAPTIC_ALL) != AUDIO_CHANNEL_NONE
                        || (chain != nullptr && chain->containsHapticGeneratingEffect_l()))) {
            // Unlock due to VibratorService will lock for this call and will
            // call Tracks.mute/unmute which also require thread's lock.
            mLock.unlock();
            const int intensity = AudioFlinger::onExternalVibrationStart(
                    track->getExternalVibration());
            mLock.lock();
            track->setHapticIntensity(static_cast<os::HapticScale>(intensity));
            // Haptic playback should be enabled by vibrator service.
            if (track->getHapticPlaybackEnabled()) {
                // Disable haptic playback of all active track to ensure only
                // one track playing haptic if current track should play haptic.
                for (const auto &t : mActiveTracks) {
                    t->setHapticPlaybackEnabled(false);
                }
            }
 
            // Set haptic intensity for effect
            if (chain != nullptr) {
                chain->setHapticIntensity_l(track->id(), intensity);
            }
        }
 
        track->mResetDone = false;
        track->resetPresentationComplete();
        mActiveTracks.add(track);
        if (chain != 0) {
            ALOGV("addTrack_l() starting track on chain %p for session %d", chain.get(),
                    track->sessionId());
            chain->incActiveTrackCnt();
        }
 
        track->logBeginInterval(patchSinksToString(&mPatch)); // log to MediaMetrics
        status = NO_ERROR;
    }
 
    onAddNewTrack_l();                                   //-----------  1
    return status;
}
```
```c
frameworks/av/services/audioflinger/Threads.cpp
@line5126 
void AudioFlinger::PlaybackThread::onAddNewTrack_l()    //------------- 这里是对我们playbackThread进行了唤醒
{
    ALOGV("signal playback thread");
    broadcast_l();
}
```
第三步,写数据,这里是将上层要播放的数据写进了共享内存里,这里的关键方法是 obtainBuffer.
AudioFlinger做为Service端会不断的接收并处理Client端 AudioTrack::write 写入的数据.
```c
frameworks/av/services/audioflinger/Track.cpp
ssize_t AudioFlinger::PlaybackThread::OutputTrack::write(void* data, uint32_t frames)
{
    ...
            status_t status = obtainBuffer(&mOutBuffer, waitTimeLeftMs);
    ...
}
```
addTrack_l 之后 playbackThread 会被唤醒,然后就会开始工作,thread_loop 会动起来.  
这里面包含集合函数: threadloop_mix, threadloop_write,threadloop_standby,分别是对音频进行混音、通过数据流将数据写到HAL层、暂停.  
上层play之后就会开始往 HAL层 写数据,然后就放出了了我们听到的音乐,这个 track 在 framework层的使命就算是成功完成了.  
然后处理的事情就交给了HAL层和kernel及ALSA.

[AudioOnAndroid](AudioOnAndroid.md)