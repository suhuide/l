[memo.md](memo.md)

```c
ls /sys/kernel/debug/pinctrl
cd /sys/kernel/debug/

mount -t debugfs none /sys/kernel/debug/
cat /sys/kernel/debug/gpio

cat /sys/kernel/debug/pinctrl/pinctrl-handles
cd /sys/kernel/debug/pinctrl/
dmesg | grep gpiod_request
cat /proc/kmsg | grep gpiod_request

// gpio number should base on [gpiochip9: GPIOs 216-238]/[gpiochip0: GPIOs 301-511]
# cat /sys/kernel/debug/gpio
# echo 19 /sys/class/gpio/export 
# echo out /sys/class/gpio/gpio19/direction 
# echo 0 /sys/class/gpio/gpio19/value
```

```c
[ 1122.190572][T10545] spf-core-platform soc:spf_core_platform: __spf_core_is_apm_ready: send_command ret

gpiochip9: GPIOs 216-238, parent: platform/soc:spf_core_platform:lpi_pinctrl@6E80000, soc:spf_core_platform:lpi_pinctrl@6E80000:
 gpio0   : in  0 2mA pull down
 gpio1   : in  0 2mA pull down
 gpio2   : in  0 2mA pull down
 gpio3   : in  0 2mA pull down
 gpio4   : in  0 2mA pull down
 gpio5   : in  0 2mA pull down
 gpio6   : in  0 2mA pull down
 gpio7   : in  0 2mA pull down
 gpio8   : in  0 2mA pull down
 gpio9   : in  0 2mA pull down
 gpio10  : in  0 2mA pull down
 gpio11  : in  0 2mA pull down
 gpio12  : in  0 2mA pull down
 gpio13  : in  0 2mA pull down
 gpio14  : in  0 2mA pull down
 gpio15  : in  0 2mA pull down
 gpio16  : in  0 2mA pull down
 gpio17  : in  0 2mA pull down
 gpio18  : in  0 2mA pull down
 gpio19  : in  2 2mA keeper
 gpio20  : in  2 4mA keeper
 gpio21  : in  0 2mA pull down
 gpio22  : in  0 2mA pull down

gpiochip8: GPIOs 239-244, parent: platform/c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800, c42d000.qcom,spmi:qcom,pmk8550@0:pinctrl@b800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : out  low  func1   vin-0 no pull                     push-pull  high    atest-1 dtest-0
 gpio4 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   low  normal  vin-0 pull-down 10uA              push-pull  low     atest-1 dtest-0
 gpio6 : in   high normal  vin-0 no pull                     push-pull  high    atest-1 dtest-0

gpiochip7: GPIOs 245-250, parent: platform/c42d000.qcom,spmi:qcom,pm8550vs@6:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550vs@6:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio4 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : out  high normal  vin-2 pull-down 10uA              push-pull  low     atest-1 dtest-0
 gpio6 : out  high normal  vin-2 pull-down 10uA              push-pull  low     atest-1 dtest-0

gpiochip6: GPIOs 251-256, parent: platform/c42d000.qcom,spmi:qcom,pm8550vs@4:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550vs@4:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : in   low  normal  vin-0 pull-down 10uA              push-pull  low     atest-1 dtest-0
 gpio4 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio6 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0

gpiochip5: GPIOs 257-262, parent: platform/c42d000.qcom,spmi:qcom,pm8550vs@3:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550vs@3:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio4 : out  high normal  vin-1 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio6 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
gpiochip4: GPIOs 263-268, parent: platform/c42d000.qcom,spmi:qcom,pm8550vs@2:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550vs@2:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio4 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio6 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0

gpiochip3: GPIOs 269-276, parent: platform/c42d000.qcom,spmi:qcom,pm8550ve_f@5:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550ve_f@5:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio4 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio6 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio7 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio8 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0

gpiochip2: GPIOs 277-288, parent: platform/c42d000.qcom,spmi:qcom,pm8550b@7:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550b@7:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio4 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio6 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio7 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio8 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio9 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio10: ---
 gpio11: in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio12: ---

gpiochip1: GPIOs 289-300, parent: platform/c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800, c42d000.qcom,spmi:qcom,pm8550@1:pinctrl@8800:
 gpio1 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio2 : in   low  normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio3 : out  low  normal  vin-1 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio4 : out  low  normal  vin-1 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio5 : in   high normal  vin-0 pull-up 31.5uA              push-pull  high    atest-1 dtest-0
 gpio6 : in   high normal  vin-1 pull-up 30uA                push-pull  high    atest-1 dtest-0
 gpio7 : ---
 gpio8 : in   low  normal  vin-1 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio9 : out  high normal  vin-0 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio10: in   low  normal  vin-1 pull-down 10uA              push-pull  high    atest-1 dtest-0
 gpio11: out  low  normal  vin-1 no pull                     push-pull  low     atest-1 dtest-0
 gpio12: in   high normal  vin-1 pull-up 31.5uA              push-pull  high    atest-1 dtest-0
gpiochip0: GPIOs 301-511, parent: platform/f000000.pinctrl, f000000.pinctrl:
 gpio0   : in  low  func0 2mA pull down
 gpio1   : in  low  func0 2mA pull down
 gpio2   : in  low  func0 2mA pull down
 gpio3   : in  low  func0 2mA pull down
 gpio4   : in  high func0 2mA pull up
 gpio5   : in  high func0 2mA pull up
 gpio6   : in  high func0 2mA pull up
 gpio7   : in  high func0 2mA pull up
 gpio8   : in  high func0 2mA no pull
 gpio9   : in  high func0 2mA no pull
 gpio10  : in  low  func0 2mA pull down
 gpio11  : in  high func0 2mA pull down
 gpio12  : out low  func0 2mA pull down
 gpio13  : out high func0 2mA pull down
 gpio14  : out low  func0 2mA no pull
 gpio15  : out high func0 2mA pull up
 gpio16  : in  low  func0 2mA no pull
 gpio17  : in  low  func0 2mA no pull
 gpio18  : out high func0 2mA pull up
 gpio19  : out high func0 8mA pull up
 gpio20  : in  high func0 2mA pull up
 gpio21  : in  high func0 2mA pull up
 gpio22  : in  low  func0 2mA pull down
 gpio23  : in  low  func0 2mA pull down
 gpio24  : in  low  func0 2mA pull down
 gpio25  : in  low  func0 2mA pull down
 gpio26  : out low  func1 2mA no pull
 gpio27  : out low  func1 2mA no pull
 gpio28  : in  high func0 2mA pull up
 gpio29  : in  high func0 2mA pull up
 gpio30  : in  low  func0 2mA pull down
 gpio31  : in  low  func0 2mA pull down
 gpio32  : in  low  func0 2mA no pull
 gpio33  : in  low  func0 2mA no pull
 gpio34  : in  high func0 2mA pull up
 gpio35  : in  high func0 2mA pull up
 gpio36  : in  low  func0 2mA pull down
 gpio37  : in  low  func0 2mA pull down
 gpio38  : in  high func1 2mA pull up
 gpio39  : in  low  func1 2mA no pull
 gpio40  : in  low  func0 2mA pull down
 gpio41  : in  low  func0 2mA pull down
 gpio42  : in  low  func0 2mA pull down
 gpio43  : in  low  func0 2mA pull down
 gpio44  : in  high func0 2mA pull up
 gpio45  : in  high func0 2mA pull up
 gpio46  : in  low  func0 2mA pull down
 gpio47  : in  low  func0 2mA pull down
 gpio48  : in  high func4 2mA pull up
 gpio49  : in  high func3 2mA pull up
 gpio50  : in  low  func3 2mA no pull
 gpio51  : in  high func3 2mA pull up
 gpio52  : in  low  func0 2mA no pull
 gpio53  : in  low  func0 2mA no pull
 gpio54  : out low  func0 2mA pull down
 gpio55  : in  low  func0 2mA pull down
 gpio56  : in  high func0 2mA pull down
 gpio57  : in  high func0 2mA pull down
 gpio58  : in  low  func0 2mA pull down
 gpio59  : in  low  func0 2mA pull down
 gpio60  : in  low  func0 2mA no pull
 gpio61  : in  low  func0 2mA no pull
 gpio62  : in  low  func0 2mA pull down
 gpio63  : in  low  func0 2mA pull down
 gpio64  : in  low  func0 2mA no pull
 gpio65  : in  low  func0 2mA no pull
 gpio66  : in  low  func0 2mA pull down
 gpio67  : in  low  func0 2mA pull down
 gpio68  : in  low  func0 2mA no pull
 gpio69  : in  low  func0 2mA no pull
 gpio70  : in  low  func0 2mA pull down
 gpio71  : in  low  func0 2mA pull down
 gpio72  : in  low  func0 2mA pull down
 gpio73  : in  low  func0 2mA pull down
 gpio74  : in  low  func0 2mA pull down
 gpio75  : in  low  func0 2mA pull down
 gpio76  : in  high func1 2mA no pull
 gpio77  : in  high func1 2mA pull down
 gpio78  : in  high func1 2mA pull up
 gpio79  : in  low  func0 2mA pull down
 gpio80  : out low  func0 2mA pull down
 gpio81  : in  low  func0 2mA pull down
 gpio82  : in  high func1 2mA pull up
 gpio83  : in  low  func1 2mA no pull
 gpio84  : in  low  func0 2mA pull down
 gpio85  : in  low  func0 2mA pull down
 gpio86  : in  low  func1 2mA pull down
 gpio87  : in  high func0 2mA pull down
 gpio88  : in  low  func0 2mA pull down
 gpio89  : in  high func2 2mA pull up
 gpio90  : in  high func3 2mA pull up
 gpio91  : in  low  func0 2mA pull down
 gpio92  : in  high func1 2mA pull down
 gpio93  : in  low  func0 2mA pull down
 gpio94  : out low  func0 2mA pull down
 gpio95  : in  high func1 2mA pull up
 gpio96  : in  high func0 2mA pull up
 gpio97  : in  low  func0 2mA pull down
 gpio98  : in  high func0 2mA pull up
 gpio99  : in  low  func0 2mA pull down
 gpio100 : in  low  func0 2mA pull down
 gpio101 : in  low  func0 2mA pull down
 gpio102 : in  low  func0 2mA pull down
 gpio103 : in  low  func0 2mA pull down
 gpio104 : in  low  func0 2mA pull down
 gpio105 : in  low  func0 2mA pull down
 gpio106 : in  low  func0 2mA pull down
 gpio107 : in  low  func0 2mA pull down
 gpio108 : in  low  func0 2mA pull down
 gpio109 : in  low  func0 2mA pull down
 gpio110 : in  low  func0 2mA pull down
 gpio111 : in  low  func0 2mA pull down
 gpio112 : in  low  func0 2mA pull down
 gpio113 : in  low  func0 2mA pull down
 gpio114 : in  low  func0 2mA pull down
 gpio115 : in  low  func0 2mA pull down
 gpio116 : in  low  func0 2mA pull down
 gpio117 : in  low  func0 2mA pull down
 gpio118 : in  low  func0 2mA pull down
 gpio119 : in  low  func0 2mA pull down
 gpio120 : in  low  func0 2mA pull down
 gpio121 : in  low  func0 2mA pull down
 gpio122 : in  low  func0 2mA pull down
 gpio123 : in  low  func0 2mA pull down
 gpio124 : in  low  func0 2mA pull down
 gpio125 : in  low  func0 2mA pull down
 gpio126 : in  low  func0 2mA pull down
 gpio127 : in  low  func0 2mA pull down
 gpio128 : in  low  func0 2mA pull down
 gpio129 : in  low  func0 2mA pull down
 gpio130 : in  low  func0 2mA pull down
 gpio131 : in  low  func0 2mA pull down
 gpio132 : in  low  func0 2mA pull down
 gpio133 : in  low  func0 2mA pull down
 gpio134 : in  low  func0 2mA pull down
 gpio135 : in  low  func0 2mA pull down
 gpio136 : in  low  func0 2mA pull down
 gpio137 : in  low  func0 2mA pull down
 gpio138 : in  low  func0 2mA pull down
 gpio139 : in  low  func0 2mA pull down
 gpio140 : in  low  func0 2mA pull down
 gpio141 : in  low  func0 2mA pull down
 gpio142 : in  low  func0 2mA pull down
 gpio143 : in  low  func0 2mA pull down
 gpio144 : in  low  func0 2mA pull down
 gpio145 : in  low  func0 2mA pull down
 gpio146 : in  low  func0 2mA pull down
 gpio147 : in  low  func0 2mA pull down
 gpio148 : in  low  func0 2mA pull down
 gpio149 : in  low  func0 2mA pull down
 gpio150 : in  low  func0 2mA pull down
 gpio151 : in  low  func0 2mA pull down
 gpio152 : in  low  func0 2mA pull down
 gpio153 : in  low  func0 2mA pull down
 gpio154 : in  low  func0 2mA pull down
 gpio155 : in  low  func0 2mA pull down
 gpio156 : in  low  func0 2mA pull down
 gpio157 : in  low  func0 2mA pull down
 gpio158 : in  low  func0 2mA pull down
 gpio159 : in  low  func0 2mA pull down
 gpio160 : in  low  func0 2mA pull down
 gpio161 : in  low  func0 2mA pull down
 gpio162 : in  low  func0 2mA pull down
 gpio163 : in  low  func0 2mA pull down
 gpio164 : in  low  func0 2mA pull down
 gpio165 : in  low  func0 2mA pull down
 gpio166 : in  low  func0 2mA pull down
 gpio167 : in  low  func0 2mA pull down
 gpio168 : in  low  func0 2mA pull down
 gpio169 : in  low  func0 2mA pull down
 gpio170 : in  low  func0 2mA pull down
 gpio171 : in  low  func0 2mA pull down
 gpio172 : in  low  func0 2mA pull down
 gpio173 : in  low  func0 2mA pull down
 gpio174 : in  low  func0 2mA pull down
 gpio175 : in  low  func0 2mA pull down
 gpio176 : in  high func0 2mA pull down
 gpio177 : in  high func0 2mA pull down
 gpio178 : in  low  func0 2mA pull down
 gpio179 : in  low  func0 2mA pull down
 gpio180 : in  low  func0 2mA pull down
 gpio181 : in  low  func0 2mA pull down
 gpio182 : in  high func0 2mA pull down
 gpio183 : in  low  func0 2mA pull down
 gpio184 : in  high func0 2mA pull down
 gpio185 : in  low  func0 2mA pull down
 gpio186 : in  low  func0 2mA pull down
 gpio187 : in  low  func0 2mA pull down
 gpio188 : in  high func0 2mA pull down
 gpio189 : in  high func0 2mA pull down
 gpio190 : in  high func0 2mA pull down
 gpio191 : in  high func0 2mA pull down
 gpio192 : in  high func0 2mA pull down
 gpio193 : in  low  func0 2mA pull down
 gpio194 : in  low  func0 2mA pull down
 gpio195 : in  high func0 2mA pull down
 gpio196 : in  low  func0 2mA pull down
 gpio197 : in  low  func0 2mA pull down
 gpio198 : in  low  func0 2mA pull down
 gpio199 : in  low  func0 2mA pull down
 gpio200 : in  low  func0 2mA pull down
 gpio201 : in  low  func0 2mA pull down
 gpio202 : in  low  func0 8mA no pull
 gpio203 : in  low  func0 2mA pull down
 gpio204 : in  low  func0 2mA pull down
 gpio205 : in  low  func0 2mA pull down
 gpio206 : in  low  func0 2mA pull down
 gpio207 : in  low  func0 2mA pull down
 gpio208 : in  low  func0 2mA pull down
 gpio209 : in  low  func0 2mA pull down
 ufs_reset: in  low  func0 8mA pull down
```
