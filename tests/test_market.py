from unittest import TestCase
from pyetrade import market
from pyetrade import etrade_config
from pyetrade._responses.market_response import QuoteResponse


class TestMarket(TestCase):

    def setUp(self):
        etrade_config.init_props(sandbox=True)
        pass

    def test_quote(self):
        return

        one_quote = market.get_quote('GOOG')
        two_quote = market.get_quote('GOOG,MSFT')
        print(two_quote.quotes)
        pass

    def test_lookup(self):
        return
        stuff = market.lookup_product('Google')
        print(stuff.product_list[0].company_name)

    def test_option_chain(self):
        return

        chn = market.get_option_chains('GOOG', 5, 2016, market.EnumOptionChainType.CALLPUT)

        print(chn.option_pair_count)

        print(chn.option_pairs[0].put)
        print(chn.option_pairs[0].call)

    def test_option_expire(self):
        exp = market.get_option_expire_dates('GOOG')
        # print(exp.expire_dates[0].expiry_type)


# from unittest import TestCase
# from etrade import market
# import json
#
# __author__ = 'glenn'
#
#
# class TestMarket(TestCase):
#     def test_market(self):
#         # print(market.lookup_product('Google'))
#         data = market.get_quote(['oibr','ec','cat','zazaza'])
#         print(json.dumps(data, sort_keys=True, indent=4))
#         # print(market.get_quote(['goog','msft','aapl']))
#         # print(market.get_option_chains('goog', 5, 2015))
#         # print(market.get_option_expire_dates('goog'))


