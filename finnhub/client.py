import json
import requests

from finnhub.exceptions import FinnhubAPIException
from finnhub.exceptions import FinnhubRequestException


class Client:
    API_URL = "https://finnhub.io/api/v1"
    DEFAULT_TIMEOUT = 10

    def __init__(self, api_key, proxies):
        self._session = self._init_session(api_key, proxies)

    @staticmethod
    def _init_session(api_key, proxies):
        session = requests.session()
        session.headers.update({"Accept": "application/json",
                                "User-Agent": "finnhub/python"})
        session.proxies = proxies
        session.params["token"] = api_key

        return session

    def close(self):
        self._session.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def _request(self, method, path, **kwargs):
        uri = "{}/{}".format(self.API_URL, path)
        kwargs["timeout"] = kwargs.get("timeout", self.DEFAULT_TIMEOUT)
        kwargs["params"] = self._format_params(kwargs.get("params", {}))

        response = getattr(self._session, method)(uri, **kwargs)
        return self._handle_response(response)

    @staticmethod
    def _handle_response(response):
        if not response.ok:
            raise FinnhubAPIException(response)

        try:
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            if 'text/csv' in content_type:
                return response.text
            if 'text/plain' in content_type:
                return response.text
            raise FinnhubRequestException("Invalid Response: {}".format(response.text))
        except ValueError:
            raise FinnhubRequestException("Invalid Response: {}".format(response.text))

    @staticmethod
    def _merge_two_dicts(first, second):
        result = first.copy()
        result.update(second)
        return result

    @staticmethod
    def _format_params(params):
        return {k: json.dumps(v) if isinstance(v, bool) else v for k, v in params.items()}

    def _get(self, path, **kwargs):
        return self._request("get", path, **kwargs)

    @property
    def api_key(self):
        return self._session.params.get("token")

    @api_key.setter
    def api_key(self, token):
        self._session.params["token"] = token

    def covid19(self):
        return self._get("/covid19/us")

    def company_profile(self, **params):
        return self._get("/stock/profile", params=params)

    def company_profile2(self, **params):
        return self._get("/stock/profile2", params=params)

    def aggregate_indicator(self, symbol, resolution):
        return self._get("/scan/technical-indicator", params={
            "symbol": symbol,
            "resolution": resolution,
        })

    def crypto_exchanges(self):
        return self._get("/crypto/exchange")

    def forex_exchanges(self):
        return self._get("/forex/exchange")

    def press_releases(self, symbol, _from=None, to=None):
        return self._get("/press-releases", params={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def company_executive(self, symbol):
        return self._get("/stock/executive", params={"symbol": symbol})

    def stock_dividends(self, symbol, _from=None, to=None):
        return self._get("/stock/dividend", params={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def stock_symbols(self, exchange):
        return self._get("/stock/symbol", params={"exchange": exchange})

    def recommendation_trends(self, symbol):
        return self._get("/stock/recommendation", params={"symbol": symbol})

    def price_target(self, symbol):
        return self._get("/stock/price-target", params={"symbol": symbol})

    def upgrade_downgrade(self, **params):
        return self._get("/stock/upgrade-downgrade", params=params)

    def option_chain(self, **params):
        return self._get("/stock/option-chain", params=params)

    def company_peers(self, symbol):
        return self._get("/stock/peers", params={"symbol": symbol})

    def company_basic_financials(self, symbol, metric):
        return self._get("/stock/metric", params={
            "symbol": symbol,
            "metric": metric
        })

    def financials(self, symbol, statement, freq):
        return self._get("/stock/financials", params={
            "symbol": symbol,
            "statement": statement,
            "freq": freq
        })

    def financials_reported(self, **params):
        return self._get("/stock/financials-reported", params=params)

    def fund_ownership(self, symbol, limit=None):
        return self._get("/stock/fund-ownership", params={
            "symbol": symbol,
            "limit": limit
        })

    def company_earnings(self, symbol, limit=None):
        return self._get("/stock/earnings", params={
            "symbol": symbol,
            "limit": limit
        })

    def company_revenue_estimates(self, symbol, freq=None):
        return self._get("/stock/revenue-estimate", params={
            "symbol": symbol,
            "freq": freq
        })

    def company_eps_estimates(self, symbol, freq=None):
        return self._get("/stock/eps-estimate", params={
            "symbol": symbol,
            "freq": freq
        })

    def exchange(self):
        return self._get("/stock/exchange")

    def filings(self, **params):
        return self._get("/stock/filings", params=params)

    def stock_symbol(self, **params):
        return self._get("/stock/symbol", params=params)

    def quote(self, symbol):
        return self._get("/quote", params={
            "symbol": symbol
        })

    def transcripts(self, _id):
        return self._get("/stock/transcripts", params={"id": _id})

    def transcripts_list(self, symbol):
        return self._get("/stock/transcripts/list", params={"symbol": symbol})

    def sim_index(self, **params):
        return self._get("/stock/similarity-index", params=params)

    def stock_candles(self, symbol, resolution, _from, to, **kwargs):
        params = self._merge_two_dicts({
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to
        }, kwargs)

        return self._get("/stock/candle", params=params)

    def stock_tick(self, symbol, date, limit, skip, _format='json', **kwargs):
        params = self._merge_two_dicts({
            "symbol": symbol,
            "date": date,
            "limit": limit,
            "skip": skip,
            "format": _format
        }, kwargs)

        return self._get("/stock/tick", params=params)

    def forex_rates(self, **params):
        return self._get("/forex/rates", params=params)

    def forex_symbols(self, exchange):
        return self._get("/forex/symbol", params={
            "exchange": exchange
        })

    def forex_candles(self, symbol, resolution, _from, to, _format='json'):
        return self._get("/forex/candle", params={
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to,
            "format": _format
        })

    def crypto_symbols(self, exchange):
        return self._get("/crypto/symbol", params={"exchange": exchange})

    def crypto_candles(self, symbol, resolution, _from, to, _format='json'):
        return self._get("/crypto/candle", params={
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to,
            "format": _format
        })

    def pattern_recognition(self, symbol, resolution):
        return self._get("/scan/pattern", params={
            "symbol": symbol,
            "resolution": resolution
        })

    def support_resistance(self, symbol, resolution):
        return self._get("/scan/support-resistance", params={
            "symbol": symbol,
            "resolution": resolution
        })

    def technical_indicator(self, symbol, resolution, _from, to, indicator, indicator_fields=None):
        indicator_fields = indicator_fields or {}
        params = self._merge_two_dicts({
            "symbol": symbol,
            "resolution": resolution,
            "from": _from,
            "to": to,
            "indicator": indicator
        }, indicator_fields)

        return self._get("/indicator", params=params)

    def stock_splits(self, symbol, _from, to):
        return self._get("/stock/split", params={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def general_news(self, category, min_id=0):
        return self._get("/news", params={
            "category": category,
            "minId": min_id
        })

    def company_news(self, symbol, _from, to):
        return self._get("/company-news", params={
            "symbol": symbol,
            "from": _from,
            "to": to
        })

    def news_sentiment(self, symbol):
        return self._get("/news-sentiment", params={
            "symbol": symbol
        })

    def ownership(self, symbol, limit=None):
        return self._get("/stock/ownership", params={
            "symbol": symbol,
            "limit": limit
        })

    def country(self):
        return self._get("/country")

    def merger_country(self):
        return self._get("/merger/country")

    def merger(self, **params):
        return self._get("/merger", params=params)

    def economic_code(self):
        return self._get("/economic/code")

    def economic_data(self, code):
        return self._get("/economic", params={"code": code})

    def calendar_economic(self):
        return self._get("/calendar/economic")

    def earnings_calendar(self, **params):
        return self._get("/calendar/earnings", params=params)

    def ipo_calendar(self, _from, to):
        return self._get("/calendar/ipo", params={
            "from": _from,
            "to": to
        })

    def indices_const(self, **params):
        return self._get("/index/constituents", params=params)

    def indices_hist_const(self, **params):
        return self._get("/index/historical-constituents", params=params)

    def etfs_profile(self, symbol):
        return self._get("/etf/profile", params={"symbol": symbol})

    def etfs_holdings(self, symbol):
        return self._get("/etf/holdings", params={"symbol": symbol})

    def etfs_ind_exp(self, symbol):
        return self._get("/etf/holdings", params={"symbol": symbol})

    def etfs_country_exp(self, symbol):
        return self._get("/etf/country", params={"symbol": symbol})

    def international_filings(self, symbol="", country=""):
        return self._get("/stock/international-filings", params={"symbol": symbol, "country": country})

    def sec_sentiment_analysis(self, access_number):
        return self._get("/stock/filings-sentiment", params={"accessNumber": access_number})

    def sec_similarity_index(self, symbol="", cik="", freq="annual"):
        return self._get("/stock/similarity-index", params={"symbol": symbol, "cik": cik, "freq": freq})

    def last_bid_ask(self, symbol):
        return self._get("/stock/bidask", params={"symbol": symbol})

    def fda_calendar(self):
        return self._get("/fda-advisory-committee-calendar")

    def symbol_lookup(self, query):
        return self._get("/search", params={"q": query})
