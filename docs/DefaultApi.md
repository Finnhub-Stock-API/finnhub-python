# finnhub.DefaultApi

All URIs are relative to *https://finnhub.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_indicator**](DefaultApi.md#aggregate_indicator) | **GET** /scan/technical-indicator | Aggregate Indicators
[**company_earnings**](DefaultApi.md#company_earnings) | **GET** /stock/earnings | Earnings Surprises
[**company_eps_estimates**](DefaultApi.md#company_eps_estimates) | **GET** /stock/eps-estimate | Earnings Estimates
[**company_executive**](DefaultApi.md#company_executive) | **GET** /stock/executive | Company Executive
[**company_metrics**](DefaultApi.md#company_metrics) | **GET** /stock/metric | Metrics
[**company_news**](DefaultApi.md#company_news) | **GET** /company-news | Company News
[**company_peers**](DefaultApi.md#company_peers) | **GET** /stock/peers | Peers
[**company_profile**](DefaultApi.md#company_profile) | **GET** /stock/profile | Company Profile
[**company_profile2**](DefaultApi.md#company_profile2) | **GET** /stock/profile2 | Company Profile 2
[**company_revenue_estimates**](DefaultApi.md#company_revenue_estimates) | **GET** /stock/revenue-estimate | Revenue Estimates
[**covid19**](DefaultApi.md#covid19) | **GET** /covid19/us | COVID-19
[**crypto_candles**](DefaultApi.md#crypto_candles) | **GET** /crypto/candle | Crypto Candles
[**crypto_exchanges**](DefaultApi.md#crypto_exchanges) | **GET** /crypto/exchange | Crypto Exchanges
[**crypto_symbols**](DefaultApi.md#crypto_symbols) | **GET** /crypto/symbol | Crypto Symbol
[**earnings_calendar**](DefaultApi.md#earnings_calendar) | **GET** /calendar/earnings | Earnings Calendar
[**filings**](DefaultApi.md#filings) | **GET** /stock/filings | Filings
[**financials**](DefaultApi.md#financials) | **GET** /stock/financials | Financial Statements
[**financials_reported**](DefaultApi.md#financials_reported) | **GET** /stock/financials-reported | Financials As Reported
[**forex_candles**](DefaultApi.md#forex_candles) | **GET** /forex/candle | Forex Candles
[**forex_exchanges**](DefaultApi.md#forex_exchanges) | **GET** /forex/exchange | Forex Exchanges
[**forex_rates**](DefaultApi.md#forex_rates) | **GET** /forex/rates | Forex rates
[**forex_symbols**](DefaultApi.md#forex_symbols) | **GET** /forex/symbol | Forex Symbol
[**fund_ownership**](DefaultApi.md#fund_ownership) | **GET** /stock/fund-ownership | Fund Ownership
[**general_news**](DefaultApi.md#general_news) | **GET** /news | General News
[**investors_ownership**](DefaultApi.md#investors_ownership) | **GET** /stock/investor-ownership | Investors Ownership
[**ipo_calendar**](DefaultApi.md#ipo_calendar) | **GET** /calendar/ipo | IPO Calendar
[**major_developments**](DefaultApi.md#major_developments) | **GET** /major-development | Major Developments
[**news_sentiment**](DefaultApi.md#news_sentiment) | **GET** /news-sentiment | News Sentiment
[**pattern_recognition**](DefaultApi.md#pattern_recognition) | **GET** /scan/pattern | Pattern Recognition
[**price_target**](DefaultApi.md#price_target) | **GET** /stock/price-target | Price Target
[**quote**](DefaultApi.md#quote) | **GET** /quote | Quote
[**recommendation_trends**](DefaultApi.md#recommendation_trends) | **GET** /stock/recommendation | Recommendation Trends
[**stock_candles**](DefaultApi.md#stock_candles) | **GET** /stock/candle | Stock Candles
[**stock_dividends**](DefaultApi.md#stock_dividends) | **GET** /stock/dividend | Dividends
[**stock_splits**](DefaultApi.md#stock_splits) | **GET** /stock/split | Splits
[**stock_symbols**](DefaultApi.md#stock_symbols) | **GET** /stock/symbol | Stock Symbol
[**stock_tick**](DefaultApi.md#stock_tick) | **GET** /stock/tick | Tick Data
[**support_resistance**](DefaultApi.md#support_resistance) | **GET** /scan/support-resistance | Support/Resistance
[**technical_indicator**](DefaultApi.md#technical_indicator) | **GET** /indicator | Technical Indicators
[**transcripts**](DefaultApi.md#transcripts) | **GET** /stock/transcripts | Earnings Call Transcripts
[**transcripts_list**](DefaultApi.md#transcripts_list) | **GET** /stock/transcripts/list | Earnings Call Transcripts List
[**upgrade_downgrade**](DefaultApi.md#upgrade_downgrade) | **GET** /stock/upgrade-downgrade | Stock Upgrade/Downgrade


# **aggregate_indicator**
> AggregateIndicators aggregate_indicator(symbol, resolution)

Aggregate Indicators

Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | symbol
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.

    try:
        # Aggregate Indicators
        api_response = api_instance.aggregate_indicator(symbol, resolution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->aggregate_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| symbol | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 

### Return type

[**AggregateIndicators**](AggregateIndicators.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_earnings**
> list[EarningResult] company_earnings(symbol, limit=limit)

Earnings Surprises

Get company historical quarterly earnings surprise going back to 2000.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
limit = 56 # int | Limit number of period returned. Leave blank to get the full history. (optional)

    try:
        # Earnings Surprises
        api_response = api_instance.company_earnings(symbol, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_earnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **limit** | **int**| Limit number of period returned. Leave blank to get the full history. | [optional] 

### Return type

[**list[EarningResult]**](EarningResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_eps_estimates**
> EarningsEstimates company_eps_estimates(symbol, freq=freq)

Earnings Estimates

Get company's EPS estimates.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
freq = 'freq_example' # str | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code> (optional)

    try:
        # Earnings Estimates
        api_response = api_instance.company_eps_estimates(symbol, freq=freq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_eps_estimates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **freq** | **str**| Can take 1 of the following values: &lt;code&gt;annual, quarterly&lt;/code&gt;. Default to &lt;code&gt;quarterly&lt;/code&gt; | [optional] 

### Return type

[**EarningsEstimates**](EarningsEstimates.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_executive**
> CompanyExecutive company_executive(symbol)

Company Executive

Get a list of company's executives and members of the Board.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.

    try:
        # Company Executive
        api_response = api_instance.company_executive(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_executive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 

### Return type

[**CompanyExecutive**](CompanyExecutive.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_metrics**
> Metrics company_metrics(symbol, metric)

Metrics

Get company key metrics such as growth, price, valuation. Full list of supported fields can be downloaded <a target=\"_blank\" href=\"https://static.finnhub.io/csv/metrics.csv\">here</a>

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
metric = 'metric_example' # str | Metric type. Can be 1 of the following values <code>price, valuation, growth, margin, management, financialStrength, perShare</code>

    try:
        # Metrics
        api_response = api_instance.company_metrics(symbol, metric)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **metric** | **str**| Metric type. Can be 1 of the following values &lt;code&gt;price, valuation, growth, margin, management, financialStrength, perShare&lt;/code&gt; | 

### Return type

[**Metrics**](Metrics.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_news**
> list[News] company_news(symbol, _from, to)

Company News

List latest company news by symbol. This endpoint is only available for US companies.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Company symbol.
_from = '2013-10-20' # date | From date <code>YYYY-MM-DD</code>.
to = '2013-10-20' # date | To date <code>YYYY-MM-DD</code>.

    try:
        # Company News
        api_response = api_instance.company_news(symbol, _from, to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Company symbol. | 
 **_from** | **date**| From date &lt;code&gt;YYYY-MM-DD&lt;/code&gt;. | 
 **to** | **date**| To date &lt;code&gt;YYYY-MM-DD&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_peers**
> list[str] company_peers(symbol)

Peers

Get company peers. Return a list of peers in the same country and GICS sub-industry

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.

    try:
        # Peers
        api_response = api_instance.company_peers(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_profile**
> CompanyProfile company_profile(symbol=symbol, isin=isin, cusip=cusip)

Company Profile

Get general information of a company. You can query by symbol, ISIN or CUSIP

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL, SBIN.NS e.g. (optional)
isin = 'isin_example' # str | ISIN (optional)
cusip = 'cusip_example' # str | CUSIP (optional)

    try:
        # Company Profile
        api_response = api_instance.company_profile(symbol=symbol, isin=isin, cusip=cusip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL, SBIN.NS e.g. | [optional] 
 **isin** | **str**| ISIN | [optional] 
 **cusip** | **str**| CUSIP | [optional] 

### Return type

[**CompanyProfile**](CompanyProfile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_profile2**
> CompanyProfile2 company_profile2(symbol=symbol, isin=isin, cusip=cusip)

Company Profile 2

Get general information of a company. You can query by symbol, ISIN or CUSIP. This is the free version of <a href=\"#company-profile\">Company Profile</a>.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL, SBIN.NS e.g. (optional)
isin = 'isin_example' # str | ISIN (optional)
cusip = 'cusip_example' # str | CUSIP (optional)

    try:
        # Company Profile 2
        api_response = api_instance.company_profile2(symbol=symbol, isin=isin, cusip=cusip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_profile2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL, SBIN.NS e.g. | [optional] 
 **isin** | **str**| ISIN | [optional] 
 **cusip** | **str**| CUSIP | [optional] 

### Return type

[**CompanyProfile2**](CompanyProfile2.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_revenue_estimates**
> RevenueEstimates company_revenue_estimates(symbol, freq=freq)

Revenue Estimates

Get company's revenue estimates.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
freq = 'freq_example' # str | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code> (optional)

    try:
        # Revenue Estimates
        api_response = api_instance.company_revenue_estimates(symbol, freq=freq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->company_revenue_estimates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **freq** | **str**| Can take 1 of the following values: &lt;code&gt;annual, quarterly&lt;/code&gt;. Default to &lt;code&gt;quarterly&lt;/code&gt; | [optional] 

### Return type

[**RevenueEstimates**](RevenueEstimates.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **covid19**
> COVID19 covid19()

COVID-19

Get real-time updates on the number of COVID-19 (Corona virus) cases in the US with a state-by-state breakdown. Data is sourced from CDC and reputable sources.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    
    try:
        # COVID-19
        api_response = api_instance.covid19()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->covid19: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**COVID19**](COVID19.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_candles**
> CryptoCandles crypto_candles(symbol, resolution, _from=_from, to=to, format=format, count=count)

Crypto Candles

Get candlestick data for crypto symbols.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.
_from = 56 # int | UNIX timestamp. Interval initial value. If count is not provided, this field is required (optional)
to = 56 # int | UNIX timestamp. Interval end value. If count is not provided, this field is required (optional)
format = 'format_example' # str | By default, <code>format=json</code>. Strings <code>json</code> and <code>csv</code> are accepted. (optional)
count = 56 # int | Shortcut to set <code>to=Unix.Now</code> and <code>from=Unix.Now - count * resolution_second</code>. (optional)

    try:
        # Crypto Candles
        api_response = api_instance.crypto_candles(symbol, resolution, _from=_from, to=to, format=format, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->crypto_candles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Use symbol returned in &lt;code&gt;/crypto/symbol&lt;/code&gt; endpoint for this field. | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 
 **_from** | **int**| UNIX timestamp. Interval initial value. If count is not provided, this field is required | [optional] 
 **to** | **int**| UNIX timestamp. Interval end value. If count is not provided, this field is required | [optional] 
 **format** | **str**| By default, &lt;code&gt;format&#x3D;json&lt;/code&gt;. Strings &lt;code&gt;json&lt;/code&gt; and &lt;code&gt;csv&lt;/code&gt; are accepted. | [optional] 
 **count** | **int**| Shortcut to set &lt;code&gt;to&#x3D;Unix.Now&lt;/code&gt; and &lt;code&gt;from&#x3D;Unix.Now - count * resolution_second&lt;/code&gt;. | [optional] 

### Return type

[**CryptoCandles**](CryptoCandles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_exchanges**
> list[str] crypto_exchanges()

Crypto Exchanges

List supported crypto exchanges

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    
    try:
        # Crypto Exchanges
        api_response = api_instance.crypto_exchanges()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->crypto_exchanges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_symbols**
> list[CryptoSymbol] crypto_symbols(exchange)

Crypto Symbol

List supported crypto symbols by exchange

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    exchange = 'exchange_example' # str | Exchange you want to get the list of symbols from.

    try:
        # Crypto Symbol
        api_response = api_instance.crypto_symbols(exchange)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->crypto_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| Exchange you want to get the list of symbols from. | 

### Return type

[**list[CryptoSymbol]**](CryptoSymbol.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **earnings_calendar**
> list[EarningRelease] earnings_calendar(_from=_from, to=to, symbol=symbol, international=international)

Earnings Calendar

Get historical and coming earnings release dating back to 2003. You can setup <a href=\"#webhook\">webhook</a> to receive real-time earnings update.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    _from = '2013-10-20' # date | From date: 2020-03-15. (optional)
to = '2013-10-20' # date | To date: 2020-03-16. (optional)
symbol = 'symbol_example' # str | Filter by symbol: AAPL. (optional)
international = None # object | Set to <code>true</code> to include international markets. Default value is <code>false</code> (optional)

    try:
        # Earnings Calendar
        api_response = api_instance.earnings_calendar(_from=_from, to=to, symbol=symbol, international=international)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->earnings_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| From date: 2020-03-15. | [optional] 
 **to** | **date**| To date: 2020-03-16. | [optional] 
 **symbol** | **str**| Filter by symbol: AAPL. | [optional] 
 **international** | [**object**](.md)| Set to &lt;code&gt;true&lt;/code&gt; to include international markets. Default value is &lt;code&gt;false&lt;/code&gt; | [optional] 

### Return type

[**list[EarningRelease]**](EarningRelease.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings**
> list[Filing] filings(symbol=symbol, cik=cik, access_number=access_number)

Filings

List company's filing.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol. Leave <code>symbol</code>,<code>cik</code> and <code>accessNumber</code> empty to list latest filings. (optional)
cik = 'cik_example' # str | CIK. (optional)
access_number = 'access_number_example' # str | Access number of a specific report you want to retrieve data from. (optional)

    try:
        # Filings
        api_response = api_instance.filings(symbol=symbol, cik=cik, access_number=access_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol. Leave &lt;code&gt;symbol&lt;/code&gt;,&lt;code&gt;cik&lt;/code&gt; and &lt;code&gt;accessNumber&lt;/code&gt; empty to list latest filings. | [optional] 
 **cik** | **str**| CIK. | [optional] 
 **access_number** | **str**| Access number of a specific report you want to retrieve data from. | [optional] 

### Return type

[**list[Filing]**](Filing.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **financials**
> FinancialStatements financials(symbol, statement, freq)

Financial Statements

Get standardized balance sheet, income statement and cash flow for global companies going back 30+ years.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
statement = 'statement_example' # str | Statement can take 1 of these values <code>bs, ic, cf</code> for Balance Sheet, Income Statement, Cash Flow respectively.
freq = 'freq_example' # str | Frequency can take 1 of these values <code>annual, quarterly, ttm, ytd</code>.  TTM (Trailing Twelve Months) option is available for Income Statement and Cash Flow. YTD (Year To Date) option is only available for Cash Flow.

    try:
        # Financial Statements
        api_response = api_instance.financials(symbol, statement, freq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **statement** | **str**| Statement can take 1 of these values &lt;code&gt;bs, ic, cf&lt;/code&gt; for Balance Sheet, Income Statement, Cash Flow respectively. | 
 **freq** | **str**| Frequency can take 1 of these values &lt;code&gt;annual, quarterly, ttm, ytd&lt;/code&gt;.  TTM (Trailing Twelve Months) option is available for Income Statement and Cash Flow. YTD (Year To Date) option is only available for Cash Flow. | 

### Return type

[**FinancialStatements**](FinancialStatements.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **financials_reported**
> FinancialsAsReported financials_reported(symbol=symbol, cik=cik, access_number=access_number, freq=freq)

Financials As Reported

Get financials as reported.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol. (optional)
cik = 'cik_example' # str | CIK. (optional)
access_number = 'access_number_example' # str | Access number of a specific report you want to retrieve financials from. (optional)
freq = 'freq_example' # str | Frequency. Can be either <code>annual</code> or <code>quarterly</code>. Default to <code>annual</code>. (optional)

    try:
        # Financials As Reported
        api_response = api_instance.financials_reported(symbol=symbol, cik=cik, access_number=access_number, freq=freq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->financials_reported: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol. | [optional] 
 **cik** | **str**| CIK. | [optional] 
 **access_number** | **str**| Access number of a specific report you want to retrieve financials from. | [optional] 
 **freq** | **str**| Frequency. Can be either &lt;code&gt;annual&lt;/code&gt; or &lt;code&gt;quarterly&lt;/code&gt;. Default to &lt;code&gt;annual&lt;/code&gt;. | [optional] 

### Return type

[**FinancialsAsReported**](FinancialsAsReported.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forex_candles**
> ForexCandles forex_candles(symbol, resolution, _from=_from, to=to, format=format)

Forex Candles

Get candlestick data for forex symbols.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.
_from = 56 # int | UNIX timestamp. Interval initial value. If count is not provided, this field is required (optional)
to = 56 # int | UNIX timestamp. Interval end value. If count is not provided, this field is required (optional)
format = 'format_example' # str | By default, <code>format=json</code>. Strings <code>json</code> and <code>csv</code> are accepted. (optional)

    try:
        # Forex Candles
        api_response = api_instance.forex_candles(symbol, resolution, _from=_from, to=to, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->forex_candles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Use symbol returned in &lt;code&gt;/forex/symbol&lt;/code&gt; endpoint for this field. | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 
 **_from** | **int**| UNIX timestamp. Interval initial value. If count is not provided, this field is required | [optional] 
 **to** | **int**| UNIX timestamp. Interval end value. If count is not provided, this field is required | [optional] 
 **format** | **str**| By default, &lt;code&gt;format&#x3D;json&lt;/code&gt;. Strings &lt;code&gt;json&lt;/code&gt; and &lt;code&gt;csv&lt;/code&gt; are accepted. | [optional] 

### Return type

[**ForexCandles**](ForexCandles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forex_exchanges**
> list[str] forex_exchanges()

Forex Exchanges

List supported forex exchanges

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    
    try:
        # Forex Exchanges
        api_response = api_instance.forex_exchanges()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->forex_exchanges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forex_rates**
> Forexrates forex_rates(base=base)

Forex rates

Get rates for all forex pairs. Ideal for currency conversion

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    base = 'base_example' # str | Base currency. Default to EUR. (optional)

    try:
        # Forex rates
        api_response = api_instance.forex_rates(base=base)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->forex_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base** | **str**| Base currency. Default to EUR. | [optional] 

### Return type

[**Forexrates**](Forexrates.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forex_symbols**
> list[ForexSymbol] forex_symbols(exchange)

Forex Symbol

List supported forex symbols.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    exchange = 'exchange_example' # str | Exchange you want to get the list of symbols from.

    try:
        # Forex Symbol
        api_response = api_instance.forex_symbols(exchange)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->forex_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| Exchange you want to get the list of symbols from. | 

### Return type

[**list[ForexSymbol]**](ForexSymbol.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fund_ownership**
> FundOwnership fund_ownership(symbol, limit=limit)

Fund Ownership

Get a full list fund and institutional investors of a company in descending order of the number of shares held.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
limit = 56 # int | Limit number of results. Leave empty to get the full list. (optional)

    try:
        # Fund Ownership
        api_response = api_instance.fund_ownership(symbol, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->fund_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **limit** | **int**| Limit number of results. Leave empty to get the full list. | [optional] 

### Return type

[**FundOwnership**](FundOwnership.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **general_news**
> list[News] general_news(category, min_id=min_id)

General News

Get latest market news.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    category = 'category_example' # str | This parameter can be 1 of the following values <code>general, forex, crypto, merger</code>.
min_id = 'min_id_example' # str | Use this field to get only news after this ID. Default to 0 (optional)

    try:
        # General News
        api_response = api_instance.general_news(category, min_id=min_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->general_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| This parameter can be 1 of the following values &lt;code&gt;general, forex, crypto, merger&lt;/code&gt;. | 
 **min_id** | **str**| Use this field to get only news after this ID. Default to 0 | [optional] 

### Return type

[**list[News]**](News.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investors_ownership**
> InvestorsOwnership investors_ownership(symbol, limit=limit)

Investors Ownership

Get a full list of shareholders/investors of a company in descending order of the number of shares held.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.
limit = 56 # int | Limit number of results. Leave empty to get the full list. (optional)

    try:
        # Investors Ownership
        api_response = api_instance.investors_ownership(symbol, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->investors_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 
 **limit** | **int**| Limit number of results. Leave empty to get the full list. | [optional] 

### Return type

[**InvestorsOwnership**](InvestorsOwnership.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipo_calendar**
> list[IPOEvent] ipo_calendar(_from, to)

IPO Calendar

Get recent and coming IPO.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    _from = '2013-10-20' # date | From date: 2020-03-15.
to = '2013-10-20' # date | To date: 2020-03-16.

    try:
        # IPO Calendar
        api_response = api_instance.ipo_calendar(_from, to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->ipo_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| From date: 2020-03-15. | 
 **to** | **date**| To date: 2020-03-16. | 

### Return type

[**list[IPOEvent]**](IPOEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **major_developments**
> MajorDevelopments major_developments(symbol, _from=_from, to=to)

Major Developments

List latest major developments of a company going back 20 years with 12M+ data points. This data can be used to highlight the most significant events. Limit to 200 results/call for Ultimate users, and 20 results/call other plans.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Company symbol.
_from = '2013-10-20' # date | From time: 2020-01-01. This option is only available for Ultimate users. (optional)
to = '2013-10-20' # date | To time: 2020-01-05. This option is only available for Ultimate users. (optional)

    try:
        # Major Developments
        api_response = api_instance.major_developments(symbol, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->major_developments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Company symbol. | 
 **_from** | **date**| From time: 2020-01-01. This option is only available for Ultimate users. | [optional] 
 **to** | **date**| To time: 2020-01-05. This option is only available for Ultimate users. | [optional] 

### Return type

[**MajorDevelopments**](MajorDevelopments.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_sentiment**
> NewsSentiment news_sentiment(symbol)

News Sentiment

Get company's news sentiment and statistics. This endpoint is only available for US companies.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Company symbol.

    try:
        # News Sentiment
        api_response = api_instance.news_sentiment(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->news_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Company symbol. | 

### Return type

[**NewsSentiment**](NewsSentiment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pattern_recognition**
> list[object] pattern_recognition(symbol, resolution)

Pattern Recognition

Run pattern recognition algorithm on a symbol. Support double top/bottom, triple top/bottom, head and shoulders, triangle, wedge, channel, flag, and candlestick patterns.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.

    try:
        # Pattern Recognition
        api_response = api_instance.pattern_recognition(symbol, resolution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->pattern_recognition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 

### Return type

**list[object]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_target**
> PriceTarget price_target(symbol)

Price Target

Get latest price target consensus.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.

    try:
        # Price Target
        api_response = api_instance.price_target(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->price_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 

### Return type

[**PriceTarget**](PriceTarget.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote**
> Quote quote(symbol)

Quote

<p>Get quote data for stocks. Constant polling is not recommended. Use websocket if you need real-time update.</p><p> Real-time stock prices for international markets are supported for Enterprise clients via our partner's feed. <a href=\"mailto:support@finnhub.io\">Contact Us</a> to learn more.</p>

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol

    try:
        # Quote
        api_response = api_instance.quote(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol | 

### Return type

[**Quote**](Quote.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendation_trends**
> RecommendationTrends recommendation_trends(symbol)

Recommendation Trends

Get latest analyst recommendation trends for a company.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL.

    try:
        # Recommendation Trends
        api_response = api_instance.recommendation_trends(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->recommendation_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. | 

### Return type

[**RecommendationTrends**](RecommendationTrends.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_candles**
> StockCandles stock_candles(symbol, resolution, _from=_from, to=to, format=format, adjusted=adjusted)

Stock Candles

<p>Get candlestick data for stocks going back 25 years.</p><p> Real-time stock prices for international markets are supported for Enterprise clients via our partner's feed. <a href=\"mailto:support@finnhub.io\">Contact Us</a> to learn more.</p>

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol.
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.
_from = 56 # int | UNIX timestamp. Interval initial value. If count is not provided, this field is required (optional)
to = 56 # int | UNIX timestamp. Interval end value. If count is not provided, this field is required (optional)
format = 'format_example' # str | By default, <code>format=json</code>. Strings <code>json</code> and <code>csv</code> are accepted. (optional)
adjusted = 'adjusted_example' # str | By default, <code>adjusted=false</code>. Use <code>true</code> to get adjusted data. (optional)

    try:
        # Stock Candles
        api_response = api_instance.stock_candles(symbol, resolution, _from=_from, to=to, format=format, adjusted=adjusted)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->stock_candles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol. | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 
 **_from** | **int**| UNIX timestamp. Interval initial value. If count is not provided, this field is required | [optional] 
 **to** | **int**| UNIX timestamp. Interval end value. If count is not provided, this field is required | [optional] 
 **format** | **str**| By default, &lt;code&gt;format&#x3D;json&lt;/code&gt;. Strings &lt;code&gt;json&lt;/code&gt; and &lt;code&gt;csv&lt;/code&gt; are accepted. | [optional] 
 **adjusted** | **str**| By default, &lt;code&gt;adjusted&#x3D;false&lt;/code&gt;. Use &lt;code&gt;true&lt;/code&gt; to get adjusted data. | [optional] 

### Return type

[**StockCandles**](StockCandles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_dividends**
> Dividends stock_dividends(symbol, _from, to)

Dividends

Get dividends data for common stocks going back 30 years.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol.
_from = '2013-10-20' # date | YYYY-MM-DD.
to = '2013-10-20' # date | YYYY-MM-DD.

    try:
        # Dividends
        api_response = api_instance.stock_dividends(symbol, _from, to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->stock_dividends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol. | 
 **_from** | **date**| YYYY-MM-DD. | 
 **to** | **date**| YYYY-MM-DD. | 

### Return type

[**Dividends**](Dividends.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_splits**
> Splits stock_splits(symbol, _from, to)

Splits

Get splits data for stocks.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol.
_from = '2013-10-20' # date | YYYY-MM-DD.
to = '2013-10-20' # date | YYYY-MM-DD.

    try:
        # Splits
        api_response = api_instance.stock_splits(symbol, _from, to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->stock_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol. | 
 **_from** | **date**| YYYY-MM-DD. | 
 **to** | **date**| YYYY-MM-DD. | 

### Return type

[**Splits**](Splits.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_symbols**
> list[Stock] stock_symbols(exchange)

Stock Symbol

List supported stocks.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    exchange = 'exchange_example' # str | Exchange you want to get the list of symbols from. List of exchanges with fundamental data can be found <a href=\"https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing\" target=\"_blank\">here</a>.

    try:
        # Stock Symbol
        api_response = api_instance.stock_symbols(exchange)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->stock_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| Exchange you want to get the list of symbols from. List of exchanges with fundamental data can be found &lt;a href&#x3D;\&quot;https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp&#x3D;sharing\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;. | 

### Return type

[**list[Stock]**](Stock.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_tick**
> TickData stock_tick(symbol, date)

Tick Data

<p>Get historical tick data for US stocks from all 13 exchanges. Return csv format. You can send the request directly to our tick server at <a href=\"https://tick.finnhub.io/\">https://tick.finnhub.io/</a> with the same path and parameters or get redirected there if you call our main server. Data is updated at the end of each trading day.</p><p>Tick data from 1993 is available for Enterprise clients via our partner's feed. <a href=\"mailto:support@finnhub.io\">Contact us</a> to learn more.</p>

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol.
date = '2013-10-20' # date | Date: 2020-04-02.

    try:
        # Tick Data
        api_response = api_instance.stock_tick(symbol, date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->stock_tick: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol. | 
 **date** | **date**| Date: 2020-04-02. | 

### Return type

[**TickData**](TickData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_resistance**
> list[float] support_resistance(symbol, resolution)

Support/Resistance

Get support and resistance levels for a symbol.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.

    try:
        # Support/Resistance
        api_response = api_instance.support_resistance(symbol, resolution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->support_resistance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 

### Return type

**list[float]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **technical_indicator**
> TechnicalIndicators technical_indicator(symbol, resolution, _from, to, indicator, indicator_specific_fields=indicator_specific_fields)

Technical Indicators

Return technical indicator with price data. List of supported indicators can be found <a href=\"https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing\" target=\"_blank\">here</a>.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | symbol
resolution = 'resolution_example' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.
_from = 56 # int | UNIX timestamp. Interval initial value. If count is not provided, this field is required
to = 56 # int | UNIX timestamp. Interval end value. If count is not provided, this field is required
indicator = 'indicator_example' # str | Indicator name. Full list can be found <a href=\"https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing\" target=\"_blank\">here</a>.
indicator_specific_fields = None # object | Check out <a href=\"https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing\" target=\"_blank\">this page</a> to see which indicators and params are supported. (optional)

    try:
        # Technical Indicators
        api_response = api_instance.technical_indicator(symbol, resolution, _from, to, indicator, indicator_specific_fields=indicator_specific_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->technical_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| symbol | 
 **resolution** | **str**| Supported resolution includes &lt;code&gt;1, 5, 15, 30, 60, D, W, M &lt;/code&gt;.Some timeframes might not be available depending on the exchange. | 
 **_from** | **int**| UNIX timestamp. Interval initial value. If count is not provided, this field is required | 
 **to** | **int**| UNIX timestamp. Interval end value. If count is not provided, this field is required | 
 **indicator** | **str**| Indicator name. Full list can be found &lt;a href&#x3D;\&quot;https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp&#x3D;sharing\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;. | 
 **indicator_specific_fields** | [**object**](.md)| Check out &lt;a href&#x3D;\&quot;https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp&#x3D;sharing\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this page&lt;/a&gt; to see which indicators and params are supported. | [optional] 

### Return type

[**TechnicalIndicators**](TechnicalIndicators.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcripts**
> EarningsCallTranscripts transcripts(id)

Earnings Call Transcripts

Get earnings call transcripts, audio and participants' list. This endpoint is only available for US companies. Earnings call transcripts for international markets are available for Enterprise clients via our partner's feed. <a href=\"mailto:support@finnhub.io\">Contact us</a> to learn more.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    id = 'id_example' # str | Transcript's id obtained with <a href=\"#transcripts-list\">Transcripts List endpoint</a>.

    try:
        # Earnings Call Transcripts
        api_response = api_instance.transcripts(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->transcripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Transcript&#39;s id obtained with &lt;a href&#x3D;\&quot;#transcripts-list\&quot;&gt;Transcripts List endpoint&lt;/a&gt;. | 

### Return type

[**EarningsCallTranscripts**](EarningsCallTranscripts.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcripts_list**
> EarningsCallTranscriptsList transcripts_list(symbol)

Earnings Call Transcripts List

List earnings call transcripts' metadata. This endpoint is only available for US companies. Earnings call transcripts for international markets are available for Enterprise clients via our partner's feed. <a href=\"mailto:support@finnhub.io\">Contact us</a> to learn more.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Company symbol: AAPL. Leave empty to list the latest transcripts

    try:
        # Earnings Call Transcripts List
        api_response = api_instance.transcripts_list(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->transcripts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Company symbol: AAPL. Leave empty to list the latest transcripts | 

### Return type

[**EarningsCallTranscriptsList**](EarningsCallTranscriptsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_downgrade**
> list[UpgradeDowngrade] upgrade_downgrade(symbol=symbol)

Stock Upgrade/Downgrade

Get latest stock upgrade and downgrade.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = finnhub.Configuration(
    host = "https://finnhub.io/api/v1",
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades. (optional)

    try:
        # Stock Upgrade/Downgrade
        api_response = api_instance.upgrade_downgrade(symbol=symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->upgrade_downgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades. | [optional] 

### Return type

[**list[UpgradeDowngrade]**](UpgradeDowngrade.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

