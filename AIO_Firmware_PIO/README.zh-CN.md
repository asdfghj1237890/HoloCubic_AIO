# HoloCubic AIO 固件

**Language / 语言 / 語言:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

这是 HoloCubic_AIO 的固件项目，使用 PlatformIO 为 ESP32 (PICO-D4) 构建。

## 构建要求

- [PlatformIO Core](https://platformio.org/) 或 [PlatformIO IDE](https://platformio.org/platformio-ide)
- 平台：ESP32 (espressif32 @ ~3.5.0)
- 框架：Arduino

## 构建说明

### 使用命令行

```bash
# 进入固件目录
cd AIO_Firmware_PIO

# 构建发布版本（默认）
pio run

# 使用特定环境构建
pio run -e HoloCubic_AIO_Releases

# 构建调试版本
pio run -e HoloCubic_AIO_Debug

# 清理构建文件
pio run -t clean

# 构建并上传到设备
pio run -t upload
```

### 使用 VS Code 配合 PlatformIO 扩展

1. 打开 VS Code
2. 安装 **PlatformIO IDE** 扩展
3. 打开 `AIO_Firmware_PIO` 文件夹
4. 点击侧边栏的 PlatformIO 图标
5. 在 **Project Tasks** → **HoloCubic_AIO_Releases** → 点击 **Build**

## 构建环境

项目有两个构建配置：

### HoloCubic_AIO_Releases（默认）
- 针对生产使用优化
- 在 `platformio.ini` 中配置为 `[env:HoloCubic_AIO_Releases]`

### HoloCubic_AIO_Debug
- 启用日志的调试构建
- 优化级别：-O0
- Arduino HAL 日志级别：1

## 输出文件

编译成功后，二进制文件位于：

```
.pio/build/HoloCubic_AIO_Releases/
```

关键文件：
- **firmware.bin** - 主应用程序固件
- **bootloader.bin** - ESP32 引导加载程序
- **partitions.bin** - 分区表

## 烧录到 ESP32

### 所需文件和烧录地址

| 文件 | 烧录地址 | 说明 |
|------|---------|------|
| `bootloader.bin` | 0x1000 | ESP32 引导加载程序 |
| `partitions.bin` | 0x8000 | 分区表 |
| `boot_app0.bin` | 0xe000 | 启动应用选择器 |
| `firmware.bin` | 0x10000 | 主固件 |

### 使用 PlatformIO 烧录

```bash
# 通过 PlatformIO 上传（最简单的方法）
pio run -t upload

# 指定自定义端口
pio run -t upload --upload-port COM5
```

### 使用 esptool 烧录

```bash
# Windows (PowerShell)
python ../AIO_Tool/esptool_v41/esptool.py --port COM5 --baud 921600 write_flash -fm qio -fs 4MB `
  0x1000 .pio/build/HoloCubic_AIO_Releases/bootloader.bin `
  0x8000 .pio/build/HoloCubic_AIO_Releases/partitions.bin `
  0xe000 boot_app0.bin `
  0x10000 .pio/build/HoloCubic_AIO_Releases/firmware.bin

# Linux/macOS
python ../AIO_Tool/esptool_v41/esptool.py --port /dev/ttyUSB0 --baud 921600 write_flash -fm qio -fs 4MB \
  0x1000 .pio/build/HoloCubic_AIO_Releases/bootloader.bin \
  0x8000 .pio/build/HoloCubic_AIO_Releases/partitions.bin \
  0xe000 boot_app0.bin \
  0x10000 .pio/build/HoloCubic_AIO_Releases/firmware.bin
```

**注意：** 将 `COM5` 更改为你实际的串口（例如 `COM3`、`/dev/ttyUSB0`、`/dev/cu.usbserial-*`）

### 擦除闪存（如有需要）

```bash
python ../AIO_Tool/esptool_v41/esptool.py --port COM5 erase_flash
```

## 串口监视器

查看串口输出：

```bash
# 使用 PlatformIO
pio device monitor

# 指定波特率
pio device monitor -b 115200
```

默认监视器设置：
- 波特率：115200
- 过滤器：esp32_exception_decoder

## 板卡配置

- **板卡：** ESP32 PICO-D4 (`pico32`)
- **CPU 频率：** 240 MHz
- **闪存频率：** 80 MHz
- **闪存模式：** QIO
- **上传速度：** 921600 波特率
- **分区方案：** `partitions-no-ota.csv`（无 OTA 更新）

## 项目结构

```
AIO_Firmware_PIO/
├── src/                    # 源代码
│   ├── HoloCubic_AIO.cpp  # 主应用程序
│   ├── app/               # 应用模块
│   ├── driver/            # 硬件驱动
│   ├── sys/               # 系统工具
│   └── resource/          # 嵌入式资源
├── lib/                   # 项目库
├── include/               # 头文件
├── platformio.ini         # PlatformIO 配置
├── partitions-no-ota.csv  # 分区表定义
└── README.md             # 说明文件
```

## 构建标志

通用构建标志（在 `platformio.ini` 中定义）：
- `-fPIC` - 位置无关代码
- `-Wreturn-type` - 警告返回类型问题
- `-Werror=return-type` - 将返回类型警告视为错误

## 故障排除

### 构建失败
- 确保 PlatformIO 已正确安装：`pio --version`
- 清理构建文件：`pio run -t clean`
- 更新平台：`pio platform update espressif32`

### 上传失败
- 检查设备是否已连接：`pio device list`
- 验证 `platformio.ini` 中的上传端口（第 33 行）
- 尝试在上传期间按住 BOOT 按钮
- 降低上传速度：将 `upload_speed = 921600` 改为 `115200`

### 串口监视器显示乱码
- 验证波特率是否匹配（115200）
- 检查 ESP32 是否正常供电
- 尝试更换 USB 线或端口

## 可用波特率

支持的上传/监视器波特率：
- 115200
- 230400
- 460800
- 576000
- 921600
- 1152000

## 其他资源

- [PlatformIO 文档](https://docs.platformio.org/)
- [ESP32 Arduino 核心](https://github.com/espressif/arduino-esp32)
- [HoloCubic_AIO 主仓库](https://github.com/ClimbSnail/HoloCubic_AIO)

## 许可证

请参阅此仓库根目录中的 LICENSE 文件。

