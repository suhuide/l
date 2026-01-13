% My Awesome Presentation
% Your Name
% 2023-10-27

---

## Agenda

- The Problem
- Our Solution
- The Results

---

## Code Example

Here is some Python code:

```python
def hello_world():
    print("Hello from PowerPoint!")
```
## 3 ISO的制作
```mermaid
graph TD
    A[开发环境]
    B[获取内核源码]
    C["配置(启用x6425E驱动)"]
    D[编译 vmlinuz + modules]
    E[debootstrap 创建 Ubuntu base]
    F[复制内核模块 + 生成 initrd]
    G[准备 ISO 结构：isolinux + EFI/BOOT]
    H["整合 bootloader(GRUB/ISOLINUX)"]
    I["生成 ISO(xorriso)"]
    J[QEMU/USB 测试]

    A --> B
    B --> C
    C --> D
    B --> E
    D --> F
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
```