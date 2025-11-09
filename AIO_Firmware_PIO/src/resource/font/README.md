# Font Directory - HoloCubic AIO

## Current Configuration

**Active Font:** `ch_font20.c` (Simplified Chinese)  
**Status:** ✅ In use by weather_gui.c  
**Last Updated:** 2025-11-09

---

## 📁 Font Files

### ch_font20.c - ⭐ ACTIVE (Simplified Chinese)
- **Size:** 1,528 KB
- **Characters:** 1,442 (88 ASCII + 585 Simplified Chinese + others)
- **Font:** Microsoft YaHei Bold (微软雅黑粗体)
- **Height:** 20px
- **Purpose:** Mainland China weather display and general Simplified Chinese UI
- **Status:** ✅ Currently active in production

**Character Set:**
```
! "#$%&'()*+,-./0123456789:;<=>?@
ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~°
一七万三上丘东严个中丰临丹主丽义乌乐九乡二云五井亚交京亳亿什仁今介仓仙代令仪们价任伊休优伦低余佛作佳依侯保信值偃儋元充光克兖公六兰共关兴兵冀内冈冶冷凉凌凤凭凯则利别力勒匀包化北区十华南博卫原厦县双口古句台叶合吉同名吕启吴吾周呼和咸哈唐商喀嘉嘴四回固国图地圳坊坛城埠堰塔壁壮夏多大天太头夷奉奎如姚姜威娄子孝孟宁安定宜宝宣宫家容宾宿密富察封尔尚尾屯山岑岗岛岩岭岳峡峨峪峰崃崇嵊川州左巩差巴市布师常平年广庄庆库应底店度康廊延建开张弱强当彦彭征徐德徽志忠忻怀总恩惠感慈成房手扎扬微承抚拉指掖揭攀收政敦文斯新方施族无日旧昆昌明春昨昭晋普景暨曲更最月有朔朝木本来杭松林枝枣染查柳树株根格桂桃桐桥桦梁梅梧棱楚榆樟武毕民气水永汉汕汝江池污汨汾沁沂沅沈沙没沧河油治泉泊波泰泸泽洛津洪洮洱洲流济浏浙浩浮海涟涿淄淖淮深清温渭港湖湘湛湾源溧溪滁滋滕满滦滨漯漳潍潜潞潭潮澳濮灌灯灵烟焦煌照熟牙牡特狮玉玛珠珲理琼瑞瓦瓯甘田甸界疆登白百皇皋益盐盖盘省眉看石码碑磐祥票福禹秦穆穴竹简米级纳绍绥维绵编罗老耒聊肃肇股肥胶自舒舞舟良色节芜芝芦芬花苏茂荆荥莆莞莱菏萍营萨葛葫蒙蓥藏虎虞蚌蛟行衡衢襄西讷许语诸调贝贡贵贺资赣赤轻辉辑辛辽达迁运远连通遂遵邓邛邡邢那邮邯邳邵邹郏郑郭郴郸都鄂酒醴里重量金钟钢钦铁铜银锡锦镇长门间阆阜防阳阴阿陆陇陕陵随雄雅集霍霸青靖鞍韩音韶顶项顺额风饶首香马驻骅高鲁鸡鸭鹤鹰鹿麻黄黑鼎齐龙。，
```

Plus extended characters for all major Chinese cities and weather terms.

---

### ch_font20_tc.c - Traditional Chinese (Backup)
- **Size:** 972 KB
- **Characters:** 994 (88 ASCII + 906 Traditional Chinese)
- **Font:** Noto Sans TC Regular
- **Height:** 20px
- **Purpose:** Taiwan weather display (optional, not currently in use)
- **Status:** ⚠️ Available as backup/optional

---

## 🎯 Usage in Code

### Current Implementation (Simplified Chinese)
```c
LV_FONT_DECLARE(ch_font20);
lv_style_set_text_font(&style, &ch_font20);
```

### To Switch to Traditional Chinese (Optional)
```c
LV_FONT_DECLARE(ch_font20_tc);
lv_style_set_text_font(&style, &ch_font20_tc);
```

And in `weather.cpp`, change:
```cpp
cfg->language = 0;  // 0 = Simplified, 1 = Traditional
```

---

## 📝 Language Configuration

The weather app supports dual-language display:

**Simplified Chinese (简体中文)** - Currently Active
- Config value: `0`
- Font: `ch_font20`
- Example: 优良、气温、风力

**Traditional Chinese (繁體中文)** - Optional
- Config value: `1`
- Font: `ch_font20_tc`
- Example: 優良、氣溫、風力

Change language in:
- `weather.cpp` line 84: Default config `cfg->language = 0;`
- `weather_gui.c` line 40: Default UI `current_language = LANG_SIMPLIFIED_CHINESE;`

---

## 📊 Directory Summary

**Total Files:** 3  
**Total Size:** ~2.5 MB  
**Fonts Available:** 2 (Simplified + Traditional)  
**Currently Active:** Simplified Chinese (ch_font20.c)  

---

## 🔧 Font Extraction Tool

To extract characters from font files, use the project's script:

```bash
python Script/get_font.py path/to/font.c
```

---

## 📖 Character Set Details

### Optimized For:
- ✅ China mainland weather API (Gaode/AMap)
- ✅ All major Chinese cities and provinces
- ✅ Complete weather terminology
- ✅ Date and time display
- ✅ High-frequency Chinese characters
- ✅ ASCII punctuation and numbers

### Coverage:
- All provincial capitals
- Major prefecture-level cities
- Weather conditions (sunny, cloudy, rain, snow, etc.)
- Wind directions and levels
- Temperature and humidity terms
- Date/time expressions (年月日时分秒周一二三...)
- Air quality levels (优良轻度中度重度严重)

---

**Last Updated:** 2025-11-09  
**Active Configuration:** Simplified Chinese (简体中文)  
**Maintained By:** HoloCubic AIO Project
