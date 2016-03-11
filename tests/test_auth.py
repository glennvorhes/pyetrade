from unittest import TestCase
from pyetrade import etrade_config
from pyetrade._authorization import auth


class AuthTest(TestCase):

    def test_get_auth(self):

        etrade_config.init_props(sandbox=True, browser='phantomjs')

        print(auth.get_current)



