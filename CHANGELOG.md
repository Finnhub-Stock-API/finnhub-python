## 2.0.0(2020-07-20)

This version simplify the usage of the library. It also makes the return data more friendly to use with other libraries like pandas

### Breaking Changes

The usage has simplify to

```python
import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key="YOUR API KEY")

# Stock candles
print(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249))
```
