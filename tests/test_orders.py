from unittest import TestCase

from pyetrade import orders
from pyetrade import etrade_config
import os
from pyetrade._error import EtradeError

__author__ = 'glenn'


class TestOrders(TestCase):

    def setUp(self):

        sandbox = True
        if sandbox:
            etrade_config.init_props(sandbox=True)
            self.account_num = 83405188
            self.order_id = 208
        else:
            self.account_num = None if 'ETRADE_ACCOUNT' not in os.environ else int(os.environ["ETRADE_ACCOUNT"])
            self.order_id = 208

    def test_orders(self):
        if self.account_num:
            order = orders.list_orders(35643476)

            if isinstance(ord, EtradeError):
                print('** ERROR **')
                print(order.msg)
            else:
                print(order.count)
                print(order.group_orders)
                print(order.orders)

    def test_cancel(self):
        cancel_response = orders.cancel_order(self.account_num, self.order_id)
        # print(cancel_response)
        if isinstance(cancel_response, EtradeError):
            print('##error##')
            print(cancel_response.msg)
        else:
            print(cancel_response.result_message)

            # print(ord)
            # print(ord.msg)
            # print(ord.error_type)
            # print(ord.count)
#
#         # equity_order_props = EquityOrderProps(83405188, 10, 'goog', EquityOrderAction.BUY)
#         # print('preview1', equity_order_props.previewId)
#         # print(order.equity_order_preview(equity_order_props))
#         # print('preview1', equity_order_props.previewId)
#         # print(order.equity_order_place(equity_order_props))
#
#         # change_props = EquityOrderChangeProps(83405188, 10, 14)
#         # print('preview1', change_props.previewId)
#         # print(order.equity_change_preview(change_props))
#         # print('preview1', change_props.previewId)
#         # print(order.equity_change_place(change_props))
#
#
#         # option_props = OptionOrderProps(83405188, 10,'goog', OptionOrderAction.BUY_OPEN, 500, CallOrPut.CALL, 450, 2015, 1, 30)
#         #
#         # print('preview1', option_props.previewId)
#         # print(order.option_order_preview(option_props))
#         # print('preview1', option_props.previewId)
#         # print(order.option_order_place(option_props))
#
#         # option_change_props = OptionOrderChangeProps(83405188, 10, 78)
#         #
#         # print('preview1', option_change_props.previewId)
#         # print(order.option_change_preview(option_change_props))
#         # print('preview1', option_change_props.previewId)
#         # print(order.option_change_place(option_change_props))
#
#         print(order.cancel_order


# from unittest import TestCase
#
# # from etrade.order import EquityOrderChangeProps, OrderAction, EquityOrderProps
# from etrade import order
#
# __author__ = 'glenn'
#
#
# class TestEquityOrder(TestCase):
#     # def test_buy_process(self):
#     # equity_order = order.EquityOrderProps(
#     #         83405188,
#     #         300,
#     #         'Goog',
#     #         order.OrderAction.BUY,
#     #         all_or_none=True,
#     #         price_type=order.PriceType.LIMIT,
#     #         limit_price=4)
#     #
#     #     print(equity_order.get_prop_dict())
#     #     print(order.equity_order_preview(equity_order))
#     #     print(equity_order.get_prop_dict())
#     #     print(order.equity_order_place(equity_order))
#
#
#     # def test_change_process(self):
#     #     change_order = order.EquityOrderChangeProps(83405188, 4, 262)
#     #     print(order.equity_change_preview(change_order))
#     #     print(change_order.get_prop_dict())
#     #     print(order.equity_change_place(change_order))
#
#     def test_option(self):
#
#
#         order_props = order.OptionOrderProps(83405188, 3, 'goog', order.OptionOrderAction.BUY_CLOSE, 4,
#                                          order.CallOrPut.CALL, 4, 2014, 12, 3)
#         print(order.option_order_preview(order_props))
#         print(order.option_order_place(order_props))
#
#         order_change_props = order.OptionOrderChangeProps(83405188, 4, 262)
#         print(order_change_props.get_prop_dict())
#         print(order.option_change_preview(order_change_props))
#         print(order_change_props.get_prop_dict())
#         print(order_change_props.previewId)
#         print(order.option_change_place(order_change_props))
#
#
#
#         print('here')
#
#
#
#
#

