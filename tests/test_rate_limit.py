from unittest import TestCase
from datetime import date
from pyetrade import etrade_config

from pyetrade import rate_limit

__author__ = 'glenn'

class TestRateLimit(TestCase):
    def setUp(self):
        etrade_config.init_props(sandbox=True, browser='phantomjs')

    def test_rate_limit(self):
        lim = rate_limit.get_rate_limit(rate_limit.EnumRateLimitModule.ACCOUNTS)
