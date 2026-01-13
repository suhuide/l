```c
cat /sys/kernel/debug/pinctrl/pinctrl-handle
Requested pin control handlers their pinmux maps:
device: soc:vcc_sdc4_3v3 current state: default
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio19 (19) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio19 (19)config 00000105
config 00000809
device: a9c000.qcom,qup_uart current state: default
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio26 (26) function: qup1_se7_l2 (202)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio26 (26)config 00000001
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio27 (27) function: qup1_se7_l3 (203)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio27 (27)config 00000001
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio26 (26) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio27 (27) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio26 (26)config 00000103
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio27 (27)config 00000103
config 00000209
device: 8804000.sdhci current state: sleep
  state: default
    type: CONFIGS_GROUP controller f000000.pinctrl group sdc2_clk (211)config 00000001
config 00001009
    type: CONFIGS_GROUP controller f000000.pinctrl group sdc2_cmd (212)config 00000105
config 00000a09
    type: CONFIGS_GROUP controller f000000.pinctrl group sdc2_data (213)config 00000105
config 00000a09
    type: MUX_GROUP controller f000000.pinctrl group: gpio80 (80) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio80 (80)config 00000105
config 00000809
  state: sleep
    type: CONFIGS_GROUP controller f000000.pinctrl group sdc2_clk (211)config 00000001
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group sdc2_cmd (212)config 00000105
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group sdc2_data (213)config 00000105
config 00000209
device: soc:gpio_key current state: default
  state: default
    type: MUX_GROUP controller c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800 group: gpio6 (5) function: normal (0)
    type: CONFIGS_GROUP controller c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800 group gpio6 (5)config 00000105
config 0000010c
config 00000114
device: 8844000.sdhci current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio50 (50) function: sdc4_clk (246)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio50 (50)config 00000001
config 00001009
    type: MUX_GROUP controller f000000.pinctrl group: gpio51 (51) function: sdc4_cmd (247)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio51 (51)config 00000105
config 00000a09
    type: MUX_GROUP controller f000000.pinctrl group: gpio89 (89) function: sdc40 (242)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio89 (89)config 00000105
config 00000a09
    type: MUX_GROUP controller f000000.pinctrl group: gpio90 (90) function: sdc41 (243)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio90 (90)config 00000105
config 00000a09
    type: MUX_GROUP controller f000000.pinctrl group: gpio48 (48) function: sdc42 (244)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio48 (48)config 00000105
config 00000a09
    type: MUX_GROUP controller f000000.pinctrl group: gpio49 (49) function: sdc43 (245)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio49 (49)config 00000105
config 00000a09
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio50 (50) function: sdc4_clk (246)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio50 (50)config 00000001
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio51 (51) function: sdc4_cmd (247)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio51 (51)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio89 (89) function: sdc40 (242)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio89 (89)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio90 (90) function: sdc41 (243)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio90 (90)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio48 (48) function: sdc42 (244)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio48 (48)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio49 (49) function: sdc43 (245)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio49 (49)config 00000105
config 00000209
device: c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800 current state: default
  state: default
    type: MUX_GROUP controller c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800 group: gpio3 (2) function: func1 (2)
    type: CONFIGS_GROUP controller c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800 group gpio3 (2)config 00000001
config 0000000c
config 00000112
config 00000014
device: a88000.qcom,qup_uart current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio38 (38) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio38 (38)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio39 (39) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio39 (39)config 00000103
config 00000209
  state: active
    type: MUX_GROUP controller f000000.pinctrl group: gpio38 (38) function: qup1_se2_l2 (182)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio38 (38)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio39 (39) function: qup1_se2_l3 (183)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio39 (39)config 00000001
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio38 (38) function: qup1_se2_l2 (182)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio38 (38)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio39 (39) function: qup1_se2_l3 (183)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio39 (39)config 00000001
config 00000209
  state: shutdown
    type: MUX_GROUP controller f000000.pinctrl group: gpio38 (38) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio38 (38)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio39 (39) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio39 (39)config 00000103
config 00000209
device: 1c00000.qcom,pcie current state: default
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio94 (94) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio94 (94)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio95 (95) function: pcie0_clk_req_n (98)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio95 (95)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio96 (96) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio96 (96)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio18 (18) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio18 (18)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio15 (15) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio15 (15)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio94 (94) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio94 (94)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio95 (95) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio95 (95)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio96 (96) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio96 (96)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio18 (18) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio18 (18)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio15 (15) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio15 (15)config 00000105
config 00000209
device: 894000.qcom,qup_uart current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio82 (82) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio82 (82)c[ 2047.701006][T17407] libprocessgroup: JoinCgroup: controller schedtune is not found
 onfig 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio83 (83) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio83 (83)config 00000103
config 00000209
  state: active
    type: MUX_GROUP controller f000000.pinctrl group: gpio82 (82) function: qup2_se5_l2 (231)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio82 (82)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio83 (83) function: qup2_se5_l3 (232)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio83 (83)config 00000001
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio82 (82) function: qup2_se5_l2 (231)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio82 (82)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio83 (83) function: qup2_se5_l3 (232)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio83 (83)config 00000001
config 00000209
  state: shutdown
    type: MUX_GROUP controller f000000.pinctrl group: gpio82 (82) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio82 (82)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio83 (83) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio83 (83)config 00000103
config 00000209
device: 898000.qcom,qup_uart current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio76 (76) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio76 (76)config 00000001
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio77 (77) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio77 (77)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio78 (78) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio78 (78)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio79 (79) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio79 (79)config 00000103
config 00000209
  state: active
    type: MUX_GROUP controller f000000.pinctrl group: gpio76 (76) function: qup2_se6_l0 (233)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio76 (76)config 00000001
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio77 (77) function: qup2_se6_l1 (234)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio77 (77)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio78 (78) function: qup2_se6_l2 (235)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio78 (78)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio79 (79) function: qup2_se6_l3 (236)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio79 (79)config 00000001
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio76 (76) function: qup2_se6_l0 (233)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio76 (76)config 00000001
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio77 (77) function: qup2_se6_l1 (234)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio77 (77)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio78 (78) function: qup2_se6_l2 (235)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio78 (78)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio79 (79) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio79 (79)config 00000103
config 00000209
  state: shutdown
    type: MUX_GROUP controller f000000.pinctrl group: gpio76 (76) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio76 (76)config 00000001
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio77 (77) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio77 (77)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio78 (78) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio78 (78)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio79 (79) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio79 (79)config 00000103
config 00000209
device: 988000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio20 (20) function: i2chub0_se2_l0 (63)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio20 (20)config 00000105
config 00000209
config 00000082
    type: MUX_GROUP controller f000000.pinctrl group: gpio21 (21) function: i2chub0_se2_l1 (64)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio21 (21)config 00000105
config 00000209
config 00000082
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio20 (20) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio21 (21) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio20 (20)config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio21 (21)config 00000209
device: 990000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio4 (4) function: i2chub0_se4_l0 (67)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio4 (4)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio5 (5) function: i2chub0_se4_l1 (68)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio5 (5)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio4 (4) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio5 (5) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio4 (4)config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio5 (5)config 00000209
device: 994000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio6 (6) function: i2chub0_se5_l0 (69)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio6 (6)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio7 (7) function: i2chub0_se5_l1 (70)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio7 (7)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio6 (6) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio7 (7) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio6 (6)config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio7 (7)config 00000209
device: a84000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio32 (32) function: qup1_se1_l0 (175)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio32 (32)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio33 (33) function: qup1_se1_l1 (176)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio33 (33)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio32 (32) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio33 (33) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio32 (32)config 00000001
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio33 (33)config 00000001
config 00000209
device: a90000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio44 (44) function: qup1_se4_l0 (188)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio44 (44)config 00000105
config 00000209
config 00000082
    type: MUX_GROUP controller f000000.pinctrl group: gpio45 (45) function: qup1_se4_l1 (189)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio45 (45)config 00000105
config 00000209
config 00000082
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio44 (44) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio45 (45) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio44 (44)config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio45 (45)config 00000209
device: a94000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio52 (52) function: qup1_se5_l0 (192)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio52 (52)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio53 (53) function: qup1_se5_l1 (193)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio53 (53)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio52 (52) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio53 (53) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio52 (52)config 00000001
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio53 (53)config 00000001
config 00000209
device: 11-001c current state: default
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio11 (11) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio11 (11)config 00000103
config 00000209
config 0000010c
device: 880000.spi current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio57 (57) function: qup2_se0_l1_mira (207)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio57 (57)config 00000103
config 00000609
    type: MUX_GROUP controller f000000.pinctrl group: gpio56 (56) function: qup2_se0_l0_mira (205)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio56 (56)config 00000103
config 00000609
    type: MUX_GROUP controller f000000.pinctrl group: gpio58 (58) function: qup2_se0_l2_mira (209)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio58 (58)config 00000103
config 00000609
    type: MUX_GROUP controller f000000.pinctrl group: gpio59 (59) function: qup2_se0_l3_mira (211)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio59 (59)config 00000103
config 00000609
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio56 (56) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio57 (57) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio58 (58) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio59 (59) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio56 (56)config 00000103
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio57 (57)config 00000103
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio58 (58)config 00000103
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio59 (59)config 00000103
config 00000209
device: soc:display_gpio_regulator@1 current state: default
  state: default
    type: MUX_GROUP controller c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800 group: gpio11 (10) function: normal (0)
    type: CONFIGS_GROUP controller c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800 group gpio11 (10)config 00000001
config 0000000c
config 00000112
config 00000114
config 00000381
device: 884000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio60 (60) function: qup2_se1_l0 (213)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio60 (60)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio61 (61) function: qup2_se1_l1 (214)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio61 (61)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio60 (60) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio61 (61) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio60 (60)config 00000001
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio61 (61)config 00000001
config 00000209
device: 888000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio64 (64) function: qup2_se2_l0 (217)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio64 (64)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio65 (65) function: qup2_se2_l1 (218)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio65 (65)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio64 (64) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio65 (65) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio64 (64)config 00000001
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio65 (65)config 00000001
config 00000209
device: 88c000.i2c current state: sleep
  state: default
    type: MUX_GROUP controller f000000.pinctrl group: gpio68 (68) function: qup2_se3_l0 (221)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio68 (68)config 00000105
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio69 (69) function: qup2_se3_l1 (222)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio69 (69)config 00000105
config 00000209
  state: sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio68 (68) function: gpio (0)
    type: MUX_GROUP controller f000000.pinctrl group: gpio69 (69) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio68 (68)config 00000001
config 00000209
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio69 (69)config 00000001
config 00000209
device: soc:qcom,dsi-display-primary current state: panel_active
  state: panel_active
    type: MUX_GROUP controller f000000.pinctrl group: gpio202 (202) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio202 (202)config 00000001
config 00000809
    type: MUX_GROUP controller f000000.pinctrl group: gpio86 (86) function: mdp_vsync (89)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio86 (86)config 00000103
config 00000209
  state: panel_suspend
    type: MUX_GROUP controller f000000.pinctrl group: gpio202 (202) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio202 (202)config 00000103
config 00000209
    type: MUX_GROUP controller f000000.pinctrl group: gpio86 (86) function: mdp_vsync (89)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio86 (86)config 00000103
config 00000209
  state: pwm_pin
    type: MUX_GROUP controller c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800 group: gpio9 (8) function: func1 (2)
    type: CONFIGS_GROUP controller c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800 group gpio9 (8)config 00000111
config 00000014
config 00000381
device: soc:spf_core_platform:fm_i2s1_pinctrl current state: aud_sleep
  state: aud_active
    type: MUX_GROUP controller f000000.pinctrl group: gpio121 (121) function: i2s1_sck (85)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio121 (121)config 00000001
config 00000809
    type: MUX_GROUP controller f000000.pinctrl group: gpio123 (123) function: i2s1_ws (86)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio123 (123)config 00000001
config 00000809
    type: MUX_GROUP controller f000000.pinctrl group: gpio122 (122) function: i2s1_data0 (83)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio122 (122)config 00000001
config 00000809
    type: MUX_GROUP controller f000000.pinctrl group: gpio124 (124) function: i2s1_data1 (84)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio124 (124)config 00000001
config 00000809
  state: aud_sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio121 (121) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio121 (121)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller f000000.pinctrl group: gpio123 (123) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio123 (123)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller f000000.pinctrl group: gpio122 (122) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio122 (122)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller f000000.pinctrl group: gpio124 (124) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio124 (124)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:rx_swr_clk_data_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio3 (3) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio3 (3)config 00000001
config 00000209
config 00000117
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio4 (4) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio4 (4)config 00000000
config 00000209
config 00000117
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio5 (5) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio5 (5)config 00000000
config 00000209
config 00000117
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio3 (3) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio3 (3)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio4 (4) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio4 (4)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio5 (5) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio5 (5)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:tx_swr_clk_data_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio14 (14) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio14 (14)config 00000000
config 00000209
config 00000117
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio14 (14) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio14 (14)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:cdc_dmic01_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio6 (6) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio6 (6)config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio7 (7) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio7 (7)config 00000209
config 0000010c
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio6 (6) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio6 (6)config 00000001
config 00000209
config 00000011
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio7 (7) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio7 (7)config 00000209
config 0000010c
device: soc:spf_core_platform:cdc_dmic23_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio8 (8) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio8 (8)config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio9 (9) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio9 (9)config 00000209
config 0000010c
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio8 (8) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio8 (8)config 00000001
config 00000209
config 00000011
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio9 (9) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio9 (9)config 00000209
config 0000010c
device: soc:spf_core_platform:cdc_dmic45_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio12 (12) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio12 (12)config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio13 (13) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio13 (13)config 00000209
config 0000010c
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio12 (12) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio12 (12)config 00000001
config 00000209
config 00000011
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio13 (13) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio13 (13)config 00000209
config 0000010c
device: soc:spf_core_platform:cdc_dmic67_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio17 (17) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio17 (17)config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio18 (18) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio18 (18)config 00000209
config 0000010c
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio17 (17) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio17 (17)config 00000001
config 00000209
config 00000011
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio18 (18) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000[ 2049.839391][   T95] PMIC_GLINK: pmic_glink_rx_callback: No client present for 32778
 group gpio18 (18)config 00000209
config 0000010c
device: soc:spf_core_platform:msm_cdc_pinctrl_0 current state: aud_sleep
  state: aud_active
    type: MUX_GROUP controller f000000.pinctrl group: gpio126 (126) function: i2s0_sck (81)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio126 (126)config 00000001
config 00000409
    type: MUX_GROUP controller f000000.pinctrl group: gpio129 (129) function: i2s0_ws (82)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio129 (129)config 00000001
config 00000409
    type: MUX_GROUP controller f000000.pinctrl group: gpio127 (127) function: i2s0_data0 (79)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio127 (127)config 00000103
config 00000409
    type: MUX_GROUP controller f000000.pinctrl group: gpio128 (128) function: i2s0_data1 (80)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio128 (128)config 00000103
config 00000409
  state: aud_sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio126 (126) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio126 (126)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller f000000.pinctrl group: gpio129 (129) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio129 (129)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller f000000.pinctrl group: gpio127 (127) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio127 (127)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller f000000.pinctrl group: gpio128 (128) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio128 (128)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:msm_cdc_pinctrl_0_mclk current state: aud_sleep
  state: aud_active
    type: MUX_GROUP controller f000000.pinctrl group: gpio125 (125) function: audio_ext_mclk0 (14)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio125 (125)config 00000001
config 00000409
  state: aud_sleep
    type: MUX_GROUP controller f000000.pinctrl group: gpio125 (125) function: gpio (0)
    type: CONFIGS_GROUP controller f000000.pinctrl group gpio125 (125)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:quat_mi2s_pinctrl current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio0 (0) function: func2 (2)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio0 (0)config 00000001
config 00000809
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio1 (1) function: func2 (2)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio1 (1)config 00000001
config 00000809
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio2 (2) function: func2 (2)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio2 (2)config 00000001
config 00000809
config 00000111
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio0 (0) function: func2 (2)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio0 (0)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio1 (1) function: func2 (2)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio1 (1)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio2 (2) function: func2 (2)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio2 (2)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:msm_cdc_pinctrl_2 current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio10 (10) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio10 (10)config 00000001
config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio11 (11) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio11 (11)config 00000001
config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio15 (15) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio15 (15)config 00000001
config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio16 (16) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio16 (16)config 00000001
config 00000209
config 00000111
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio10 (10) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio10 (10)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio11 (11) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio11 (11)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio15 (15) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio15 (15)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio16 (16) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio16 (16)config 00000103
config 00000209
config 0000010c
device: soc:spf_core_platform:msm_cdc_pinctrl_4 current state: none
  state: aud_active
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio19 (19) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio19 (19)config 00000001
config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio20 (20) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio20 (20)config 00000001
config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio21 (21) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio21 (21)config 00000001
config 00000209
config 00000111
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio22 (22) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio22 (22)config 00000001
config 00000209
config 00000111
  state: aud_sleep
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio19 (19) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio19 (19)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio20 (20) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio20 (20)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio21 (21) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio21 (21)config 00000103
config 00000209
config 0000010c
    type: MUX_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group: gpio22 (22) function: func1 (1)
    type: CONFIGS_GROUP controller soc:spf_core_platform:lpi_pinctrl@6E80000 group gpio22 (22)config 00000103
config 00000209
config 0000010c
```
```c
cat pinctrl-maps
Pinctrl maps:
device soc:vcc_sdc4_3v3
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio19
function gpio

device soc:vcc_sdc4_3v3
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio19
config 00000105
config 00000809

device a9c000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio26
function qup1_se7_l2

device a9c000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio26
config 00000001
config 00000209

device a9c000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio27
function qup1_se7_l3

device a9c000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio27
config 00000001
config 00000209

device a9c000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio26
function gpio

device a9c000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio27
function gpio

device a9c000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio26
config 00000103
config 00000209

device a9c000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio27
config 00000103
config 00000209

device 8804000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group sdc2_clk
config 00000001
config 00001009

device 8804000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group sdc2_cmd
config 00000105
config 00000a09

device 8804000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group sdc2_data
config 00000105
config 00000a09

device 8804000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio80
function gpio

device 8804000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio80
config 00000105
config 00000809

device 8804000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group sdc2_clk
config 00000001
config 00000209

device 8804000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group sdc2_cmd
config 00000105
config 00000209

device 8804000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group sdc2_data
config 00000105
config 00000209

device 1c00000.qcom,pcie
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio94
function gpio

device 1c00000.qcom,pcie
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio94
config 00000103
config 00000209

device 1c00000.qcom,pcie
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio95
function pcie0_clk_req_n

device 1c00000.qcom,pcie
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio95
config 00000105
config 00000209

device 1c00000.qcom,pcie
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio96
function gpio

device 1c00000.qcom,pcie
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio96
config 00000105
config 00000209

device 1c00000.qcom,pcie
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio18
function gpio

device 1c00000.qcom,pcie
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio18
config 00000105
config 00000209

device 1c00000.qcom,pcie
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio15
function gpio

device 1c00000.qcom,pcie
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio15
config 00000105
config 00000209

device 1c00000.qcom,pcie
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio94
function gpio

device 1c00000.qcom,pcie
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio94
config 00000103
config 00000209

device 1c00000.qcom,pcie
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio95
function gpio

device 1c00000.qcom,pcie
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio95
config 00000105
config 00000209

device 1c00000.qcom,pcie
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio96
function gpio

device 1c00000.qcom,pcie
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio96
config 00000105
config 00000209

device 1c00000.qcom,pcie
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio18
function gpio

device 1c00000.qcom,pcie
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio18
config 00000105
config 00000209

device 1c00000.qcom,pcie
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio15
function gpio

device 1c00000.qcom,pcie
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio15
config 00000105
config 00000209

device soc:gpio_key
state default
type MUX_GROUP (2)
controlling device c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800
group gpio6
function normal

device soc:gpio_key
state default
type CONFIGS_GROUP (4)
controlling device c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800
group gpio6
config 00000105
config 0000010c
config 00000114

device 8844000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio50
function sdc4_clk

device 8844000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio50
config 00000001
config 00001009

device 8844000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio51
function sdc4_cmd

device 8844000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio51
config 00000105
config 00000a09

device 8844000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio89
function sdc40

device 8844000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio89
config 00000105
config 00000a09

device 8844000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio90
function sdc41

device 8844000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio90
config 00000105
config 00000a09

device 8844000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio48
function sdc42

device 8844000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio48
config 00000105
config 00000a09

device 8844000.sdhci
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio49
fu[  356.893161][   T95] PMIC_GLINK: pmic_glink_rx_callback: No client present for 32778
nction sdc43

device 8844000.sdhci
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio49
config 00000105
config 00000a09

device 8844000.sdhci
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio50
function sdc4_clk

device 8844000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio50
config 00000001
config 00000209

device 8844000.sdhci
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio51
function sdc4_cmd

device 8844000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio51
config 00000105
config 00000209

device 8844000.sdhci
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio89
function sdc40

device 8844000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio89
config 00000105
config 00000209

device 8844000.sdhci
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio90
function sdc41

device 8844000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio90
config 00000105
config 00000209

device 8844000.sdhci
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio48
function sdc42

device 8844000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio48
config 00000105
config 00000209

device 8844000.sdhci
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio49
function sdc43

device 8844000.sdhci
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio49
config 00000105
config 00000209

device c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800
state default
type MUX_GROUP (2)
controlling device c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800
group gpio3
function func1

device c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800
state default
type CONFIGS_GROUP (4)
controlling device c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800
group gpio3
config 00000001
config 0000000c
config 00000112
config 00000014

device soc:display_gpio_regulator@1
state default
type MUX_GROUP (2)
controlling device c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800
group gpio11
function normal

device soc:display_gpio_regulator@1
state default
type CONFIGS_GROUP (4)
controlling device c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800
group gpio11
config 00000001
config 0000000c
config 00000112
config 00000114
config 00000381

device a88000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio38
function gpio

device a88000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio38
config 00000105
config 00000209

device a88000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio39
function gpio

device a88000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio39
config 00000103
config 00000209

device a88000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio38
function qup1_se2_l2

device a88000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio38
config 00000105
config 00000209

device a88000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio39
function qup1_se2_l3

device a88000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio39
config 00000001
config 00000209

device a88000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio38
function qup1_se2_l2

device a88000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio38
config 00000105
config 00000209

device a88000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio39
function qup1_se2_l3

device a88000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio39
config 00000001
config 00000209

device a88000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio38
function gpio

device a88000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio38
config 00000105
config 00000209

device a88000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio39
function gpio

device a88000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio39
config 00000103
config 00000209

device 988000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio20
function i2chub0_se2_l0

device 988000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio20
config 00000105
config 00000209
config 00000082

device 988000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio21
function i2chub0_se2_l1

device 988000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio21
config 00000105
config 00000209
config 00000082

device 988000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio20
function gpio

device 988000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio21
function gpio

device 988000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio20
config 00000209

device 988000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio21
config 00000209

device 894000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio82
function gpio

device 894000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio82
config 00000105
config 00000209

device 894000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio83
function gpio

device 894000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio83
config 00000103
config 00000209

device 894000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio82
function qup2_se5_l2

device 894000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio82
config 00000105
config 00000209

device 894000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio83
function qup2_se5_l3

device 894000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio83
config 00000001
config 00000209

device 894000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio82
function qup2_se5_l2

device 894000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio82
config 00000105
config 00000209

device 894000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio83
function qup2_se5_l3

device 894000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio83
config 00000001
config 00000209

device 894000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio82
function gpio

device 894000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio82
config 00000105
config 00000209

device 894000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio83
function gpio

device 894000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio83
config 00000103
config 00000209

device 11-001c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio11
function gpio

device 11-001c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio11
config 00000103
config 00000209
config 0000010c

device 898000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio76
function gpio

device 898000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio76
config 00000001
config 00000209

device 898000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio77
function gpio

device 898000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio77
config 00000103
config 00000209

device 898000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio78
function gpio

device 898000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio78
config 00000105
config 00000209

device 898000.qcom,qup_uart
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio79
function gpio

device 898000.qcom,qup_uart
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio79
config 00000103
config 00000209

device 898000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio76
function qup2_se6_l0

device 898000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio76
config 00000001
config 00000209

device 898000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio77
function qup2_se6_l1

device 898000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio77
config 00000103
config 00000209

device 898000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio78
function qup2_se6_l2

device 898000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio78
config 00000105
config 00000209

device 898000.qcom,qup_uart
state active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio79
function qup2_se6_l3

device 898000.qcom,qup_uart
state active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio79
config 00000001
config 00000209

device 898000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio76
function qup2_se6_l0

device 898000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio76
config 00000001
config 00000209

device 898000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio77
function qup2_se6_l1

device 898000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio77
config 00000103
config 00000209

device 898000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio78
function qup2_se6_l2

device 898000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio78
config 00000105
config 00000209

device 898000.qcom,qup_uart
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio79
function gpio

device 898000.qcom,qup_uart
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio79
config 00000103
config 00000209

device 898000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio76
function gpio

device 898000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio76
config 00000001
config 00000209

device 898000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio77
function gpio

device 898000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio77
config 00000103
config 00000209

device 898000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio78
function gpio

device 898000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio78
config 00000105
config 00000209

device 898000.qcom,qup_uart
state shutdown
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio79
function gpio

device 898000.qcom,qup_uart
state shutdown
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio79
config 00000103
config 00000209

device 990000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio4
function i2chub0_se4_l0

device 990000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio4
config 00000105
config 00000209

device 990000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio5
function i2chub0_se4_l1

device 990000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio5
config 00000105
config 00000209

device 990000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio4
function gpio

device 990000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio5
function gpio

device 990000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio4
config 00000209

device 990000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio5
config 00000209

device 880000.spi
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio57
function qup2_se0_l1_mira

device 880000.spi
state default
type CONFIGS_GROUP (4)
con[  358.184637][ T5242] libprocessgroup: JoinCgroup: controller schedtune is not found
\0trolling device f000000.pinctrl
group gpio57
config 00000103
config 00000609

device 880000.spi
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio56
function qup2_se0_l0_mira

device 880000.spi
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio56
config 00000103
config 00000609

device 880000.spi
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio58
function qup2_se0_l2_mira

device 880000.spi
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio58
config 00000103
config 00000609

device 880000.spi
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio59
function qup2_se0_l3_mira

device 880000.spi
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio59
config 00000103
config 00000609

device 880000.spi
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio56
function gpio

device 880000.spi
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio57
function gpio

device 880000.spi
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio58
function gpio

device 880000.spi
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio59
function gpio

device 880000.spi
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio56
config 00000103
config 00000209

device 880000.spi
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio57
config 00000103
config 00000209

device 880000.spi
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio58
config 00000103
config 00000209

device 880000.spi
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio59
config 00000103
config 00000209

device 994000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio6
function i2chub0_se5_l0

device 994000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio6
config 00000105
config 00000209

device 994000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio7
function i2chub0_se5_l1

device 994000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio7
config 00000105
config 00000209

device 994000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio6
function gpio

device 994000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio7
function gpio

device 994000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio6
config 00000209

device 994000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio7
config 00000209

device a84000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio32
function qup1_se1_l0

device a84000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio32
config 00000105
config 00000209

device a84000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio33
function qup1_se1_l1

device a84000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio33
config 00000105
config 00000209

device a84000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio32
function gpio

device a84000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio33
function gpio

device a84000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio32
config 00000001
config 00000209

device a84000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio33
config 00000001
config 00000209

device a90000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio44
function qup1_se4_l0

device a90000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio44
config 00000105
config 00000209
config 00000082

device a90000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio45
function qup1_se4_l1

device a90000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio45
config 00000105
config 00000209
config 00000082

device a90000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio44
function gpio

device a90000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio45
function gpio

device a90000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio44
config 00000209

device a90000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio45
config 00000209

device a94000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio52
function qup1_se5_l0

device a94000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio52
config 00000105
config 00000209

device a94000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio53
function qup1_se5_l1

device a94000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio53
config 00000105
config 00000209

device a94000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio52
function gpio

device a94000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio53
function gpio

device a94000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio52
config 00000001
config 00000209

device a94000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio53
config 00000001
config 00000209

device 884000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio60
function qup2_se1_l0

device 884000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio60
config 00000105
config 00000209

device 884000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio61
function qup2_se1_l1

device 884000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio61
config 00000105
config 00000209

device 884000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio60
function gpio

device 884000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio61
function gpio

device 884000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio60
config 00000001
config 00000209

device 884000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio61
config 00000001
config 00000209

device 888000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio64
function qup2_se2_l0

device 888000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio64
config 00000105
config 00000209

device 888000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio65
function qup2_se2_l1

device 888000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio65
config 00000105
config 00000209

device 888000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio64
function gpio

device 888000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio65
function gpio

device 888000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio64
config 00000001
config 00000209

device 888000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio65
config 00000001
config 00000209

device 88c000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio68
function qup2_se3_l0

device 88c000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio68
config 00000105
config 00000209

device 88c000.i2c
state default
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio69
function qup2_se3_l1

device 88c000.i2c
state default
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio69
config 00000105
config 00000209

device 88c000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio68
function gpio

device 88c000.i2c
state sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio69
function gpio

device 88c000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio68
config 00000001
config 00000209

device 88c000.i2c
state sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio69
config 00000001
config 00000209

device soc:qcom,dsi-display-primary
state panel_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio202
function gpio

device soc:qcom,dsi-display-primary
state panel_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio202
config 00000001
config 00000809

device soc:qcom,dsi-display-primary
state panel_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio86
function mdp_vsync

device soc:qcom,dsi-display-primary
state panel_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio86
config 00000103
config 00000209

device soc:qcom,dsi-display-primary
state panel_suspend
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio202
function gpio

device soc:qcom,dsi-display-primary
state panel_suspend
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio202
config 00000103
config 00000209

device soc:qcom,dsi-display-primary
state panel_suspend
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio86
function mdp_vsync

device soc:qcom,dsi-display-primary
state panel_suspend
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio86
config 00000103
config 00000209

device soc:qcom,dsi-display-primary
state pwm_pin
type MUX_GROUP (2)
controlling device c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800
group gpio9
function func1

device soc:qcom,dsi-display-primary
state pwm_pin
type CONFIGS_GROUP (4)
controlling device c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800
group gpio9
config 00000111
config 00000014
config 00000381

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio121
function i2s1_sck

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio121
config 00000001
config 00000809

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio123
function i2s1_ws

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio123
config 00000001
config 00000809

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio122
function i2s1_data0

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio122
config 00000001
config 00000809

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio124
function i2s1_data1

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio124
config 00000001
config 00000809

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio121
function gpio

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio121
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio123
function gpio

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio123
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio122
function gpio

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio122
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio124
function gpio

device soc:spf_core_platform:fm_i2s1_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio124
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio3
function func1

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio3
config 00000001
config 00000209
config 00000117

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio4
function func1

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio4
config 00000000
config 00000209
config 00000117

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio5
function func1

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio5
config 00000000
config 00000209
config 00000117

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio3
function func1

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio3
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio4
function func1

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio4
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio5
function func1

device soc:spf_core_platform:rx_swr_clk_data_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio5
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:tx_swr_clk_data_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio14
function func1

device soc:spf_core_platform:tx_swr_clk_data_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio14
config 00000000
config 00000209
config 00000117

device soc:spf_core_platform:tx_swr_clk_data_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio14
function func1

device soc:spf_core_platform:tx_swr_clk_data_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio14
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio6
function func1

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio6
config 00000209
config 00000111

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio7
function func1

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio7
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio6
function func1

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio6
config 00000001
config 00000209
config 00000011

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio7
function func1

device soc:spf_core_platform:cdc_dmic01_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio7
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio8
function func1

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio8
config 00000209
config 00000111

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio9
function func1

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio9
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio8
function func1

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio8
config 00000001
config 00000209
config 00000011

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio9
function func1

device soc:spf_core_platform:cdc_dmic23_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio9
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio12
function func1

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio12
config 00000209
config 00000111

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio13
function func1

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio13
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio12
function func1

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio12
config 00000001
config 00000209
config 00000011

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio13
function func1

device soc:spf_core_platform:cdc_dmic45_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio13
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio17
function func1

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio17
config 00000209
config 00000111

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio18
function func1

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio18
config 00000209
config 0000010c

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio17
function func1

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio17
config 00000001
config 00000209
config 00000011

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio18
function func1

device soc:spf_core_platform:cdc_dmic67_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio18
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio126
function i2s0_sck

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio126
config 00000001
config 00000409

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio129
function i2s0_ws

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio129
config 00000001
config 00000409

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio127
function i2s0_data0

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio127
config 00000103
config 00000409

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio128
function i2s0_data1

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio128
config 00000103
config 00000409

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio126
function gpio

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio126
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio129
function gpio

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio129
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio127
function gpio

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio127
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio128
function gpio

device soc:spf_core_platform:msm_cdc_pinctrl_0
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio128
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_0_mclk
state aud_active
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio125
function audio_ext_mclk0

device soc:spf_core_platform:msm_cdc_pinctrl_0_mclk
state aud_active
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio125
config 00000001
config 00000409

device soc:spf_core_platform:msm_cdc_pinctrl_0_mclk
state aud_sleep
type MUX_GROUP (2)
controlling device f000000.pinctrl
group gpio125
function gpio

device soc:spf_core_platform:msm_cdc_pinctrl_0_mclk
state aud_sleep
type CONFIGS_GROUP (4)
controlling device f000000.pinctrl
group gpio125
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio0
function func2

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio0
config 00000001
config 00000809
config 00000111

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio1
function func2

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio1
config 00000001
config 00000809
config 00000111

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio2
function func2

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio2
config 00000001
config 00000809
config 00000111

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio0
function func2

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio0
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio1
function func2

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio1
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio2
function func2

device soc:spf_core_platform:quat_mi2s_pinctrl
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio2
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio10
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio10
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio11
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio11
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio15
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio15
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio16
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio16
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio10
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio10
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio11
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio11
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio15
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio15
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio16
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_2
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio16
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio19
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio19
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio20
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio20
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio21
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio21
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio22
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_active
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio22
config 00000001
config 00000209
config 00000111

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio19
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio19
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio20
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio20
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio21
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio21
config 00000103
config 00000209
config 0000010c

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type MUX_GROUP (2)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio22
function func1

device soc:spf_core_platform:msm_cdc_pinctrl_4
state aud_sleep
type CONFIGS_GROUP (4)
controlling device soc:spf_core_platform:lpi_pinctrl@6E80000
group gpio22
config 00000103
config 00000209
config 0000010c
```