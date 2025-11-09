# AccuWeather API 迁移指南

## 变更摘要

已将 Weather App 从高德地图 API 迁移到 AccuWeather API。

**注意**: 所有旧的代码都已注释保留在原始文件中，方便日后参考或恢复。

## 主要变更

### 1. API 端点
- **旧版**: 高德地图 REST API (`restapi.amap.com`)
- **新版**: AccuWeather API (`dataservice.accuweather.com`)
  - Location Search API: 获取城市的 Location Key
  - Current Conditions API: 获取实时天气
  - 5-Day Forecast API: 获取 5 天预报

### 2. 配置参数
| 旧参数名称 | 新参数名称 | 说明 |
|-----------|-----------|------|
| `tianqi_url` | (移除) | 不再需要 URL 配置 |
| `tianqi_city_code` | `city_name` | 城市名称 (英文) |
| `tianqi_api_key` | `api_key` | AccuWeather API Key |
| - | `location_key` | AccuWeather Location Key (自动缓存) |
| `weatherUpdataInterval` | `weatherUpdataInterval` | (保持不变) |
| `timeUpdataInterval` | `timeUpdataInterval` | (保持不变) |
| `language` | `language` | (保持不变) |

### 3. 配置文件
- **旧版**: `/weather_2111.cfg`
- **新版**: `/weather_accu.cfg`

### 4. 默认配置
```cpp
API Key: xxxxxxxx
城市: Beijing (可通过 WebServer 修改，支持 Taipei 等城市)
语言: 简体中文 (Simplified Chinese)
更新间隔: 900 秒 (15 分钟)
```

**重要更新**：移除 `language` 参数后，API 现在可以搜索到 Taipei 和其他国际城市了！

## 功能改进

### 天气图标映射
- 从文字匹配改为 AccuWeather Icon Code (1-44) 映射
- 新增 `mapAccuWeatherIcon()` 函数处理图标转换
- 支持更完整的天气状态 (包含夜间模式)

### 数据获取流程
1. 首次使用时，通过 Location Search API 获取城市的 Location Key
2. Location Key 会被缓存到配置文件中，避免重复查询
3. 使用 Location Key 查询实时天气和预报数据

### API 响应示例

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
    "Direction": {"Localized": "东北"},
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

## WebServer 设置界面

访问 `http://holocubic.local/weather_setting` 可设置：
- AccuWeather API Key
- 城市名称 (英文，例如: Taipei, Tokyo, New York)
- 天气更新周期
- 日期更新周期
- 界面语言 (简体/繁体中文)

## 注意事项

1. **API Key 限制**: 
   - AccuWeather 免费版有每日 50 次请求限制，请注意更新频率
   - **部分 API key 可能不包含预报功能**，只能获取实时天气
   
2. **城市名称**: 
   - 建议使用英文城市名称进行搜索
   - 如果留空，系统会自动使用您的公网 IP 检测城市
   - 某些 API key 可能有地区限制（例如只限中国大陆城市）
   
3. **Location Key**: 会自动缓存，变更城市时会自动清除并重新获取

4. **空气质量**: AccuWeather 免费版不提供 AQI，改用 UV Index 估算

5. **风力等级**: 从风速 (km/h) 转换，每 5 km/h 为一个等级

6. **IP 检测**: 
   - 使用您的公网 IP（WAN IP），而非局域网 IP（192.168.x.x）
   - 如果使用 VPN，会检测到 VPN 服务器的位置

## 测试建议

1. 首次启动时，检查 Serial Monitor 确认 Location Key 获取成功
2. 验证天气数据显示正确 (温度、湿度、天气状况)
3. 测试切换不同城市
4. 确认 5 天预报曲线图显示正常

## 故障排除

如果天气无法更新：
1. 检查 WiFi 连接状态
2. 验证 API Key 是否有效
3. 确认城市名称拼写正确
4. 检查 Serial Monitor 的错误信息
5. 确认未超过 API 请求限制

## 相关文件

- `AIO_Firmware_PIO/src/app/weather/weather.cpp` - 主要逻辑
- `AIO_Firmware_PIO/src/app/weather/weather_gui.c` - GUI 界面 (未变更)
- `AIO_Firmware_PIO/src/app/server/web_setting.cpp` - WebServer 设置页面


