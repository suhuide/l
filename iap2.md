
[memo.md](memo.md)  
# iAP2协议
## 前言

iAP2协议，是苹果MFi技术中的一种，是一个非常完整、经典的通讯协议。两个设备互相使用数据包来通信，考虑到了通讯的完整性、正确性和效率。

作为数据包通信学习，是一个非常好的案例。

## 正文

配件可以使用iAP2协议来访问高级设备功能。其中一项功能是通过iOS外部附件框架与第三方iOS应用程序进行安全通信的能力。

iOS External Accessory Framework:

About External Accessories

在Accessory Interface Specification R39.pdf中，第57章，是关于iAP2的协议描述。

## 57. iAP2

iAP2是iAP1的完全替代者，不向后兼容(backward compatible)。

iAP缩写表示的是Interface Accessory Protocol.

### 57.1 iAP2 Connection

一个iAP2连接是由一个iAP2传输通道(iAP2 Link)和一个或多个iAP2会话组成。

### 57.2 iAP Link

每一个iAP2连接都是从附件和设备之间通过支持的传输建立一个通道开始的。链接协议提供了一个与传输无关的机制，用于可靠和有序地发布属于一个或多个iAP2会话的数据包。该协议也可基于每个连接进行配置，并可在任何特定的传输方式或附件使用情况下进行优化以获得最佳性能。这些协议的功能是为了实现以下这些目标：

- 对收到的数据包进行ACK确认。

- 重传只需要重新发送序列中未被确认的数据包。

- 对iAP2会话的明确和有效支持。

支持iAP2的传输方式：
- Bluetooth
- UART
- USB Device Mode
- USB Host Mode
- Apple Lightning Audio

支持上面这些传输方式的设备，都可以和配件建立iAP2的连接。一些传输方式对不同的功能会更加合适，所以在配件设计过程中，选择合适的传输方式是最优先的事。

#### 57.2.1 Packet Structure

每个通信数据包应以一个固定大小的9字节的头开始，包括校验和。头后面数据是一个可选的可变长度的数据有效载荷。头部和有效载荷都有各自的校验和。如果没有有效载荷数据，就没有有效载荷校验和。

Table 57-1 iAP2 Link Packet Structure  
Start of Packet MSB (0xFF)  
Start of Packet LSB (0x5A)  
Packet Length MSB  
Packet Length LSB  
Control Byte  
Packet Sequence Number  
Packet Acknowledgement Number  
Session Identifier  
Header Checksum  
…  
Payload Data  
…  
Payload Checksum  

##### 57.2.1.1 Start of Packet

每个iAP2链接数据包的前两个字节总是FF 5A。如果在传输流中检测到这些字节，那么配件和设备都应尝试将后面的字节解析为有效的数据包。

##### 57.2.1.2 Packet Length

接下来的两个字节表示以字节为单位的数据包长度，并且总是以无符号的16位大端整数表示。一个没有有效载荷数据的链接数据包的长度固定是9字节（从数据包的开始到头校验和）。否则，数据包长度是从数据包开始到最后一个字节的有效载荷数据，包括有效载荷校验和。例如，一个有1个字节的有效载荷数据的链接数据包，其数据包长度为11字节。数据包的最大有效载荷数据大小为65525字节；具有这种有效载荷的数据包的包长为65535字节。

##### 57.2.1.3 Control Byte

控制字节中的位表明数据包中存在的内容。
- SYN, EAK, 和 RST 位是相互排斥的。
- ACK位可与SYN位结合。
- EAK位总是与ACK位一起设置。
- RST位从不与任何其他位一起设置。
- SLP位从不与任何其他位一起设置。
- 所有未分配的位应被设置为0。

当SYN、EAK或RST的任何位被设置时，iAP2会话有效载荷不能出现。反之，带有iAP2会话有效载荷的链接数据包总是设置ACK位。

Table 57-2 iAP2 Link Control Byte Bits

|Bit |Name |Meaning |
|----|-----|--------|
|7   |SYN  |Link Synchronization Payload is present |
|6   |ACK  |Packet Acknowledgement Number is valid, and iAP2 Session Payload may be present |
|5   |EAK  |Extended Acknowledgement Payload is present |
|4   |RST  |Link Reset |
|3   |SLP  |Device Sleep |


下面的内容将会使用这些描述表示带有某种control byte的link packet。

##### 57.2.1.4 Packet Sequence Number

每个链接数据包都包含一个数据包序列号，用来唯一识别传输中的该数据包。当首次创建链路时，设备和附件都应在发送其第一个SYN/SYN+ACK包之前随机选择一个初始序列号。每次发送带有iAP2会话或链路同步有效载荷数据的数据包时，序列号都会增加1，否则，在发送数据包时序列号不会增加。以前发送的数据包的重新传输应保留相同的数据包序列号。序列号在达到255时包回0。The sequence number wraps back to 0 upon reaching 255.

注：设备和配件应该各自使用自己的包序列号。

##### 57.2.1.5 Packet Acknowledgement Number

只有当控制字节中的ACK位被设置时，数据包确认号码才有意义。如果没有设置ACK，则发送方应将数据包确认号设置为0，而接收方应将其忽略。

如果设置了ACK，此数据包是接收方向发送方回复一个数据包用来确认，里面包含的数据包确认号表示的是收到的上一个按顺序接受的数据包号码。例如，如果配件收到的数据包序列号是1、2、3和5，那么配件发送的下一个数据包里的数据包确认号将是3，因为5是不按顺序收到的。

##### 57.2.1.6 Session Identifier

会话标识符只有在控制字节中的ACK位被设置且存在iAP2会话有效载荷时才有意义。如果满足这两个条件，会话标识符将是一个非零数字，指定iAP2连接中的一个特定会话。否则，会话标识符应被设置为0。

##### 57.2.1.7 Header Checksum

头部校验和的计算方法是将以下所有数据包的字节相加。如果报头校验和的值与根据校验和计算的值不一致，接收方应从下一个检测到的数据包开始序列重新开始数据包解析工作。

· Start of Packet MSB
· Start of Packet LSB
· Packet Length MSB
· Packet Length LSB
· Control Byte
· Packet Sequence Number
· Packet Acknowledgement Number
· Session Identifier

##### 57.2.1.8 Payload Data

这一部分是可选的，它的存在应与控制字节中的位的状态相匹配。可能的最大有效载荷大小为65,525字节。

##### 57.2.1.9 Payload Checksum

当且仅当有效载荷数据存在时，有效载荷校验字节才会出现。如果存在有效载荷数据，则对有效载荷数据的所有字节进行校验。如果有效载荷校验和中的值与根据校验和计算的值不一致，接收方应从下一个检测到的数据包开始序列重新开始数据包解析。

##### 57.2.1.10 Checksum Calculation

iAP2使用的校验和字节是为每个发送的数据包计算的。其目的是让所有被校验的（无符号8位）字节和校验（无符号8位）字节的总和，忽略任何无符号8位溢出，等于0x00。这允许一个快速的方法来验证数据包的正确传输。校验字节的计算方法是：取被校验的（无符号8位）字节之和的最小有效字节，然后取补码。

下面是代码示例：
```c
uint8_t 
checksum_calculation(uint8_t *buffer, uint16_t start, uint16_t length)
{

    uint16_t i;

    uint8_t sum = 0;

    for (i = start; i < (start + length); i++) {

        sum += buffer[i];

    }

    return (uint8_t)(0x100 - sum); /* 2's complement */

}
```
#### 57.2.2 Link Synchronization Payload

关于包头后面的负载数据：链路同步有效载荷（Link Synchronization Payload / LSP）用于建立链路，并在设备和接入点之间同步包序号。它还包含可协商的链接参数。

Table 57-3 Link Synchronization Payload (Version 1)  
Link Version (0x01)  
Maximum Number of Outstanding Packets
Maximum Received Packet Length MSB  
Maximum Received Packet Length LSB  
Retransmission Timeout MSB  
Retransmission Timeout LSB  
Cumulative Acknowledgement Timeout MSB  
Cumulative Acknowledgement Timeout LSB  
Maximum Number of Retransmissions    
Maximum Cumulative Acknowledgements   
iAP2 Session 1: Session Identifier  
iAP2 Session 1: Session Type  
iAP2 Session 1: Session Version  
…  
iAP2 Session N: Session Identifier  
iAP2 Session N: Session Type  
iAP2 Session N: Session Version  

##### 57.2.2.1 Link Version

- 正在建立的链接的版本。所有数据包的有效载荷都可能根据链路版本的不同而不同。

- 目前链路版本的唯一有效值是1。

- 这是一个可协商的参数。

- 附件和设备都应同意相同的值。

##### 57.2.2.2 Maximum Number of Outstanding Packets

- 在没有收到对方ACK的情况下，可以发送的未决数据包的最大数目

- 有效值为1到127。

- 这不是一个可协商的参数。

- 配件和设备可以提出并使用不同的值。

- 在不等待设备确认的情况下，配件发送的数据包数量不得超过设备建议的最大未决数据包数量，反之亦然。

##### 57.2.2.3 Maximum Received Packet Length

- 以字节为单位的可以接手的最大可能的包长。

- 有效值为24至65535。

- 这不是一个可协商的参数。

- 配件和设备可以提出并使用不同的值。

##### 57.2.2.4 Retransmission Timeout

- 没有收到ACK时重发一个包的超时时间，单位为毫秒。这应该被设置为一个与数据包在链路传输上的传输时间相近的值。

- 有效值为20毫秒至65535毫秒。

- 这是一个可协商的参数。

- 配件和设备都应同意相同的值。

##### 57.2.2.5 Cumulative Acknowledgement Timeout

- 以毫秒为单位的超时值，当不在接受到新的数据包时，要发送ACK数据确认包。
- 有效值为10毫秒至等待重传超时时间的一半。
- 这是一个可协商的参数。
- 配件和设备都应同意相同的值。

##### 57.2.2.6 Maximum Number of Retransmissions

- 在链路被认为是断开之前尝试的最大数据包重传数量。
- 有效值为1到30。
- 这是一个可协商的参数。
- 配件和设备都应同意相同的值。

##### 57.2.2.7 Maximum Cumulative Acknowledgements

- 当按序列接收到的最大数量的数据包时，就要发送ACK确认数据包。
- 有效值为0-127或最大未处理数据包数量，以较小者为准。
- 这是一个可协商的参数。
- 配件和设备都应同意相同的值。

##### 57.2.2.8 ZeroACK/ZeroRetransmit Link Configurations

从iOS 8.3开始，配件可以选择协商一个ZeroACK/ZeroRetransmit链路配置，而不期待重传的数据包或数据包确认。建议使用的条件是，底层传输有自己的可靠传输机制，并且配件可以完全利用这些机制。这种类型的iAP2连接方式，可用的传输层是USB主机模式、USB设备模式和蓝牙RFCOMM传输。

设备仍将使用数据包序列号检测掉落的链接数据包并重置iAP2链接。

如果在典型的使用过程中经常发生丢包，附件不应使用这种链路配置，并应准备在复位发生时重新建立链路，而不丢失状态或影响用户功能。

- 当设备检测到丢包时，将向附件发送RST，链路层协商将以附件的SYN包重新开始。
- 当附件使用数据包序列号检测到一个丢弃的数据包时，附件应发送一个SYN数据包以重新启动链路协商

为了协商零应答/零重传的链路配置，以下可协商的链路参数应设置为0：

- 重传超时
- 累计确认超时
- 最大重传次数
- 最大累计确认次数

一些设备和/或iOS版本可能会拒绝协商零ACK/零重传链接配置的尝试。如果配件声称与这些设备/iOS版本兼容，则应保留协商带有确认和重传的链接的能力。配件应发送一个SYN数据包，而不是SYN+ACK，来更新参数以继续协商。

配件应通过管理其iAP2会话的通讯，来解决在链路层缺乏流量控制(flow control)的情况。例如，在开始文件传输前，应通过发送StopMediaLibraryUpdate来暂停MediaLibraryUpdate消息，并在适当时恢复其他活动。同样的注意事项也适用于外部配件协议消息。

Accessories shall account for the lack of flow control at the link layer by  managing their iAP2 session traffic.

##### 57.2.2.9 iAP2 Sessions

- 配件将使用iAP2会话与设备进行通信。
- 会话标识符对每个定义的会话都是唯一的。0不是一个有效的会话标识符。
- 会话类型和版本应是有效的。
- 这是一个可协商的参数。
- 配件和设备都应同意相同的值。

#### 57.2.3 iAP2 Session Payload

iAP2会话有效载荷在后面有专门说明。只要存在iAP2会话有效载荷，控制字节中的ACK位应被设置。

#### 57.2.4 Extended Acknowledgement Payload

Extended Acknowledgement Payload用于确认不按顺序收到的数据包。

该有效载荷具有以下属性：

- 控制字节中的EAK和ACK位都应被设置。
- 数据包确认号包含依次收到的最后一个数据包的序列号。
- 有效载荷数据部分包含一个或多个不按顺序收到的数据包的序列号。它们不是这些数据包的确认。确认将在以后的数据包中单独发送，并在ACK字段中标明适当的号码。

Table 57-4 EAK Packet Payload (Link v1)  
1st Out of Sequence Acknowledgement Number  
…  
Nth Out of Sequence Acknowledgement Number  

#### 57.2.5 Reset

控制字节中的RST位被设备用来重置一个连接。这种链接数据包没有有效载荷，只能由设备发送。

#### 57.2.6 Sleep

本节仅适用于集成以下Lightning连接器的配件：

· Lightning (C78-USBH)

· Lightning (C79-USBH)

· Lightning (C79-UART)

· Lightning (C79-LA)

· Lightning (C78-STROBE-USBH)

· Lightning (C78-STROBE-UART)

· Lightning (C78-STROBE-LA)

控制字节中的SLP位被设备用来表示它即将进入睡眠状态。这种链接数据包没有有效载荷，只能由设备发送。

一旦进入睡眠状态，设备将停止供应附属电源。如果设备退出睡眠状态，它将再次开始供应配件电源。

如果配件能够暂停和恢复链路层，配件应在附件电源恢复后等待500毫秒，然后重新初始化链路。在这段时间内，配件可能会收到来自设备的ACK信号，该信号是链路层恢复的信号，并用于同步序列号（设备发出的最后一个包的序列号）和ACK号（设备收到的最后一个包的序号）。

如果配件不能暂停和恢复链路层，在重新初始化链路前，配件应在电源恢复后等待80毫秒。

#### 57.2.7 Operation

##### 57.2.7.1 Record

所有链接的实施都应在链接的特定记录中存储以下变量。这些变量将在描述iAP2链接操作的后续章节中被提及。

Table 57-5 iAP2 Link Operation Record Variables

|Variable |Description|
|-------------|-----------|
|SentACKTimer|A timer keeping track of the elapsed time (ms) since the last ACK packet was sent|
|NextSentPSN| The Packet Sequence Number of the next packet to be sent|
|OldestSentUnacknowledgedPSN| The Packet Sequence Number of the oldest unacknowledged packet|
|InitialSentPSN| The Packet Sequence Number used for the very first packet sent|
|LastReceivedInSequencePSN|The Packet Sequence Number of the last packet received correctly and in sequence|
|InitialReceivedPSN| The Packet Sequence Number of the very first packet received|
|ReceivedOutOfSequencePSNs[n]|An array of Packet Sequence Numbers received and acknowledged out of sequence|

##### 57.2.7.2 Initialization

一旦传输连接已经建立，配件应确认设备是否支持iAP2，以1赫兹（每秒一次）发送以下字节序列，直到收到设备的响应：

FF 55 02 00 EE 10.

如果设备支持iAP2, 配件会受到同样的字节序列。

如果设备只支持iAP1，配件会收到下面的某个数据序列：

55 04 00 02 04 EE 08  
55 02 00 00 FE  
FF 55 04 00 02 04 EE 08  
FF 55 02 00 00 FE  

如果配件收到上面的数据序列之一，需要发送下面的字节序列给设备，来表示不兼容：

FF 55 0E 00 13 FF FF FF FF FF FF FF FF FF FF FF FF EB

配件应将设备返回的应答作为最终应答，不允许重传或重试。

##### 57.2.7.3 Synchronization

该链接的一个显著特点是支持在任何类型的传输上自动协商传输参数。这允许链接根据设备和配件的能力进行扩展。链接初始化有3个主要目的：

- 确定设备和配件双方都能接受的链路配置参数。
- 搜索配置参数中的错误。
- 如果不能达成协议，就终止链接。

当底层传输连接已建立，iAP协议也兼容时，就会启动一个链接。这时，配件先发送一个SYN数据包，里面的链接同步数据负载包含了链接所需的参数，以及随机生成的数据包序列号。设备将以SYN+ACK数据包回应，确认收到附件的SYN数据包、它自己想要的连接参数和它随机产生的数据包序列号。

如果设备和配件对所有可协商的连接参数提出了相同的值，附件应发送一个来自设备的最新SYN+ACK的最终ACK包，并且连接被认为已经建立。否则，SYN+ACK包将继续交换，最多10次，直到所有可协商的连接参数都达成一致。如果发生10次交换而没有就可协商的连接参数达成协议，设备将停止响应配件发送的任何进一步的数据包。

有时，设备将无法立即响应从配件收到的SYN数据包。配件可以用相同的有效负载数据和相同的数据包序列号重新发送SYN数据包。附件可以每秒继续这样做，直到设备发送SYN+ACK响应，确认先前发送的数据包序列号。一旦收到设备的响应，附件应忽略任何随后进入的具有相同数据包序列号的SYN+ACK数据包。

如果配件的最终链路同步有效负载数据中含有无效的非协商数据，设备将发送一个RST数据包以重置链路。

在同步过程中，假定以下默认链路配置参数，直到同步完成之前，以下默认链路配置参数。

在同步过程中，在同步完成之前，假定使用以下的默认链路配置参数：

Table 57-6 Default link parameters during synchronization

|Parameter |Default Value|
|-------------|-----------|
|Maximum Number of Outstanding Packets|1|
|Maximum Received Packet Length|128 bytes|
|Retransmission Timeout|1000 ms|
|Cumulative Ack Timeout|10 ms|
|Maximum Number of Retransmissions|30|
|Maximum Cumulative Acknowledgements|0|

下表包含了一些使用iAP2协议的传输方式所推荐的链接配置参数。

这些值只是作为开发的初始值，针对某个特定配件使用的话，需要经过相应的核实才行。

Table 57-7 Recommended link parameters for USB Host Mode transport (Full Speed)

|Parameter |Recommended Value|
|-------------|-----------|
|Maximum Number of Outstanding Packets|5|
|Maximum Received Packet Length |4096 bytes|
|Retransmission Timeout |2000 ms|
|Cumulative Ack Timeout |22 ms|
|Maximum Number of Retransmissions |30|
|Maximum Cumulative Acknowledgements |3|

Table 57-8 Recommended link parameters for USB Device Mode transport (Full  Speed)

这个和上面一样。

Table 57-9 Recommended link parameters for Bluetooth transport

|Parameter |Recommended Value|
|-------------|-----------|
|Maximum Number of Outstanding Packets|5|
|Maximum Received Packet Length |2048 bytes|
|Retransmission Timeout |1500 ms|
|Cumulative Ack Timeout |73 ms|
|Maximum Number of Retransmissions |30|
|Maximum Cumulative Acknowledgements |3|

Table 57-10 Recommended link parameters for 115.2 kbps UART transport

|Parameter |Recommended Value|
|-------------|-----------|
|Maximum Number of Outstanding Packets|4|
|Maximum Received Packet Length |256 bytes|
|Retransmission Timeout |1000 ms|
|Cumulative Ack Timeout |133 ms|
|Maximum Number of Retransmissions |30|
|Maximum Cumulative Acknowledgements |2|

##### 57.2.7.4 Acknowledgements

为了保证数据包派发成功，链路协议同时使用了数据包的接收确认和重传。每个带有有效负载数据的数据包和SYN数据包在被接收方收到并认可后，需要接收方回复ACK。回复的ACK数据包不需要另一方再回复ACK。损坏的数据包被丢弃，不需要回复ACK。当数据包在重传超时规定的时间内未被接收方确认时，发送方将重传数据包。

有两种类型的数据包确认方式(ACK)。累积确认用于确认收到的所有按顺序接收到的数据包，指定的是某个最新发送的符合顺序的数据包。扩展确认允许接收方确认不按顺序的数据包。使用的确认类型只是根据数据包到达顺序而定。在可能的情况下，链路实现应使用累积确认，并仅在数据包被非按顺序接收时使用扩展确认。

一旦收到一个或多个不按顺序的数据包，接收方应立即生成并发送扩展确认。

如果相应的ACK在传输中丢失，同一个有效载荷数据可能被多次接收。发生这种情况时，接收方应重新发送有效负载数据的ACK。

##### 57.2.7.5 Retransmissions

数据包在底层传输时，可能会丢失或损坏。这样就可能被数据包丢弃。如前所提的数据包的回复ACK机制，要求接收方正确收到一个有效数据包时，要回复一个ACK的数据包。

为了检测丢失的数据包，发送方应为每个发出的数据包启用一个重传超时时间。这个定时器的时间是根据协商确定的。当收到一个数据包的确认时，该数据包的定时器被取消。如果定时器在收到确认之前过期，则数据包被重传，定时器被重新启动。可以重传的最大次数，是根据链接同步期间协商而定的。

##### 57.2.7.6 Flow Control

iAP2链路使用了流控机制，根据未收到确认的数据包个数，和链路配置参数里的最大未决数据包个数。该参数由双方在创建链路时指定，并应根据各自分配给链路的缓冲区的数量和大小来设置。一旦设定，该参数在连接时保持不变。

该链路采用了序列号窗口的概念，用于可接受的数据包序列号。窗口的左边缘是最后一个确认的数据包序列号加1。窗口的右边缘等于最后一个序列内确认的数据包序列号加最大未决数据包数量。链路发送者发送数据包，直到达到接收者的最大未处理数据包数量。一旦达到限制，发送方只能收到一个确认包，再发送一个新数据包。

当一个收到的数据包的数据包序列号落在窗口内，它就被确认。分两种情况。如果数据包序列号等于左边缘（即它是下一个预期的数据包序列号），则以累积确认（ACK）确认该数据包，并且接受窗口的左边缘和右边缘递增一个。如果收到的数据包的序列号在窗口内，但不在序列内，则用扩展确认（EAK）来确认。窗口不作调整，并记录收到的不符合顺序的数据包。收到的链路数据包序列号在窗口之外的数据包应被丢弃；并表明链路不稳定，可能需要重置。

当发送方收到扩展确认（EAK）时，发送方不应在发送接收窗口之外的数据包。如果一个数据包没有被确认，但所有后续的数据包都被收到并确认，就可能发生这种情况。这一要求将把窗口的左边缘固定在未被确认的数据包的序列号上。随着其他数据包的发送，下一个数据包序列号将接近并最终超过右边缘。这时，没有更多的数据包可以被发送，直到未被确认的数据包被确认。

##### 57.2.7.7 Reset

设备可以在任何时候向配件发送一个RST数据包。收到RST数据包后，附件应在收到RST数据包后1秒内向设备发送SYN数据包，然后进行同步处理。

配件应终止底层传输连接，然后再重新连接。如果UART传输处于活动状态，只有手动的断开再接入配合和设备的Lightning连接器才可以。当必须重连时，表明协商的链接参数设置不合理，一般情况下不应该发生这种情况。


# External Accessory Protocol
[MFI IAP2 EAP session实现跟苹果APP经典蓝牙自定义数据通信](https://blog.csdn.net/XiaoXiaoPengBo/article/details/154234784)
[USB-和苹果手机通过EAP通信](https://www.cnblogs.com/god-of-death/p/18976847)
[iOS App 连接外设的几种方式](https://blog.csdn.net/qq_34047841/article/details/72822480)

# Reference
[iAP2](https://blog.csdn.net/guoqx/article/details/126125672)
