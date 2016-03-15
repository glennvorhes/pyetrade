from enum import Enum

import requests

from ._auth import auth
from ._decorators import ProcessResult
from ._urls import order_urls
from ._responses import order_response
from ._error import EtradeError

__author__ = 'glenn'


class EnumOrderTerm(Enum):
    GOOD_UNTIL_CANCEL = 'GOOD_UNTIL_CANCEL'
    GOOD_FOR_DAY = 'GOOD_FOR_DAY'
    IMMEDIATE_OR_CANCEL = 'IMMEDIATE_OR_CANCEL'
    FILL_OR_KILL = 'FILL_OR_KILL'


class EnumEquityOrderAction(Enum):
    BUY = 'BUY'
    SELL = 'SELL'
    BUY_TO_COVER = 'BUY_TO_COVER'
    SELL_SHORT = 'SELL_SHORT'


class EnumOptionOrderAction(Enum):
    BUY_OPEN = 'BUY_OPEN'
    SELL_OPEN = 'SELL_OPEN'
    BUY_CLOSE = 'BUY_CLOSE'
    SELL_CLOSE = 'SELL_CLOSE'


class EnumOptionPriceType(Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'
    STOP = 'STOP'
    STOP_LIMIT = 'STOP_LIMIT'


class EnumEquityPriceType(Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'
    STOP = 'STOP'
    STOP_LIMIT = 'STOP_LIMIT'
    MARKET_ON_CLOSE = 'MARKET_ON_CLOSE'


class EnumRoutingDestination(Enum):
    AUTO = 'AUTO'
    ARCA = 'ARCA'
    NSDQ = 'NSDQ'
    NYSE = 'NYSE'


class EnumMarketSession(Enum):
    REGULAR = 'REGULAR'
    EXTENDED = 'EXTENDED'


class EnumCallOrPut(Enum):
    CALL = 'CALL'
    PUT = "PUT"


@ProcessResult(order_response.OrderListResponse)
def list_orders(account_id):
    """
    list orders

    :param account_id: account id
    :type account_id: int
    :return: the order list response
    :rtype: order_response.OrderListResponse|EtradeError
    """
    assert isinstance(account_id, int)
    return requests.get(order_urls.orders_list(account_id), auth=auth.get_current)


@ProcessResult(order_response.OrderCancelResponse)
def cancel_order(account_id, order_id):
    """
    Cancel order

    :param account_id: account id
    :type account_id: int
    :param order_id: order id
    :type order_id: int
    :return: the cancel response
    :rtype: order_response.OrderCancelResponse|EtradeError
    """
    data = {
        "cancelOrder": {
            "-xmlns": "http://order.etws.etrade.com",
            "cancelOrderRequest": {
                "accountId": account_id,
                "orderNum": order_id
            }
        }
    }

    return requests.post(order_urls.orders_cancel(), json=data, auth=auth.get_current)


#
# @ProcessResult('previewEquityOrderResponse', add_preview_id=True)
# def equity_order_preview(equity_order_props):
#     """
#     Preview equity order
#
#     :param equity_order_props: the equity order properties
#     :type equity_order_props: EquityOrderProps
#     :return: equity preview response
#     :rtype: Response
#     """
#     assert isinstance(equity_order_props, EquityOrderProps)
#     data = {
#         "PreviewEquityOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "EquityOrderRequest": equity_order_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_equity_preview, json=data, auth=auth.current)
#
#
# @ProcessResult('placeEquityOrderResponse')
# def equity_order_place(equity_order_props):
#     """
#     Place Equity Order
#
#     :param equity_order_props: equity order properties
#     :type equity_order_props: EquityOrderProps
#     :return: place order response
#     :rtype: Response
#     """
#     assert isinstance(equity_order_props, EquityOrderProps)
#
#     data = {
#         "PlaceEquityOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "EquityOrderRequest": equity_order_props.get_prop_dict()
#         }
#     }
#     return requests.post(order_urls.orders_equity_place, json=data, auth=auth.current)
#
#
# @ProcessResult('previewChangeEquityOrderResponse', add_preview_id=True)
# def equity_change_preview(equity_order_change_props):
#     """
#     Change equity order preview
#
#     :param equity_order_change_props: change equity order properties
#     :type equity_order_change_props: EquityOrderChangeProps
#     :return: the change preview response
#     :rtype: Response
#     """
#
#     assert isinstance(equity_order_change_props, EquityOrderChangeProps)
#
#     data = {
#         "previewChangeEquityOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "changeEquityOrderRequest": equity_order_change_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_equity_change_preview, json=data, auth=auth.current)
#
#
# @ProcessResult('placeChangeEquityOrderResponse')
# def equity_change_place(equity_order_change_props):
#     """
#     Place equity order change
#
#     :param equity_order_change_props:
#     :type equity_order_change_props: EquityOrderChangeProps
#     :return: the change response
#     :rtype: Response
#     """
#     assert isinstance(equity_order_change_props, EquityOrderChangeProps)
#     data = {
#         "placeChangeEquityOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "changeEquityOrderRequest": equity_order_change_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_equity_change_place, json=data, auth=auth.current)
#
#
# @ProcessResult('previewOptionOrderResponse', add_preview_id=True)
# def option_order_preview(option_order_props):
#     """
#     Preview option order
#
#     :param option_order_props: the option order properties
#     :type option_order_props: OptionOrderProps
#     :return: the option order preview response
#     :rtype: Response
#     """
#     assert isinstance(option_order_props, OptionOrderProps)
#
#     data = {
#         "PreviewOptionOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "OptionOrderRequest": option_order_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_option_preview, json=data, auth=auth.current)
#
#
# @ProcessResult('placeOptionOrderResponse')
# def option_order_place(option_order_props):
#     """
#     Place option order
#
#     :param option_order_props: the option order properties
#     :type option_order_props: OptionOrderProps
#     :return: the option order place response
#     :rtype: Response
#     """
#     assert isinstance(option_order_props, OptionOrderProps)
#
#     data = {
#         "PlaceOptionOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "OptionOrderRequest": option_order_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_option_place, json=data, auth=auth.current)
#
#
# @ProcessResult('previewChangeOptionOrderResponse', add_preview_id=True)
# def option_change_preview(option_change_props):
#     """
#     Option order change preview
#
#     :param option_change_props: the option order change properties
#     :type option_change_props: OptionOrderChangeProps
#     :return: the option order change preview response
#     :rtype: Response
#     """
#     assert isinstance(option_change_props, OptionOrderChangeProps)
#     data = {
#         "previewChangeOptionOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "changeOptionOrderRequest": option_change_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_option_change_preview, json=data, auth=auth.current)
#
#
# @ProcessResult('placeChangeOptionOrderResponse')
# def option_change_place(option_change_props):
#     """
#     Option order change place
#
#     :param option_change_props: the option order change properties
#     :type option_change_props: OptionOrderChangeProps
#     :return: the option order change place response
#     :rtype: Response
#     """
#     assert isinstance(option_change_props, OptionOrderChangeProps)
#
#     data = {
#         "placeChangeOptionOrder": {
#             "-xmlns": "http://order.etws.etrade.com",
#             "changeOptionOrderRequest": option_change_props.get_prop_dict()
#         }
#     }
#
#     return requests.post(order_urls.orders_option_change_place, json=data, auth=auth.current)
