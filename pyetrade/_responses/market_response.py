from ._response_base import ResponseBase as _ResponseBase
from ._response_base import _gen_class_stub


class LookupResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self._wrap_dict_in_list('product_list')
        self.product_list = [_ProductInfoLookup(**info) for info in self._inner_dict['product_list']]
        """
        :type: list of _ProductInfoLookup
        """


class _ProductInfo:
    def __init__(self, exchange=None, symbol=None, type_=None):
        self.exchange = exchange
        self.symbol = symbol
        self.type_ = type_


class _ProductInfoLookup(_ProductInfo):
    def __init__(self, exchange=None, symbol=None, security_type=None, company_name=None):
        super().__init__(exchange, symbol, security_type)
        self.company_name = company_name


class _FullQuote:
    def __init__(self, adj_non_adj_flag=None, annual_dividend=None, ask=None, ask_exchange=None, ask_size=None,
                 ask_time=None, bid=None, bid_exchange=None, bid_size=None, bid_time=None, chg_close=None,
                 chg_close_prcn=None, company_name=None, days_to_expiration=None, dir_last=None, dividend=None,
                 eps=None, est_earnings=None, ex_div_date=None, exchg_last_trade=None, fsi=None, high=None, high52=None,
                 high_ask=None, high_bid=None, last_trade=None, low=None, low52=None, low_ask=None, low_bid=None,
                 num_trades=None, open=None, open_interest=None, option_style=None, option_underlier=None,
                 prev_close=None, prev_day_volume=None, primary_exchange=None, symbol_desc=None, today_close=None,
                 total_volume=None, upc=None, volume10_day=None):
        self.adj_non_adj_flag = adj_non_adj_flag
        self.annual_dividend = annual_dividend
        self.ask = ask
        self.ask_exchange = ask_exchange
        self.ask_size = ask_size
        self.ask_time = ask_time
        self.bid = bid
        self.bid_exchange = bid_exchange
        self.bid_size = bid_size
        self.bid_time = bid_time
        self.chg_close = chg_close
        self.chg_close_prcn = chg_close_prcn
        self.company_name = company_name
        self.days_to_expiration = days_to_expiration
        self.dir_last = dir_last
        self.dividend = dividend
        self.eps = eps
        self.est_earnings = est_earnings
        self.ex_div_date = ex_div_date
        self.exchg_last_trade = exchg_last_trade
        self.fsi = fsi
        self.high = high
        self.high52 = high52
        self.high_ask = high_ask
        self.high_bid = high_bid
        self.last_trade = last_trade
        self.low = low
        self.low52 = low52
        self.low_ask = low_ask
        self.low_bid = low_bid
        self.num_trades = num_trades
        self.open = open
        self.open_interest = open_interest
        self.option_style = option_style
        self.option_underlier = option_underlier
        self.prev_close = prev_close
        self.prev_day_volume = prev_day_volume
        self.primary_exchange = primary_exchange
        self.symbol_desc = symbol_desc
        self.today_close = today_close
        self.total_volume = total_volume
        self.upc = upc
        self.volume10_day = volume10_day


class _QuoteData:
    def __init__(self, all_=None, date_time=None, product=None):
        self.all_ = _FullQuote(**all_)
        self.date_time = date_time
        self.product = _ProductInfo(**product)


class QuoteResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self._wrap_dict_in_list('quote_data')

        self.quotes = [_QuoteData(**q) for q in self._inner_dict['quote_data']]
        """
        :type: list of _QuoteData
        """


class _OptionProduct:
    def __init__(self, exchange_code=None, symbol=None, type_code=None):
        self.exchange_code = exchange_code
        self.symbol = symbol
        self.type_code = type_code


class _OptionExpireDate:
    def __init__(self, day=None, expiry_type=None, month=None, year=None):
        self.day = day
        self.expiry_type = expiry_type
        self.month = month
        self.year = year


class _Option:
    def __init__(self, expire_date=None, product=None, root_symbol=None, strike_price=None):
        expire_date = {} if expire_date is None else expire_date
        product = {} if product is None else product

        self.expire_date = _OptionExpireDate(**expire_date)
        self.product = _OptionProduct(**product)
        self.root_symbol = root_symbol
        self.strike_price = strike_price


class _OptionPairs:
    def __init__(self, call_count=None, pair_type=None, put=None, call=None, put_count=None):

        if call is None:
            call = []
        elif isinstance(call, dict):
            call = [call]

        if put is None:
            put = []
        elif isinstance(put, dict):
            put = [put]

        for p in put:
            try:
                del p['@xsi.type']
            except KeyError:
                pass

        for c in call:
            try:
                del c['@xsi.type']
            except KeyError:
                pass

        self.call_count = call_count
        self.pair_type = pair_type
        self.put = [_Option(**o) for o in put]
        self.call = [_Option(**o) for o in call]
        self.put_count = put_count


class OptionChainResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self._wrap_dict_in_list('option_pairs')
        self.option_pair_count = self._inner_dict['option_pair_count']
        self.symbol = self._inner_dict['symbol']
        self.option_pairs = [_OptionPairs(**pr) for pr in self._inner_dict['option_pairs']]
        """
        :type: list of _OptionPairs
        """


class OptionExpireResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self._wrap_dict_in_list('expire_dates')

        self.expire_dates = [_OptionExpireDate(**e) for e in self._inner_dict['expire_dates']]
        """
        :type: list of _OptionExpireDate
        """
