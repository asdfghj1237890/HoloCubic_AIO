# HoloCubic_AIO (All in one for HoloCubic)
### _You can also read a translated version of this file [中文版](https://github.com/ClimbSnail/HoloCubic_AIO/blob/main/README.md) or [in Korean 한국어](./README.md)._

"AIO" means All in one, which aims to integrate as many functions as possible into Holocubic AIO firmware and insist on open source. At present, the firmware source code reaches ` 2W + ` line, and the upper computer source code reaches ` 4K ` line (all excluding font pictures). We sincerely invite you to jointly develop AIO firmware, upper computer and its periphery, so that the firmware can meet the needs of more people. 

* The original author's project link https://github.com/peng-zhihui/HoloCubic
* Address of the project https://github.com/ClimbSnail/HoloCubic_AIO (latest version)
* Or https://gitee.com/ClimbSnailQ/HoloCubic_AIO 

### Developer
* AIO Framework Development and Some APP Writing: [ClimbSnail] (https://github.com/ClimbSnail)
* 2048 Game Application Development: [AndyXFuture] (https://github.com/AndyXFuture)
* New Weather Clock Application Development: [PuYuuu] (https://github.com/PuYuuu)
* BiliBili fan application development: [cnzxo] (https://github.com/cnzxo/)
* Memorial Day, Heartbeat App Development: [WoodwindHu] (https://github.com/WoodwindHu)
* PC Resource Monitor App Development: [Jumping99] (https://github.com/Jumping99)
* Multi-function Animation App Development: [LHYHHD] (https://github.com/LHYHHD)
* Developers continue to join. . . . 

_**Welcome to AIO internal test QQ discussion group**_

一群群号 755143193
二群群号 860112883
三群群号 676732387
四群群号 749207817
五群群号 866784418

![QQ_Group](https://gitee.com/ClimbSnailQ/Project_Image/raw/master/OtherProject/holocubic_qq_group.jpg)

### Main features 
1. Aggregate a variety of apps, with built-in weather, clock, photo album, special effects animation, video playback, computer screen projection, web settings and so on. (Reference manual for specific use of each APP)
2. Whether tf card is plugged in or not, whether mpu6050 is welded normally, and whether wifi is connected (2.4 G wifi must be used) will not affect the system startup.
3. The program is relatively modular and low coupling.
4. Provide web interface for distribution network and other setting options. Note: Refer to ` APP introduction ` for specific operation
5. Provide web-side connection. Besides supporting ip access, it also supports domain name direct access http://holocubic (some browsers may not support it well)
6. Provide web files to upload to SD card (including deletion), without unplugging SD to update pictures.
7. Provide a complete set of upper computer software and open source upper computer source code. Https://github.com/ClimbSnail/HoloCubic_AIO_Tool 

### This firmware designs a set of low coupling framework, which is more conducive to the realization of multi-functions 
Bilibili function operation demonstration video link https://www.bilibili.com/video/BV1wS4y1R7YF/

![HomePage](Image/holocubic_main.jpg)

![HomePage](Image/holocubic_home.png)

![UploadPage](Image/holocubic_upload.png)

![SettingPage](Image/holocubic_setting.png)


### Firmware brushing tool (no IDE environment required) 
Download the upper computer in the group for brushing.
1. `bootloader_dio_40m. bin` booted `bootloader`.
2. `partitions.bin` partition file
3. `boot_app0.bin`
4. Latest firmware `HoloCubic_AIO_XXX.bin` 

The ` HoloCubic_AIO_XXX. bin ` file is updated with each version update, and the other three files remain basically unchanged.

Put the first three files above in the same directory as ` CubicAIO_Tool. Exe `, double-click to run ` CubicAIO_Tool. Exe `, and select the latest firmware ` HoloCubic_AIO_XXX. bin ` in the software to brush the firmware.

Host computer operation demonstration video link https://b23.tv/5e6udh

Like AIO firmware, this host computer insists on open source, and its open source address is https://github.com/ClimbSnail/HoloCubic_AIO_Tool 

![AIO_TOOL](Image/holocubic_aio_tool.png)

![AIO_TOOL](https://gitee.com/ClimbSnailQ/Project_Image/raw/master/OtherProject/holocubic_aio_tool.png)

### Precautions for startup 
Since the small TV uses MPU6050 gyroscope accelerometer, it is necessary to keep the small TV naturally (do not hold it in hand) 3 seconds before power-on, and wait for the sensor to initialize. After initialization, the RGB light will fully light up, and then it can operate normally. Inserting or not inserting the memory card will not affect the normal boot. If there is a problem with 6050 welding, the attitude reading will be disordered after initialization (phenomenon: the application will be continuously switched). 

### Function switching instructions:
1. The file system of the TF card is fat32. TF is non-essential hardware, but photo albums, video playback and other functions need to rely on this. If you are going to use the memory card, it is best to put all the files and folders in the directory of the memory card in this project in the root directory of the TF card before using the memory card.
2. Plugging tf memory card or not will not affect boot, but will affect the functions of some apps (which will be explained in the introduction of each app).
3. Shake from side to side to switch and select various apps.
4. Tilt forward for 1s to enter the APP application on the current page, and more functions will be integrated in the future. Also, tilt back for 1s to exit the APP.

### Introduction to APP

##### Web Configuration Service (Web Server)
![WebPage](Image/holocubic_web.png)

1. Operating conditions: None. Note: WiFi and other information is stored in flash, memory card does not affect the connection of WiFi function.
2. When enabled, ` Web Sever Start 'is displayed. The small TV turns on AP mode, which is built on ` AP_IP ` (marked on the service interface of the screen). The hot spot of AP mode is called ` HoloCubic_AIO ` without password.
3. Start using the computer in the same network environment (same network segment) as' HoloCubic '. If you haven't connected to WiFi before, you need to use your computer to connect to WiFi without password, which is a hot spot named ` HoloCubic_AIO ` released by HoloCubic.
4. Enter ` Local_IP ` or ` AP_IP ` in the browser address bar (http://192.168.4.2 also supports domain name direct access to http://holocubic) to enter the administrative settings background. It is recommended to use ` ip address ` access.
5. System parameters, weather APP parameters, photo album parameters, player parameters and so on can be set in the webpage.
6. Because of the large number of apps at present, it is cumbersome to switch and find, so you can also configure the "self-starting app" in the "Web Server". 

##### File Manager (File Manager)
Function: Manage the files on the memory card through the wireless network.

1. Run APP condition: WiFi must be configured normally. Memory card must be inserted. To avoid restarting due to insufficient power during WiFi connection, please ensure that the USB port is fully powered. At present, some functions are still under development.
2. Entering the ` Holocubic 'file manager will automatically connect to the configured WiFi and display the IP address.
3. Unfinished: Fill in your IP address of 'Holocubic' in the file manager software of the upper computer (the port can be changed without changing), and click Connect.
Note: Currently the file manager temporarily uses windows explorer, and enter ftp://holocubic: aio @ 192.168. 123.241 in the address bar (192.168. 123.241 is the IP address displayed on my little TV, if prompted to turn on access, turn it on) 

##### Photo album (Picture)
1. Conditions for running APP: A memory card must be inserted, a ` image/` directory must exist under the root directory of the memory card (you can also use the ` Web Server service ` APP to upload photos through the browser), and a picture file (jpg or bin) must exist under the ` image/` directory.
2. Convert the pictures to be played into a certain format (. jpg or. bin), and then save them in the ` image/` directory. The file name of the pictures must be English characters or numbers.
3. After entering the photo album app with firmware, the picture file in the ` image/` directory will be read.
4. The web page side of ` WebServer ` can set additional functions. 

About picture conversion: Use the attached upper computer conversion (resolution is arbitrary, the software will automatically compress to the specified resolution).
* Common weather pictures, converted to C Array, format Indexed 16 colors, select C Array.
* Images that are not commonly used can be converted into (True color with alpha, select Binary RGB565) bin files and stored in SD cards, which can save some program storage space and increase functions. Conversion to jpg images is supported. 

##### Video playback (Media)
1. Conditions for running APP: Memory card must be inserted, and ` movie/` directory must exist under the root directory of memory card.
2. Convert the video to be played (preferably 1: 1 aspect ratio) into a target file (mjpeg or rgb format) by using the conversion tool matched with this firmware, and store it in the ` movie/` directory. The video file name must be English characters or numbers.
3. After running the player app, the video files in the ` movie/` directory will be read.
4. Under the default power, it enters the low power consumption mode after 90 s without any action, and enters the second-level low power consumption mode after 120s, which is manifested by the decrease of the number of playing frames.
5. The web page side of ` WebServer ` can set additional functions. 

##### Screen share, screen share
1. Conditions for running the app: No memory card is required, but you need to use the ` Web Server Service ` app to set your wifi password (make sure you can connect to the router). To avoid restarting due to insufficient power during WiFi connection, please ensure that the USB port is fully powered.
2. At present, the upper computer uses third-party software, and will independently write the projection upper computer in the later stage to improve the performance.
3. The upper computer of this screen projection is the upper computer of [Daguai] (https://gitee.com/superddg123/esp32-TFT/tree/master).
4. The web page side of ` WebServer ` can set additional functions. 

##### Weather (Weather)
There are two weather clock apps 
###### New version of weather
1. The new version by `PuYuuu` mimics the `misaka` clock interface. Uses Amap Weather API.
2. Conditions for running APP: Must be in a networked state.
3. To use the new weather clock, you need to modify the `city name (precise city code)` and `API personal Key` in the "Web Server" web service. (City code reference table https://lbs.amap.com/api/webservice/download, Key acquisition method https://lbs.amap.com/api/webservice/create-project-and-key) 
###### Old version of weather old
1. The old UI design mimics [CWEIB] (https://github.com/CWEIB)
2. Conditions for running APP: It must be networked and set the location, weather_key. It works normally in most cases without inserting a memory card.
3. Generally, it can work without inserting a memory card, but some weather icons are stored in the memory card (because the internal flash is not enough), so it is necessary to copy the ` weather/` folder attached to the firmware to the root directory of the tf card.
4. To use the old weather clock, you need to modify the "intimate weather city name" and "key" of intimate weather in the "Web Server" web service. (The application address is https://seniverse.com. The program uses the v3 version of api by default.)

Note: Even after the network is disconnected, the clock still runs. (It is best to connect WiFi when starting up, which will automatically synchronize the clock. Try to synchronize the clock intermittently during use) 

##### Special Effects Animation (Idea)
1. Run APP condition: None. Built-in special effects animation.

Note: Transplant the function of "Peter Pan", thank you here! 

##### 2048 APP
1. The '2048' game was written and agreed by group friend 'AndyXFuture' and incorporated into AIO firmware by 'ClimbSnail'. The original project link is ` https://github.com/AndyXFuture/HoloCubic-2048-animm '
2. Run APP condition: None. As long as the basic screen lights up.
3. Operation Note: The game "up" and "down" operation because of the original "enter" and "exit" as the same action, the system has been operating for a differentiated action, the game "up" and "down" normal operation can be, "enter" and "exit" need to tilt 1 second before triggering. 

##### BiliBili APP
1. Run app condition: A folder named ` bilibili ` must be in the memory card. Wifi must be configured normally. To avoid restarting due to insufficient power during WiFi connection, please ensure that the USB port is fully powered.
2. 'UID' viewing method: Open bilibili on the computer browser and log in to the account. After that, the browser opens a blank page and pastes Enter this website https://space.bilibili.com/. A string of pure digital codes will automatically appear at the tail of the website, which is UID.
3. Before using it for the first time, fill in the ` UID ` code on the Web page of ` WebServer App '.
4. It is necessary to add a picture named ` avatar.bin ` own bilibili avatar in the folder named ` bilibili ` in the memory card, and a ` bin ` file with a resolution of ` 100*100 ` (it can be converted by AIO host computer). 

Note: The program is written by ` cnzxo `. 

##### Anniversaries (Anniversaries)
1. Run APP condition: Networking status
2. Before using it for the first time, you should fill in the name and date of the anniversary on the webpage of ` WebServer App `. At present, you can set up two anniversaries. The words supported by anniversaries are ` birthday and graduation, raising small dinosaurs, planting potatoes, wife, girlfriend, parents, milk, siblings, brothers and sisters, wedding anniversary '. If the words contained in the anniversaries name are not within this range, please generate your own font file and replace the ` src\ app\ anniversaries\ msyhbd_24. c ` file. Date format such as ` 2022.5.8 ', if the year is set to 0, it is considered to be a repetitive anniversary (such as birthday) every year.

Note: Remembrance Day and Heartbeat are reproduced from the [LizCubic] (https://github.com/qingehao/LizCubic) project. The program is written by ` WoodwindHu ` 

##### Heartbeat (Heartbeat)
1. Conditions for running APP: networked status (performance mode needs to be turned on), an mqtt server with open port 1883, and two HoloCubic.
2. Before using it for the first time, fill in the configuration on the Web page of ` WebServer App '. Role can choose 0 and 1 to represent the two HoloCubic interactions, respectively. Client_id is the unique identification of the device. Please set the two Holocubic to the same QQ number here. Mqtt_server fills in its own mqtt server address, and port fills in the port number. The user name and password depend on the specific server configuration.
3. After setting up the heartbeat APP, turn on the automatic networking and open the mqtt client. Automatically enter the APP after receiving another HoloCubic message. Entering the APP in the normal way automatically sends a message to another HoloCubic.
4. Update free services from time to time in the group. You can ask the management or group friends for specific configuration parameters.

Note: Remembrance Day and Heartbeat are reproduced from the [LizCubic] (https://github.com/qingehao/LizCubic) project. The program is written by ` WoodwindHu ` 

##### Stock quotes in real time (Stock)
1. Run APP condition: WiFi must be configured normally. To avoid restarting due to insufficient power during WiFi connection, please ensure that the USB port is fully powered.
2. Before using it for the first time, modify the stock code you want on the Web page of WebServer App.

Note: The program is written by ` redwolf `

##### PC Resource Monitor (PC Resource)
1. Run APP condition: WiFi must be configured normally. PC and HoloCubic must be on the same network segment. Set the PC service IP address in `WebServer APP` (refer to the tutorial for details).
2. Download [AIDA64](https://www.aida64.com/downloads), install AIDA64 on your PC and import the configuration file `aida64_setting.rslcd` (located in the `AIO_Firmware_PIO\src\app\pc_resource` directory or in the group files).

Note: The detailed operation steps are lengthy, see the group documentation. This application is developed by `Jumping99`.

##### Multi-function Animation (LH&LXW)

Download the firmware with the LH&LXW APP for your transparent small TV, enter the system, select the LH&LXW APP, tilt backward to enter the APP, tilt forward to exit the APP, tilt left/right to select different functions, tilt backward to enter the selected function.

【Function Description】

Function 1: Code Rain; After entering this function - tilt left/right to switch code rain size, tilt forward to exit this function.

Function 2: Cyber Album; After entering this function - tilt left to stop automatic switching, tilt right to resume automatic switching, tilt backward to switch between static and dynamic, tilt forward to exit this function.

Before entering this function, make sure your memory card has the following files:
```
1. ./LH&LXW/cyber/imgx.cyber stores the image files to be displayed (x is 0~99)
2. ./LH&LXW/cyber/cyber_num.txt stores the number of image files to be displayed (00~99) for example, 7 images, write 07
Note: The number of images in ./LH&LXW/cyber/imgx.cyber must equal the number of image files entered by the user in ./LH&LXW/cyber/cyber_num.txt
```
The .cyber format image files are generated by the following python code:
```python
import cv2
img_path = './123.jpg'# Input image path (image size must be 48x40)
out_path = './123.cyber'# Output file path
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
with open(out_path, 'wb') as f:
    for a in img:
        for b in a:
            f.write(b)
```

Function 3: QQ Super Emoji; After entering this function - tilt left/right to select different emojis, tilt backward to play the current emoji, tilt forward during playback to exit playback, tilt forward when selecting emojis to exit this function. The emoji automatically loops for 33.3 seconds, then plays the next one. During playback, you can manually switch by tilting left/right.

Before entering this function, make sure your memory card has the following files:
```
1. ./LH&LXW/emoji/videos/videox.mjpeg stores the videos to be played (size 240x240) (x is 0~99)
2. ./LH&LXW/emoji/images/imagex.bin stores the cover images of the videos to be played (size 60x60) (x is 0~99)
3. ./LH&LXW/emoji/emoji_num.txt stores the number of videos to be played (00~99) for example, 7 videos, write 07

Note: The number of videos in ./LH&LXW/emoji/videos/ must equal the number of cover images in ./LH&LXW/emoji/images/
and must equal the number of videos entered by the user in ./LH&LXW/emoji/emoji_num.txt.
```
Function 4: Eyeball; After entering this function - tilt left/right to switch eye styles, tilt forward to exit this function.

Function 5: Dynamic Heart; After entering this function - shake the small TV, the particles forming the ♥ will also shake. After stopping shaking, the particles will gather back into a ♥ shape, tilt forward to exit this function.

APP demonstration video: 【LVGL menu#transparent small TV#LVGL development】 https://www.bilibili.com/video/BV1wK421173C/?share_source=copy_web&vd_source=68337adbea96c8cef50403a4b2809df6 


### About compiling engineering code
1. This project code is based on the ESP32-Pico Arduino platform of PlatformIO plug-in on vcode. Specific tutorials can be found in Bilibili. Recommended Tutorial [https://b23.tv/kibhGD] (https://b23.tv/kibhGD)
2. Remember to modify the ` upload_port 'field in the ` platformio.ini' file under the project to correspond to its own COMM port.
3. At present, the latest version does not need to modify the SPI pins in the SPI library. A SPI library with modified SPI pins is placed separately under the ` lib ` of this project. The following are the actions of previous versions (negligible) 

~~Then you need to modify an official library file to use it normally (otherwise, the memory card will fail to read):
Both PlatformIO and ArduinoIDE users need to install the Arduino firmware support package of ESP32 (Baidu has a large number of tutorials). Either way, you need to modify the ` MISO ` default pin in the ` SPI ` library to ` 26 `, such as the package path of the arduinoIDE to ` esp32\ hardware\ esp32\ 1.0. 4\ libraries\ SPI\ src\ SPI.cpp ` file, **Modify the MISO to 26 in the following code**：~~
```
    if(sck == -1 && miso == -1 && mosi == -1 && ss == -1) {
        _sck = (_spi_num == VSPI) ? SCK : 14;
        _miso = (_spi_num == VSPI) ? MISO : 12; // 需要改为26
        _mosi = (_spi_num == VSPI) ? MOSI : 13;
        _ss = (_spi_num == VSPI) ? SS : 15;
```
~~This is because two hardware SPIs are used to connect the screen and SD card on the hardware, in which the default MISO pin of HSPI is 12, and 12 is used to set the flash level when powering up in ESP32. Pulling up before powering up will cause the chip to fail to start, so we replace the default pin with 26.~~

### Program frame diagram 

![HoloCubic_AIO_Frame](Image/holocubic_AIO_Frame.png)

![HoloCubic_AIO_Frame](https://gitee.com/ClimbSnailQ/Project_Image/raw/master/OtherProject/holocubic_AIO_Frame.png)

AIO framework explanation link https://www.bilibili.com/video/BV1jh411a7pV?P=4

You can pay attention to the design of UI by yourself `Edgeline`, `gui-guide` and other tools.

PlatformIO Simulator https://github.com/lvgl/lv_platformio

Application Icon (128*128): You can download Ali Vector Map https://www.iconfont.cn/

Error location code during debugging: ` xtensa-esp32-elf-addr2line-pfiaC-e firmware name. elf Backtrace address information `

Learn about LVGL: 'http://lvgl.100ask.org', 'http://lvgl.100ask.net'

Font generation for lvgl can be done using: ` LvglFontTool v0.4 ` already placed in the Doc directory

C file to extract all Chinese characters: You can use the project under the ` Script/get_font. py ` script extraction. ` Path to python get_font. py font. c file ` 

### Version Update Log
CurVersion:v2.3.0

#### HoloCubic_AIO Firmware_v2.3.x.bin
1. Stock: Refactored data processing and UI, added international stock market support, fixed memory leaks/overflows.
2. Weather: Integrated AccuWeather API, improved stability, optimized multi-language and traditional Chinese font.
3. Web Settings: Enhanced multi-language and interface performance.
4. Anniversary: Fixed time API.
5. Others: Streamlined unnecessary functions and resources; fixed font inclusion issues; optimized Pomodoro interface.

#### HoloCubic_AIO Firmware_v2.2.x.bin
1. Updated LVGL to v8.3.3, modified all APPs involving LVGL.
2. Reviewed all functions with return values but no return statement.

#### HoloCubic_AIO Firmware_v2.1.x.bin
1. Added weather font library.
2. Added Stock APP.
3. Added brightness adjustment threshold to avoid crashes.

#### HoloCubic_AIO Firmware_v2.0.x.bin
1. Fixed the issue of 7-day weather only reading Beijing, modified API, added humidity.
2. Support adjusting mpu6050 operation direction mapping.
3. Support littlefs (transfer existing kv storage).
4. SD card supports SPI, SD dual mode (to be updated).
5. Added parameter settings.
6. Jointly adjusted screen projection host computer (to be updated).
7. Fixed 2048 (to be updated).
8. Support hiding APPs (to be updated).
9. Fixed Bilibili API and memory leaks.
10. Fixed memory leaks caused by styles not using lv_style_reset when all Apps use lvgl.
11. New weather supports three-character city names.
12. Added performance mode support.
13. Added HeartBeat and Anniversary Apps.

##### HoloCubic_AIO Firmware_v1.9.x.bin
1. Major changes to screen sharing APP, fixed screen lag issue (to prevent overheating, performance is set to medium).
2. Added support for FTP file transfer (host computer not updated).
3. Added heat control during video playback to avoid ESP32 damage due to overheating.

##### HoloCubic_AIO Firmware_v1.8.x.bin
1. Added 2048 game app, new weather clock, Bilibili fans app.
2. Modified MPU6050 operation, added two key values.
3. Modified picture loop playback. Fixed original clock interface lag issue.
4. Added event queue.

##### HoloCubic_AIO Firmware_v1.7.x.bin
1. Added screen sharing. Added Setting app.
2. Added app names.
3. Added adjustment of screen brightness and direction in WebServer.
4. Effectively added support for switching direction in video and photo album.
5. Fixed overlapping images caused by graphics not being cleared in Idea App.
6. Fixed memory release issues in some apps.
7. Changed weather icons to Qweather icons.

##### HoloCubic_AIO Firmware_v1.6.x.bin
1. Adjusted screen brightness, WiFi scheduling control, reduced power consumption.
2. Modified TFT_eSpi library to eliminate "screen splash" after boot.
3. On the premise of maintaining the original RGB playback function, added mjpeg video playback function, increasing video frame rate to 20fps.

##### HoloCubic_AIO Firmware_v1.5.x.bin
1. Added video playback (continuous improvement).
2. Added MPU6050 calibration to achieve compatibility with tilted bases.
3. Photo album function supports jpg and bin dual formats.
4. Added Idea animation APP.
5. Accelerated boot display.

##### HoloCubic_AIO Firmware_v1.4.bin
1. Extensively modified program framework.
2. Added screen brightness.
3. Fixed original photo album "white screen" phenomenon when switching.

##### HoloCubic_AIO Firmware_v1.3.bin
1. Moved WiFi configuration information from memory card to flash, enabling apps that are not photo albums to work without a memory card. Configuration APP needs to be used in the browser to configure network information at boot. Subsequent firmware upgrades do not require reconfiguration.
2. Adjusted RGB ambient light.
3. Added `movie` directory in memory card (for future expansion).

##### HoloCubic_AIO_Tool Host Computer_v1.6.0
1. Added multi-language support (Traditional Chinese, English, etc.).
2. Added tool settings page.
3. Fixed MJPEG tool issues, added video conversion logging and thread support.
4. Improved ffmpeg command real-time output capture functionality.
5. Enhanced error handling and validation for input files.

### Acknowledgement
* ESP32 Memory Distribution https://blog.csdn.net/espressif/article/details/112956403
* Video playback https://github.com/moononournation/RGB565_video
* FTP reference document https://blog.csdn.net/zhubao124/article/details/81662775
* ESP32 arduino running dual-core https://www.yiboard.com/thread-1344-1-1.html
* Mandatory Portal Authentication https://blog.csdn.net/xh870189248/article/details/102892766
* Thanks to the authors of the open source libraries used in the `lib 'directory 
