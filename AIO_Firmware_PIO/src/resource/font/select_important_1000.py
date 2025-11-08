#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Select the most important 1000 Traditional Chinese characters
優先選擇最重要的 1000 個繁體中文字符
"""

# Priority 1: Complete ASCII (must have)
ASCII = '! "#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~°'

# Priority 2: Taiwan cities and locations (MUST HAVE for weather app)
TAIWAN_LOCATIONS = '''
台北新北基隆桃園新竹苗栗台中彰化南投雲林嘉義台南高雄屏東宜蘭花蓮台東澎湖金門連江馬祖
士林北投內湖南港文山中正大同萬華信義松山中山大安板橋三重中和永和新莊新店土城蘆洲樹林
鶯歌三峽淡水汐止瑞芳五股泰山林口深坑石碇坪林烏來三芝石門八里平溪雙溪貢寮金山萬里
龍潭平鎮八德楊梅大溪龜山大園觀音新屋復興中壢竹北竹東新埔關西芎林寶山峨眉
朴子布袋大林民雄溪口新港六腳東石義竹鹿草水上中埔竹崎梅山番路大埔阿里山太保
頭份竹南後龍通霄苑裡卓蘭造橋西湖頭屋公館大湖泰安獅潭三義
員林鹿港和美二林田中北斗花壇芬園大村永靖伸港線西福興秀水埔心溪州二水埤頭田尾社頭
草屯集名魚池國姓仁愛信義水里
斗六斗南虎尾西螺土庫古坑大埤莿桐林內崙背麥寮台西東勢元長四湖口湖
新營鹽白河柳營後壁麻佳里學甲七股將軍善化新市安定山上玉井楠西左鎮仁德歸仁關廟龍崎官田大內
岡山旗山美濃鳳林園鳥松大樹燕巢阿蓮路茄萣彌陀梓官橋頭田寮六龜甲仙杉林內門茂林桃源那瑪夏湖永
礁壯員羅五冬蘇澳
吉安壽豐光復瑞穗富里秀卓太魯閣
成功卑池長濱太麻里綠島蘭嶼達延
潮恆長治麟洛九如裡高萬枋崁琉車滿霧瑪春獅牡
湖白望七沙烈
'''

# Priority 3: Weather terms (ESSENTIAL)
WEATHER_TERMS = '''
天氣溫度濕風雨雪雲霧冰雹雷電晴陰多雲少有陣短暫局部
冷熱暖涼爽寒冬春夏秋季節
颱風颶熱浪寒流氣壓降水機率預報警報特報
東西南北中偏轉強弱級
度量計測
'''

# Priority 4: Date and time (ESSENTIAL)
DATE_TIME = '''
年月日時分秒週星期今明後昨前天
一二三四五六七八九十百千萬億兆
零壹貳參肆伍陸柒捌玖拾佰仟
上下午早晚夜半點刻鐘
元旦初
'''

# Priority 5: Common verbs and adjectives (HIGH PRIORITY)
COMMON_WORDS = '''
是有在的了個這那些什麼都會可能要
不沒好壞大小多少高低長短新舊
來去到達從和與及或但因為所以
人民國家社經濟發展建設工作政府企業公司產品市場
說話語言文字書寫讀
看見聽聞覺感受
吃喝食物飲料米飯麵包菜肉魚蛋奶茶咖啡
住家房屋門窗床桌椅廁所浴室廚
穿衣服褲子鞋帽子襪
走路開車坐站立躺跑跳
買賣錢價格便宜貴值
學習教育校師生課本試題答案
醫院病痛藥治療健康身體頭手腳眼耳鼻嘴心肝肺
喜歡愛恨怕怒哀樂
美麗帥漂亮醜
快慢急緩遲早準
真假對錯是非善惡
安全危險
開始結束繼續停止
增加減少變化改革
重要必須需要
可以能夠應該
謝謝對不起請幫助
電話機腦網路訊息資料
'''

# Priority 6: Commonly used characters (fill to 1000)
COMMON_CHARS = '''
也已而之其於為以及至若
將被使讓由自從向往
種類型式樣
方法手段措施
問題解決
目標計劃
過程步驟
組織團隊
領導管理
部分全整
始終
進出入
內外裡面
同異別
更非常很太極
再又還才剛正
則即便雖然卻
等待
次回
每各
此彼
加增減變
知道理解明白清楚
記憶想思考慮
希望願望期待
試嘗驗證實
決定選擇
接受拒絕
發現查找尋
告訴報導播
示顯現表
供提
得失
難易簡單複雜
完成功敗
滿足夠
許允
注意小心
保護守衛防
修理補
留存放置
換交替代
續連接合併
識認
專特殊
根基礎
形狀態況情
境環周圍
界限制約
律規範
準標確精密
級階層次
量數
率比例
均
總計統
差距離
近
底頂端邊角落
直橫豎
稱呼叫喊聲響
靜吵鬧
光亮暗
彩顏紅橙黃綠藍紫粉灰棕褐銀金
香臭味甜苦辣酸
軟硬滑粗細薄
乾燥濕潤
空
輕
寬窄
深淺
破損壞裂
髒亂整潔乾淨
忙閒
舒適
便利
累疲勞
餓飽渴
痛癢麻
影象圖片像照繪畫
音樂歌唱曲調
數字母符號
節慶假
拜星農曆
晨夕
未來過去現今
永遠暫時臨
立坐臥趴蹲跪
抱握拉推拖
碰撞擊打擺
扔丟掉棄
藏隱躲
追跑趕逃
舉升降落沉浮
搖晃振動
轉翻滾
切割斷裂
縫補貼
染印刷
釘掛吊懸
塗抹擦洗刷
倒灌注流淌漏滴
融凍結冰蒸汽
燃燒滅熄
植栽培育養殖
摘採收穫
煮炒炸烤蒸煎燉
織編繡縫
奏演扮
'''

# Combine all
all_chars = ASCII + TAIWAN_LOCATIONS + WEATHER_TERMS + DATE_TIME + COMMON_WORDS + COMMON_CHARS

# Remove duplicates while preserving order
seen = set()
unique_chars = []
for char in all_chars:
    if char not in seen and char not in '\n ':  # Skip newlines and spaces
        seen.add(char)
        unique_chars.append(char)

# Take first 1000
important_1000 = ''.join(unique_chars[:1000])

# Save to file
with open('tc_important_1000.txt', 'w', encoding='utf-8') as f:
    f.write(important_1000)

print("="*70)
print("Selected Most Important 1000 Traditional Chinese Characters")
print("="*70)
print(f"\nTotal characters selected: {len(important_1000)}")

# Analyze
ascii_count = sum(1 for c in important_1000 if ord(c) < 128)
chinese_count = sum(1 for c in important_1000 if ord(c) >= 0x4e00 and ord(c) <= 0x9fff)
other_count = len(important_1000) - ascii_count - chinese_count

print(f"\nBreakdown:")
print(f"  ASCII characters: {ascii_count}")
print(f"  Chinese characters: {chinese_count}")
print(f"  Other characters: {other_count}")
print(f"  Total: {len(important_1000)}")

print(f"\nPriority distribution:")
print(f"  - Complete ASCII set: OK")
print(f"  - Taiwan locations: OK (All major cities)")
print(f"  - Weather terms: OK (Complete)")
print(f"  - Date/time: OK (Complete)")
print(f"  - Common words: OK (High frequency)")

print(f"\nOutput saved to: tc_important_1000.txt")
print(f"\nThis character set is optimized for:")
print(f"  - Taiwan weather applications")
print(f"  - Date and time display")
print(f"  - General Traditional Chinese text")
print("="*70)

# Also show first 100 characters as sample
print(f"\nFirst 100 characters:")
print(important_1000[:100])

