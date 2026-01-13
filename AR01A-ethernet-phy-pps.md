

# Config
```c
void ptp_pps_event(struct ptp_info *ptp, u8 gpo, u32 sec)
{
	u32 pattern;
	u32 ctrl;
	u32 nsec;
	u32 pulse = (20000000 / 8);	/* 20 ms */
	u32 cycle = 1000000000;
	u16 cnt = 0;
	u8 tso = ptp->pps_tso;
	u8 event = TRIG_POS_PERIOD;
	struct ksz_sw *sw = ptp->parent;
    
	ptp_tx_off(ptp, tso);

	/* Config pattern. */
	ctrl = trig_event_gpo(gpo, event);
	ctrl |= TRIG_NOTIFY;
	ctrl |= TRIG_NOW;
	ctrl |= trig_cascade(TRIG_CASCADE_UPS_M);
	sw->reg->w32(sw, REG_TRIG_CTRL__4, ctrl);

	/* Config pulse width. */
	if (pulse > TRIG_PULSE_WIDTH_M)
		pulse = TRIG_PULSE_WIDTH_M;
	sw->reg->w24(sw, REG_TRIG_PULSE_WIDTH__4 + 1, pulse);

	/* Config cycle width. */
	sw->reg->w32(sw, REG_TRIG_CYCLE_WIDTH, cycle);

	/* Config trigger count. */
	pattern = cnt;
	pattern <<= TRIG_CYCLE_CNT_S;
	sw->reg->w32(sw, REG_TRIG_CYCLE_CNT, pattern);

	/* Config trigger time. */
	if (ptp->pps_offset >= 0)
		nsec = ptp->pps_offset;
	else {
		nsec = NANOSEC_IN_SEC + ptp->pps_offset;
		sec--;
	}
	ptp_tx_start(ptp, tso, sec, nsec);
}  /* ptp_pps_event */
```

# Register
```c
REG_TRIG_CTRL__4        -   0x0538
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x05 0x38 r4
0x3f 0x50 0x00 0x00
[0x0538+2]=0x00 -> GPIO_1

REG_TRIG_PULSE_WIDTH__4 -   0x0548
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x05 0x48 r4
0x00 0x26 0x25 0xa0
[0x0548]=0x00, 0x2625A0 -> 2500000x8=20000000ns=20ms

REG_TRIG_CYCLE_WIDTH    -   0x053C
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x05 0x3c r4
0x3b 0x9a 0xca 0x00
[0x053C]=0x3B, 0x3B9ACA00 -> 1000000000ns

REG_TRIG_CYCLE_CNT      -   0x0540
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x05 0x40 r4
0x00 0x00 0x00 0x00

```
[GPIO Output clock example for KSZ8563 and KSZ9563](https://microchip.my.site.com/s/article/GPIO-Output-clock-example-for-KSZ8563-and-KSZ9563)
```c
ww 500 0002
wd 520 00000002
wd 52c 00000004
wd 538 00500000
wd 53c 00989680
wd 548 00098968
wd 530 01234567
wd 534 00000001
wd 52c 00000008
ww 500 0003
```
```c
#!/bin/bash
#ww 500 0002
i2ctransfer -f -y 5 w2@0x5f 0x05 0x00 r2
usleep 50000 
i2ctransfer -f -y 5 w4@0x5f 0x05 0x00  0x00 0x02
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x00 r2
usleep 50000 

#wd 520 00000002
i2ctransfer -f -y 5 w2@0x5f 0x05 0x20 r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x20  0x00  0x00 0x00 0x02
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x20 r4
usleep 50000 

#wd 52c 00000004
i2ctransfer -f -y 5 w2@0x5f 0x05 0x2c r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x2c  0x00  0x00 0x00 0x04
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x2c r4
usleep 50000 

#wd 538 00500000
i2ctransfer -f -y 5 w2@0x5f 0x05 0x38 r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x38  0x00  0x50 0x00 0x00
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x38 r4
usleep 50000 

#wd 53c 00989680
i2ctransfer -f -y 5 w2@0x5f 0x05 0x3c r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x3c  0x00  0x98 0x96 0x80
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x3c r4
usleep 50000 

#wd 548 00098968
i2ctransfer -f -y 5 w2@0x5f 0x05 0x48 r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x48  0x00  0x09 0x89 0x68
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x48 r4
usleep 50000 

#wd 530 01234567
i2ctransfer -f -y 5 w2@0x5f 0x05 0x30 r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x30  0x01  0x23 0x45 0x67
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x30 r4
usleep 50000 

#wd 534 00000001
i2ctransfer -f -y 5 w2@0x5f 0x05 0x34 r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x34  0x00  0x00 0x00 0x01
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x34 r4
usleep 50000 

#wd 52c 00000008
i2ctransfer -f -y 5 w2@0x5f 0x05 0x2c r4
usleep 50000 
i2ctransfer -f -y 5 w6@0x5f 0x05 0x2c  0x00  0x00 0x00 0x08
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x2c r4
usleep 50000 

#ww 500 0003
i2ctransfer -f -y 5 w2@0x5f 0x05 0x00 r2
usleep 50000 
i2ctransfer -f -y 5 w4@0x5f 0x05 0x00  0x00 0x03
usleep 50000 
i2ctransfer -f -y 5 w2@0x5f 0x05 0x00 r2
usleep 50000 

```

# 5.1.1.4 Global Chip ID 3 Register
Address: 0x0003 Size: 8 bits
0 Global Software Reset
Refer to the Switch Operation Register for another reset control bit.
0 = Normal operation 
1 = Resets the data path and state machines, but not register values.

## Set reset bit
```c
i2ctransfer -f -y 5 w3@0x5f 0x00 0x03  0x61
```
### Ping fail

```c
PS C:\Users\huide> ping 10.42.10.11

Pinging 10.42.10.11 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 10.42.10.11:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
PS C:\Users\huide> ping 10.42.10.11
```
### Switch function is disabled
```c
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x03 0x00  r1
0x00
```
### Mac address invalid
```c
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x03 0x02  r6
0x00 0x00 0x00 0x00 0x00 0x00
```
### Switch ISP TPID Register 
```c
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x03 0x0A  r2
0x00 0x00
```
## Clear reset bit
```c
i2ctransfer -f -y 5 w3@0x5f 0x00 0x03  0x60
```
### Ping Success
```c
Pinging 10.42.10.11 with 32 bytes of data:
Reply from 10.42.10.11: bytes=32 time=1ms TTL=64
Reply from 10.42.10.11: bytes=32 time=2ms TTL=64
Reply from 10.42.10.11: bytes=32 time=2ms TTL=64
Reply from 10.42.10.11: bytes=32 time=2ms TTL=64

Ping statistics for 10.42.10.11:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 2ms, Average = 1ms
```
### Switch function is enabled
```c
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x03 0x00  r1
0x01
```
### Mac address valid
```c
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x03 0x02  r6
0x00 0x10 0xa1 0xff 0xff 0xff
```
### Switch ISP TPID Register 
```c
root@linaro-alip:/# i2ctransfer -f -y 5 w2@0x5f 0x03 0x0A  r2
0x91 0x00
```