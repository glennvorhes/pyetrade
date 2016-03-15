from ._response_base import ResponseBase as _ResponseBase
import json


class _SymbolInfo:
    def __init__(self, call_put=None, exp_day=None, exp_month=None, exp_year=None, strike_price=None, symbol=None):
        self.call_put = call_put
        self.exp_month = exp_month
        self.symbol = symbol
        self.strike_price = strike_price
        self.exp_year = exp_year
        self.exp_day = exp_day


class _LegDetails:
    def __init__(self, estimated_commission=None, estimated_fees=None, executed_price=None, filled_quantity=None,
                 leg_number=None, order_action=None, ordered_quantity=None, reserve_quantity=None,
                 symbol_description=None, symbol_info=None):
        self.estimated_commission = estimated_commission
        self.estimated_fees = estimated_fees
        self.executed_price = executed_price
        self.filled_quantity = filled_quantity
        self.leg_number = leg_number
        self.order_action = order_action
        self.ordered_quantity = ordered_quantity
        self.reserve_quantity = reserve_quantity
        self.symbol_description = symbol_description
        self.symbol_info = _SymbolInfo(**symbol_info)


class Order:
    def __init__(self, all_or_none=None, bracket_limit_price=None, initial_stop_price=None, leg_details=None,
                 limit_price=None, order_executed_time=None, order_id=None,
                 order_placed_time=None, order_status=None, order_term=None, order_type=None, order_value=None,
                 price_type=None, replaced_by_order_id=None, replaces_order_id=None, routing_destination=None,
                 stop_price=None, trail_price=None, trigger_price=None):
        self.all_or_none = all_or_none
        self.bracket_limit_price = bracket_limit_price
        self.initial_stop_price = initial_stop_price
        if isinstance(leg_details, dict):
            leg_details = [leg_details]
        self.leg_details = [_LegDetails(**l) for l in leg_details]
        self.limit_price = limit_price
        self.order_executed_time = order_executed_time
        self.order_id = order_id
        self.order_placed_time = order_placed_time
        self.order_status = order_status
        self.order_term = order_term
        self.order_type = order_type
        self.order_value = order_value
        self.price_type = price_type
        self.replaced_by_order_id = replaced_by_order_id
        self.replaces_order_id = replaces_order_id
        self.routing_destination = routing_destination
        self.stop_price = stop_price
        self.trail_price = trail_price
        self.trigger_price = trigger_price


class _GroupOrder:
    def __init__(self, cumulative_estimated_commission=None, cumulative_estimated_fees=None, group_order_id=None,
                 group_order_type=None, order=None, total_order_value=None):
        self.cumulative_estimated_commission = cumulative_estimated_commission
        self.cumulative_estimated_fees = cumulative_estimated_fees
        self.group_order_id = group_order_id
        self.group_order_type = group_order_type
        self.total_order_value = total_order_value

        if isinstance(order, dict):
            order = [order]

        self.orders = [Order(**o) for o in order]
        """
        :type: list of Order
        """


class OrderListResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self._inner_dict = self._inner_dict['order_list_response']

        self.count = self._inner_dict['count']
        self.marker = self._inner_dict['marker'] if 'marker' in self._inner_dict else ''
        self._wrap_dict_in_list('order_details')

        self.orders = []
        """
        :type: list of Order
        """

        self.group_orders = []
        """
        :type: list of _GroupOrder
        """

        self._inner_dict['order_details'] = self._inner_dict['order_details'] or []

        for order in self._inner_dict['order_details']:
            if 'group_order' in order:
                self.group_orders.append(_GroupOrder(**order['group_order']))
            elif 'order' in order:
                self.orders.append(Order(**order['order']))


class OrderCancelResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self._inner_dict = self._inner_dict['cancel_response']
        self.account_id = self._inner_dict['account_id']
        self.cancel_time = self._inner_dict['cancel_time']
        self.order_num = self._inner_dict['order_num']
        self.result_message = self._inner_dict['result_message']


class _OrderMessage:
    def __init__(self, msg_code=None, msg_desc=None):
        self.msg_code = msg_code
        self.msg_desc = msg_desc


class EquityOrderPreview(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self._inner_dict = self._inner_dict['equity_order_response']
        self.account_id = self._inner_dict['account_id']
        self.all_or_none = self._inner_dict['all_or_none']
        self.estimated_commission = self._inner_dict['estimated_commission']
        self.estimated_total_amount = self._inner_dict['estimated_total_amount']
        self.limit_price = self._inner_dict['limit_price']
        self.order_action = self._inner_dict['order_action']
        self.order_term = self._inner_dict['order_term']
        self.preview_id = None if 'preview_id' not in self._inner_dict else self._inner_dict['preview_id']
        self.preview_time = None if 'preview_time' not in self._inner_dict else self._inner_dict['preview_time']
        self.price_type = self._inner_dict['price_type']
        self.quantity = self._inner_dict['quantity']
        self.reserve_order = self._inner_dict['reserve_order']
        self.reserve_quantity = self._inner_dict['reserve_quantity']
        self.stop_price = self._inner_dict['stop_price']
        self.symbol = self._inner_dict['symbol']
        self.symbol_desc = self._inner_dict['symbol_desc']


class EquityOrderPlace(EquityOrderPreview):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        del self.preview_id
        del self.preview_time
        self._wrap_dict_in_list('message_list')
        self.message_list = [_OrderMessage(**m) for m in self._inner_dict['message_list']]
        """
        :type: list of _OrderMessage
        """


class EquityOrderChangePreview(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self._inner_dict = self._inner_dict['equity_order_response']
        self.order_num = self._inner_dict['order_num']
        self.order_time = self._inner_dict['order_time']
