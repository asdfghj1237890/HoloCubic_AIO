# AccuWeather API Migration Guide

## 變更摘要

已將 Weather App 從高德地圖 API 遷移到 AccuWeather API。

**注意**: 所有舊的程式碼都已註解保留在原始檔案中，方便日後參考或復原。

## 主要變更

### 1. API 端點
- **舊版**: 高德地圖 REST API (`restapi.amap.com`)
- **新版**: AccuWeather API (`dataservice.accuweather.com`)
  - Location Search API: 取得城市的 Location Key
  - Current Conditions API: 取得即時天氣
  - 5-Day Forecast API: 取得 5 天預報

### 2. 配置參數
| 舊參數名稱 | 新參數名稱 | 說明 |
|-----------|-----------|------|
| `tianqi_url` | (移除) | 不再需要 URL 配置 |
| `tianqi_city_code` | `city_name` | 城市名稱 (英文) |
| `tianqi_api_key` | `api_key` | AccuWeather API Key |
| - | `location_key` | AccuWeather Location Key (自動快取) |
| `weatherUpdataInterval` | `weatherUpdataInterval` | (保持不變) |
| `timeUpdataInterval` | `timeUpdataInterval` | (保持不變) |
| `language` | `language` | (保持不變) |

### 3. 配置檔案
- **舊版**: `/weather_2111.cfg`
- **新版**: `/weather_accu.cfg`

### 4. 預設配置
```cpp
API Key: xxxxxxxx
城市: Beijing (可透過 WebServer 修改，支援 Taipei 等城市)
語言: 簡體中文 (Simplified Chinese)
更新間隔: 900 秒 (15 分鐘)
```

**重要更新**：移除 `language` 參數後，API 現在可以搜尋到 Taipei 和其他國際城市了！

## 功能改進

### 天氣圖示映射
- 從文字匹配改為 AccuWeather Icon Code (1-44) 映射
- 新增 `mapAccuWeatherIcon()` 函式處理圖示轉換
- 支援更完整的天氣狀態 (包含夜間模式)

### 資料擷取流程
1. 首次使用時，透過 Location Search API 取得城市的 Location Key
2. Location Key 會被快取到配置檔中，避免重複查詢
3. 使用 Location Key 查詢即時天氣和預報資料

### API 回應範例

#### Current Conditions
```json
[{
  "LocalObservationDateTime": "2024-03-21T18:30:00+08:00",
  "WeatherText": "晴朗",
  "WeatherIcon": 1,
  "Temperature": {
    "Metric": {"Value": 19.0, "Unit": "C"}
  },
  "RelativeHumidity": 38,
  "Wind": {
    "Direction": {"Localized": "東北"},
    "Speed": {"Metric": {"Value": 5.5, "Unit": "km/h"}}
  },
  "UVIndex": 3
}]
```

#### 5-Day Forecast
```json
{
  "DailyForecasts": [
    {
      "Date": "2024-03-21T07:00:00+08:00",
      "Temperature": {
        "Minimum": {"Value": 10.0, "Unit": "C"},
        "Maximum": {"Value": 25.0, "Unit": "C"}
      },
      "Day": {"Icon": 3, "IconPhrase": "Partly Sunny"},
      "Night": {"Icon": 35, "IconPhrase": "Partly Cloudy"}
    }
  ]
}
```

## WebServer 設定介面

訪問 `http://holocubic.local/weather_setting` 可設定：
- AccuWeather API Key
- 城市名稱 (英文，例如: Taipei, Tokyo, New York)
- 天氣更新週期
- 日期更新週期
- 界面語言 (簡體/繁體中文)

## 注意事項

1. **API Key 限制**: 
   - AccuWeather 免費版有每日 50 次請求限制，請注意更新頻率
   - **部分 API key 可能不包含預報功能**，只能取得即時天氣
   
2. **城市名稱**: 
   - 建議使用英文城市名稱進行搜尋
   - 如果留空，系統會自動使用您的公網 IP 偵測城市
   - 某些 API key 可能有地區限制（例如只限中國大陸城市）
   
3. **Location Key**: 會自動快取，變更城市時會自動清除並重新取得

4. **空氣品質**: AccuWeather 免費版不提供 AQI，改用 UV Index 估算

5. **風力等級**: 從風速 (km/h) 轉換，每 5 km/h 為一個等級

6. **IP 偵測**: 
   - 使用您的公網 IP（WAN IP），而非區域網路 IP（192.168.x.x）
   - 如果使用 VPN，會偵測到 VPN 伺服器的位置

## 測試建議

1. 首次啟動時，檢查 Serial Monitor 確認 Location Key 取得成功
2. 驗證天氣資料顯示正確 (溫度、濕度、天氣狀況)
3. 測試切換不同城市
4. 確認 5 天預報曲線圖顯示正常

## 故障排除

如果天氣無法更新：
1. 檢查 WiFi 連線狀態
2. 驗證 API Key 是否有效
3. 確認城市名稱拼寫正確
4. 檢查 Serial Monitor 的錯誤訊息
5. 確認未超過 API 請求限制

## 相關檔案

- `AIO_Firmware_PIO/src/app/weather/weather.cpp` - 主要邏輯
- `AIO_Firmware_PIO/src/app/weather/weather_gui.c` - GUI 介面 (未變更)
- `AIO_Firmware_PIO/src/app/server/web_setting.cpp` - WebServer 設定頁面

