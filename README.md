# finnhub-python
- API documentation: https://finnhub.io/docs/api
- API version: 1.0.0
- Package version: 1.0.1

## Requirements.

Python 2.7 and 3.4+

## Installation

Install package
```sh
pip install finnhub-python
```

## Getting Started

```python
from __future__ import print_function

import time
import finnhub
from finnhub.rest import ApiException
from pprint import pprint

# Configure API key
configuration = finnhub.Configuration(
    api_key = {
        'token': 'YOUR_API_KEY'
    }
)

# Enter a context with an instance of the API client
with finnhub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finnhub.DefaultApi(api_client)
    symbol = 'AAPL' # str | symbol
    resolution = 'D' # str | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange.

    try:
        # Aggregate Indicators
        api_response = api_instance.aggregate_indicator(symbol, resolution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->aggregate_indicator: %s\n" % e)
    
```

## API Endpoints

All URIs are relative to *https://finnhub.io/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**aggregate_indicator**](docs/DefaultApi.md#aggregate_indicator) | **GET** /scan/technical-indicator | Aggregate Indicators
*DefaultApi* | [**company_earnings**](docs/DefaultApi.md#company_earnings) | **GET** /stock/earnings | Earnings Surprises
*DefaultApi* | [**company_eps_estimates**](docs/DefaultApi.md#company_eps_estimates) | **GET** /stock/eps-estimate | Earnings Estimates
*DefaultApi* | [**company_executive**](docs/DefaultApi.md#company_executive) | **GET** /stock/executive | Company Executive
*DefaultApi* | [**company_metrics**](docs/DefaultApi.md#company_metrics) | **GET** /stock/metric | Metrics
*DefaultApi* | [**company_news**](docs/DefaultApi.md#company_news) | **GET** /company-news | Company News
*DefaultApi* | [**company_peers**](docs/DefaultApi.md#company_peers) | **GET** /stock/peers | Peers
*DefaultApi* | [**company_profile**](docs/DefaultApi.md#company_profile) | **GET** /stock/profile | Company Profile
*DefaultApi* | [**company_profile2**](docs/DefaultApi.md#company_profile2) | **GET** /stock/profile2 | Company Profile 2
*DefaultApi* | [**company_revenue_estimates**](docs/DefaultApi.md#company_revenue_estimates) | **GET** /stock/revenue-estimate | Revenue Estimates
*DefaultApi* | [**covid19**](docs/DefaultApi.md#covid19) | **GET** /covid19/us | COVID-19
*DefaultApi* | [**crypto_candles**](docs/DefaultApi.md#crypto_candles) | **GET** /crypto/candle | Crypto Candles
*DefaultApi* | [**crypto_exchanges**](docs/DefaultApi.md#crypto_exchanges) | **GET** /crypto/exchange | Crypto Exchanges
*DefaultApi* | [**crypto_symbols**](docs/DefaultApi.md#crypto_symbols) | **GET** /crypto/symbol | Crypto Symbol
*DefaultApi* | [**earnings_calendar**](docs/DefaultApi.md#earnings_calendar) | **GET** /calendar/earnings | Earnings Calendar
*DefaultApi* | [**filings**](docs/DefaultApi.md#filings) | **GET** /stock/filings | Filings
*DefaultApi* | [**financials**](docs/DefaultApi.md#financials) | **GET** /stock/financials | Financial Statements
*DefaultApi* | [**financials_reported**](docs/DefaultApi.md#financials_reported) | **GET** /stock/financials-reported | Financials As Reported
*DefaultApi* | [**forex_candles**](docs/DefaultApi.md#forex_candles) | **GET** /forex/candle | Forex Candles
*DefaultApi* | [**forex_exchanges**](docs/DefaultApi.md#forex_exchanges) | **GET** /forex/exchange | Forex Exchanges
*DefaultApi* | [**forex_rates**](docs/DefaultApi.md#forex_rates) | **GET** /forex/rates | Forex rates
*DefaultApi* | [**forex_symbols**](docs/DefaultApi.md#forex_symbols) | **GET** /forex/symbol | Forex Symbol
*DefaultApi* | [**fund_ownership**](docs/DefaultApi.md#fund_ownership) | **GET** /stock/fund-ownership | Fund Ownership
*DefaultApi* | [**general_news**](docs/DefaultApi.md#general_news) | **GET** /news | General News
*DefaultApi* | [**investors_ownership**](docs/DefaultApi.md#investors_ownership) | **GET** /stock/investor-ownership | Investors Ownership
*DefaultApi* | [**ipo_calendar**](docs/DefaultApi.md#ipo_calendar) | **GET** /calendar/ipo | IPO Calendar
*DefaultApi* | [**major_developments**](docs/DefaultApi.md#major_developments) | **GET** /major-development | Major Developments
*DefaultApi* | [**news_sentiment**](docs/DefaultApi.md#news_sentiment) | **GET** /news-sentiment | News Sentiment
*DefaultApi* | [**pattern_recognition**](docs/DefaultApi.md#pattern_recognition) | **GET** /scan/pattern | Pattern Recognition
*DefaultApi* | [**price_target**](docs/DefaultApi.md#price_target) | **GET** /stock/price-target | Price Target
*DefaultApi* | [**quote**](docs/DefaultApi.md#quote) | **GET** /quote | Quote
*DefaultApi* | [**recommendation_trends**](docs/DefaultApi.md#recommendation_trends) | **GET** /stock/recommendation | Recommendation Trends
*DefaultApi* | [**stock_candles**](docs/DefaultApi.md#stock_candles) | **GET** /stock/candle | Stock Candles
*DefaultApi* | [**stock_dividends**](docs/DefaultApi.md#stock_dividends) | **GET** /stock/dividend | Dividends
*DefaultApi* | [**stock_splits**](docs/DefaultApi.md#stock_splits) | **GET** /stock/split | Splits
*DefaultApi* | [**stock_symbols**](docs/DefaultApi.md#stock_symbols) | **GET** /stock/symbol | Stock Symbol
*DefaultApi* | [**stock_tick**](docs/DefaultApi.md#stock_tick) | **GET** /stock/tick | Tick Data
*DefaultApi* | [**support_resistance**](docs/DefaultApi.md#support_resistance) | **GET** /scan/support-resistance | Support/Resistance
*DefaultApi* | [**technical_indicator**](docs/DefaultApi.md#technical_indicator) | **GET** /indicator | Technical Indicators
*DefaultApi* | [**transcripts**](docs/DefaultApi.md#transcripts) | **GET** /stock/transcripts | Earnings Call Transcripts
*DefaultApi* | [**transcripts_list**](docs/DefaultApi.md#transcripts_list) | **GET** /stock/transcripts/list | Earnings Call Transcripts List
*DefaultApi* | [**upgrade_downgrade**](docs/DefaultApi.md#upgrade_downgrade) | **GET** /stock/upgrade-downgrade | Stock Upgrade/Downgrade

## Models

 - [AggregateIndicators](docs/AggregateIndicators.md)
 - [COVID19](docs/COVID19.md)
 - [Company](docs/Company.md)
 - [CompanyExecutive](docs/CompanyExecutive.md)
 - [CompanyNewsStatistics](docs/CompanyNewsStatistics.md)
 - [CompanyProfile](docs/CompanyProfile.md)
 - [CompanyProfile2](docs/CompanyProfile2.md)
 - [CryptoCandles](docs/CryptoCandles.md)
 - [CryptoSymbol](docs/CryptoSymbol.md)
 - [Development](docs/Development.md)
 - [Dividends](docs/Dividends.md)
 - [EarningEstimate](docs/EarningEstimate.md)
 - [EarningRelease](docs/EarningRelease.md)
 - [EarningResult](docs/EarningResult.md)
 - [EarningsCallTranscripts](docs/EarningsCallTranscripts.md)
 - [EarningsCallTranscriptsList](docs/EarningsCallTranscriptsList.md)
 - [EarningsEstimates](docs/EarningsEstimates.md)
 - [Estimate](docs/Estimate.md)
 - [Filing](docs/Filing.md)
 - [FinancialStatements](docs/FinancialStatements.md)
 - [FinancialsAsReported](docs/FinancialsAsReported.md)
 - [ForexCandles](docs/ForexCandles.md)
 - [ForexSymbol](docs/ForexSymbol.md)
 - [Forexrates](docs/Forexrates.md)
 - [FundOwnership](docs/FundOwnership.md)
 - [IPOEvent](docs/IPOEvent.md)
 - [Indicator](docs/Indicator.md)
 - [Investor](docs/Investor.md)
 - [InvestorsOwnership](docs/InvestorsOwnership.md)
 - [MajorDevelopments](docs/MajorDevelopments.md)
 - [Metrics](docs/Metrics.md)
 - [News](docs/News.md)
 - [NewsSentiment](docs/NewsSentiment.md)
 - [PriceTarget](docs/PriceTarget.md)
 - [Quote](docs/Quote.md)
 - [RecommendationTrends](docs/RecommendationTrends.md)
 - [Report](docs/Report.md)
 - [RevenueEstimates](docs/RevenueEstimates.md)
 - [Sentiment](docs/Sentiment.md)
 - [Splits](docs/Splits.md)
 - [Stock](docs/Stock.md)
 - [StockCandles](docs/StockCandles.md)
 - [StockTranscripts](docs/StockTranscripts.md)
 - [TechnicalAnalysis](docs/TechnicalAnalysis.md)
 - [TechnicalIndicators](docs/TechnicalIndicators.md)
 - [TickData](docs/TickData.md)
 - [TranscriptContent](docs/TranscriptContent.md)
 - [TranscriptParticipant](docs/TranscriptParticipant.md)
 - [Trend](docs/Trend.md)
 - [UpgradeDowngrade](docs/UpgradeDowngrade.md)

## License

MIT License

Copyright (c) 2020 Finnhub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
