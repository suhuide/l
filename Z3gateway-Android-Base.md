# 构建基于Android平台的Z3Gateway
## NDK 环境搭建
从[NDK Downloads](https://developer.android.google.cn/ndk/downloads?hl=en)下载。
解压安装好后，转到Z3Gateway目录下，直接命令行进行编译。  
这中间，关键点在Android.mk编写， 找个 Android.mk , 依葫芦画瓢。
要加的.c文件与头文件，要参照原本的makefile(Z3Gateway.project.mak)。
以下是我改后完整的.mk文件。 
```c
#用于在开发树中查找源文件。宏函数my-dir由编译系统提供，用于返回当前路径（即包含Android.mk文件的目录）
LOCAL_PATH := $(call my-dir)

#CLEAR_VARS由编译系统提供，用于清除许多LOCAL_XXX变量，如： LOCAL_MODULE, LOCAL_SRC_FILES, LOCAL_STATIC_LIBRARIES...
include $(CLEAR_VARS)

#编译的目标对象，LOCAL_MODULE变量必须定义，以标识在Android.mk文件中描述的每个模块。名称必须是唯一的，而且不包含任何空格
LOCAL_MODULE := z3

# 定义需要追加的宏
LOCAL_CFLAGS += \
    -DSL_COMPONENT_CATALOG_PRESENT=1 \
    -DPLATFORM_HEADER=\"platform-header.h\" \
    -DEZSP_HOST=1 \
    -DGATEWAY_APP=1 \
    -DUC_BUILD=1 \
    -DEZSP_ASH=1 \
    -DEZSP_UART=1 \
    -DUSE_ZAP_CONFIG=1 \
    -DEZSP_APPLICATION_HAS_MFGLIB_HANDLER=1 \
    -DCONFIGURATION_HEADER=\"app/framework/util/config.h\"
	
LOCAL_CFLAGS += -pie -fPIE 
LOCAL_LDFLAGS += -pie -fPIE

CFILES =  main.c
CFILES +=  app.c

CFILES +=  autogen/sl_cli_command_table.c
CFILES +=  autogen/sl_cli_instances.c
CFILES +=  autogen/sl_cluster_service_gen.c
CFILES +=  autogen/sl_event_handler.c
CFILES +=  autogen/sl_iostream_handles.c
CFILES +=  autogen/sli_cli_hooks.c
CFILES +=  autogen/zap-cli.c
CFILES +=  autogen/zap-cluster-command-parser.c
CFILES +=  autogen/zap-event.c
CFILES +=  autogen/zigbee_common_callback_dispatcher.c
CFILES +=  autogen/zigbee_host_callback_dispatcher.c
CFILES +=  autogen/zigbee_stack_callback_dispatcher.c
CFILES +=  autogen/zigbee_zcl_callback_dispatcher.c

CFILES +=  gecko_sdk_4.4.3/platform/common/src/sl_assert.c
CFILES +=  gecko_sdk_4.4.3/platform/common/src/sl_slist.c
CFILES +=  gecko_sdk_4.4.3/platform/common/src/sl_string.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli_arguments.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli_command.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli_input.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli_io.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli_threaded_host.c
CFILES +=  gecko_sdk_4.4.3/platform/service/cli/src/sl_cli_tokenize.c
CFILES +=  gecko_sdk_4.4.3/platform/service/iostream/src/sl_iostream.c
CFILES +=  gecko_sdk_4.4.3/platform/service/iostream/src/sl_iostream_stdio.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_common_ash/src/ash-common.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_hal/src/crc.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_hal/src/ember-printf-convert.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_hal/src/micro_host.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_hal/src/random.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_hal/src/system-timer.c
CFILES +=  gecko_sdk_4.4.3/platform/service/legacy_host/src/token.c
CFILES +=  gecko_sdk_4.4.3/platform/service/system/src/sl_system_init.c
CFILES +=  gecko_sdk_4.4.3/platform/service/system/src/sl_system_process_action.c
CFILES +=  gecko_sdk_4.4.3/platform/service/token_manager/src/sl_token_def.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host/ash/ash-host-ui.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host/ash/ash-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host/ezsp-host-io.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host/ezsp-host-queues.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host/ezsp-host-ui.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli/core-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli/network-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli/option-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli/security-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli/zcl-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli/zdo-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/common/zigbee_app_framework_common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/common/zigbee_app_framework_host_cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/ezsp/ezsp-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/file-descriptor-dispatch/file-descriptor-dispatch-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/file-descriptor-dispatch/file-descriptor-dispatch.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/gateway/gateway-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/gateway/gateway-support-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/gateway/gateway-support.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/ncp-configuration/ncp-configuration.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/address-table/address-table-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/address-table/address-table.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/basic/basic-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/basic/basic.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/color-control-server/color-control-server-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/color-control-server/color-control-server.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/concentrator/concentrator-support-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/concentrator/concentrator-support.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/counters/counters-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/counters/counters-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/counters/counters-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/counters/counters-ota-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/debug-print/sl_zigbee_debug_print.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ezmode-commissioning/ez-mode-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ezmode-commissioning/ez-mode.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ezmode-commissioning/ezmode-commissioning-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/green-power-client/green-power-client.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/green-power-common/green-power-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ias-zone-client/ias-zone-client-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ias-zone-client/ias-zone-client.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/identify-feedback/identify-feedback.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/identify/identify-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/identify/identify-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/identify/identify.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/level-control/level-control-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/level-control/level-control.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/manufacturing-library-cli/manufacturing-library-cli-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator-security/network-creator-security-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator-security/network-creator-security.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator/network-creator-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator/network-creator-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator/network-creator.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-steering/network-steering-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-steering/network-steering-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-steering/network-steering-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-steering/network-steering-v2.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-steering/network-steering.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/on-off/on-off-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/on-off/on-off.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-common/ota-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server-policy/ota-server-policy-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server-policy/ota-server-policy.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server/ota-server-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server/ota-server-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server/ota-server-dynamic-block-period.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server/ota-server-page-request.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server/ota-server.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-storage-common/ota-storage-common-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-storage-common/ota-storage-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-storage-posix-filesystem/ota-storage-linux.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/poll-control-client/poll-control-client-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/poll-control-client/poll-control-client.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/reporting/reporting-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/reporting/reporting-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/reporting/reporting-default-configuration.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/reporting/reporting.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/scan-dispatch/scan-dispatch.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/simple-metering-client/simple-metering-client-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/simple-metering-client/simple-metering-client-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/simple-metering-client/simple-metering-client.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/stack-diagnostics/stack-diagnostics.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/test-harness/read-write-attributes.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/test-harness/test-harness-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/test-harness/test-harness.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/time-server/time-server.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/trust-center-nwk-key-update-broadcast/trust-center-nwk-key-update-broadcast.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/trust-center-nwk-key-update-periodic/trust-center-nwk-key-update-periodic.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/trust-center-nwk-key-update-unicast/trust-center-nwk-key-update-unicast.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/update-tc-link-key/update-tc-link-key-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/update-tc-link-key/update-tc-link-key-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/update-tc-link-key/update-tc-link-key.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/zcl-framework-core/zcl-framework-core-cb.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/zcl_cli/zigbee-zcl-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/zcl_cli/zigbee-zcl-custom-cluster-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/zcl_cli/zigbee-zcl-global-cli.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/security/af-node.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/security/af-security-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/security/af-trust-center.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/security/crypto-state.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/service-function/sl_service_function.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/signature-decode/sl_signature_decode.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/af-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/af-event.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/af-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/attribute-size.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/attribute-storage.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/attribute-table.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/client-api.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/global-callback.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/global-other-callback.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/message.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/multi-network.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/print-formatter.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/print.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/process-cluster-message.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/process-global-message.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/service-discovery-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/service-discovery-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/time-util.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/util.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/framework/util/zcl-util.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/common/library.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/ezsp/ezsp-callbacks.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/ezsp/ezsp-enum-decode.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/ezsp/ezsp-frame-utilities.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/ezsp/ezsp.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/ezsp/serial-interface-uart.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/security/security-address-cache.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/serial/linux-serial.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/serial/sl_zigbee_command_interpreter.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/zigbee-framework/zigbee-device-common.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/app/util/zigbee-framework/zigbee-device-host.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/stack/config/ember-configuration-host-access.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/stack/gp/gp-util.c
CFILES +=  gecko_sdk_4.4.3/protocol/zigbee/stack/security/zigbee-security-manager-host.c
CFILES +=  gecko_sdk_4.4.3/util/silicon_labs/silabs_core/event_queue/event-queue.c
CFILES +=  gecko_sdk_4.4.3/util/silicon_labs/silabs_core/memory_manager/sl_malloc.c
CFILES +=  gecko_sdk_4.4.3/util/third_party/printf/printf.c
CFILES +=  gecko_sdk_4.4.3/util/third_party/printf/src/iostream_printf.c
LOCAL_SRC_FILES := $(CFILES)

INCLUDES = $(LOCAL_PATH)
INCLUDES += $(LOCAL_PATH)/autogen
INCLUDES += $(LOCAL_PATH)/config
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/cli/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/cli/src
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/CMSIS/Core/Include
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/emlib/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/emlib/host/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/common/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/iostream/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/legacy_common_ash/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/legacy_hal/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/util/third_party/printf
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/util/third_party/printf/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/util/silicon_labs/silabs_core
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/util/silicon_labs/silabs_core/event_queue
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/util/silicon_labs/silabs_core/memory_manager
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/system/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/address-table
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/basic
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/util/serial
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/service-function
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/color-control-server
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/concentrator
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/counters
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/debug-print
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ezmode-commissioning
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/util/ezsp
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/util/zigbee-framework
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/platform/host
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/include
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/radio/mac
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/token_manager/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/ezsp-host/ash
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/file-descriptor-dispatch
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin-host/gateway
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/green-power-client
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/gp
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/green-power-common
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/common
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/legacy_host/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/config
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/zll
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/core
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/platform/service/legacy_printf/inc
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ias-zone-client
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/identify
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/level-control
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/manufacturing-library-cli
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-creator-security
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/network-steering
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/on-off
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-common
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server-policy
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-server
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-storage-simple
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-storage-common
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/ota-storage-posix-filesystem
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/poll-control-client
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/reporting
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/scan-dispatch
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/stack/security
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/signature-decode
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/simple-metering-client
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/test-harness
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/xncp-test-harness
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/time-server
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/trust-center-nwk-key-update-broadcast
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/trust-center-nwk-key-update-unicast
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/update-tc-link-key
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/include
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/util
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/security
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/util/counters
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/cli
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/util/common
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/util/security
INCLUDES += $(LOCAL_PATH)/gecko_sdk_4.4.3/protocol/zigbee/app/framework/plugin/zcl-framework-core
LOCAL_C_INCLUDES := $(INCLUDES)

include $(BUILD_EXECUTABLE)

#APP_ABI             := armeabi-v7a x86 x86_64 arm64-v8a
APP_ABI := arm64-v8a
```

## 构建 Z3Gateway
跳转到工程目录，执行以下指令。
```c
Windows:
$ D:\android-ndk-r26d-windows\ndk-build.cmd NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk APP_PLATFORM=android-21
Linux:
$ /d/android-ndk-r26d-windows/ndk-build.cmd NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk APP_PLATFORM=android-21
MacOS:
$ /Applications/AndroidNDK11579264.app/Contents/NDK/ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk APP_PLATFORM=android-21
```
## 编译结果
```c
..\z3>D:\android-ndk-r26d-windows\ndk-build.cmd NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk APP_PLATFORM=android-21
[arm64-v8a] Compile        : z3 <= main.c
[arm64-v8a] Compile        : z3 <= app.c
[arm64-v8a] Compile        : z3 <= sl_cli_command_table.c
[arm64-v8a] Compile        : z3 <= sl_cli_instances.c
[arm64-v8a] Compile        : z3 <= sl_cluster_service_gen.c
[arm64-v8a] Compile        : z3 <= sl_event_handler.c
[arm64-v8a] Compile        : z3 <= sl_iostream_handles.c
[arm64-v8a] Compile        : z3 <= sli_cli_hooks.c
[arm64-v8a] Compile        : z3 <= zap-cli.c
[arm64-v8a] Compile        : z3 <= zap-cluster-command-parser.c
[arm64-v8a] Compile        : z3 <= zap-event.c
[arm64-v8a] Compile        : z3 <= zigbee_common_callback_dispatcher.c
[arm64-v8a] Compile        : z3 <= zigbee_host_callback_dispatcher.c
[arm64-v8a] Compile        : z3 <= zigbee_stack_callback_dispatcher.c
[arm64-v8a] Compile        : z3 <= zigbee_zcl_callback_dispatcher.c
[arm64-v8a] Compile        : z3 <= sl_assert.c
[arm64-v8a] Compile        : z3 <= sl_slist.c
[arm64-v8a] Compile        : z3 <= sl_string.c
[arm64-v8a] Compile        : z3 <= sl_cli.c
[arm64-v8a] Compile        : z3 <= sl_cli_arguments.c
[arm64-v8a] Compile        : z3 <= sl_cli_command.c
[arm64-v8a] Compile        : z3 <= sl_cli_input.c
[arm64-v8a] Compile        : z3 <= sl_cli_io.c
[arm64-v8a] Compile        : z3 <= sl_cli_threaded_host.c
[arm64-v8a] Compile        : z3 <= sl_cli_tokenize.c
[arm64-v8a] Compile        : z3 <= sl_iostream.c
[arm64-v8a] Compile        : z3 <= sl_iostream_stdio.c
[arm64-v8a] Compile        : z3 <= ash-common.c
[arm64-v8a] Compile        : z3 <= crc.c
[arm64-v8a] Compile        : z3 <= ember-printf-convert.c
[arm64-v8a] Compile        : z3 <= micro_host.c
[arm64-v8a] Compile        : z3 <= random.c
[arm64-v8a] Compile        : z3 <= system-timer.c
[arm64-v8a] Compile        : z3 <= token.c
[arm64-v8a] Compile        : z3 <= sl_system_init.c
[arm64-v8a] Compile        : z3 <= sl_system_process_action.c
[arm64-v8a] Compile        : z3 <= sl_token_def.c
[arm64-v8a] Compile        : z3 <= ash-host-ui.c
[arm64-v8a] Compile        : z3 <= ash-host.c
[arm64-v8a] Compile        : z3 <= ezsp-host-io.c
[arm64-v8a] Compile        : z3 <= ezsp-host-queues.c
[arm64-v8a] Compile        : z3 <= ezsp-host-ui.c
[arm64-v8a] Compile        : z3 <= core-cli.c
[arm64-v8a] Compile        : z3 <= network-cli.c
[arm64-v8a] Compile        : z3 <= option-cli.c
[arm64-v8a] Compile        : z3 <= security-cli.c
[arm64-v8a] Compile        : z3 <= zcl-cli.c
[arm64-v8a] Compile        : z3 <= zdo-cli.c
[arm64-v8a] Compile        : z3 <= zigbee_app_framework_common.c
[arm64-v8a] Compile        : z3 <= zigbee_app_framework_host_cb.c
[arm64-v8a] Compile        : z3 <= ezsp-cb.c
[arm64-v8a] Compile        : z3 <= file-descriptor-dispatch-cb.c
[arm64-v8a] Compile        : z3 <= file-descriptor-dispatch.c
[arm64-v8a] Compile        : z3 <= gateway-cb.c
[arm64-v8a] Compile        : z3 <= gateway-support-cli.c
[arm64-v8a] Compile        : z3 <= gateway-support.c
[arm64-v8a] Compile        : z3 <= ncp-configuration.c
[arm64-v8a] Compile        : z3 <= address-table-cli.c
[arm64-v8a] Compile        : z3 <= address-table.c
[arm64-v8a] Compile        : z3 <= basic-cb.c
[arm64-v8a] Compile        : z3 <= basic.c
[arm64-v8a] Compile        : z3 <= color-control-server-cb.c
[arm64-v8a] Compile        : z3 <= color-control-server.c
[arm64-v8a] Compile        : z3 <= concentrator-support-cli.c
[arm64-v8a] Compile        : z3 <= concentrator-support.c
[arm64-v8a] Compile        : z3 <= counters-cb.c
[arm64-v8a] Compile        : z3 <= counters-cli.c
[arm64-v8a] Compile        : z3 <= counters-host.c
[arm64-v8a] Compile        : z3 <= counters-ota-host.c
[arm64-v8a] Compile        : z3 <= sl_zigbee_debug_print.c
[arm64-v8a] Compile        : z3 <= ez-mode-cli.c
[arm64-v8a] Compile        : z3 <= ez-mode.c
[arm64-v8a] Compile        : z3 <= ezmode-commissioning-cb.c
[arm64-v8a] Compile        : z3 <= green-power-client.c
[arm64-v8a] Compile        : z3 <= green-power-common.c
[arm64-v8a] Compile        : z3 <= ias-zone-client-cli.c
[arm64-v8a] Compile        : z3 <= ias-zone-client.c
[arm64-v8a] Compile        : z3 <= identify-feedback.c
[arm64-v8a] Compile        : z3 <= identify-cb.c
[arm64-v8a] Compile        : z3 <= identify-cli.c
[arm64-v8a] Compile        : z3 <= identify.c
[arm64-v8a] Compile        : z3 <= level-control-cb.c
[arm64-v8a] Compile        : z3 <= level-control.c
[arm64-v8a] Compile        : z3 <= manufacturing-library-cli-host.c
[arm64-v8a] Compile        : z3 <= network-creator-security-cli.c
[arm64-v8a] Compile        : z3 <= network-creator-security.c
[arm64-v8a] Compile        : z3 <= network-creator-cb.c
[arm64-v8a] Compile        : z3 <= network-creator-cli.c
[arm64-v8a] Compile        : z3 <= network-creator.c
[arm64-v8a] Compile        : z3 <= network-steering-cb.c
[arm64-v8a] Compile        : z3 <= network-steering-cli.c
[arm64-v8a] Compile        : z3 <= network-steering-host.c
[arm64-v8a] Compile        : z3 <= network-steering-v2.c
[arm64-v8a] Compile        : z3 <= network-steering.c
[arm64-v8a] Compile        : z3 <= on-off-cb.c
[arm64-v8a] Compile        : z3 <= on-off.c
[arm64-v8a] Compile        : z3 <= ota-common.c
[arm64-v8a] Compile        : z3 <= ota-server-policy-cb.c
[arm64-v8a] Compile        : z3 <= ota-server-policy.c
[arm64-v8a] Compile        : z3 <= ota-server-cb.c
[arm64-v8a] Compile        : z3 <= ota-server-cli.c
[arm64-v8a] Compile        : z3 <= ota-server-dynamic-block-period.c
[arm64-v8a] Compile        : z3 <= ota-server-page-request.c
[arm64-v8a] Compile        : z3 <= ota-server.c
[arm64-v8a] Compile        : z3 <= ota-storage-common-cli.c
[arm64-v8a] Compile        : z3 <= ota-storage-common.c
[arm64-v8a] Compile        : z3 <= ota-storage-linux.c
[arm64-v8a] Compile        : z3 <= poll-control-client-cli.c
[arm64-v8a] Compile        : z3 <= poll-control-client.c
[arm64-v8a] Compile        : z3 <= reporting-cb.c
[arm64-v8a] Compile        : z3 <= reporting-cli.c
[arm64-v8a] Compile        : z3 <= reporting-default-configuration.c
[arm64-v8a] Compile        : z3 <= reporting.c
[arm64-v8a] Compile        : z3 <= scan-dispatch.c
[arm64-v8a] Compile        : z3 <= simple-metering-client-cb.c
[arm64-v8a] Compile        : z3 <= simple-metering-client-cli.c
[arm64-v8a] Compile        : z3 <= simple-metering-client.c
[arm64-v8a] Compile        : z3 <= stack-diagnostics.c
[arm64-v8a] Compile        : z3 <= read-write-attributes.c
[arm64-v8a] Compile        : z3 <= test-harness-host.c
[arm64-v8a] Compile        : z3 <= test-harness.c
[arm64-v8a] Compile        : z3 <= time-server.c
[arm64-v8a] Compile        : z3 <= trust-center-nwk-key-update-broadcast.c
[arm64-v8a] Compile        : z3 <= trust-center-nwk-key-update-periodic.c
[arm64-v8a] Compile        : z3 <= trust-center-nwk-key-update-unicast.c
[arm64-v8a] Compile        : z3 <= update-tc-link-key-cb.c
[arm64-v8a] Compile        : z3 <= update-tc-link-key-cli.c
[arm64-v8a] Compile        : z3 <= update-tc-link-key.c
[arm64-v8a] Compile        : z3 <= zcl-framework-core-cb.c
[arm64-v8a] Compile        : z3 <= zigbee-zcl-cli.c
[arm64-v8a] Compile        : z3 <= zigbee-zcl-custom-cluster-cli.c
[arm64-v8a] Compile        : z3 <= zigbee-zcl-global-cli.c
[arm64-v8a] Compile        : z3 <= af-node.c
[arm64-v8a] Compile        : z3 <= af-security-common.c
[arm64-v8a] Compile        : z3 <= af-trust-center.c
[arm64-v8a] Compile        : z3 <= crypto-state.c
[arm64-v8a] Compile        : z3 <= sl_service_function.c
[arm64-v8a] Compile        : z3 <= sl_signature_decode.c
[arm64-v8a] Compile        : z3 <= af-common.c
[arm64-v8a] Compile        : z3 <= af-event.c
[arm64-v8a] Compile        : z3 <= af-host.c
[arm64-v8a] Compile        : z3 <= attribute-size.c
[arm64-v8a] Compile        : z3 <= attribute-storage.c
[arm64-v8a] Compile        : z3 <= attribute-table.c
[arm64-v8a] Compile        : z3 <= client-api.c
[arm64-v8a] Compile        : z3 <= global-callback.c
[arm64-v8a] Compile        : z3 <= global-other-callback.c
[arm64-v8a] Compile        : z3 <= message.c
[arm64-v8a] Compile        : z3 <= multi-network.c
[arm64-v8a] Compile        : z3 <= print-formatter.c
[arm64-v8a] Compile        : z3 <= print.c
[arm64-v8a] Compile        : z3 <= process-cluster-message.c
[arm64-v8a] Compile        : z3 <= process-global-message.c
[arm64-v8a] Compile        : z3 <= service-discovery-common.c
[arm64-v8a] Compile        : z3 <= service-discovery-host.c
[arm64-v8a] Compile        : z3 <= time-util.c
[arm64-v8a] Compile        : z3 <= util.c
[arm64-v8a] Compile        : z3 <= zcl-util.c
[arm64-v8a] Compile        : z3 <= library.c
[arm64-v8a] Compile        : z3 <= ezsp-callbacks.c
[arm64-v8a] Compile        : z3 <= ezsp-enum-decode.c
[arm64-v8a] Compile        : z3 <= ezsp-frame-utilities.c
[arm64-v8a] Compile        : z3 <= ezsp.c
[arm64-v8a] Compile        : z3 <= serial-interface-uart.c
[arm64-v8a] Compile        : z3 <= security-address-cache.c
[arm64-v8a] Compile        : z3 <= linux-serial.c
[arm64-v8a] Compile        : z3 <= sl_zigbee_command_interpreter.c
[arm64-v8a] Compile        : z3 <= zigbee-device-common.c
[arm64-v8a] Compile        : z3 <= zigbee-device-host.c
[arm64-v8a] Compile        : z3 <= ember-configuration-host-access.c
[arm64-v8a] Compile        : z3 <= gp-util.c
[arm64-v8a] Compile        : z3 <= zigbee-security-manager-host.c
[arm64-v8a] Compile        : z3 <= event-queue.c
[arm64-v8a] Compile        : z3 <= sl_malloc.c
[arm64-v8a] Compile        : z3 <= printf.c
[arm64-v8a] Compile        : z3 <= iostream_printf.c
[arm64-v8a] Executable     : z3
[arm64-v8a] Install        : z3 => libs/arm64-v8a/z3
```
## 运行
可执行文件
```c
z3/obj/local/arm64-v8a/z3
```
推到Android机子里，一般直接放/data下，需要给权限。以下log是RK平台上运行的，QCOM平台一样适用。 
```c
chmod 777 z3
```
串口是/dev/ttyACM0， 波特率为115200。
```c
rk3566_r:/data # ./z3 -n 1 -f x -b 115200 -p /dev/ttyACM0
Reset info: 11 (SOFTWARE)
ezsp ver 0x0D stack type 0x02 stack ver. [7.4.3 GA build 0]
Ezsp Config: set address table size to 0x0002:Success: set
Ezsp Config: set TC addr cache to 0x0002:Success: set
Ezsp Config: set MAC indirect TX timeout to 0x1E00:Success: set
Ezsp Config: set max hops to 0x001E:Success: set
Ezsp Config: set tx power mode to 0x8000:Success: set
Ezsp Config: set supported networks to 0x0001:Success: set
Ezsp Config: set stack profile to 0x0002:Success: set
Ezsp Config: set security level to 0x0005:Success: set
Ezsp Value : set end device keep alive support mode to 0x00000003:Success: set
Ezsp Policy: set binding modify to "allow for valid endpoints & clusters only":Success: set
Ezsp Policy: set message content in msgSent to "return":Success: set
Ezsp Value : set maximum incoming transfer size to 0x00000052:Success: set
Ezsp Value : set maximum outgoing transfer size to 0x00000052:Success: set
Ezsp Value : set default timeout for transient device table to 0x00002710:Success: set
Ezsp Config: set binding table size to 0x0002:Success: set
Ezsp Config: set key table size to 0x0004:Success: set
Ezsp Config: set max end device children to 0x0006:Success: set
Ezsp Config: set aps unicast message count to 0x000A:Success: set
Ezsp Config: set broadcast table size to 0x000F:Success: set
Ezsp Config: set neighbor table size to 0x0010:Success: set
Ezsp Config: set end device poll timeout to 0x0008:Success: set
Ezsp Config: set zll group addresses to 0x0000:Success: set
Ezsp Config: set zll rssi threshold to 0xFFD8:Success: set
Ezsp Config: set transient key timeout to 0x012C:Success: set
Ezsp Config: set retry size to 0x0010:Success: set
Ezsp Endpoint 1 added, profile 0x0104, in clusters: 8, out clusters 17
Ezsp Endpoint 242 added, profile 0xA1E0, in clusters: 0, out clusters 1
Starting identifying on endpoint 0x01, identify time is 0 sec
Stopping identifying on endpoint 0x01
No endpoints identifying; stopping identification feedback.
Found 0 files

Z3Gateway>
```
下面是列举出所支持的指令。 
```c
Z3Gateway>help
help
  zcl                           ZCL commands
  info                          Prints information about the network state, clusters, and endpoints.
  libs                          Lists which optional libraries of the stack are implemented on this device.
  bsend                         Sends a message.
                                [uint8] Source endpoint
  send                          Sends a message.
                                [uint16] Destination
                                [uint8] Source endpoint
                                [uint8] Destination endpoint
  read                          Reads a message.
                                [uint8] Endpoint
                                [uint16] Cluster ID
                                [uint16] Attribute ID
                                [uint8] 1 if server direction, 0 if client direction
  write                         Writes a message.
                                [uint8] Endpoint
                                [uint16] Cluster ID
                                [uint16] Attribute ID
                                [uint8] Mask
                                [uint8] Data type
                                [hex] Data byte
  reset                         Resets the node.
  raw                           Creates a message by specifying the raw bytes. Use the send command to send the message once it has been created. Ex: raw 0x000F {00 0A 00 11 22 33 44 55} sends a message to cluster 15 (0x000F) of length 8 which includes the ZCL header.
                                [uint16] ClusterId
                                [hex] Data
  send_multicast                Sends a pre-buffered multicast message to a given group ID from a given endpoint.
                                [uint16] groupId
                                [uint8] src-endpoint
  send-using-multicast-binding  When sending using a binding, specifies whether a multicast binding should be used.
                                [uint8] useMulticastBinding
  timesync                      Sends a read attr for the time of the device specified. It sets a flag so when it gets the response it writes the time to its own time attr.
                                [uint16] Id
                                [uint8] srcEndpoint
                                [uint8] destEndpoint
  config-cca-mode               Set the configured 802.15.4 CCA mode in the radio. See documentation regarding RAIL_IEEE802154_CcaMode_t.
                                [uint8] A RAIL_IEEE802154_CcaMode_t value
  version                       Shows the version of the software.
  events                        Print active events.
  endpoints                     endpoint related commands.
  security                      security related commands
  zigbee_print
  suppress                      Commands to suppress automatic responses
  plugin
  network                       Network related commands.
  keys                          Security keys related commands.
  option                        Option related commands.
  plugin
  changekey                     changekey related commands.
  zdo                           Zdo related commands.
  print                         print related commands.
  custom                        Custom commands

```
以下是组网相关指令。
```c
network
Z3Gateway>  form                          Forms a network on a given channel, with a given TX Power and PAN ID.
                                [uint8] The channel on which to form the network
                                [int8] One-byte signed value indicating the TX Power that the radio should be set to
                                [uint16] The PAN ID on which to form the network
  join                          Joins a network on a given channel, with a given TX Power and PAN ID.
                                [uint8] The channel on which to join the network
                                [int8] One-byte signed value indicating the TX Power that the radio should be set to
                                [uint16] The PAN ID on which to join the network
  pjoin                         Turns permit joining on for the amount of time indicated.
                                [uint8] A single byte indicating how long the device should have permit joining turn on for. A value of 0xff turns permit join indefinitely.
  leave                         Leaves a network.
  rejoin                        ReJoins a network.
                                [uint8] Boolean network key availability
                                [uint32] Channel mask
  rejoin-diff-device-type       Rejoins an existing network in a secure or insecure manner with a different device type.
                                [uint8] Boolean network key availability
                                [int32] Channel mask
                                [uint8] An enumeration indicating the device type to rejoin as.The stack only accepts EMBER_END_DEVICE and EMBER_SLEEPY_END_DEVICE.
  extpanid                      Writes the extended pan ID for the device.
                                [hex] extpanid
  isopen                        Checks network pjoin status.
  broad-pjoin                   Permits joining on the network for a given number of seconds AND broadcasts a ZDO Mgmt Permit Joining request to all routers.
                                [uint8] A single byte indicating how long the device should have permit joining turned on for. A value of 0xff turns on permit join indefinitely.
  change-channel                Attempts to change device over to a different channel given in the channel argument.
                                [uint8] The channel to change to
  set                           Sets the network index used by all future CLI commands.  Before executing a CLI command, the framework switches to this network.  After the command finishes executing, the framework switches back to the previous network.  The CLI uses the same network index until the device resets or it is changed through this command.
                                [uint8] index
  init                          Initializes a network; this is a test command used for tc-swap-out testing.
  id                            Prints the current Node ID, EUI64, and Pan ID.
  change-keep-alive-mode        Switches between different keep alive modes supported by a router.
                                [uint8] Keep alive mode
  timeout-option-mask           Attempts to change the child timeout option mask to filter out undesirable values (e.g. no more than 3 days).
                                [uint16] timeout option mask
  multi-phy-start               Used to start multi-PHY interface other than native and form the network. The stack uses same PanId as native radio network.
                                [uint8] page
                                [uint8] channel
                                [int8] power
                                [uint8opt] optionsMask (Bit 0 = Routers allowed, Bit 1 = Broadcast allowed)
  multi-phy-stop                Terminates the multi-PHY interface
  find                          network find commands.

```