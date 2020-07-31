import requests
import json

from finnhub.exceptions import FinnhubAPIException
from finnhub.exceptions import FinnhubRequestException

class Client:
    API_URL = "https://finnhub.io/api/v1"

    def __init__(self, api_key, requests_params=None):
        self.api_key = api_key
        self.session = self._init__session()
        self._requests_params = requests_params

    def _init__session(self):
        session = requests.session()
        session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'finnhub/python'})
        return session

    def _request(self, method, uri, **kwargs):
        kwargs['timeout'] = 10
        data = kwargs.get('data', None)

        if data and isinstance(data, dict):
            kwargs['data'] = data
        else:
            kwargs['data'] = {}

        kwargs['data']['token'] = self.api_key
        kwargs['params'] = kwargs['data']

        del(kwargs['data'])
        response = getattr(self.session, method)(uri, **kwargs)

        return self._handle_response(response)

    def _create_api_uri(self, path):
        return "{}/{}".format(self.API_URL, path)

    def _request_api(self, method, path, **kwargs):
        uri = self._create_api_uri(path)
        return self._request(method, uri, **kwargs)

    def _handle_response(self, response):
        if not str(response.status_code).startswith('2'):
            raise FinnhubAPIException(response)
        try:
            return response.json()
        except ValueError:
            raise FinnhubRequestException("Invalid Response: {}".format(response.text))

    def _merge_two_dicts(self, a, b):
        result = a.copy()
        result.update(b)
        return result

    def _str_to_bool(self, **kwargs):
        for i in kwargs:
            if (kwargs[i] == True): kwargs[i] = "true"
            elif (kwargs[i] == False): kwargs[i] = "false"
        return kwargs

    def _get(self, path, **kwargs):
        params = self._str_to_bool(**kwargs)
        return self._request_api('get', path, **params)

    def covid19(self):
        return self._get("/covid19/us")

    def company_profile(self, **params):
        return self._get("/stock/profile", data=params)

    def company_profile2(self, **params):
        return self._get("/stock/profile2", data=params)

    def aggregate_indicator(self, symbol, resolution):
        return self._get("/scan/technical-indicator", data={
            "symbol": symbol,
            "resolution": resolution,
        })

    def crypto_exchanges(self):
        return self._get("/crypto/exchange")

    def forex_exchanges(self):
        return self._get("/forex/exchange")

    def major_developments(self, symbol, _from=None, to=None):
        return self._get("/major-development", data={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def company_executive(self, symbol):
        return self._get("/stock/executive", data={
            "symbol": symbol
        })

    def stock_dividends(self, symbol, _from = None, to = None):
        return self._get("/stock/dividend", data={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def stock_symbols(self, exchange):
        return self._get("/stock/symbol", data = {
            "exchange": exchange
        })

    def recommendation_trends(self, symbol):
        return self._get("/stock/recommendation", data={
            "symbol": symbol
        })

    def price_target(self, symbol):
        return self._get("/stock/price-target", data={
            "symbol": symbol
        })

    def upgrade_downgrade(self, **params):
        return self._get("/stock/upgrade-downgrade", data=params)

    def option_chain(self, **params):
        return self._get("/stock/option-chain", data=params)

    def company_peers(self, symbol):
        return self._get("/stock/peers", data={
            "symbol": symbol
        })
    
    def company_basic_financials(self, symbol, metric):
        return self._get("/stock/metric", data={
            "symbol": symbol,
            "metric": metric
        })
    
    def financials(self, symbol, statement, freq):
        return self._get("/stock/financials", data ={
            "symbol": symbol,
            "statement": statement,
            "freq": freq
        })
    
    def financials_reported(self, **params):
        return self._get("/stock/financials-reported", data=params)

    def fund_ownership(self, symbol, limit=None):
        return self._get("/stock/fund-ownership", data={
            "symbol": symbol,
            "limit": limit
        })

    def company_earnings(self, symbol, limit=None):
        return self._get("/stock/earnings", data={
            "symbol": symbol,
            "limit": limit
        })

    def company_revenue_estimates(self, symbol, freq=None):
        return self._get("/stock/revenue-estimate", data = {
            "symbol": symbol,
            "freq": freq
        })

    def company_eps_estimates(self, symbol, freq=None):
        return self._get("/stock/eps-estimate", data = {
            "symbol": symbol,
            "freq": freq
        })

    def exchange(self):
        return self._get("/stock/exchange")
    
    def filings(self, **params):
        return self._get("/stock/filings", data=params)

    def stock_symbol(self, **params):
        return self._get("/stock/symbol", data=params)

    def quote(self, symbol):
        return self._get("/quote", data={
            "symbol": symbol
        })

    def transcripts(self, id):
        return self._get("/stock/transcripts", data={
            "id": id
        })
    
    def transcripts_list(self, symbol):
        return self._get("/stock/transcripts/list", data={
            "symbol": symbol
        })
    
    def sim_index(self, **params):
        return self._get("/stock/similarity-index", data = params)

    def stock_candles(self, symbol, resolution, _from, to, **kwargs):
        data = self._merge_two_dicts({
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to
        }, kwargs)

        return self._get("/stock/candle", data=data)

    def stock_tick(self, symbol, date, limit, skip, **kwargs):
        data = self._merge_two_dicts({
            "symbol": symbol,
            "date": date,
            "limit": limit,
            "skip": skip,
            "format": format
        }, kwargs)

        return self._get("/stock/tick", data=data)

    def forex_rates(self, **params):
        return self._get("/forex/rates", data=params)

    def forex_symbols(self, exchange):
        return self._get("/forex/symbol", data={
            "exchange": exchange
        })

    def forex_candles(self, symbol, resolution, _from, to, format=None):
        return self._get("/forex/candle", data={
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to,
            "format": format
        })

    def crypto_symbols(self, exchange):
        return self._get("/crypto/symbol", data={
            "exchange": exchange
        })

    def crypto_candles(self, symbol, resolution, _from, to, format=None):
        return self._get("/crypto/candle", data={
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to,
            "format": format
        })

    def pattern_recognition(self, symbol, resolution):
        return self._get("/scan/pattern", data={
            "symbol": symbol,
            "resolution": resolution
        })

    def support_resistance(self, symbol, resolution):
        return self._get("/scan/support-resistance", data={
            "symbol": symbol,
            "resolution": resolution
        })

    def technical_indicator(self, symbol, resolution, _from, to, indicator, indicator_fields = {}):
        data = self._merge_two_dicts({
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to,
            "indicator": indicator
        }, indicator_fields)

        return self._get("/indicator", data=data)

    def stock_splits(self, symbol, _from, to):
        return self._get("/stock/split", data={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def general_news(self, category, min_id=None):
        return self._get("/news", data={
            "category": category,
            "minId": min_id
        })

    def company_news(self, symbol, _from, to):
        return self._get("/company-news", data={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def news_sentiment(self, symbol):
        return self._get("/news-sentiment", data={
            "symbol": symbol
        })

    def investors_ownership(self, symbol, limit=None):
        return self._get("/stock/investor-ownership", data = {
            "symbol": symbol,
            "limit": limit
        })

    def country(self):
        return self._get("/country")

    def merger_country(self):
        return self._get("/merger/country")

    def merger(self, **params):
        return self._get("/merger", data=params)

    def economic_code(self):
        return self._get("/economic/code")

    def economic_data(self, code):
        return self._get("/economic", data={"code": code})

    def calendar_economic(self):
        return self._get("/calendar/economic")

    def earnings_calendar(self, **params):
        return self._get("/calendar/earnings", data=params)

    def ipo_calendar(self, _from, to):
        return self._get("/calendar/ipo", data = {
            "from": _from,
            "to": to 
        })

    def calendar_ico(self):
        return self._get("/calendar/ico")

    def indices_const(self, **params):
        return self._get("/index/constituents", data = params)
    
    def indices_hist_const(self, **params):
        return self._get("/index/historical-constituents", data = params)

    def etfs_profile(self, symbol):
        return self._get("/etf/profile", data = {"symbol":symbol})

    def etfs_holdings(self, symbol):
        return self._get("/etf/holdings", data = {"symbol":symbol})

    def etfs_ind_exp(self, symbol):
        return self._get("/etf/holdings", data = {"symbol":symbol})

    def etfs_country_exp(self, symbol):
        return self._get("/etf/country", data = {"symbol": symbol})
        
        