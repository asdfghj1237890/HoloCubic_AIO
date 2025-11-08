# HoloCubic AIO Firmware

**Language / 语言 / 語言:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

This is the firmware project for HoloCubic_AIO, built with PlatformIO for ESP32 (PICO-D4).

## Build Requirements

- [PlatformIO Core](https://platformio.org/) or [PlatformIO IDE](https://platformio.org/platformio-ide)
- Platform: ESP32 (espressif32 @ ~3.5.0)
- Framework: Arduino

## Build Instructions

### Using Command Line

```bash
# Navigate to the firmware directory
cd AIO_Firmware_PIO

# Build the release version (default)
pio run

# Build with specific environment
pio run -e HoloCubic_AIO_Releases

# Build debug version
pio run -e HoloCubic_AIO_Debug

# Clean build files
pio run -t clean

# Build and upload to device
pio run -t upload
```

### Using VS Code with PlatformIO Extension

1. Open VS Code
2. Install the **PlatformIO IDE** extension
3. Open the `AIO_Firmware_PIO` folder
4. Click the PlatformIO icon in the sidebar
5. Under **Project Tasks** → **HoloCubic_AIO_Releases** → click **Build**

## Build Environments

The project has two build configurations:

### HoloCubic_AIO_Releases (Default)
- Optimized for production use
- Located in `platformio.ini` as `[env:HoloCubic_AIO_Releases]`

### HoloCubic_AIO_Debug
- Debug build with logging enabled
- Optimization level: -O0
- Arduino HAL log level: 1

## Output Files

After successful compilation, binary files are located in:

```
.pio/build/HoloCubic_AIO_Releases/
```

Key files:
- **firmware.bin** - Main application firmware
- **bootloader.bin** - ESP32 bootloader
- **partitions.bin** - Partition table

## Flashing to ESP32

### Required Files and Flash Addresses

| File | Flash Address | Description |
|------|--------------|-------------|
| `bootloader.bin` | 0x1000 | ESP32 bootloader |
| `partitions.bin` | 0x8000 | Partition table |
| `boot_app0.bin` | 0xe000 | Boot application selector |
| `firmware.bin` | 0x10000 | Main firmware |

### Flash Using PlatformIO

```bash
# Upload via PlatformIO (easiest method)
pio run -t upload

# Specify custom port
pio run -t upload --upload-port COM5
```

### Flash Using esptool

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

**Note:** Change `COM5` to your actual serial port (e.g., `COM3`, `/dev/ttyUSB0`, `/dev/cu.usbserial-*`)

### Erase Flash (if needed)

```bash
python ../AIO_Tool/esptool_v41/esptool.py --port COM5 erase_flash
```

## Serial Monitor

To view serial output:

```bash
# Using PlatformIO
pio device monitor

# With specific baud rate
pio device monitor -b 115200
```

Default monitor settings:
- Baud rate: 115200
- Filter: esp32_exception_decoder

## Board Configuration

- **Board:** ESP32 PICO-D4 (`pico32`)
- **CPU Frequency:** 240 MHz
- **Flash Frequency:** 80 MHz
- **Flash Mode:** QIO
- **Upload Speed:** 921600 baud
- **Partition Scheme:** `partitions-no-ota.csv` (No OTA updates)

## Project Structure

```
AIO_Firmware_PIO/
├── src/                    # Source code
│   ├── HoloCubic_AIO.cpp  # Main application
│   ├── app/               # Application modules
│   ├── driver/            # Hardware drivers
│   ├── sys/               # System utilities
│   └── resource/          # Embedded resources
├── lib/                   # Project libraries
├── include/               # Header files
├── platformio.ini         # PlatformIO configuration
├── partitions-no-ota.csv  # Partition table definition
└── README.md             # This file
```

## Build Flags

Common build flags (defined in `platformio.ini`):
- `-fPIC` - Position independent code
- `-Wreturn-type` - Warn about return type issues
- `-Werror=return-type` - Treat return type warnings as errors

## Troubleshooting

### Build Fails
- Ensure PlatformIO is properly installed: `pio --version`
- Clean build files: `pio run -t clean`
- Update platform: `pio platform update espressif32`

### Upload Fails
- Check if device is connected: `pio device list`
- Verify upload port in `platformio.ini` (line 33)
- Try holding the BOOT button during upload
- Reduce upload speed: change `upload_speed = 921600` to `115200`

### Serial Monitor Shows Garbage
- Verify baud rate matches (115200)
- Check that ESP32 is properly powered
- Try different USB cable or port

## Available Baud Rates

Supported upload/monitor baud rates:
- 115200
- 230400
- 460800
- 576000
- 921600
- 1152000

## Additional Resources

- [PlatformIO Documentation](https://docs.platformio.org/)
- [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32)
- [HoloCubic_AIO Main Repository](https://github.com/ClimbSnail/HoloCubic_AIO)

## License

See the LICENSE file in the root directory of this repository.

