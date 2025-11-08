# HoloCubic AIO 韌體

**Language / 语言 / 語言:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

這是 HoloCubic_AIO 的韌體專案，使用 PlatformIO 為 ESP32 (PICO-D4) 建構。

## 建構需求

- [PlatformIO Core](https://platformio.org/) 或 [PlatformIO IDE](https://platformio.org/platformio-ide)
- 平台：ESP32 (espressif32 @ ~3.5.0)
- 框架：Arduino

## 建構說明

### 使用命令列

```bash
# 進入韌體目錄
cd AIO_Firmware_PIO

# 建構發布版本（預設）
pio run

# 使用特定環境建構
pio run -e HoloCubic_AIO_Releases

# 建構除錯版本
pio run -e HoloCubic_AIO_Debug

# 清理建構檔案
pio run -t clean

# 建構並上傳到裝置
pio run -t upload
```

### 使用 VS Code 搭配 PlatformIO 擴充套件

1. 開啟 VS Code
2. 安裝 **PlatformIO IDE** 擴充套件
3. 開啟 `AIO_Firmware_PIO` 資料夾
4. 點擊側邊欄的 PlatformIO 圖示
5. 在 **Project Tasks** → **HoloCubic_AIO_Releases** → 點擊 **Build**

## 建構環境

專案有兩個建構設定：

### HoloCubic_AIO_Releases（預設）
- 針對正式使用最佳化
- 在 `platformio.ini` 中設定為 `[env:HoloCubic_AIO_Releases]`

### HoloCubic_AIO_Debug
- 啟用日誌的除錯建構
- 最佳化等級：-O0
- Arduino HAL 日誌等級：1

## 輸出檔案

編譯成功後，二進位檔案位於：

```
.pio/build/HoloCubic_AIO_Releases/
```

關鍵檔案：
- **firmware.bin** - 主應用程式韌體
- **bootloader.bin** - ESP32 開機引導程式
- **partitions.bin** - 分區表

## 燒錄到 ESP32

### 所需檔案和燒錄位址

| 檔案 | 燒錄位址 | 說明 |
|------|---------|------|
| `bootloader.bin` | 0x1000 | ESP32 開機引導程式 |
| `partitions.bin` | 0x8000 | 分區表 |
| `boot_app0.bin` | 0xe000 | 啟動應用程式選擇器 |
| `firmware.bin` | 0x10000 | 主韌體 |

### 使用 PlatformIO 燒錄

```bash
# 透過 PlatformIO 上傳（最簡單的方法）
pio run -t upload

# 指定自訂連接埠
pio run -t upload --upload-port COM5
```

### 使用 esptool 燒錄

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

**注意：** 將 `COM5` 更改為你實際的序列埠（例如 `COM3`、`/dev/ttyUSB0`、`/dev/cu.usbserial-*`）

### 清除快閃記憶體（如有需要）

```bash
python ../AIO_Tool/esptool_v41/esptool.py --port COM5 erase_flash
```

## 序列埠監視器

檢視序列埠輸出：

```bash
# 使用 PlatformIO
pio device monitor

# 指定鮑率
pio device monitor -b 115200
```

預設監視器設定：
- 鮑率：115200
- 過濾器：esp32_exception_decoder

## 板卡設定

- **板卡：** ESP32 PICO-D4 (`pico32`)
- **CPU 頻率：** 240 MHz
- **快閃記憶體頻率：** 80 MHz
- **快閃記憶體模式：** QIO
- **上傳速度：** 921600 鮑率
- **分區方案：** `partitions-no-ota.csv`（無 OTA 更新）

## 專案結構

```
AIO_Firmware_PIO/
├── src/                    # 原始碼
│   ├── HoloCubic_AIO.cpp  # 主應用程式
│   ├── app/               # 應用模組
│   ├── driver/            # 硬體驅動程式
│   ├── sys/               # 系統工具
│   └── resource/          # 嵌入式資源
├── lib/                   # 專案函式庫
├── include/               # 標頭檔
├── platformio.ini         # PlatformIO 設定
├── partitions-no-ota.csv  # 分區表定義
└── README.md             # 說明檔案
```

## 建構旗標

通用建構旗標（在 `platformio.ini` 中定義）：
- `-fPIC` - 位置無關程式碼
- `-Wreturn-type` - 警告回傳型別問題
- `-Werror=return-type` - 將回傳型別警告視為錯誤

## 疑難排解

### 建構失敗
- 確保 PlatformIO 已正確安裝：`pio --version`
- 清理建構檔案：`pio run -t clean`
- 更新平台：`pio platform update espressif32`

### 上傳失敗
- 檢查裝置是否已連接：`pio device list`
- 驗證 `platformio.ini` 中的上傳連接埠（第 33 行）
- 嘗試在上傳期間按住 BOOT 按鈕
- 降低上傳速度：將 `upload_speed = 921600` 改為 `115200`

### 序列埠監視器顯示亂碼
- 驗證鮑率是否相符（115200）
- 檢查 ESP32 是否正常供電
- 嘗試更換 USB 線或連接埠

## 可用鮑率

支援的上傳/監視器鮑率：
- 115200
- 230400
- 460800
- 576000
- 921600
- 1152000

## 其他資源

- [PlatformIO 文件](https://docs.platformio.org/)
- [ESP32 Arduino 核心](https://github.com/espressif/arduino-esp32)
- [HoloCubic_AIO 主倉儲](https://github.com/ClimbSnail/HoloCubic_AIO)

## 授權

請參閱此倉儲根目錄中的 LICENSE 檔案。

