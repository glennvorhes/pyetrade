from pyetrade._responses._response_base import _convert, _fix_dict, _gen_class_stub
from unittest import TestCase

test_dict = {'quoteData': [
    {'dateTime': '12:14:22 EST 02-24-2010', 'product': {'exchange': 'Q', 'symbol': 'MSFT', 'type': 'EQ'},
     'all': {'bidTime': '12:14:22 EST 02-24-2010', 'lowAsk': 28.39, 'askExchange': 'NASDAQ National Market Sys (NMS)',
             'low52': 14.87, 'numTrades': 61376, 'daysToExpiration': 0, 'companyName': 'MICROSOFT CORP',
             'todayClose': 0, 'exDivDate': '11/17/2009', 'totalVolume': 22403011, 'upc': 0, 'high': 28.77,
             'chgClose': -0.3400000000000001, 'high52': 31.5, 'bid': 28.7, 'estEarnings': 1.811, 'open': 28.52,
             'lowBid': 28, 'highBid': 28.76, 'dividend': 0.13, 'optionUnderlier': '', 'prevClose': 28.73,
             'volume10Day': 56676460, 'ask': 28.71, 'low': 28.38, 'bidExchange': '', 'openInterest': 0,
             'highAsk': 28.77, 'askTime': '12:14:22 EST 02-24-2010', 'symbolDesc': 'MICROSOFT CORP',
             'exchgLastTrade': 'Pacific', 'chgClosePrcn': -15.11, 'eps': 1.81, 'lastTrade': 28.705,
             'annualDividend': 0.52, 'optionStyle': '', 'askSize': 15600, 'dirLast': 'U', 'primaryExchange': 'Q',
             'adjNonAdjFlag': False, 'bidSize': 15600, 'prevDayVolume': 75648887, 'fsi': 'N'}}]}


class TestResponse(TestCase):
    def test_convert(self):
        self.assertEqual(_convert('TestCase'), 'test_case')
        self.assertEqual(_convert('testCase'), 'test_case')
        self.assertEqual(_convert('testCase'), 'test_case')

    def test_fix_dict(self):
        return
        input_dict = {'One': 1, "TwoTwo": 'two', 'type': 1}

        other = _fix_dict(input_dict)

        self.assertTrue('two_two' in other)
        self.assertTrue('type_' in other)

        other = _fix_dict(test_dict)
        print(other)

    def test_gen_class(self):
        other = _fix_dict(test_dict)
        print(_gen_class_stub(other))
