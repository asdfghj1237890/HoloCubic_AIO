# AccuWeather API Migration Guide

## Summary

Migrated the Weather App from Amap (高德地图) API to AccuWeather API.

**Note**: All legacy code has been commented out and preserved in the original files for future reference or rollback.

## Major Changes

### 1. API Endpoints
- **Old**: Amap REST API (`restapi.amap.com`)
- **New**: AccuWeather API (`dataservice.accuweather.com`)
  - Location Search API: Retrieve city Location Key
  - Current Conditions API: Retrieve real-time weather
  - 5-Day Forecast API: Retrieve 5-day forecast

### 2. Configuration Parameters
| Old Parameter | New Parameter | Description |
|---------------|---------------|-------------|
| `tianqi_url` | (removed) | URL configuration no longer needed |
| `tianqi_city_code` | `city_name` | City name (English) |
| `tianqi_api_key` | `api_key` | AccuWeather API Key |
| - | `location_key` | AccuWeather Location Key (auto-cached) |
| `weatherUpdataInterval` | `weatherUpdataInterval` | (unchanged) |
| `timeUpdataInterval` | `timeUpdataInterval` | (unchanged) |
| `language` | `language` | (unchanged) |

### 3. Configuration File
- **Old**: `/weather_2111.cfg`
- **New**: `/weather_accu.cfg`

### 4. Default Configuration
```cpp
API Key: xxxxxxxx
City: Beijing (can be changed via WebServer, supports Taipei and other cities)
Language: Simplified Chinese
Update Interval: 900 seconds (15 minutes)
```

**Important Update**: After removing the `language` parameter, the API can now search for Taipei and other international cities!

## Feature Improvements

### Weather Icon Mapping
- Changed from text matching to AccuWeather Icon Code (1-44) mapping
- Added `mapAccuWeatherIcon()` function to handle icon conversion
- Supports more comprehensive weather states (including night mode)

### Data Retrieval Flow
1. On first use, retrieve the city's Location Key via Location Search API
2. Location Key is cached in the configuration file to avoid repeated queries
3. Use Location Key to query real-time weather and forecast data

### API Response Examples

#### Current Conditions
```json
[{
  "LocalObservationDateTime": "2024-03-21T18:30:00+08:00",
  "WeatherText": "Sunny",
  "WeatherIcon": 1,
  "Temperature": {
    "Metric": {"Value": 19.0, "Unit": "C"}
  },
  "RelativeHumidity": 38,
  "Wind": {
    "Direction": {"Localized": "NE"},
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

## WebServer Configuration Interface

Visit `http://holocubic.local/weather_setting` to configure:
- AccuWeather API Key
- City name (English, e.g., Taipei, Tokyo, New York)
- Weather update interval
- Date update interval
- Interface language (Simplified/Traditional Chinese)

## Important Notes

1. **API Key Limitations**: 
   - AccuWeather free tier has a daily limit of 50 requests, please monitor update frequency
   - **Some API keys may not include forecast functionality**, only current weather available
   
2. **City Name**: 
   - Recommended to use English city names for search
   - If left empty, the system will automatically detect the city using your public IP
   - Some API keys may have regional restrictions (e.g., limited to mainland China cities only)
   
3. **Location Key**: Automatically cached, will be cleared and re-fetched when changing cities

4. **Air Quality**: AccuWeather free tier does not provide AQI, using UV Index as an estimate instead

5. **Wind Level**: Converted from wind speed (km/h), each 5 km/h equals one level

6. **IP Detection**: 
   - Uses your public IP (WAN IP), not local network IP (192.168.x.x)
   - If using VPN, will detect VPN server location

## Testing Recommendations

1. On first startup, check Serial Monitor to confirm Location Key retrieval was successful
2. Verify weather data displays correctly (temperature, humidity, weather conditions)
3. Test switching between different cities
4. Confirm 5-day forecast chart displays normally

## Troubleshooting

If weather fails to update:
1. Check WiFi connection status
2. Verify API Key is valid
3. Confirm city name spelling is correct
4. Check Serial Monitor for error messages
5. Confirm API request limit has not been exceeded

## Related Files

- `AIO_Firmware_PIO/src/app/weather/weather.cpp` - Main logic
- `AIO_Firmware_PIO/src/app/weather/weather_gui.c` - GUI interface (unchanged)
- `AIO_Firmware_PIO/src/app/server/web_setting.cpp` - WebServer configuration page


