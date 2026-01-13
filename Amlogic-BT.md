[Amlogic.md](Amlogic.md)
# Controller
<font color="#dd00dd">AW55S2-50B1</font><br />
The chip is a Bluetooth 5.0 + BLE dual-mode and EDR-compliant baseband processor and 2.4GHz
transceiver. The Bluetooth subsystem presents a standard Host Controller Interface (HCI) via a high-
speed UARTand PCM for audio.

# HCI&PCM
|   Connect       | Pin |
|    ----         |    ----  |
| PCM             |    GPIOX_7->DOUT,GPIOX_8->DIN, GPIOX_9->SYNC,GPIOX_10->CLK  |
| uart_A          |    GPIOX_11->TX,GPIOX_12->RX, GPIOX_13->CTS,GPIOX_14->RTS |
| BT_EN           |    GPIOX_16 |
| HOST_WAKE_BT    |    GPIOX_17 |
# Host
## [BlueZ](https://mirrors.edge.kernel.org/pub/linux/bluetooth/) version upgrade
It locate at ./vendor/amlogic/bluez/bluez5_utils/
Just unzip or pull code into this path should work.
## BT mesh support
Found Bluez 5.49 or later version support mesh.
Just enable the feature(--enable-mesh) in makefile should work.
Check the display version by edit BLUEZ5_UTILS_VERSION.
```c
./buildroot/package/amlogic/bluez5-utils/bluez5_utils.mk

BLUEZ5_UTILS_VERSION = 5.49

BLUEZ5_UTILS_CONF_OPTS = 	\
	--enable-tools 		\
	--enable-library 	\
	--enable-mesh	 	\
	--disable-cups
```
Mesh feature have some dependencies need to perpared fisrt, such as json-c and ell.
Otherwise relevant build error will pop out. Configure in file a4_ba400_spk_a64_release_defconfig.
```c
./buildroot/configs/a4_ba400_spk_a64_release_defconfig

BR2_PACKAGE_DISPLAYCARD_AML_IMP=n
BR2_PACKAGE_JSON_C=y
BR2_PACKAGE_ELL=y
```
If still report related error, it may need a <font color="#dd00dd">rebuild/reinstall</font>.
```
make json-c-rebuild &&  make ell-rebuild
```
```c
rm -rf output/a4_ba400_spk_a64_release/build/bluez5-utils-5.49/
source setenv.sh a4_ba400_spk_a64_release
make bluez5-utils-rebuild
```
[Amlogic-BT-Mesh.md](Amlogic-BT-Mesh.md)

# Testing
Bluetooth start and stop.
```c
/etc/init.d/S44bluetooth stop
/etc/init.d/S44bluetooth start
```
For BLE test, it needs re-issue a start BLE, then you can find and connect the device by smartphone.
```c
/etc/init.d/S44bluetooth start BLE
```

Log enable.
```c
#BLUEZ
#set debug=1 in file /etc/bluetooth/main.conf
#bluetoothd: /etc/bluetooth/bluetoothd.log
#bluealsa: /etc/bluetooth/bluealsa.log
#bluealsa-aplay: /etc/bluetooth/bluealsa-aplay.log
```
# S1 to S2 patch
## Buildroot conifg
Move to
```c
./buildroot/configs/a4_ba400_spk_a64_release_defconfig
```
add,
```c
BR2_PACKAGE_AML_WIFI_W1U=y
BR2_PACKAGE_AML_BT_W1U=y
```
## Exchange source code
Unzip w1u.tar.gz and replace directory ./hardware/aml-5.4/wifi/amlogic/w1u
## Build
```c
source setenv.sh a4_ba400_spk_a64_release&&make aml-wifi-rebuild&&make

# App reference
## HCI attach
```c
./etc/init.d/S44bluetooth
./buildroot/package/amlogic/bluez5-utils/bluez_tool.sh
./buildroot/board/amlogic/mesona213y_au401/rootfs/etc/init.d/S44bluetooth

aml_bt_init()
{
	if [ -f /sys/bus/mmc/devices/mmc1:0000/mmc1:0000:1/device ]; then
		bt_chip_id=`cat /sys/bus/mmc/devices/mmc1:0000/mmc1:0000:1/device`
	else
		bt_chip_id=`cat /sys/bus/mmc/devices/mmc0:0000/mmc0:0000:1/device`
	fi
	case "${bt_chip_id}" in
	0x8888)  #w1 need insmod ko
		modprobe sdio_bt
		;;
	esac

	usleep 200000
	hciattach -s 115200 /dev/ttyS1 aml &> /dev/null
	usleep 100000
}
```

## Device Name
Refer to 
./buildroot/board/amlogic/mesona213y_au401/rootfs/etc/init.d/S44bluetooth
It read the name from /etc/board_info then write into main.conf, so edit board_info can change th device name.
```c
./buildroot/board/amlogic/mesona4_ba400_spk/rootfs/etc/board_info
+++ b/board/amlogic/mesona4_ba400_spk/rootfs/etc/board_info
@ -1 +1 @
-default-name-prefix=AmlSpeaker
+default-name-prefix=ChefSpeaker

```
BLE operatrion, refer to 
./vendor/amlogic/bluez/bluez5_utils/tools/btgatt-server.c

```c
//name
static void gap_device_name_write_cb(struct gatt_db_attribute *attrib,
									 unsigned int id, uint16_t offset,
									 const uint8_t *value, size_t len,
									 uint8_t opcode, struct bt_att *att,
									 void *user_data)
{
```
## BLE UUID
```c
//UUID
	/* Add the GAP service */
	bt_uuid16_create(&uuid, UUID_GAP);
```
## BLE Service
```c
//service
static void gatt_service_changed_cb(struct gatt_db_attribute *attrib,
									unsigned int id, uint16_t offset,
									uint8_t opcode, struct bt_att *att,
									void *user_data)

static void gatt_svc_chngd_ccc_read_cb(struct gatt_db_attribute *attrib,
									   unsigned int id, uint16_t offset,
									   uint8_t opcode, struct bt_att *att,
									   void *user_data)

static void gatt_svc_chngd_ccc_write_cb(struct gatt_db_attribute *attrib,
										unsigned int id, uint16_t offset,
										const uint8_t *value, size_t len,
										uint8_t opcode, struct bt_att *att,
										void *user_data)

static void user_service_read_cb(struct gatt_db_attribute *attrib,
								 unsigned int id, uint16_t offset,
								 uint8_t opcode, struct bt_att *att,
								 void *user_data)

static void user_service_write_cb(struct gatt_db_attribute *attrib,
								  unsigned int id, uint16_t offset,
								  const uint8_t *value, size_t len,
								  uint8_t opcode, struct bt_att *att,
								  void *user_data)
```
## BLE Advertising and connection
### Api and file
```c
//adv
static void set_adv_data(void)
static void set_adv_response(void)
static void set_adv_parameters(void)
static void set_adv_enable(int enable)
```
```c
BLE ADV and connect test
./vendor/amlogic/bluez/bluez5_utils/tools/btgatt-server.c
```
### Test log
```c
/ # ./usr/bin/btgatt-server
BLUEZ-GATT:
// l2cap_le_att_listen_and_accept()
BLUEZ-GATT: Started listening on ATT channel. Waiting for connections

//BLE device "ChefSpeaker-d337b" found by phone,click connect, then....

BLUEZ-GATT: Connect from 65:71:B5:5F:CB:26
BLUEZ-GATT: Running GATT server
BLUEZ-GATT: GAP Device Name Read called
BLUEZ-GATT: Service Changed CCC Write called
BLUEZ-GATT: Service Changed Enabled: true
```
## A2DP
### AVRCP API
```c
//AVRCP
//vendor/amlogic/bluez/bluez-alsa/utils/a2dp_ctl.h
int start_play(void);
int stop_play(void);
int pause_play(void);
int next(void);
int previous(void);
int volume_up();
int volume_down();
int volume_set(int volume);
```
### A2DP dynamic control
```c
//./vendor/amlogic/bluez/bluez5_utils/profiles/audio/a2dp.c
static void bt_a2dp_sink_connect(const void *buf, uint16_t len)
{
	/* TODO */

	DBG("");

	ipc_send_rsp(hal_ipc, HAL_SERVICE_ID_A2DP_SINK, HAL_OP_A2DP_CONNECT,
							HAL_STATUS_UNSUPPORTED);
}

static void bt_a2dp_sink_disconnect(const void *buf, uint16_t len)
{
	/* TODO */

	DBG("");

	ipc_send_rsp(hal_ipc, HAL_SERVICE_ID_A2DP_SINK, HAL_OP_A2DP_DISCONNECT,
							HAL_STATUS_UNSUPPORTED);
}
```
```c
//./vendor/amlogic/bluez/bluez-alsa/utils/lib_a2dp_ctl.c
int connect_dev(const char* bddr)
{

	GVariant *result;
	GError *error = NULL;
	int ret = 1;
	char obj[256] = {0};

	if (NULL == conn) {
		INFO("No connection!! Please init first\n");
		return ret;
	}

	if (strlen(bddr) != strlen("xx:xx:xx:xx:xx:xx")) {
		INFO("Bad bddr\n");
		return ret;
	}

	sprintf(obj, "/org/bluez/hci0/dev_%s", bddr);

	INFO("Target obj: %s\n", obj);

	if (strncmp("/org/bluez", TRANSPORT_OBJECT, 10) == 0) {
		INFO("There is Connected Device\n");

		if (strncmp(obj, TRANSPORT_OBJECT, 37) != 0) {
			INFO("Disconnect previous device\n");
			disconnect_dev();
			sleep(1);
		}
	}

	GVariant *param;
	/*if we are central, we should connect target's sink uuid*/
	if (strcmp(device_mode, "central") == 0)
		param = g_variant_new("(s)", A2DP_SINK_UUID);
	else
		param = g_variant_new("(s)", A2DP_SOURCE_UUID);


	result = g_dbus_connection_call_sync(conn,
			"org.bluez",
			obj,
			DEVICE_INTERFACE,
			"ConnectProfile",
			param,
			NULL,
			G_DBUS_CALL_FLAGS_NONE,
			-1,
			NULL,
			&error);

	if (result == NULL) {
		INFO("Error: %s\n", error->message);
		g_error_free (error);
		return ret;
	} else
		ret = 0;


	g_variant_unref(result);

	return ret;
}
```
## HFP
### API
```c
//HFP API
	answer_call();
	VGS_up();
	VGM_up();
	VGS_down();
	VGM_down();
	reject_call();
```
### test log
```c
//HFP
# ./usr/bin/hfp_ctl
//vendor/amlogic/bluez/bluez-alsa/utils/hfp_ctl.c:80
[HFP_CTL][hfp_ctl_init] Server is ready for connection...
```
### HFP dynamic control
```c
//./vendor/amlogic/bluez/bluez-alsa/utils/sco_handler.c
int set_sco_enable(int enable)
{
	INFO("%s sco stream\n", enable == 0 ? "Disable" : "Enable");
	if (sco_enabled == enable) {
		INFO("sco stream %s already\n", enable == 0 ? "disabled" : "enabled");
		return 0;
	}

	sco_enabled = enable;
	if (enable) {
		get_alsa_device();
#ifdef AVOID_UAC
		INFO("enable uac virtual sound card\n");
		uac_audio_enable(1);
#endif
		if (pthread_create(&sco_rx_thread, NULL, sco_rx_cb, NULL)) {
			INFO("rx thread create failed: %s\n", strerror(errno));
			sco_enabled = 0;
			return -1;
		} else
			pthread_setname_np(sco_rx_thread, "sco_rx_thread");

		if (pthread_create(&sco_tx_thread, NULL, sco_tx_cb, NULL)) {
			INFO("tx thread create failed: %s\n", strerror(errno));
			sco_enabled = 0;
			return -1;
		} else
			pthread_setname_np(sco_tx_thread, "sco_tx_thread");

	} else {
		if (sco_rx_thread) {
			pthread_detach(sco_rx_thread);
			sco_rx_thread  = 0;
		}
		if (sco_tx_thread) {
			pthread_detach(sco_tx_thread);
			sco_tx_thread  = 0;
		}
	}

	return 0;

}
```
## White list
```c
//./vendor/amlogic/bluez/bluez5_utils/src/adapter.c
void adapter_whitelist_add(struct btd_adapter *adapter, struct btd_device *dev)
{
	struct mgmt_cp_add_device cp;

	if (!kernel_conn_control)
		return;

	memset(&cp, 0, sizeof(cp));
	bacpy(&cp.addr.bdaddr, device_get_address(dev));
	cp.addr.type = BDADDR_BREDR;
	cp.action = 0x01;

	mgmt_send(adapter->mgmt, MGMT_OP_ADD_DEVICE,
				adapter->dev_id, sizeof(cp), &cp,
				add_whitelist_complete, adapter, NULL);
}
```


## RSSI

[Amlogic.md](Amlogic.md)