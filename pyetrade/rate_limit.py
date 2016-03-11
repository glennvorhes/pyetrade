from enum import Enum

import requests

from ._authorization import auth
from ._decorators import ProcessResult
from . import etrade_config
from ._responses.rate_limit_response import RateLimitResponse
from ._urls import rate_limit_urls

__author__ = 'glenn'


class EnumRateLimitModule(Enum):
    ACCOUNTS = 'ACCOUNTS'
    MARKET = 'MARKET'
    ORDER = 'ORDER'


# TODO fix reference to oauth consumer key
@ProcessResult(RateLimitResponse)
def get_rate_limit(rate_limit_module):
    """
    Get rate/usage limit

    :param rate_limit_module: the domain to check the limit
    :type rate_limit_module: EnumRateLimitModule
    :return: the response
    :rtype: RateLimitResponse|EtradeError
    """
    assert isinstance(rate_limit_module, EnumRateLimitModule)

    params = dict(
        oauth_consumer_key=etrade_config.oauth_consumer_key,
        oauth_token=auth.get_current.client.resource_owner_key,
        module=rate_limit_module.value
    )

    return requests.get(rate_limit_urls.rate_limit(params), auth=auth.get_current)
