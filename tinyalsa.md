
使用命令前先用 tinymix  切换到音频通道  比如选通SPK  tinymix  0  SPK  
tinycap /sdcard/test.pcm -D 0 -d 0 -c 4 -r 48000 -b 32 -p 768 -n 10
-D  card        声卡
-d  device     设备
-c  channels  通道
-r  rate   采样率
-b  bits   pcm 位宽
-p  period_size   一次中断的帧数
-n  n_periods     周期数

```
odin:/ # cat /proc/asound/cards
 0 [bengalqrdsndcar]: bengal-qrd-snd- - bengal-qrd-snd-card
                      bengal-qrd-snd-card
```

1，tinycap
```
odin:/ # tinycap
Usage: tinycap file.wav [-D card] [-d device] [-c channels] [-r rate] [-b bits] [-p period_size] [-n n_periods] [-T capture time]
```

- -D  card        声卡

- -d  device     设备

- -c  channels  通道

- -r  rate   采样率

- -b  bits   pcm 位宽

- -p  period_size   一次中断的帧数

- -n  n_periods     周期数

例子： tinycap /sdcard/test.pcm -D 0 -d 0 -c 4 -r 48000 -b 32 -p 768 -n 10

声卡0；设备0；四通道；48K采样率；32位位宽；一帧数据存储大小；采样n次

2，tinyplay
参数与tinycap大体一样
```
odin:/ # tinyplay
Usage: tinyplay file.wav [-D card] [-d device] [-p period_size] [-n n_periods]
```

3，tinymix
```
odin:/ # tinymix -D 0
Mixer name: 'bengal-qrd-snd-card'
Number of controls: 189
ctl     type    num     name                                     value

0       ENUM    1       TX DMIC MUX0                             ZERO
1       ENUM    1       TX DMIC MUX1                             ZERO
2       ENUM    1       TX DMIC MUX2                             ZERO
3       ENUM    1       TX DMIC MUX3                             ZERO
4       ENUM    1       TX DEC0 MUX                              MSM_DMIC
5       ENUM    1       TX DEC1 MUX                              MSM_DMIC
6       ENUM    1       TX DEC2 MUX                              MSM_DMIC
7       ENUM    1       TX DEC3 MUX                              MSM_DMIC
8       BOOL    1       TX_AIF1_CAP Mixer DEC0                   Off
9       BOOL    1       TX_AIF1_CAP Mixer DEC1                   Off
10      BOOL    1       TX_AIF1_CAP Mixer DEC2                   Off
11      BOOL    1       TX_AIF1_CAP Mixer DEC3                   Off
12      BOOL    1       TX_AIF2_CAP Mixer DEC0                   Off
13      BOOL    1       TX_AIF2_CAP Mixer DEC1                   Off
14      BOOL    1       TX_AIF2_CAP Mixer DEC2                   Off
15      BOOL    1       TX_AIF2_CAP Mixer DEC3                   Off
16      BOOL    1       TX_AIF3_CAP Mixer DEC0                   Off
17      BOOL    1       TX_AIF3_CAP Mixer DEC1                   Off
18      BOOL    1       TX_AIF3_CAP Mixer DEC2                   Off
19      BOOL    1       TX_AIF3_CAP Mixer DEC3                   Off
20      ENUM    1       TX SMIC MUX0                             ZERO
21      ENUM    1       TX SMIC MUX1                             ZERO
22      ENUM    1       TX SMIC MUX2                             ZERO
23      ENUM    1       TX SMIC MUX3                             ZERO
24      ENUM    1       RX SWR TX MUX0                           SWR_MIC
25      ENUM    1       RX SWR TX MUX1                           SWR_MIC
26      INT     1       TX_DEC0 Volume                           84
27      INT     1       TX_DEC1 Volume                           84
28      INT     1       TX_DEC2 Volume                           84
29      INT     1       TX_DEC3 Volume                           84
30      BOOL    1       TX LPI Enable                            Off
31      ENUM    1       DEC0 MODE                                ADC_DEFAULT
32      ENUM    1       DEC1 MODE                                ADC_DEFAULT
33      ENUM    1       DEC2 MODE                                ADC_DEFAULT
34      ENUM    1       DEC3 MODE                                ADC_DEFAULT
35      BOOL    1       DEC0_BCS Switch                          Off
36      ENUM    1       BCS Channel                              CH0
37      ENUM    1       BCS CH_SEL                               SWR_MIC6
38      ENUM    1       RX_MACRO RX0 MUX                         ZERO
39      ENUM    1       RX_MACRO RX1 MUX                         ZERO
40      ENUM    1       RX_MACRO RX2 MUX                         ZERO
41      ENUM    1       RX_MACRO RX3 MUX                         ZERO
42      ENUM    1       RX_MACRO RX4 MUX                         ZERO
43      ENUM    1       RX_MACRO RX5 MUX                         ZERO
44      ENUM    1       IIR0 INP0 MUX                            ZERO
45      ENUM    1       IIR0 INP1 MUX                            ZERO
46      ENUM    1       IIR0 INP2 MUX                            ZERO
47      ENUM    1       IIR0 INP3 MUX                            ZERO
48      ENUM    1       IIR1 INP0 MUX                            ZERO
49      ENUM    1       IIR1 INP1 MUX                            ZERO
50      ENUM    1       IIR1 INP2 MUX                            ZERO
51      ENUM    1       IIR1 INP3 MUX                            ZERO
52      ENUM    1       RX MIX TX0 MUX                           ZERO
53      ENUM    1       RX MIX TX1 MUX                           ZERO
54      ENUM    1       RX MIX TX2 MUX                           ZERO
55      ENUM    1       RX INT0 DEM MUX                          NORMAL_DSM_OUT
56      ENUM    1       RX INT1 DEM MUX                          NORMAL_DSM_OUT
57      ENUM    1       RX INT0_2 MUX                            ZERO
58      ENUM    1       RX INT1_2 MUX                            ZERO
59      ENUM    1       RX INT2_2 MUX                            ZERO
60      ENUM    1       RX INT0_1 MIX1 INP0                      ZERO
61      ENUM    1       RX INT0_1 MIX1 INP1                      ZERO
62      ENUM    1       RX INT0_1 MIX1 INP2                      ZERO
63      ENUM    1       RX INT1_1 MIX1 INP0                      ZERO
64      ENUM    1       RX INT1_1 MIX1 INP1                      ZERO
65      ENUM    1       RX INT1_1 MIX1 INP2                      ZERO
66      ENUM    1       RX INT2_1 MIX1 INP0                      ZERO
67      ENUM    1       RX INT2_1 MIX1 INP1                      ZERO
68      ENUM    1       RX INT2_1 MIX1 INP2                      ZERO
69      ENUM    1       RX INT0_1 INTERP                         ZERO
70      ENUM    1       RX INT1_1 INTERP                         ZERO
71      ENUM    1       RX INT2_1 INTERP                         ZERO
72      ENUM    1       RX INT0_2 INTERP                         ZERO
73      ENUM    1       RX INT1_2 INTERP                         ZERO
74      ENUM    1       RX INT2_2 INTERP                         ZERO
75      ENUM    1       RX INT0 MIX2 INP                         ZERO
76      ENUM    1       RX INT1 MIX2 INP                         ZERO
77      ENUM    1       RX INT2 MIX2 INP                         ZERO
78      BOOL    1       RX INT2_1 VBAT RX AUX VBAT Enable        Off
79      INT     1       RX_RX0 Digital Volume                    84
80      INT     1       RX_RX1 Digital Volume                    84
81      INT     1       RX_RX2 Digital Volume                    81
82      INT     1       RX_RX0 Mix Digital Volume                84
83      INT     1       RX_RX1 Mix Digital Volume                84
84      INT     1       RX_RX2 Mix Digital Volume                84
85      BOOL    1       RX_COMP1 Switch                          Off
86      BOOL    1       RX_COMP2 Switch                          Off
87      ENUM    1       HPH Idle Detect                          OFF
88      ENUM    1       RX_EAR Mode                              OFF
89      ENUM    1       RX_HPH HD2 Mode                          OFF
90      ENUM    1       RX_HPH_PWR_MODE                          ULP
91      ENUM    1       RX_GSM mode Enable                       OFF
92      BOOL    1       RX_Softclip Enable                       Off
93      BOOL    1       AUX_HPF Enable                           On
94      INT     1       IIR0 INP0 Volume                         54
95      INT     1       IIR0 INP1 Volume                         84
96      INT     1       IIR0 INP2 Volume                         84
97      INT     1       IIR0 INP3 Volume                         84
98      INT     1       IIR1 INP0 Volume                         84
99      INT     1       IIR1 INP1 Volume                         84
100     INT     1       IIR1 INP2 Volume                         84
101     INT     1       IIR1 INP3 Volume                         84
102     BOOL    1       IIR0 Enable Band1                        Off
103     BOOL    1       IIR0 Enable Band2                        Off
104     BOOL    1       IIR0 Enable Band3                        Off
105     BOOL    1       IIR0 Enable Band4                        Off
106     BOOL    1       IIR0 Enable Band5                        Off
107     BOOL    1       IIR1 Enable Band1                        Off
108     BOOL    1       IIR1 Enable Band2                        Off
109     BOOL    1       IIR1 Enable Band3                        Off
110     BOOL    1       IIR1 Enable Band4                        Off
111     BOOL    1       IIR1 Enable Band5                        Off
112     INT     5       IIR0 Band1                               0 0 0 0 0
113     INT     5       IIR0 Band2                               0 0 0 0 0
114     INT     5       IIR0 Band3                               0 0 0 0 0
115     INT     5       IIR0 Band4                               0 0 0 0 0
116     INT     5       IIR0 Band5                               0 0 0 0 0
117     INT     5       IIR1 Band1                               0 0 0 0 0
118     INT     5       IIR1 Band2                               0 0 0 0 0
119     INT     5       IIR1 Band3                               0 0 0 0 0
120     INT     5       IIR1 Band4                               0 0 0 0 0
121     INT     5       IIR1 Band5                               0 0 0 0 0
122     ENUM    1       VA DMIC MUX0                             ZERO
123     ENUM    1       VA DMIC MUX1                             ZERO
124     ENUM    1       VA SMIC MUX0                             ZERO
125     ENUM    1       VA SMIC MUX1                             ZERO
126     ENUM    1       VA DEC0 MUX                              MSM_DMIC
127     ENUM    1       VA DEC1 MUX                              MSM_DMIC
128     BOOL    1       VA_AIF1_CAP Mixer DEC0                   Off
129     BOOL    1       VA_AIF1_CAP Mixer DEC1                   Off
130     BOOL    1       VA_AIF2_CAP Mixer DEC0                   Off
131     BOOL    1       VA_AIF2_CAP Mixer DEC1                   Off
132     BOOL    1       VA_AIF3_CAP Mixer DEC0                   Off
133     BOOL    1       VA_AIF3_CAP Mixer DEC1                   Off
134     INT     1       VA_DEC0 Volume                           84
135     INT     1       VA_DEC1 Volume                           84
136     BOOL    1       LPI Enable                               Off
137     INT     1       HPHL Impedance                           0
138     INT     1       HPHR Impedance                           0
139     INT     1       HPH Type                                 0
140     ENUM    1       EAR PA GAIN                              G_6_DB
141     ENUM    1       RX HPH Mode                              CLS_H_ULP
142     BOOL    1       HPHL_COMP Switch                         Off
143     BOOL    1       HPHR_COMP Switch                         Off
144     BOOL    1       ADC2_BCS Disable                         Off
145     INT     1       HPHL Volume                              20
146     INT     1       HPHR Volume                              20
147     INT     1       ADC1 Volume                              12
148     INT     1       ADC2 Volume                              12
149     INT     1       ADC3 Volume                              12
150     ENUM    1       ADC1 ChMap                               ZERO
151     ENUM    1       ADC2 ChMap                               ZERO
152     ENUM    1       ADC3 ChMap                               ZERO
153     ENUM    1       DMIC0 ChMap                              ZERO
154     ENUM    1       DMIC1 ChMap                              ZERO
155     ENUM    1       MBHC ChMap                               ZERO
156     ENUM    1       DMIC2 ChMap                              ZERO
157     ENUM    1       DMIC3 ChMap                              ZERO
158     ENUM    1       DMIC4 ChMap                              ZERO
159     ENUM    1       DMIC5 ChMap                              ZERO
160     ENUM    1       TX CH1 PWR                               L1
161     ENUM    1       TX CH3 PWR                               L1
162     BOOL    1       BT SOC status                            Off
163     BOOL    1       BT set feedback channel                  Off
164     BYTE    80      CODEC_DMA-LPAIF_RXTX-RX-0 Channel Map     00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
165     ENUM    1       aw87xxx_profile_switch_0                 Off
166     INT     1       aw87xxx_vmax_get_0                       0
167     ENUM    1       aw87xxx_monitor_switch_0                 Disable
168     ENUM    1       aw87xxx_spin_switch                      spin_0
169     INT     1       aw87xxx_hal_monitor_time                 3000
170     BYTE    80      CODEC_DMA-LPAIF_RXTX-RX-1 Channel Map     00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
171     BYTE    80      CODEC_DMA-LPAIF_RXTX-RX-2 Channel Map     00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
172     BYTE    80      CODEC_DMA-LPAIF_RXTX-RX-3 Channel Map     00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
173     BYTE    80      CODEC_DMA-LPAIF_RXTX-TX-3 Channel Map     00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
174     BYTE    80      CODEC_DMA-LPAIF_RXTX-TX-4 Channel Map     00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
175     BYTE    80      CODEC_DMA-LPAIF_VA-TX-0 Channel Map       00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
176     BYTE    80      CODEC_DMA-LPAIF_VA-TX-1 Channel Map       00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
177     BYTE    80      CODEC_DMA-LPAIF_VA-TX-2 Channel Map       00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
178     BYTE    80      SLIM-DEV1-RX-7 Channel Map                01  00  00  00  9d  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00
179     BYTE    80      SLIM-DEV1-TX-7 Channel Map                01  00  00  00  9f  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00
180     BYTE    80      SLIM-DEV1-TX-8 Channel Map                02  00  00  00  a0  00  00  00  a1  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00  00
  00  00  00  00  00  00  00  00  00  00  00  00  00  00
181     ENUM    1       ADC2 MUX                                 INP2
182     BOOL    1       ADC1_MIXER Switch                        Off
183     BOOL    1       ADC2_MIXER Switch                        Off
184     ENUM    1       RDAC3_MUX                                RX1
185     BOOL    1       EAR_RDAC Switch                          Off
186     BOOL    1       AUX_RDAC Switch                          Off
187     BOOL    1       HPHL_RDAC Switch                         Off
188     BOOL    1       HPHR_RDAC Switch                         Off
```

Tinymix有五个成员变量

1，ctl 成员的id号

2，type 类型( INT，BOOL，ENUM字串形式，BYTE 八位十六进制数组)

3，num  num_value(第五个成员value的个数有几个)

4，name

5，value 

实现的源码可以参考： exteral/tinyalsa/tinymix.c

实现过程：

mixer = mixer_open(card);  //通过声卡得到mixer
