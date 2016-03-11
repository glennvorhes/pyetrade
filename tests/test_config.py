from unittest import TestCase
from pyetrade import etrade_config


class ConfigTest(TestCase):

    def test_config(self):

        self.assertIsInstance(etrade_config.sandbox, bool)
        #
        # etrade_config.sandbox = True
        # print(etrade_config.consumer_key)
        # etrade_config.sandbox = False
        # print(etrade_config.consumer_key)

