| Task ID  | Task name | Desciption  |Priority |Date to start| Dead line |
|----------|-----------|-------------|---------|-------------|-----------|
|7547	|客户需求按模块分析总结需要做的事情以及难点，完成架构设计|					|3	|2024/3/1	|2024/3/12	
|7546	|audio配置工具的使用							 |			|3	|2024/2/16	|2024/3/1	
|7545	|音频驱动bringup 流程研究						 |			|3	|2024/3/5	|2024/3/7	
|7544	|音频架构图中每个模块的作用						 |			|3	|2024/3/1	|2024/3/5	
|7543	|音频数据是怎么传输的				|从kernel到middleware到framework		|3	|2024/2/27	|2024/2/29	
|7542	|Audio Framework 音频数据格式研究		 |	有那几种数据格式，长度，构成等		|3	|2024/2/23	|2024/2/26	
|7541	|Audio Framework 关键数据结构研究与分享	 |		需要讲解关键的数据结构以及里面成员的含义	|3	|2024/2/19	|2024/2/22	
|7540	|App是如何配置蓝牙音频通路的研究与验证 |								|3	|2024/2/3	|2024/2/16	
|7452	|ADSP代码编译			 |							|3	|2024/1/29	|2024/1/31	
|7404	|实验 BT音频和本地音频两个通路能否同时打开	 |						|3	|2024/1/17	|2024/1/26	
|7330	|找市面上对比的翻译耳机					 |				|3	|2024/1/10	|2024/1/12	
|7315	|蓝牙部分音频通路研究					 |				|3	|2024/1/10	|2024/1/12	

#输出通道切换
```c
frameworks/base/core/tests/coretests/AndroidManifest.xml:47:    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```

```c

frameworks/base/media/java/android/media/AudioManager.java:2052:    public void setBluetoothScoOn(boolean on){
frameworks/base/media/java/android/media/AudioManager.java:2055:            service.setBluetoothScoOn(on);
frameworks/base/media/java/android/media/AudioManager.java:2341:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2347:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2353:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2359:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2365:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2371:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2377:     * setBluetoothScoOn() methods instead.
frameworks/base/media/java/android/media/AudioManager.java:2391:     * setBluetoothScoOn() methods instead.
frameworks/base/services/core/java/com/android/server/audio/AudioDeviceBroker.java:433:    /*package*/ void setBluetoothScoOnByApp(boolean on) {
frameworks/base/services/core/java/com/android/server/audio/AudioDeviceBroker.java:445:    /*package*/ void setBluetoothScoOn(boolean on, String eventSource) {
frameworks/base/services/core/java/com/android/server/audio/AudioDeviceBroker.java:446:        //Log.i(TAG, "setBluetoothScoOn: " + on + " " + eventSource);
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4232:    /** @see AudioManager#setBluetoothScoOn(boolean) */
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4233:    public void setBluetoothScoOn(boolean on) {
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4234:        if (!checkAudioSettingsPermission("setBluetoothScoOn()")) {
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4240:            mDeviceBroker.setBluetoothScoOnByApp(on);
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4247:        final String eventSource = new StringBuilder("setBluetoothScoOn(").append(on)
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4252:                + MediaMetrics.SEPARATOR + "setBluetoothScoOn")
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4259:        mDeviceBroker.setBluetoothScoOn(on, eventSource);
frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4264:     * called setBluetoothScoOn() */
frameworks/base/services/core/java/com/android/server/audio/BtHelper.java:326:                    mDeviceBroker.setBluetoothScoOn(true, "BtHelper.receiveBtEvent");
frameworks/base/services/core/java/com/android/server/audio/BtHelper.java:329:                    mDeviceBroker.setBluetoothScoOn(false, "BtHelper.receiveBtEvent");
frameworks/base/services/core/java/com/android/server/audio/BtHelper.java:514:        mDeviceBroker.setBluetoothScoOn(false, "resetBluetoothSco");

packages/apps/Dialer/java/com/android/dialer/app/voicemail/VoicemailAudioManager.java:145:      audioManager.startBluetoothSco();

  private void applyBluetoothScoState() {
    if (bluetoothScoEnabled) {
      audioManager.startBluetoothSco();
      // The doc for startBluetoothSco() states it could take seconds to establish the SCO
      // connection, so we should probably resume the playback after we've acquired SCO.
      // In practice the delay is unnoticeable so this is ignored for simplicity.
      audioManager.setBluetoothScoOn(true);
    } else {
      audioManager.setBluetoothScoOn(false);
      audioManager.stopBluetoothSco();
    }
  }
```
```c

packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:362:            setSpeakerphoneOn(false);
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:562:            setSpeakerphoneOn(false);
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:768:            setSpeakerphoneOn(false);
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:900:            setSpeakerphoneOn(false);
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:1112:            setSpeakerphoneOn(true);
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:1598:    private void setSpeakerphoneOn(boolean on) {
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:1601:            mAudioManager.setSpeakerphoneOn(on);
packages/services/Telecomm/src/com/android/server/telecom/CallAudioRouteStateMachine.java:1846:        setSpeakerphoneOn(initState.getRoute() == CallAudioState.ROUTE_SPEAKER);

frameworks/base/media/java/android/media/MediaRouter.java:249:                Log.v(TAG, "Audio routes updated: " + newRoutes + ", a2dp=" + isBluetoothA2dpOn());
frameworks/base/media/java/android/media/MediaRouter.java:262:        boolean isBluetoothA2dpOn() {
frameworks/base/media/java/android/media/MediaRouter.java:264:                return mBluetoothA2dpRoute != null && mAudioService.isBluetoothA2dpOn();
frameworks/base/media/java/android/media/MediaRouter.java:384:            RouteInfo selectedRoute = isBluetoothA2dpOn()
frameworks/base/media/java/android/media/MediaRouter.java:1033:        final RouteInfo currentSystemRoute = sStatic.isBluetoothA2dpOn()
frameworks/base/media/java/android/media/MediaRouter.java:1096:        if (sStatic.mSelectedRoute != sStatic.mBluetoothA2dpRoute && sStatic.isBluetoothA2dpOn()) {
frameworks/base/media/java/android/media/MediaRouter.java:1435:                dispatchRouteVolumeChanged(sStatic.mAudioService.isBluetoothA2dpOn() ?
frameworks/base/media/java/android/media/AudioManager.java:2091:    public boolean isBluetoothA2dpOn() {
frameworks/base/media/java/android/media/AudioManager.java:2404:     * isBluetoothScoOn(), isBluetoothA2dpOn() and isWiredHeadsetOn() methods instead.

    public void setSpeakerphoneOn(boolean on){
        final IAudioService service = getService();
        try {
            service.setSpeakerphoneOn(mICallBack, on);
        } catch (RemoteException e) {
            throw e.rethrowFromSystemServer();
        }
    }

    public boolean isSpeakerphoneOn() {
        final IAudioService service = getService();
        try {
            return service.isSpeakerphoneOn();
        } catch (RemoteException e) {
            throw e.rethrowFromSystemServer();
        }
     }

    public void setBluetoothScoOn(boolean on){
        final IAudioService service = getService();
        try {
            service.setBluetoothScoOn(on);
        } catch (RemoteException e) {
            throw e.rethrowFromSystemServer();
        }
    }

    public boolean isBluetoothScoOn() {
        final IAudioService service = getService();
        try {
            return service.isBluetoothScoOn();
        } catch (RemoteException e) {
            throw e.rethrowFromSystemServer();
        }
    }

    @Deprecated public void setBluetoothA2dpOn(boolean on){
    }

    public boolean isBluetoothA2dpOn() {
        if (AudioSystem.getDeviceConnectionState(DEVICE_OUT_BLUETOOTH_A2DP,"")
                == AudioSystem.DEVICE_STATE_AVAILABLE) {
            return true;
        } else if (AudioSystem.getDeviceConnectionState(DEVICE_OUT_BLUETOOTH_A2DP_HEADPHONES,"")
                == AudioSystem.DEVICE_STATE_AVAILABLE) {
            return true;
        } else if (AudioSystem.getDeviceConnectionState(DEVICE_OUT_BLUETOOTH_A2DP_SPEAKER,"")
                == AudioSystem.DEVICE_STATE_AVAILABLE) {
            return true;
        }
        return false;
    }  

    @Deprecated public void setWiredHeadsetOn(boolean on){
    }

    public boolean isWiredHeadsetOn() {
        if (AudioSystem.getDeviceConnectionState(DEVICE_OUT_WIRED_HEADSET,"")
                == AudioSystem.DEVICE_STATE_UNAVAILABLE &&
            AudioSystem.getDeviceConnectionState(DEVICE_OUT_WIRED_HEADPHONE,"")
                == AudioSystem.DEVICE_STATE_UNAVAILABLE &&
            AudioSystem.getDeviceConnectionState(DEVICE_OUT_USB_HEADSET, "")
              == AudioSystem.DEVICE_STATE_UNAVAILABLE) {
            return false;
        } else {
            return true;
        }
    }

frameworks/base/services/core/java/com/android/server/audio/AudioService.java:4228:    public boolean isSpeakerphoneOn() {
    /** @see AudioManager#isSpeakerphoneOn() */
    public boolean isSpeakerphoneOn() {
        return mDeviceBroker.isSpeakerphoneOn();
    }

    /** @see AudioManager#isBluetoothA2dpOn() */
    public boolean isBluetoothA2dpOn() {
        return mDeviceBroker.isBluetoothA2dpOn();
    }

    /** @see AudioManager#isBluetoothScoOn()
     * Note that it doesn't report internal state, but state seen by apps (which may have
     * called setBluetoothScoOn() */
    public boolean isBluetoothScoOn() {
        return mDeviceBroker.isBluetoothScoOnForApp();
    }
```

A2DP：是一种单向的高品质音频数据传输链路，通常用于播放立体声音乐；
SCO： 则是一种双向的音频数据的传输链路，该链路只支持8K及16K单声道的音频数据，只能用于普通语音的传输，若用于播放音乐那就只能呵呵了。

两者的主要区别是：A2DP只能播放，默认是打开的，而SCO既能录音也能播放，默认是关闭的。 如果要录音肯定要打开sco啦，因此调用上面的setBluetoothScoOn(boolean on)就可以通过蓝牙耳机录音、播放音频了，录完、播放完记得要关闭。

另外，在Android系统中通过AudioManager.setMode()方法来管理播放模式。在setMode()方法中有以下几种对应不同的播放模式:

MODE_NORMAL : 普通模式，既不是铃声模式也不是通话模式
MODE_RINGTONE : 铃声模式
MODE_IN_CALL : 通话模式
MODE_IN_COMMUNICATION : 通信模式，包括音/视频,VoIP通话.(3.0加入的，与通话模式类似)
在设置播放模式的时候，需要考虑流类型，我在这里使用的流类型是 STREAM_MUSIC ，所以切换播放设备的时候就需要设置为MODE_IN_COMMUNICATION 模式而不是 MODE_NORMAL 模式

切换音频Audio输出

```c
public class AudioUtils {
    private static int lastModel = -10;
    /**
     * 音频外放
     */
    public static void changeToSpeaker(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        //注意此处，蓝牙未断开时使用MODE_IN_COMMUNICATION而不是MODE_NORMAL
        audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
        audioManager.stopBluetoothSco();
        audioManager.setBluetoothScoOn(false);
        audioManager.setSpeakerphoneOn(true);
    }

    /**
     * 切换到蓝牙音箱
     */
    public static void changeToHeadset(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
        audioManager.startBluetoothSco();
        audioManager.setBluetoothScoOn(true);
        audioManager.setSpeakerphoneOn(false);
    }

    /**
     * 切换到听筒
     */
    public static void changeToReceiver(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        audioManager.setSpeakerphoneOn(false);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            audioManager.setMode(AudioManager.MODE_IN_COMMUNICATION);
        } else {
            audioManager.setMode(AudioManager.MODE_IN_CALL);
        }
    }


    public static void dispose(Context context, AudioManager.OnAudioFocusChangeListener focusRequest) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        audioManager.setMode(lastModel);
        if (audioManager.isBluetoothScoOn()) {
            audioManager.setBluetoothScoOn(false);
            audioManager.stopBluetoothSco();
        }
        audioManager.unloadSoundEffects();
        if (null != focusRequest) {
            audioManager.abandonAudioFocus(focusRequest);
        }
    }


    public static void getModel(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        lastModel = audioManager.getMode();
    }

    public static void changeToNomal(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        audioManager.setMode(AudioManager.MODE_NORMAL);
    }

    public static boolean isWiredHeadsetOn(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        return audioManager.isWiredHeadsetOn();
    }

    public static boolean isBluetoothA2dpOn(Context context) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        return audioManager.isBluetoothA2dpOn();
    }

    /**
     * context 传入的是MicroContext.getApplication()
     * @param context
     */
    public static void choiceAudioModel(Context context) {
        if (isWiredHeadsetOn(context)) {
            changeToReceiver(context);
        } else if (isBluetoothA2dpOn(context)) {
            changeToHeadset(context);
        } else {
            changeToSpeaker(context);
        }
    }

    public static void pauseMusic(Context context, AudioManager.OnAudioFocusChangeListener focusRequest) {
        AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
        audioManager.requestAudioFocus(focusRequest, AudioManager.STREAM_MUSIC, AUDIOFOCUS_GAIN);
    }


}

```

监听蓝牙连接状态
首先注意使用前需要以下权限：
```
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
<uses-permission android:name="android.permission.BLUETOOTH" />
```
根据这篇文章，我们发现可以使用 AudioManager.ACTION_AUDIO_BECOMING_NOISY

```
/**
 * 有注释的广播，蓝牙连接时都会用到
 */
intentFilter.addAction(BluetoothDevice.ACTION_FOUND); //搜索蓝压设备，每搜到一个设备发送一条广播
intentFilter.addAction(BluetoothDevice.ACTION_BOND_STATE_CHANGED); //配对开始时，配对成功时
intentFilter.addAction(BluetoothDevice.ACTION_ACL_CONNECTED); //配对时，发起连接
intentFilter.addAction(BluetoothDevice.ACTION_ACL_DISCONNECT_REQUESTED);
intentFilter.addAction(BluetoothDevice.ACTION_ACL_DISCONNECTED); //配对结束时，断开连接
intentFilter.addAction(PAIRING_REQUEST); //配对请求（Android.bluetooth.device.action.PAIRING_REQUEST）

intentFilter.addAction(BluetoothAdapter.ACTION_DISCOVERY_STARTED); //开始搜索
intentFilter.addAction(BluetoothAdapter.ACTION_DISCOVERY_FINISHED); //搜索结束。重新搜索时，会先终止搜索
intentFilter.addAction(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
intentFilter.addAction(BluetoothAdapter.ACTION_STATE_CHANGED); //本机开启、关闭蓝牙开关 
intentFilter.addAction(BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED); //蓝牙设备连接或断开
intentFilter.addAction(BluetoothAdapter.ACTION_LOCAL_NAME_CHANGED); //更改蓝牙名称，打开蓝牙时，可能会调用多次
intentFilter.addAction(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
intentFilter.addAction(BluetoothAdapter.ACTION_REQUEST_ENABLE);
intentFilter.addAction(BluetoothAdapter.ACTION_SCAN_MODE_CHANGED); //搜索模式改变

```
BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED ：指的是本地蓝牙适配器的连接状态的发生改变（比如没有关闭本机蓝牙开关时，另外一个配对设备自己把连接断开）

BluetoothAdapter.ACTION_STATE_CHANGED ：指的是本地蓝牙适配器的状态已更改。 例如，蓝牙开关打开或关闭。

换句话说，一个是用于连接状态的变化，另一个用于蓝牙适配器本身的状态变化。
经过测试发现，如果只使用BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED 监听广播，则会接收不到“主动关闭本机蓝牙开关”的广播事件。
但只是用BluetoothAdapter.ACTION_STATE_CHANGED 的话，很明显这时候蓝牙设备并未真正配对。

```c
public class BluetoothConnectionReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent){
        if (BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED.equals(intent.getAction())) {      //蓝牙连接状态
            int state = intent.getIntExtra(BluetoothAdapter.EXTRA_CONNECTION_STATE, -1);
            if (state == BluetoothAdapter.STATE_CONNECTED || state == BluetoothAdapter.STATE_DISCONNECTED) {
                //连接或失联，切换音频输出（到蓝牙、或者强制仍然扬声器外放）
            }
        } else if (BluetoothAdapter.ACTION_STATE_CHANGED.equals(intent.getAction())){   //本地蓝牙打开或关闭
            int state = intent.getIntExtra(BluetoothAdapter.EXTRA_STATE, -1);
            if (state == BluetoothAdapter.STATE_OFF || state == BluetoothAdapter.STATE_TURNING_OFF) {
                 //断开，切换音频输出
            }
        }

    }
}

```
```c
BluetoothConnectionReceiver audioNoisyReceiver = new BluetoothConnectionReceiver();

//蓝牙状态广播监听
IntentFilter audioFilter = new IntentFilter();
audioFilter.addAction(BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED);
audioFilter.addAction(BluetoothAdapter.ACTION_STATE_CHANGED);
mContext.registerReceiver(audioNoisyReceiver, audioFilter);

```
```c
frameworks/base/packages/SettingsLib/src/com/android/settingslib/bluetooth/BluetoothEventManager.java:92:        addHandler(BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED,
frameworks/base/packages/SettingsLib/src/com/android/settingslib/bluetooth/BluetoothCallback.java:83:     * It is listening {@link android.bluetooth.BluetoothAdapter#ACTION_CONNECTION_STATE_CHANGED}
packages/apps/Bluetooth/tests/unit/src/com/android/bluetooth/btservice/PhonePolicyTest.java:783:                intent = new Intent(BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED);
packages/apps/Bluetooth/src/com/android/bluetooth/btservice/AdapterProperties.java:633:                Intent intent = new Intent(BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED);
packages/apps/Settings/src/com/android/settings/bluetooth/BluetoothSliceBuilder.java:59:        INTENT_FILTER.addAction(BluetoothAdapter.ACTION_CONNECTION_STATE_CHANGED);

```

Audio
```c
frameworks/base/media/java/android/media/AudioRecord.java:548:        public Builder setAudioSource(@Source int source) throws IllegalArgumentException {

```