from enum import Enum

import requests as _requests

from ._auth import auth as _auth
from ._decorators import ProcessResult
from ._urls import market_urls as _market_urls
from ._responses import market_response
from ._error import EtradeError

__author__ = 'glenn'


class EnumSecurityType(Enum):
    EQUITY = 'EQ'
    MUTUAL_FUND = 'MF'


class EnumOptionChainType(Enum):
    CALL = "CALL"
    PUT = "PUT"
    CALLPUT = 'CALLPUT'


@ProcessResult(market_response.LookupResponse)
def lookup_product(lookup_str, security_type=EnumSecurityType.EQUITY):
    """
    Lookup a product by text

    :param lookup_str: lookup text
    :type lookup_str: str
    :param security_type: the security type
    :type security_type: EnumSecurityType
    :return: product response
    :rtype: market_response.LookupResponse|EtradeError
    """
    assert isinstance(lookup_str, str)
    assert isinstance(security_type, EnumSecurityType)
    params = dict(company=lookup_str.upper(), type=security_type.value)
    return _requests.get(_market_urls.market_lookup(params), auth=_auth.get_current)


@ProcessResult(market_response.QuoteResponse)
def get_quote(symbol_s):
    """
    Get quote data

    :param symbol_s: single symbol or a list of symbols
    :type symbol_s: str|list
    :return: the quote data
    :rtype: market_response.QuoteResponse|EtradeError
    """
    return _requests.get(_market_urls.market_quote(symbol_s), auth=_auth.get_current)


@ProcessResult(market_response.OptionChainResponse)
def get_option_chains(underlier, expiration_month, expiration_year,
                      chain_type=EnumOptionChainType.CALLPUT, skip_adjusted=True):
    """
    Get option chains

    :param underlier: underlier
    :type underlier: str
    :param expiration_month: expiration month
    :type expiration_month: int
    :param expiration_year: expiration year
    :type expiration_year: int
    :param chain_type: chain type
    :type chain_type: EnumOptionChainType
    :return: the option chains
    :param skip_adjusted:
    :type skip_adjusted: bool
    :rtype: market_response.OptionChainResponse|EtradeError
    """

    assert isinstance(underlier, str)
    assert isinstance(expiration_month, int)
    assert isinstance(expiration_year, int)
    assert isinstance(chain_type, EnumOptionChainType)
    params = dict(underlier=underlier.upper(), expirationMonth=expiration_month,
                  expirationYear=expiration_year, chainType=chain_type.value,
                  skipAdjusted=skip_adjusted)

    return _requests.get(_market_urls.market_option_chains(params), auth=_auth.get_current)


@ProcessResult(market_response.OptionExpireResponse)
def get_option_expire_dates(underlier):
    """
    Get option chain expire dates

    :param underlier: the underlier
    :type underlier: str
    :return: the option chain expired dates
    :rtype: market_response.OptionExpireResponse|EtradeError
    """
    assert isinstance(underlier, str)
    params = dict(underlier=underlier.upper())

    return _requests.get(_market_urls.market_option_expire_date(params), auth=_auth.get_current)
