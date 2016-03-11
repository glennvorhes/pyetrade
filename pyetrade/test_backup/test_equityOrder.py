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
