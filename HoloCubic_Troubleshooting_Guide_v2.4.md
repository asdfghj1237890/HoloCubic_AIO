###### <sub>All In One™</sub><br />Zhihui's `HoloCubic` Mini TV<br />──<br /><sup>Beginner's Production Guide</sup><br />`#Latest Version|V2.4#`<br /><br /><br />**Sujian Danmo, Liuma Xiaoge, Mysterious Treasure Room, Wuchang Miaotai, Zuimeng, Dong Xiaoxin, Xiao Erhei, Southern Anhui Romantic Revolution, Xieqian, Yiye Zhiqiu**<br />*Must Read Before Joining Group*

[TOC]

<details>
<summary>Chapter 1  Preface</summary>

# Chapter 1  Preface

This document is from `HoloCubic AIO Multi-function Firmware Group 755143193`, and is a detailed description of making `HoloCubic` and `AIO Firmware (All in One)`. Transparent Mini TV Introduction: https://www.bilibili.com/video/BV1jh411a7pV?p=6. If you have questions, ask politely - group members are contributing with love. `Note: Read the manual before asking questions`

The main content of this article is compiled based on existing materials in the group.

Original author's project link: https://github.com/peng-zhihui/HoloCubic

Group owner's project address: https://github.com/ClimbSnail/HoloCubic_AIO (latest version) or: https://gitee.com/ClimbSnailQ/HoloCubic_AIO

`Video References:`

`Group Owner (ClimbSnail Bilibili: Liuma Xiaoge) Video Collection 📝`:
https://www.bilibili.com/video/BV1jh411a7pV/?spm_id_from=333.788.recommend_more_video.0

`Yiye Zhiqiu's Comprehensive Tutorial`: https://www.bilibili.com/video/BV11h41147iJ?spm_id_from=333.999.0.0

`Mysterious Treasure Room's [Production Pitfall Avoidance] 💡`: https://b23.tv/WuBqTGO

`Xieqian's Soldering Reference Tutorial`: https://b23.tv/A83JUGt

`Group Member Xuedin Tutorial Reference`: https://www.bilibili.com/video/BV1eu411i7Qo

Others to be added...

</details>

<details>
<summary>Chapter 2  Hardware, Shell and Other Production</summary>

# Chapter 2  Hardware, Shell and Other Production

`All hardware files mentioned in Chapter 2 are in the group file folder "Hardware Shell Related" in the corresponding version package`

<details>
<summary>Pre-production Preparation</summary>

## Pre-production Preparation

Install Altium Designer (abbreviated as "AD", available in group files folder "Developer Tools", can be downloaded by yourself)

Installation purposes: 
① Convenient to open schematic & PCB when there are soldering problems
② Package for PCB manufacturer (such as JLCPCB). To avoid splitting order suspicion, it is recommended to add or delete some silkscreen. (If you don't know how to modify or generate Gerber files, you can use "Huaqiu DFM" to directly generate Gerber files, method in 2.3.2)

`Install "JLCPCB Order Assistant" - Essential for free PCB`

Download link (upper right corner: Download PC Assistant): https://www.jlc.com/

</details>

<details>
<summary>Hardware Versions (Images from Group Members)</summary>

## Hardware Versions (Images from Group Members)

Zhihui has four versions: transparent base Naive, metal, Iron Man Ironman, and BiliBili angel base. Most group members use the transparent base Naive version.

`① Transparent Base Naive Version (Board thickness recommended 1.2mm)`:

`② Metal/Transparent Version (Board thickness recommended 1.2mm [Transparent Metal2.0 supports 1.6mm, but 1.2mm recommended])`:

`③ Iron Man Ironman Version (Zhihui's original file, board thickness recommended 1.0mm)`:

`④ BiliBili Angel Base Version`: None

Most group members use the transparent base Naive version. Of course, the group owner also made many metal Metal versions. Some group members also made Iron Man head versions.

Many experts have written different firmware, and firmware versions are basically compatible with these two hardware versions (at least the group owner's AIO firmware is fully compatible).

Note the original author Zhihui's circuit has timing issues (`C7 capacitor needs to be changed to 1uF~10uF to solve`). The group has improved versions (`Be sure to check the latest version in group files`).

Note:

**①** `Hardware only supports 2.4G WiFi.` 5G and dual-band combined are not supported. No firmware can break through hardware limitations.

**②** `For those without electronics background, no hands-on ability but want to play`, it is recommended to ask group members, some have finished products for transfer or sale (`The cost of making it successfully once is about 200 yuan, please consider carefully before making`).

**③** If you're not sure about component purchases, be sure to ask group members!!!

**④** `New DC-DC (metal) version, LDO (LP2992 or ME6211C33), DCDC (MP1471) choose one [If MP1471 is soldered, both expansion board and main board LDO must be removed].`

**⑤** Metal and Naive compatibility needs to check the latest in the group (`version packages`)

</details>

<details>
<summary>PCB Fabrication</summary>

## PCB Fabrication

### File Download and Instructions

`Step 1`: After learning about group materials through 2.2, confirm the hardware version and download the corresponding PCB files from the AIO group files (group files will be updated regularly, old files will be removed).

`Note: Group files are tested and improved by the group owner`

`Step 2`: After downloading and extracting, five files will appear (latest files come with `one-click generate fabrication files` program). Using Metal version as example.

### PCB Modification Tutorial (Old method, now deprecated)

`Note: Must use AD to modify silkscreen before ordering`, add or delete silkscreen, then compress and package the PCB file to JLCPCB. If you don't know how to modify silkscreen, generating Gerber files also works. (If you don't know how to generate Gerber files, you can download "Huaqiu DFM" software)

#### How to Use Huaqiu DFM to Generate Gerber

Huaqiu DFM download link: https://dfm.elecfans.com/index

Network disk download link: https://www.aliyundrive.com/s/vh9fgUf57jz

`① Common Gerber File List`

When making PCB boards, the Gerber files delivered to the PCB manufacturer must include 1-10 and 15 below, where 11-14 can be omitted, but it is recommended to include them together in the Gerber files.

1. GTO (Top Overlay): Top silkscreen layer, commonly white oil.
2. GTS (Top Solder): Top solder mask layer, commonly green oil.
3. GTL (Top Layer): Top routing layer.
4. Gtp (Top Paste Mask): Top solder paste protection layer.
5. GBp (Bottom Paste Mask): Bottom solder paste protection layer.
6. GBL (Bottom Layer): Bottom routing layer.
7. GBS (Bottom Solder): Bottom solder mask layer, commonly green oil.
8. GBO (Bottom Overlay): Bottom silkscreen layer, commonly white oil.
9. GMx (Mechanical) or GKO (Keep-out Layer): Used to define board frame, select which layer the frame is on.
10. Gx (Mid Layer): Middle signal layer X, as many files as there are middle layers.
11. Gd (Drill Drawing): Drilling drawing layer.
12. Gg (Drill Guide): Drilling instruction layer.
13. Gpt (Top Pad Master): Top pad layer.
14. Gpb (Bottom Pad Master): Bottom pad layer.
15. NC drill Files: Drilling files, AD export is generally txt file.

### JLCPCB PCB Fabrication

`Step 1`: Use the `one-click generate JLCPCB free Gerber files` in the corresponding version PCB file folder, double-click to run and generate the latest fabrication files. Package each gerber subfolder under the generated `AIO_Gerber_xxx` folder into compressed packages separately.

`Step 2`: Open JLCPCB order software, upload the just created compressed package fabrication file, please be patient during parsing.

`Step 3`: After parsing is complete, the order option class shown in the figure below will appear. The board length and width will generally be automatically recognized. If it cannot be automatically recognized, you can fill in randomly such as 5x5, etc. The board factory will adjust it later. Board quantity is 5 (exceeding cannot be free).

`Step 4`: Board thickness depends on your chosen mini TV version.

`Step 5`: Solder mask color can be chosen according to your preference.

`Step 6`: Whether to open stencil file.

Note: Newbies are recommended to open the main board front stencil. The group will provide stencil files. You can find stencil sellers on Taobao yourself, price is 10~20 (excluding postage).

</details>

<details>
<summary>Material and Tool Purchasing</summary>

## Material and Tool Purchasing

### Component Purchasing (Refer to BOM table in AIO group online documents)

**①** There is a BOM list in the files. You can purchase components according to BOM (Taobao Youxin Electronics recommended for purchase). MPU 6050 can be purchased as module for disassembly. You can also refer to recommended links in group online documents: https://docs.qq.com/sheet/DQUpSbmN4TVNha0h0

**②** Screen can be purchased from Taobao Zhongjingyuan (brand Hancai [currently the best display effect])

**③** If you don't know or are unsure, you can ask group members.

**④** Capacitor/resistor withstand voltage ≥5V are all acceptable (such as 16V, 24V, 50V, etc.) [Only for this project]

**⑤** Connector socket model: flip-down 8P (both expansion board and main board use this), ribbon cable buy same-direction 0.5 * 8P (naive recommended 6cm, metal use 3cm).

**⑥** Zhihui's original card slot model is DM3D-SF (not recommended). Improved board card slot see group online document link or Taobao search flip-in welding TF card socket (8P)

**⑦** When purchasing LDO, be sure to pay attention to the model, ME6211C33 [the 33 at the end means 3.3V] don't buy wrong, some group members bought wrong.

Note: Some components are recommended to buy 1-2 more, flip-down 8P socket recommended to buy 6-8

**⑧** Memory card selection

The firmware has certain compatibility issues with memory cards, not all are compatible. Currently supports `SD and SDHC type memory cards, does not support SDXC!` Recommended verified memory cards:

① Aigo 32G regular card. Taobao about 20 yuan. (Cost-effective, recommended)
② SanDisk 32G regular card. Taobao about 30.

**⑨** Screen issues

Screen specifications: 1.3 inch, driver ST7789, resolution 240*240, soldering 12Pin. Most screen boards are metal shell, `pay attention to short circuit issues!`

There are many such screens online, but for making Holocubic you need to choose carefully, the screen will affect the overall display effect. Currently tested many screen manufacturers, the best effect is Zhongjingyuan.

Not recommended to use other manufacturers' screens for making Holocubic. Below is actual comparison (please ignore background differences):

Left: Zhongjingyuan (Hancai) Right: Youzhijing

The difference between the two screens after attaching the prism is mainly that the blank area around the `Youzhijing` display is seriously blue, which greatly affects the final effect. The blank area display of `Zhongjingyuan` is very pure. Note: Actually Zhongjingyuan bottom color is also blue, but very slight.

About brightness issue (not related to screen):
You can also see from the above picture that the left is obviously brighter. This is because the left did not tear off the protective film on the factory polarizer (can increase brightness), while the color on the left becomes extremely inaccurate due to refraction of the protective film. Students who have done experiments will also find that after tearing off the protective film, the brightness of prism X-axis placement and Y-axis placement is different. Human eyes are more sensitive to color than brightness. Personally recommend tearing off the protective film. (`Brightness can be improved by purchasing 6:4 prism, 6:4 brightness is slightly higher than 5:5 brightness`)

Of course, if you care more about brightness, you can also not tear off the protective film. When buying screens, you can ask the seller to ship with protective film and not put that green label on the protective film.

### Production Tools (Reference group owner)

`① Soldering category`

Soldering iron (936 station is affordable with many tip styles);
Soldering station, also called: teppanyaki (500w Luxianzi);
Tweezers (0402 is small, recommended to use pointed tweezers);
Solder wire (0.3mm/0.5mm/1.0mm DIY commonly uses these three specifications),
Flux and solder paste recommended to buy Weixiulao brand (if conditions permit, you can buy Japanese brand Zhongya).

`② Sandpaper`

300 grit, 800 grit, 5000 grit, 8000 grit, purchase according to needs (larger number means finer polishing)

High-transparency shell is frosted shell polished with fine sandpaper and sprayed with varnish.

`Group owner recommends 400 and 800 grit, coarse grinding + fine grinding. 800 grit can grind out frosted feeling. Additionally, polishing needs water polishing, otherwise the polished surface will be full of scratches under light.`

`③ Glue (see group owner's tutorial)`

704 glue (seal screen frame gap), UV glue or B-7000 [for attaching screen]. Note: UV glue requires additional purchase of curing lamp. Prism attachment video tutorial: https://www.bilibili.com/video/BV1jh411a7pV?p=5

### Shell Production

Pure white can go to Sanweihou (JLCPCB)

Semi-transparent can go to Weilaigongchang or Taobao (or consult group members)

Metal CNC (car has left) [Can wait for group owner's Iron Man car]

</details>

<details>
<summary>3D Printing of Shell</summary>

## 3D Printing of Shell

`All latest model files are in the group corresponding version package!!!`

`① Naive transparent base (improved version)`

1. Suitable for Naive version hardware.
2. Original design uses screws to connect upper and lower shell, but group members have magnetic improved version (magnets are 3*3mm round magnets) recommended to use improved version.
3. Base uses 3D printer production, recommended to use semi-transparent printing effect.
4. If the printed surface wants to be frosted, recommend using 800 grit sandpaper to polish under running water.
5. If finding online printing service, pay attention to tolerances, shell too small cannot fit main board.
6. Main board thickness 1.2mm (using improved shell). Expansion board thickness 1.2mm.

`② Metal base (improved version)`

1. Suitable for Metal version hardware.
2. Base uses 3D printer production, recommended to use semi-transparent printing effect.
3. If the printed surface wants to be frosted, recommend using 800 grit sandpaper to polish under running water.
4. v1.0 and v2.0 versions are modified based on Zhihui's original version, bottom opened memory card slot.
5. v1.0 and v2.0 are compatible with all versions of main board and expansion board in this folder. Recommended PCB board thickness 1.2mm (main board and screen version)

`V1.0 left and right reinforcement seats are too large, V2.0 optimizes this defect.`

`③ Ironman Iron Man base`

1. Suitable for Ironman version hardware.
2. Zhihui's original base recommended: main board thickness 1.0mm. Expansion board thickness 1.0mm.

`④ BiliBili`

Base temporarily unavailable. (See group files)

`⑤ Iron Man head`

Base temporarily unavailable. Open source address: https://gitee.com/qlexcel/holo-iron-man

</details>

<details>
<summary>Dynamic BOM Usage and Production</summary>

## Dynamic BOM Usage and Production

Purpose: Dynamic placement files can improve PCB board component soldering efficiency, recommended to use. AIO materials already come with this tool, can be used directly.

### Dynamic BOM Usage

`Step 1`: Open the soldering diagram file marked in 2.2.2

`Step 2`: Mouse click on the left component it will display specific content (same components will also be highlighted)

`Step 3`: If you want to see component first Pin, you can set it in upper right corner settings

### Dynamic BOM Production (This is extended learning, not necessary operation)

Note: AD production dynamic BOM script link: https://github.com/lianlian33/InteractiveHtmlBomForAD

Can't open can download via network disk: https://www.aliyundrive.com/s/f6VVYfwsQ3S

Or in group files "Developer Tools" inside "InteractiveHtmlBomForAD"

## Improved Expansion Board Introduction

`V1.5`

1. Expansion board improved version, added 662k 3.3v 300ma voltage regulator chip (shares screen current, thereby reducing device restart caused by insufficient main board 2992 voltage regulator chip power supply);
2. Expansion board also suitable for MetalV2.0 shell

`V2.0`

1. Expansion board improved version, added MP1471 power management chip (reduces device restart and heating problems caused by insufficient main board LP2992 or ME6211 voltage regulator chip power supply);
2. Expansion board suitable for MetalV2.0 shell, Naïve needs mold modification

## PCB to PCBA Soldering

Note: Reference group file "Main Board Soldering Problem Troubleshooting Methods"

Since the main board component package is 0402, for those without electronics background, no hands-on ability and no soldering experience, it is somewhat difficult. As for the difficulty level, it depends on everyone's "skills".

Generally solder in order from small to large component size. It is recommended to use reflow station or hot air gun, not recommended to use soldering iron alone. For those who have never soldered, or usually don't solder, only done electronics electrical training, it is recommended to buy a heating station. Taobao has Luxianzi reflow station for over 20 yuan (for station usage method please check bilibili yourself). This is completely sufficient (of course rich people can get a hot air gun plus station combination), then add a soldering iron.

All components on the back of the main board (SD card slot and 4 resistors), not soldering will not affect board normal use. It is recommended to solder after screen soldering and testing is complete.

About difficulty in applying solder: For those who don't understand anything, it is recommended to make a stencil on Taobao. For those who haven't done it before, it is recommended to use group files to make stencil. After using stencil to apply solder (medium temperature solder paste is fine, buy a small can of 30 grams can be used for a long time, Pinduoduo 20 yuan), according to group soldering comparison diagram, place components in position, put on station to heat. During solder melting process, component position may shift, adjust position with tweezers. (Note: When soldering esp32, place chip in good position, after solder melts, turn off heating station switch, press chip more with tweezers while cooling)

PS: C7 capacitor optional 1uF~10uF. (Especially those bought from Taobao "Geek***", need attention)

#### Main Board PCB Soldering Start

`① Ensure computer port can recognize [Before powering on, must use multimeter to test whether power and ground are short-circuited]`

`Step 1`: Solder LDO and surrounding resistors and capacitors

Resistors, capacitors, transistors (VT1-2, 8050), voltage regulator chip (LP2992) solder first, antenna (A1) and light (D1) can be soldered last.

`Step 2`: Solder CP2102 and Type C interface

After step one soldering is complete, prepare to solder CP2102 (U1) and Type C interface. If this part soldering has no problems, at this time plug board into computer (before plugging into computer use multimeter buzzer mode to test whether VCC (5V) and GND are short-circuited), computer's device manager can recognize the serial port.

Note: Soldering direction - chip dot to PCB white

`② Common soldering problems in this part`:

`Ⅰ No response after plugging into computer`

High probability is cold solder joint. First use naked eye or magnifying glass to see if there is solder bridge, then with computer or power supply connected, set multimeter to DC voltage mode (remember not to use ohm mode, whoever uses knows) check LP2992 (ME6211) pin voltage, see if there is 5V and 3.3V output, then check CP2102 and Type C, and whether R1 resistor is not soldered well, press with tweezers.

`Note: Data cable should not use charging-only type, must be able to transmit data`

`Ⅱ Computer prompts abnormal current in USB port after power-on`

Board VCC and GND are short-circuited or LDO is broken. (To avoid unexpected losses, it is recommended to measure whether power [5V & 3V3] and ground [GND] are short-circuited before power-on)

`Solution`: Check board, re-solder or replace LDO

`Ⅲ After power-on, computer recognizes CP2102, but with yellow exclamation mark`

`Solution`: Driver not installed, group files have driver, download and install driver.

`Ⅳ Others`

May still be cold solder joint or wrong direction or chip broken. Check 2992 pin voltage, whether there is 5V and 3.3V output, then check CP2102 and Type C.

`Solution`: Test whether it is cold solder joint or Type-C socket problem

`Ⅴ CP2102 driver changed`

`Solution`: [Follow the screenshots showing driver management steps]

`③ Ensure ESP32 can communicate normally with serial port`

`Step 3`: Solder esp32 (U4) chip

Note: ESP32 soldering direction - chip dot to PCB bevel

After serial port is OK, start soldering ESP32. This should be the hardest chip to solder on the board. Sometimes after soldering, ESP32 chip can work normally, can burn program, blink LED can flash normally, but this does not mean your soldering has no problem. There may still be some IO pins short-circuited or cold soldered, causing problems when you connect screen later - screen not lighting or display problems, even MPU6050 cannot connect normally, etc.

Note:

**①** TF card socket on back and four 10K pull-up resistors do not affect burning and use.
**②** When burning firmware please sync with group files latest firmware, try not to use "ancient" firmware
**③** Burning succeeded may not light LED (may be cold solder or light broken), but if firmware burning did not succeed LED definitely will not light.

Your computer is through USB → Type C → CP2102 → ESP32, for burning program. Any communication failure in the middle will cause firmware writing failure.

After soldering is complete, can first use PC software to check whether serial port has serial port information printing, `serial port print baud rate is 115200` (baud rate: 115200 [not 1152000, also not 921600 (use 921600 when downloading, of course 115200 is also OK just slower)]), if soldering has no problem (only means serial port can communicate normally with ESP32, does not mean other IO ports have no problem) there will be serial port information, cold solder will not.

`Under normal soldering conditions, the voltage of the collector of the two 8050s, that is, the topmost Pin pin, is around 3.3V.`

Regarding the above rst:, boot related instructions see Chapter 5, ESP32 Basics.

`④ Common soldering problems in this part`

`Ⅰ Cannot flash firmware by plugging into computer`

PC software stuck at last bit not moving & using VS Code burning prompts connect ESP 32 time out ...---...----...---- This situation is mostly ESP32 cold solder, what connection failure, or flash error, are ESP32 chip cold solder. Re-solder, too much solder (causing pin adhesion) or too little solder (just not soldered on) will cause this problem. Must flexibly use tweezers, flux, solder wick, reflow station.

`Solution`: Add solder for re-soldering, can refer to videos in homepage. (If useful or successful remember to give them one-click triple 😁)

`Ⅱ C7 capacitor is 0.1uF`

Zhihui's original file uses 0.1uf, so using Zhihui's source file for fabrication, C7 capacitor used is basically 0.1uF. C7 soldered with 0.1uF capacitor, then connection to download program fails, but during program download process, after short-connecting ESP32 GPIO0 pin, program can download normally. It is recommended to change C7 capacitor to 1uF~10uF.

`Solution`: Change C7 capacitor to 1uF~10uF.

`Ⅲ Others`

May also be CP2102 chip and R3 resistor not soldered well, or two transistors, or 4 small components beside U2...

`Solution`: Re-component solder and try.

`Ⅳ Keeps restarting after burning`

May be other pins of 32 cold soldered or solder-bridged causing continuous restart. Being able to burn and read serial port only means burning pins are OK, does not mean other pins of 32 are OK

`Solution`: Add solder, use tweezers to move, gently press to squeeze out excess solder inside.

`⑤ Main board front unsoldered parts`

`Step 4`: Solder remaining components on front

If your ESP32 can burn program normally, then you are only 50% away from success.

MPU6050, FPC 8P socket, RGB lights, 2.4G antenna, light sensor (can skip soldering)

Note: MPU 6050 soldering direction - dot to white dot; 2.4G antenna dot to horizontal bar; light sensor AA to white dot.

`⑥ Common problems in this part`:

`Ⅰ APP switches by itself`

(1) Caused by not completing initialization after power-on

`Solution`: Power off, place horizontally and wait for MPU 6050 initialization to complete (lights start changing)

(2) Cold solder

If your MPU6050 is cold soldered, when you burn group test firmware, program will get stuck at MPU6050 initialization, causing you to start doubting life, wondering if your ESP32 chip is broken again.

`Solution`: Re-add solder. (Can refer to Mysterious Treasure Room brother's video)

(3) MPU 6050 bypass capacitor

Some group members have wrong capacitor or cold solder near MPU 6050.

`Solution`: Add solder to MPU 6050 (if adding solder doesn't work can try adding solder to bottom right two Pins of ESP 32) and nearby capacitors (or directly replace and re-solder).

`Ⅱ Bought fake MPU6050 & Broken`

Through serial port information see MPU 6050 keeps reporting ****** 80% possibility is broken or 20% possibility is cold solder

`Solution`: Replace new MPU 6050 or add solder (80% probability chip is broken, 20% probability is cold solder)

`Ⅲ Light sensor soldering problem`

Through serial port information see MPU 6050 reports
[E][esp32-hal-i2c.c:1434]i2cCheckLineState(): Bus Invalid State, TwoWire() Can't init sda=1, scl=0

`Solution`: Confirm whether light sensor is soldered correctly or remove light sensor, re-solder MPU 6050. (PS: Some group members are because light sensor soldering direction is wrong)

Below figure only for reference after soldering complete

#### Expansion Board PCB Soldering Start

Expansion board has no difficulty. According to material list and PCB directly solder screen, FFC and MOS transistor. Note expansion board has two versions, one is original version (not recommended), another is optimized version (recommended to use group owner's latest DC-DC expansion board [full blood version], ME 6211 + with 622K optimized version [half blood version]).

When soldering screen ribbon cable, best not to use reflow station, directly use soldering iron, apply a little solder paste, otherwise easy to burn screen.

MP1471 soldering horizontal line direction downward

Common problems in this part

Screen board only has backlight

Please measure according to group file reference voltage, troubleshoot step by step.

Socket soldering must be careful!!!

</details>

</details>

<details>
<summary>Chapter 3  PC Software Related Issues</summary>

# Chapter 3  PC Software Related Issues

<details>
<summary>PC Software Display Incomplete</summary>

## PC Software Display Incomplete

Problem: Windows 11 or Windows 10 opening PC software may show incomplete display

Solution: In computer resolution interface, adjust scaling ratio. Then reopen PC software. If no change, restart computer and open PC software again.

</details>

<details>
<summary>PC Software Serial Port Information</summary>

## PC Software Serial Port Information

<details>
<summary>MPU 6050 Initialization Failed</summary>

### MPU 6050 Initialization Failed

Problem: MPU 6050 initialization failed or no connection

Solution: MPU 6050 cold solder, add solder location see above main board soldering.

</details>

<details>
<summary>TF Card Cannot Read (TF Card Socket Voltage Diagram)</summary>

### TF Card Cannot Read (TF Card Socket Voltage Diagram)

Problem: TF card cannot read normally or could recognize for a while then cannot recognize.

Solution: First confirm whether it is memory card (TF card, Note: TF card maximum support 32G) problem. If not, then it may be cold solder problem. As shown in figure below, may be resistor or ESP32 corresponding one or more Pin pins cold solder, need to add solder!

</details>

<details>
<summary>Cannot Burn</summary>

### Cannot Burn

Problem: Cannot clear, progress bar stuck at last bit, no serial port information (baud rate: 115200 [not 1152000, also not 921600 (use 921600 when downloading, of course 115200 is also OK just slower)])

Solution: ESP 32 cold solder, need to add solder. (Zhihui's original version please change C7 capacitor to 1-10uF) Please refer to previous main board soldering.

</details>

</details>

</details>

<details>
<summary>Chapter 4  How to Use Multimeter</summary>

# Chapter 4  How to Use Multimeter

Taking Fluke as example, as shown in figure above, multimeter outer ring is generally divided into six parts: AC current mode (A~), DC current mode (A-), AC voltage mode (V~), DC voltage mode (V-), resistance mode (Ω), buzzer mode (🔈 symbol).

<details>
<summary>Measuring Voltage (Using Mini TV Main Board as Example) [Must be DC voltage mode]</summary>

## Measuring Voltage (Using Mini TV Main Board as Example) [Must be DC voltage mode]

① Set multimeter to DC mode (if has gears please select appropriate gear yourself, generally select from large to small)
② One probe of digital multimeter to ground, one to Pin pin or pad to be tested (as shown, one probe on Type-C, one probe on 5V Pin pin of LDO).

Note: Pointer multimeter must pay attention to positive and negative poles, avoid multimeter damage.

</details>

<details>
<summary>Testing Continuity (Using Mini TV Main Board as Example) [Must power off]</summary>

## Testing Continuity (Using Mini TV Main Board as Example) [Must power off]

① Set multimeter to buzzer mode (test short circuit or continuity)
② If mini TV power supply (VCC) and ground (GND) are short-circuited (one probe on GND, one probe on 5V or 3V3), if there is buzzer sound means short circuit (continuity), otherwise no. If checking whether component is broken (such as resistor, capacitor, etc.), place two probes on both ends of component respectively, buzzer sound means broken (except 0Ω type), otherwise no.

</details>

</details>

<details>
<summary>Chapter 5  ESP32 Basics: rst cause and boot mode at Startup</summary>

# Chapter 5  ESP32 Basics: rst cause and boot mode at Startup

At ESP32 startup, ROM CODE reads GPIO state and rst cause state, then determines ESP32 working mode.

Through understanding and mastering rst cause and boot mode, helps locate certain system problems.

For example:
ESP32 startup will have following print:
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

ROM CODE baud rate is 115200

System Reset Introduction and ESP32 Startup rst cause

<details>
<summary>System Reset Introduction</summary>

System Reset Introduction

System provides three levels of reset methods: CPU reset, core reset, system reset.

All resets do not affect data in MEM. The figure shows entire subsystem structure and each reset method:

CPU reset: Only resets all registers of CPU.

Core reset: Except RTC, will reset all digital registers including CPU, all peripherals and digital GPIO.

System reset: Will reset all chip registers including RTC.

In most cases, APP_CPU and PRO_CPU will be immediately reset, some reset sources can only reset one of them.

APP_CPU and PRO_CPU reset reasons are also different respectively:

After system reset starts,

PRO_CPU can read register RTC_CNTL_RESET_CAUSE_PROCPU to get reset source;

APP_CPU can read register RTC_CNTL_RESET_CAUSE_APPCPU to get reset source.

</details>

<details>
<summary>ESP32 Startup rst cause</summary>

ESP32 Startup rst cause

For example ESP32 startup will have following print:
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

[Reference table showing reset causes]

</details>

<details>
<summary>ESP32 Power-on boot mode</summary>

ESP32 Power-on boot mode

ESP32 judges strapping pin state at power-on, and determines boot mode.

For example two common power-on prints:

Firmware download mode:
rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))

Chip running mode:
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

Taking ESP32-WROOM-32 as example.

Boot value determined by 6-bit value of strapping pins [MTDI, GPIO0, GPIO2, GPIO4, MTDO, GPIO5] together.

Article link: https://blog.csdn.net/espressif/article/details/107977962

</details>

Good luck everyone!

</details>

<details>
<summary>Chapter 6  Appendix (PCB Wiring Diagram)</summary>

# Chapter 6  Appendix (PCB Wiring Diagram)

<details>
<summary>Main Board</summary>

## Main Board

[Multiple PCB wiring diagrams and schematics would be shown here in the original]

</details>

<details>
<summary>Expansion Board</summary>

## Expansion Board

`① Version 2.0`

[PCB diagrams]

`② Version 1.5`

[PCB diagrams]

`③ Version 1.2`

[PCB diagrams]

</details>

</details>

<details>
<summary>Chapter 7  Q&A</summary>

# Chapter 7  Q&A

## Hardware Related Q&A Summary
__This file is from `HoloCubic AIO Multi-function Firmware` Group 755143193, compiled by ClimbSnail (Bilibili: Liuma Xiaoge).__

Transparent Mini TV Introduction: https://www.bilibili.com/video/BV1jh411a7pV?p=6

<details>
<summary>1. Hardware Versions</summary>

### 1. Hardware Versions
##### Overview
Zhihui has four versions: transparent base `Naive`, `metal`, Iron Man `Ironman` and `BiliBili angel base`. Most group members use transparent base `Naive` version.

Many experts have written `Holocubic firmware`. Firmware versions are basically compatible with these two hardware versions (at least AIO firmware is fully compatible). Choose which version to make yourself. Original author `Zhihui`'s part of circuit has problems, group has improved versions.

Important! Hardware only supports `2.4G` wifi. `5G` and `dual-band combined` are not supported. No firmware can break through hardware limitations.

Note: For those without electronics background who want to play, can ask group members, some have finished products for transfer or sale.

</details>

<details>
<summary>2. Hardware Related</summary>

### 2. Hardware Related
Group's improved various version PCBs and bases are classified and packaged in `Hardware Shell Related` folder, can download by yourself. Various hardware version PCBs and various shells may have incompatibility issues (may not fit), please try to use files within same compressed package for production and carefully read version instructions inside.

##### Component Purchasing
1. Most components can be purchased from Taobao `Youxin Electronics`.
2. `AN5120` antenna on main board is hard to search, recommend directly buying `Youxin Electronics` `AN2051` 2.4G antenna.
3. Screen and main board connection uses FPC socket, purchase FPC socket specification `pitch 0.5 8P flip-down` and FPC ribbon cable specification `pitch 0.5 8P same direction 6cm`.
4. Prism and screen, screen expansion board and base bonding, all recommend using `B7000 glue` or `UV glue`. Note: `UV glue` requires additional purchase of curing lamp. Prism attachment video tutorial: https://www.bilibili.com/video/BV1jh411a7pV?p=5
5. Zhihui's original `naive` and `Iron Man Ironman` memory card slot models are both `DM3D-SF` (few on Taobao, relatively expensive). Group hardware is improved memory card slot version `naive` and `metal` universal main board, slot is flip-type, link in group shared documents.

##### Naive Transparent Base Version Hardware
1. Main board (same as metal main board) if making please use group's improved circuit files. (Note: Original version used slot is hard to buy and designed C7 capacitor as `0.1uf` is design defect, schematic prompt "first short connection" conclusion is wrong, cannot fundamentally solve automatic download. Need C7 changed to `1uf~10uf` can solve problem, no need for short connection operation at any time.)
2. As shown below, original expansion board GND uses copper pour connection, and middle two coppers only connected at arrow pointing position, when processing PCB easily leads to not connecting, thus GND open circuit, phenomenon is screen backlight not lighting. Here recommend using group file modified hardware PCB file for fabrication.
![holocubic_extern_err](./Image/holocubic_extern_err.png)
3. `Main board` and `expansion board` thickness related to shell. Specifically see each version shell recommended dimensions.

##### Metal Transparent Base Version Hardware
1. Main board (same as naive main board) if making please use group's improved circuit files. (Note: Original version used slot is hard to buy and designed C7 capacitor as `0.1uf` is design defect, schematic prompt "first short connection" conclusion is wrong, cannot fundamentally solve automatic download. Need C7 changed to `1uf~10uf` can solve problem, no need for short connection operation at any time.)
2. As shown below, original expansion board GND uses copper pour connection, and middle two coppers only connected at arrow pointing position, when processing PCB easily leads to not connecting, thus GND open circuit, phenomenon is screen backlight not lighting. Here recommend using group file modified hardware PCB file for fabrication.
![holocubic_extern_err](./Image/holocubic_extern_err.png)
3. `Main board` and `expansion board` thickness related to shell. Specifically see each version shell recommended dimensions.

##### Ironman Iron Man Version Hardware
1. Screen and main board uses `gopin spring pogo pin` connection, specification: `8Pin double row`, pitch `2.54`, height `7mm`.
2. Screen board pogo pin hole has problem of being too small, need to expand by yourself.
3. `Main board` and `expansion board` thickness related to shell. Specifically see each version shell recommended dimensions.

##### BiliBili Angel Base Version Hardware
Only a few group members in group have made, if interested can ask in group.

</details>

<details>
<summary>3. Shell 3D Printing</summary>

### 3. Shell 3D Printing
##### Naive Transparent Base (Improved Version)
1. Suitable for `Naive` version hardware.
2. Original design uses screws to connect upper and lower shell, but group has expert magnetic improved version (magnets are 3*3mm round magnets) recommend using improved version.
3. Base uses 3D printer production, recommended to use semi-transparent printing effect.
4. If printed surface wants frosted effect, recommend first using 400 grit then with 800 grit sandpaper polishing under running water.
5. If finding online printing service, pay attention to tolerances, shell too small main board cannot fit.
6. Main board thickness `1.2mm` (using improved shell). Expansion board thickness `1.2mm`.

##### Metal Base (Improved Version)
1. Suitable for `Metal` version hardware.
2. Because prism bonds glass screen, shaking may damage, so group members shared reinforced base (recommended). Recommended main board thickness `1.2mm`. Expansion board thickness `1.2mm`.

##### Ironman Iron Man Base
1. Suitable for `Ironman` version hardware.
2. Zhihui's original base recommended: main board thickness `1.0mm`. Expansion board thickness `1.0mm`.

##### BiliBili Base
Temporarily unavailable

</details>

<details>
<summary>4. Memory Card Selection</summary>

### 4. Memory Card Selection
Firmware has certain compatibility issues with memory cards, not all are compatible. Recommended verified memory cards below:
1. Aigo 32G regular card. Taobao about 20 yuan. (Cost-effective, recommended)
2. SanDisk 32G regular card. Taobao about 30.

</details>

<details>
<summary>5. Screen Issues</summary>

### 5. Screen Issues
Screen specifications: 1.3 inch, driver ST7789, resolution 240*240, soldering 12Pin.

There are many such screens online, but for making holocubic need to choose carefully, screen will affect overall display effect. Currently tested many screen manufacturers, best effect is Zhongjingyuan. Not recommended to use other manufacturers' screens for making Holocubic.

###### Actual comparison below (please ignore background differences):
Left: Zhongjingyuan (Hancai) Right: Youzhijing
![holocubic_scr_compare](./Image/holocubic_scr_compare.jpg)

Difference between two screens after attaching prism is mainly `Youzhijing` display's surrounding blank area is seriously blue, greatly affects final effect. `Zhongjingyuan`'s blank area display is very pure. Note: Actually Zhongjingyuan bottom color also blue, but very slight.

About brightness issue (not related to screen):
Can also see from above picture, left is obviously brighter. This is because left did not tear off factory polarizer protective film (can increase brightness), while left color becomes extremely inaccurate due to protective film refraction. Students who did experiments will also find, after tearing off protective film, prism `X-axis` placement and `Y-axis` placement brightness is different. Human eyes more sensitive to color compared to brightness. Personally recommend tearing off protective film. Of course, if care more about brightness can also not tear off protective film. When buying screen can ask seller to ship with protective film and not put that green label on protective film.

</details>

<details>
<summary>6. About Soldering</summary>

### 6. About Soldering
1. Due to main board package and compact layout, soldering process easily causes some pins not soldered or cold solder. Please be careful.
2. Iron Man version hardware, most screen boards are metal shell, pay attention to short circuit problems.
3. When testing main board, recommend using `AIO firmware` full set of tools for testing. Before flashing install CP2102 driver. If using `AIO PC software` flashing stuck not moving, please check main board (don't doubt tools or firmware).
4. Flashing success also does not mean hardware completely no problem. If iic circuit soldering has problem, will cause gyroscope cannot use cannot switch pages. If memory card incompatible will cause cannot read memory card or `holocubic` restart. For specific problem location, please directly check `AIO PC software` print information to judge which part has problem, or screenshot print information ask group members.

</details>

<details>
<summary>7. Epilogue</summary>

### 7. Epilogue
If have problems check documents more. If documents don't mention then ask group members. Finally, wish everyone can successfully use `Holocubic`.

</details>

</details>

<details>
<summary>Chapter 8  Hardware Version Instructions</summary>

# Chapter 8  Hardware Version Instructions

<details>
<summary>Metal Version</summary>

## Metal Version

## This is Metal version hardware shell materials in AIO firmware group
To newcomers: Making Holocubic always use latest version shell and PCB, latest versions definitely compatible with each other.

<details>
<summary>Shell Files</summary>

#### Shell Files
`v1.0` and `v2.0` versions are both modified based on Zhihui's original version, bottom opened memory card slot. `v1.0` and `v2.0` shells compatible with all version main boards and expansion boards in this package. Recommended compatible PCB board fabrication 1.2mm thickness (main board and screen version)

v1.0 left and right reinforcement seats too wide, v2.0 optimizes this defect.

</details>

<details>
<summary>Screen Board</summary>

#### Screen Board
Compatible with all main boards. Version instructions below. Recommended fabrication 1.2mm thickness. _Note: Folder contains troubleshooting voltage diagram "Metal (DCDC) Screen Board Reference Voltage"_.

##### v1.2
Based on Zhihui's original version added LDO 662K to share main board LDO current pressure, greatly reduces heating and restart problems. Can replace Zhihui's original version without any changes, only suitable for Metal version shell (including original Metal shell).

##### v1.5
Modified PCB layout based on `v1.2`, making layout close to Naive version, convenient to check common problems. _Note: Folder has Zhihui's original screen board voltage diagram "Naive Original Screen Board Reference Voltage (Ver4.1).png", because circuit close to modified version, can have certain reference value_

##### v2.0
Screen board added DC-DC solution on original LDO solution (two solutions coexist, need to choose one for soldering).
* If solder ME6211 almost identical to v1.5 version screen board (note v1.5 version uses LDO is 662K).
* If solder DC-DC circuit, please remove main board LDO (screen board will automatically power main board), completely solves heating problem (can be used to run full blood state AIO firmware, best experience).

##### v2.1 (Metal and Naive share this version)
Screen board added DC-DC solution on original LDO solution (two solutions coexist, need to choose one for soldering).
* If solder ME6211 almost identical to v1.5 version screen board (note v1.5 version uses LDO is 662K).
* If solder DC-DC circuit, please remove main board LDO (screen board will automatically power main board), completely solves heating problem (can be used to run full blood state AIO firmware, best experience).

Note: Completely identical in function to `Metal v2.0` version screen board, but optimized PCB routing, power ripple improved from v2.0's `22mv` to `18mv`. Reduced top and bottom layer copper pour area, reduced signal shielding.

</details>

<details>
<summary>Main Board</summary>

#### Main Board
All version main boards are modified based on Zhihui's original naive main board. Note: All Metal main boards identical to Naive main board. Recommended fabrication 1.2mm thickness. Main boards in files suitable for all screen boards and shells in this folder.

##### v1.3
`pin2pin` replaced LP2992 with ME6211. WS2818 5050 replaced with side light WS2812 4020 version. (Note: This version not recommended for making, please prioritize V2.0 version main board)

##### v2.0
pin2pin replaced LP2992 with ME6211. Replaced TF card slot (cheap and easy to buy). But to ensure as consistent as possible with original version, RGB lights still use original WS2812 5050

</details>

</details>

<details>
<summary>Naive Version</summary>

## Naive Version

## This is Metal version hardware shell materials in AIO firmware group
To newcomers: Making Holocubic always use latest version shell and PCB, latest versions definitely compatible with each other.

<details>
<summary>Shell Files</summary>

#### Shell Files
##### Naive shell divided into upper and lower two parts, choose upper and lower shell combination yourself.
`Naive magnetic base (lower hollowed out)` added TF card slot opening window, convenient to take card. Other versions please see files yourself. Recommended compatible PCB board fabrication 1.2mm thickness (main board and screen version)
`Naive magnetic base (upper)` only supports `v1.5` version screen board in this package.
`Naive magnetic base (upper) v2.0` compatible with all (including Metal) DCDC version screen boards, and `v1.5` version screen board in this package.
`Naive magnetic base (lower hollowed out)`, `Naive magnetic base (lower fully enclosed)`, `high leg bottom (lower)` all support all version main boards.

</details>

<details>
<summary>Screen Board</summary>

#### Screen Board
Compatible with all main boards. Version instructions below. Recommended fabrication 1.2mm thickness.

##### v1.5
Based on Zhihui's original version added LDO 662K to share main board LDO current pressure, greatly reduces heating and restart problems. Can replace Zhihui's original version without any changes, supports all Naive version shells also supports original Metal shell.

##### v2.1 (Metal and Naive share this version)
Screen board added DC-DC solution on original LDO solution (two solutions coexist, need to choose one for soldering).
* If solder ME6211 almost identical to v1.5 version screen board (note v1.5 version uses LDO is 662K).
* If solder DC-DC circuit, please remove main board LDO (screen board will automatically power main board), completely solves heating problem (can be used to run full blood state AIO firmware, best experience).

Note: Completely identical in function to `Metal v2.0` version screen board, but optimized PCB routing, power ripple improved from v2.0's `22mv` to `18mv`. Reduced top and bottom layer copper pour area, reduced signal shielding.

</details>

<details>
<summary>Main Board</summary>

#### Main Board
All version main boards are modified based on Zhihui's original naive main board. Note: All Metal main boards identical to Naive main board. Recommended fabrication 1.2mm thickness. Main boards in files suitable for all screen boards and shells in this folder.

##### v1.3
pin2pin replaced LP2992 with ME6211. WS2818 5050 replaced with side light WS2812 4020 version. (Note: This version not recommended for making, please prioritize V2.0 version main board)

##### v2.0
pin2pin replaced LP2992 with ME6211. Replaced TF card slot (cheap and easy to buy). But to ensure as consistent as possible with original version, RGB lights still use original WS2812 5050

</details>

</details>

</details>
</details>

</details>
