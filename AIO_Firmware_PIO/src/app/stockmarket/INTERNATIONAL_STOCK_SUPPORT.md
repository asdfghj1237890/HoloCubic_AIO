# International Stock Market Support

## Overview

The stock market app has been upgraded to support international stock markets beyond Chinese stocks. You can now track stocks from:

- **US Market** (United States) - NASDAQ, NYSE, etc.
- **CN Market** (China) - Shanghai and Shenzhen Stock Exchanges
- **HK Market** (Hong Kong) - Hong Kong Stock Exchange

## Key Features

### Multi-Market Support
- **US Stocks**: Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), etc.
- **Chinese Stocks**: Use stock codes like 601126, 000001 (with or without sh/sz prefix)
- **Hong Kong Stocks**: Use stock codes with .HK suffix support

### Dual API Integration
1. **Sina Finance API** - For Chinese market (CN)
   - Supports Shanghai (sh) and Shenzhen (sz) exchanges
   - Real-time data with volume and turnover

2. **Yahoo Finance API** - For international markets (US, HK, etc.)
   - Global stock data
   - JSON-based modern API
   - Extensive market coverage

## Configuration

### Web Interface
Access the stock settings through the web interface:

1. Navigate to the stock settings page
2. Enter the **Stock Symbol**:
   - US stocks: `AAPL`, `TSLA`, `GOOGL`, etc.
   - Chinese stocks: `601126`, `sh601126`, `sz000001`, etc.
   - Hong Kong stocks: `0700`, `9988`, etc.

3. Select **Market Type**:
   - US (United States)
   - CN (China)
   - HK (Hong Kong)

4. Set **Update Interval** in milliseconds (default: 10000ms = 10 seconds)

### Example Configurations

#### US Stock - Apple Inc.
- Stock Symbol: `AAPL`
- Market Type: `US`
- Update Interval: `10000`

#### Chinese Stock - China Shenhua Energy
- Stock Symbol: `601126` or `sh601126`
- Market Type: `CN`
- Update Interval: `10000`

#### Hong Kong Stock - Tencent Holdings
- Stock Symbol: `0700`
- Market Type: `HK`
- Update Interval: `10000`

## Display Information

The stock app displays:
- **Stock Name/Symbol**: Company name or ticker
- **Current Price**: Real-time stock price
- **Change Value**: Price change from previous close
- **Change Percentage**: Percentage change
- **Open**: Opening price
- **High**: Daily high
- **Previous Close**: Yesterday's closing price
- **Low**: Daily low
- **Volume**: Trading volume (in millions)
- **Turnover**: Trading turnover (in billions)

### Color Coding (Taiwan/Hong Kong Style)
- 🟢 **Green**: Stock price UP (gain) ↑ - Green arrow pointing up
- 🔴 **Red**: Stock price DOWN (loss) ↓ - Red arrow pointing down

Note: This follows Taiwan/Hong Kong convention (green=up, red=down), which is opposite to Mainland China convention. Both the text color and arrow icon color match this convention.

## Technical Details

### File Changes

#### `stockmarket.cpp`
- Added `market_type` configuration parameter
- Implemented `buildStockSymbol()` for market-specific formatting
- Refactored `http_request()` to support multiple APIs
- Added `parse_sina_data()` for Chinese market data
- Added `parse_yahoo_data()` for international market data with JSON parsing
- Updated configuration persistence to save market type
- Enhanced error handling and logging

#### `stockmarket_gui.c`
- Internationalized display labels (English)
- Updated to show stock name/symbol properly
- Improved layout for international stocks

#### `web_setting.cpp`
- Added market type dropdown selector
- Updated form to accept new stock symbol parameter
- Enhanced configuration save/load functions
- Improved user interface with clear labels

### Data Structures

```cpp
struct B_Config
{
    String stock_symbol;          // Stock symbol (e.g., AAPL, TSLA, 601126)
    String market_type;           // Market type: CN, US, HK
    unsigned long updataInterval; // Update interval (milliseconds)
};
```

### API Endpoints

**Chinese Market (Sina Finance)**
```
http://hq.sinajs.cn/list={symbol}
Example: http://hq.sinajs.cn/list=sh601126
```

**International Markets (Yahoo Finance)**
```
https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d
Example: https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=1d&range=1d
```

## Backward Compatibility

The implementation maintains backward compatibility:
- Old `stock_id` parameter is automatically converted to `stock_symbol`
- Existing Chinese stock configurations will continue to work
- Default market type is set to `US` for new installations

## Network Requirements

- Active WiFi connection required
- HTTPS support for Yahoo Finance API
- HTTP support for Sina Finance API
- Recommended timeout: 2-3 seconds

## Troubleshooting

### Stock Data Not Updating
1. Check WiFi connection
2. Verify stock symbol is correct for the selected market
3. Ensure market type matches the stock symbol
4. Check serial monitor for error messages

### Parsing Errors
- **Chinese stocks**: Ensure stock code has correct sh/sz prefix or let the system add it
- **US stocks**: Use standard ticker symbols (all caps)
- **Hong Kong stocks**: Use numeric codes (e.g., 0700, 9988)

### Common Error Messages
- `[HTTP] Http request failed.` - Network connectivity issue
- `[JSON] Parse failed` - Invalid response from Yahoo Finance
- `[Parse] Failed to parse stock data` - Data structure mismatch

## Future Enhancements

Potential additions:
- Support for more exchanges (Tokyo, London, etc.)
- Historical price charts
- Multiple stock watchlist
- Price alerts
- Currency conversion for international stocks

## Dependencies

- **ArduinoJson** - For parsing Yahoo Finance JSON responses
- **HTTPClient** - For making API requests
- **WiFi** - Network connectivity

## Testing

Recommended test cases:
1. US tech stock (AAPL, MSFT, GOOGL)
2. Chinese bank stock (601126, 601398)
3. Hong Kong tech stock (0700, 9988)
4. Switch between different markets
5. Network disconnect/reconnect scenarios

## Credits

Original Implementation: HoloCubic AIO Project
International Support Enhancement: 2025

## License

Follows the parent project's license terms.

