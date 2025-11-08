# Font Directory Files Explanation
# 字型目錄檔案說明

---

## 📁 Font Files (字型檔案)

### ✅ **ch_font20_tc.c** - ⭐ ACTIVE IN USE
- **Size:** 1,094 KB
- **Characters:** 994 (88 ASCII + 905 Traditional Chinese)
- **Purpose:** Production-ready Traditional Chinese font
- **Usage:** Currently active in weather_gui.c - Taiwan weather and general Traditional Chinese display
- **Status:** ✅ Integrated and ready for compilation

### ch_font20.c - Simplified Chinese
- **Size:** 1,528 KB
- **Characters:** 1,442 (585 Simplified Chinese)
- **Purpose:** Original Simplified Chinese font (mainland China)
- **Usage:** For Simplified Chinese display

---

## 🔤 Font Source

### GenJyuuGothic-Normal.ttf
- Japanese font with excellent CJK character support
- Used to generate Traditional Chinese fonts
- High-quality, clean design suitable for embedded displays

---

## 🛠️ Generation Scripts (生成腳本)

### **gen_final.js** - ⭐ Main Generation Script
- **Purpose:** Generate ch_font20_tc.c
- **Usage:** `node gen_final.js`
- **What it does:** Reads tc_safe_1000.txt and generates the 994-character font

### select_important_1000.py
- **Purpose:** Select the most important 1000 Traditional Chinese characters
- **Usage:** `python select_important_1000.py`
- **Output:** tc_important_1000.txt
- **Customization:** Edit this file to change which characters are included

### generate_safe_1000.py
- **Purpose:** Remove CMD special characters from character set
- **Usage:** `python generate_safe_1000.py`
- **Input:** tc_important_1000.txt
- **Output:** tc_safe_1000.txt
- **What it removes:** `<>|&^%` (CMD special characters)

---

## 📝 Character Set Data (字符集資料)

### **tc_safe_1000.txt** - ⭐ Used for Generation
- **Characters:** 994 (CMD-safe)
- **Purpose:** Input for gen_final.js
- **Content:** All selected characters without CMD special chars

### tc_important_1000.txt
- **Characters:** 1000
- **Purpose:** Selected important characters before safety filtering
- **Content:** Prioritized Taiwan locations, weather terms, common words

### tc_chars.txt
- **Characters:** 1465
- **Purpose:** Complete Traditional Chinese character reference
- **Usage:** For reference only; contains all possible characters

---

## 📚 Documentation (文件)

### **README.md** - ⭐ Main Documentation
- Complete guide for font generation
- Usage instructions
- Multiple generation methods
- Troubleshooting

### FONT_GENERATION_SUMMARY.md
- Quick reference for the generation process
- Summary of what was generated
- Success criteria and comparison

---

## 🎯 Quick Start

### To Generate the Font:
```bash
cd AIO_Firmware_PIO/src/resource/font
node gen_final.js
```

### To Customize Character Set:
1. Edit `select_important_1000.py` (add/remove characters)
2. Run: `python select_important_1000.py`
3. Run: `python generate_safe_1000.py`
4. Run: `node gen_final.js`

### To Use in Code:
```c
LV_FONT_DECLARE(ch_font20_tc);
lv_style_set_text_font(&style, &ch_font20_tc);
```

---

## 🗑️ Files You Can Delete (if needed)

If you need to save space and won't regenerate fonts:

### Keep These (Minimum for usage):
- ✅ **ch_font20_tc.c** - The Traditional Chinese font (1,094 KB) - **REQUIRED & ACTIVE**
- ✅ **ch_font20.c** - Simplified Chinese font (if needed)

### Keep for Regeneration:
- ✅ **GenJyuuGothic-Normal.ttf** - Source font (10 MB)
- ✅ **gen_final.js** - Generation script
- ✅ **tc_safe_1000.txt** - Character set
- ✅ **README.md** - Documentation

### Optional:
- `select_important_1000.py` - Only needed if customizing characters
- `generate_safe_1000.py` - Only needed if customizing characters
- `tc_chars.txt` - Reference only
- `FILES_EXPLANATION.md` - This file

---

**Last Updated:** 2025-11-08  
**Font Version:** ch_font20_tc.c (994 characters) ⭐ ACTIVE  
**Directory Size:** ~12.6 MB (10 files)  
**Status:** Integrated in weather_gui.c

