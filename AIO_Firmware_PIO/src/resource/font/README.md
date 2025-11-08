## ch_font_20.c中的字体
字体是`微软雅黑粗体`，字形高度为`20`

字库如下：
! "#$%&'()*+,-./0123456789:;<=>?@
ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~°
一七万三上丘东严个中丰临丹主丽义乌乐九乡二云五井亚交京亳亿什仁今介仓仙代令仪们价任伊休优伦低余佛作佳依侯保信值偃儋元充光克兖公六兰共关兴兵冀内冈冶冷凉凌凤凭凯则利别力勒匀包化北区十华南博卫原厦县双口古句台叶合吉同名吕启吴吾周呼和咸哈唐商喀嘉嘴四回固国图地圳坊坛城埠堰塔壁壮夏多大天太头夷奉奎如姚姜威娄子孝孟宁安定宜宝宣宫家容宾宿密富察封尔尚尾屯山岑岗岛岩岭岳峡峨峪峰崃崇嵊川州左巩差巴市布师常平年广庄庆库应底店度康廊延建开张弱强当彦彭征徐德徽志忠忻怀总恩惠感慈成房手扎扬微承抚拉指掖揭攀收政敦文斯新方施族无日旧昆昌明春昨昭晋普景暨曲更最月有朔朝木本来杭松林枝枣染查柳树株根格桂桃桐桥桦梁梅梧棱楚榆樟武毕民气水永汉汕汝江池污汨汾沁沂沅沈沙没沧河油治泉泊波泰泸泽洛津洪洮洱洲流济浏浙浩浮海涟涿淄淖淮深清温渭港湖湘湛湾源溧溪滁滋滕满滦滨漯漳潍潜潞潭潮澳濮灌灯灵烟焦煌照熟牙牡特狮玉玛珠珲理琼瑞瓦瓯甘田甸界疆登白百皇皋益盐盖盘省眉看石码碑磐祥票福禹秦穆穴竹简米级纳绍绥维绵编罗老耒聊肃肇股肥胶自舒舞舟良色节芜芝芦芬花苏茂荆荥莆莞莱菏萍营萨葛葫蒙蓥藏虎虞蚌蛟行衡衢襄西讷许语诸调贝贡贵贺资赣赤轻辉辑辛辽达迁运远连通遂遵邓邛邡邢那邮邯邳邵邹郏郑郭郴郸都鄂酒醴里重量金钟钢钦铁铜银锡锦镇长门间阆阜防阳阴阿陆陇陕陵随雄雅集霍霸青靖鞍韩音韶顶项顺额风饶首香马驻骅高鲁鸡鸭鹤鹰鹿麻黄黑鼎齐龙。，

### 字库提取
可以使用工程下的`Script/get_font.py`脚本提取。`python get_font.py 字模.c文件的路径`



### by：神秘藏宝室   添加，为了适配高德API内的城市添加字库，修改后的字体如下：
字体是`微软雅黑粗体`，字形高度为`20`
≤! "#$%&'()*+,-./0123456789:;<=>?@
ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~°  
一七万三上丘东严个中丰临丹主丽义乌乐九乡二云五井亚交京亳亿什仁今介仓仙代令仪们价任伊休优伦低余佛作佳依侯保信值偃儋元充光克兖公六兰共关兴兵冀内冈冶冷凉凌凤凭凯则利别力勒匀包化北区十华南博卫原厦县双口古句台叶合吉同名吕启吴吾周呼和咸哈唐商喀嘉嘴四回固国图地圳坊坛城埠堰塔壁壮夏多大天太头夷奉奎如姚姜威娄子孝孟宁安定宜宝宣宫家容宾宿密富察封尔尚尾屯山岑岗岛岩岭岳峡峨峪峰崃崇嵊川州左巩差巴市布师常平年广庄庆库应底店度康廊延建开张弱强当彦彭征徐德徽志忠忻怀总恩惠感慈成房手扎扬微承抚拉指掖揭攀收政敦文斯新方施族无日旧昆昌明春昨昭晋普景暨曲更最月有朔朝木本来杭松林枝枣染查柳树株根格桂桃桐桥桦梁梅梧棱楚榆樟武毕民气水永汉汕汝江池污汨汾沁沂沅沈沙没沧河油治泉泊波泰泸泽洛津洪洮洱洲流济浏浙浩浮海涟涿淄淖淮深清温渭港湖湘湛湾源溧溪滁滋滕满滦滨漯漳潍潜潞潭潮澳濮灌灯灵烟焦煌照熟牙牡特狮玉玛珠珲理琼瑞瓦瓯甘田甸界疆登白百皇皋益盐盖盘省眉看石码碑磐祥票福禹秦穆穴竹简米级纳绍绥维绵编罗老耒聊肃肇股肥胶自舒舞舟良色节芜芝芦芬花苏茂荆荥莆莞莱菏萍营萨葛葫蒙蓥藏虎虞蚌蛟行衡衢襄西讷许语诸调贝贡贵贺资赣赤轻辉辑辛辽达迁运远连通遂遵邓邛邡邢那邮邯邳邵邹郏郑郭郴郸都鄂酒醴里重量金钟钢钦铁铜银锡锦镇长门间阆阜防阳阴阿陆陇陕陵随雄雅集霍霸青靖鞍韩音韶顶项顺额风饶首香马驻骅高鲁鸡鸭鹤鹰鹿麻黄黑鼎齐龙。，人淀沟柔谷红辰坻静蓟陉矿裕藁栾正寿邑赞极氏赵路润曹妃亭戴黎卢丛复涉磁邱馆陶魏柏隆尧巨宗竞秀莲苑涞望易蠡野下园全礼沽蔚宽围场皮献村次厂故小迎杏尖草坪烦荣浑郊盂党留垣壶右社权昔祁遥猗闻喜稷绛芮府繁峙神寨岢岚偏沃翼洞隰蒲离楼赛罕土默旗托仑拐联勃科腾翁牛喇敖后奈曼胜准前审赉诺莫斡陈磴卓王盟突嘎尼仆寺镶蓝善姑于法旅立千岫桓振站鲅鱼圈边细彰圣宏伟弓洼道绿农船梨宇鲜乾扶汪外锋昂基碾拜冠恒滴向工萝贤友谊让胡杜伯美翠好荫汤旺箐岔进茄爱逊孙嫩漠加奇浦汇陀虹杨闵玄邺鼓栖霞雨淳贾沛睢相盱眙响射邗徒豫沭泗拱墅萧钱塘庐曙鄞象苍浔越柯婺游岱椒居环缙畲瑶蜀巢镜鸠弋沚为会庵谢八潘涂含烈濉官枞观歙黟琅琊谯颍埇砀璧涡至郎泾绩旌闽思翔厢涵荔屿尤将鲤芗霄诏汀蕉屏柘谱滩栗濂柴桑修渝分章犹寻干袁载铅横鄱历槐崂李即墨薛峄儿垦罘牟蓬招寒朐汶乳莒郯费茌莘沾棣单郓鄄管街符杞尉考瀍涧嵩殷滑淇浚牧获解放陟范鄢郾召渑宛卧淅浉始潢息驿蔡舆确泌岸硚陂塞茅箭郧伍点军猇秭归樊掇刀洋悟梦监团英浠蕲曾苗架芙蓉心麓荷淞渌攸茶炎晖雁蒸步君澧植赫禾零牌溆晃侗芷星凰丈埔番禺从增浈斗濠澄禅坎坡廉雷电端要紫榕郁邕鸣融叠彩各恭圩藤覃业果仫佬毛等棠涯崖迈涪渡坝碚綦足黔潼垫巫柱酉羊郫堂沿叙蔺梓羌剑阁犍研夹沐彝部珙筠邻渠经棉壤若孜孚炉稻得拖觉冕烽播真仡务湄习织雍碧阡印晴贞谟册亨秉穗瓮独呈禄劝麒麟傣冲巧蒗祜佤澜朗耿谋弥砚畴版勐腊漾濞巍颇芒盈怒傈僳迪堆卡迦结仲聂类丁脱隅乃囊措错浪比申索班戈札噶革改勤灞未央阎鄠耀岐旬功彬起勉略脂堡柞麦积祝崆峒瓜岷宕两撒迭碌湟互助循晏刚久杂称谦茫峻直辖磨坂碱吐鄯坤垒精楞轮犁且末焉耆硕车提恰疏附莎伽策敏蕴可仔埗荃葵模凼填旋转不期冬初少劲疾暴狂爆飓热带霾阵并伴冰雹降雪冻尘卷雾浓知惊蛰种暑秋处露霜闰廿【】鼠兔蛇猴狗猪甲乙丙戊己庚壬癸丑寅卯巳午戌亥旦宵劳动秘室


以下符号因为 其他字体经常缺字符，使用微软雅黑内没有
用的微软雅黑  20号  0x2264

---

## ch_font20_tc.c (Traditional Chinese Font) 繁體中文字型 ⭐ ACTIVE

**Current Font:** `GenJyuuGothic-Normal.ttf` (源柔ゴシック)  
**Font Height:** `20px`  
**BPP:** `4` (16 gray levels)  
**File Size:** 1,094 KB  
**Character Count:** **994 characters** (88 ASCII + 905 Traditional Chinese + 1 other)  
**Status:** ✅ **Active in weather_gui.c - Production ready!**

### Character Set (字庫)
This comprehensive font includes:
- ✅ Complete ASCII set (safe for command line - no special chars like `<>|&^%`)
- ✅ **All Taiwan cities, counties, townships, and districts** (完整台灣縣市鄉鎮地名)
- ✅ **Complete weather terminology** (完整天氣術語)
- ✅ **Date and time expressions** (日期時間)
- ✅ **High-frequency Traditional Chinese characters** (常用繁體中文字)
- ✅ **Common verbs, adjectives, and nouns** (常用動詞、形容詞、名詞)

**Optimized for:**
- Taiwan weather display applications
- General Traditional Chinese UI text
- Date/time display
- Location names (Taiwan-specific)

**Generated with:** `gen_final.js` (Node.js script bypassing shell encoding issues)

---

### ✅ **RECOMMENDED: Generate with Node.js Script** (推薦方法)

For generating fonts with 1000+ characters, use the provided Node.js script which bypasses shell encoding issues:

```bash
cd AIO_Firmware_PIO/src/resource/font
node gen_final.js
```

This script:
- Reads characters from `tc_safe_1000.txt` (994 characters, CMD-safe)
- Uses `execSync` to call `lv_font_conv` directly
- Handles UTF-8 encoding correctly
- Generates `ch_font20_tc.c` (~1.09 MB, 994 characters)

**Prerequisites:**
- Node.js and npm installed
- `lv_font_conv` available via npx (installed automatically)

**Character set customization:**
```bash
# Optional: Customize character set
python select_important_1000.py  # Select important characters
python generate_safe_1000.py     # Make CMD-safe (removes <>|&^%)
```

---

### Key Points (重點提示)

✅ **Font Format Support:**
- ✅ TTF (TrueType Font) - **Recommended** (GenJyuuGothic-Normal.ttf included)
- ✅ WOFF (Web Open Font Format)
- ❌ TTC (TrueType Collection) - Not supported by lv_font_conv

✅ **Generation Method:**
- **Recommended:** Use `gen_final.js` Node.js script (handles encoding correctly)
- Generates 994 characters in ~30-60 seconds
- No command-line length or encoding issues

✅ **Character Set:**
- **Current:** 994 characters (optimized for Taiwan)
- **Customizable:** Edit `select_important_1000.py` to add/remove characters
- **Complete reference:** 1465 characters available in `tc_chars.txt`

### Usage in Code (程式碼使用方法)

1. **Declare the font:**
```c
LV_FONT_DECLARE(ch_font20_tc);
```

2. **Use in style:**
```c
lv_style_t tc_font_style;
lv_style_init(&tc_font_style);
lv_style_set_text_font(&tc_font_style, &ch_font20_tc);
lv_obj_add_style(label, &tc_font_style, LV_STATE_DEFAULT);
```

### Notes (注意事項)

- ✅ Font is already integrated into `src/app/weather/weather_gui.c`
- ✅ `GenJyuuGothic-Normal.ttf` supports Traditional Chinese, Simplified Chinese, Japanese, and Korean
- The generated font file size: ~20-150 KB depending on character count
- Ensure sufficient flash memory space before adding large character sets
- Can coexist with Simplified Chinese font (ch_font20.c)
- Perfect for Taiwan weather apps and Traditional Chinese content

### Troubleshooting (故障排除)

**Issue:** Characters display as boxes/missing  
**Solution:** Regenerate font with missing characters added to `tc_safe_1000.txt`

**Issue:** Need more characters  
**Solution:** Edit `select_important_1000.py`, add characters, then run all 3 scripts

**Issue:** `npx` or Node.js not found  
**Solution:** Install Node.js from https://nodejs.org/

---

## Files in this Directory (目錄檔案)

### Font Files (字型檔案)
- `ch_font20.c` - Simplified Chinese font (簡體中文, 1,528 KB)
- `ch_font20_tc.c` - **Traditional Chinese font (繁體中文, 1,094 KB)** ⭐ **ACTIVE**

### Source & Tools (來源與工具)
- `GenJyuuGothic-Normal.ttf` - Source font file (源字型檔, 10 MB)
- `gen_final.js` - **Main generation script** ⭐
- `select_important_1000.py` - Character selection script
- `generate_safe_1000.py` - CMD-safe character filter

### Character Sets (字符集)
- `tc_safe_1000.txt` - **994 characters for generation** ⭐
- `tc_chars.txt` - Full 1465 character reference

### Documentation (文件)
- `README.md` - This file ⭐
- `FILES_EXPLANATION.md` - Detailed file descriptions

---

**Last Updated:** 2025-11-08  
**Font Generated With:** GenJyuuGothic-Normal.ttf  
**Generator:** lv_font_conv (via gen_final.js)  
**Current Font:** ch_font20_tc.c (994 characters, 1,094 KB)  
**Status:** ✅ Active in weather_gui.c - Production ready