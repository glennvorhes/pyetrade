from .orders import EnumCallOrPut, EnumEquityOrderAction, EnumOrderTerm, EnumEquityPriceType, \
    EnumMarketSession, EnumRoutingDestination, EnumOptionOrderAction
import uuid


class _OrderPropsBase(object):
    def __init__(
            self,
            account_id,
            quantity,
            order_term=EnumOrderTerm.GOOD_FOR_DAY,
            price_type=EnumEquityPriceType.MARKET,
            stop_price=None,
            limit_price=None,
            all_or_none=False,
            reserve_order=False,
            reserve_quantity=None):
        """


        :param account_id: account id
        :type account_id: int
        :param quantity: quantity
        :type quantity: int
        :param order_term: order term
        :type order_term: EnumOrderTerm
        :param price_type: price type
        :type price_type: EnumEquityPriceType
        :param stop_price: stop price
        :type stop_price: float|int|None
        :param limit_price: limit price
        :param all_or_none: float|int|None
        :param reserve_order: is reserve order
        :type reserve_order: bool
        :param reserve_quantity: is reserve quantity
        :type reserve_quantity: bool
        :raise Exception:
        """
        assert isinstance(account_id, int)
        assert isinstance(quantity, int)
        assert isinstance(order_term, EnumOrderTerm)
        assert isinstance(price_type, EnumEquityPriceType)
        assert isinstance(stop_price, (float, type(None),))
        assert isinstance(limit_price, (float, type(None),))
        assert isinstance(all_or_none, bool)
        assert isinstance(reserve_order, bool)

        self.accountId = account_id
        self.quantity = quantity

        self.priceType = price_type.value

        # Need stop price if in these values
        if price_type in (EnumEquityPriceType.STOP, EnumEquityPriceType.STOP_LIMIT) \
                and stop_price is None:
            raise Exception('need to add a stop price for these price types')
        self.stopPrice = stop_price

        # Need limit price if in these values
        if price_type in (EnumEquityPriceType.LIMIT, EnumEquityPriceType.STOP_LIMIT) \
                and limit_price is None:
            raise Exception('need to add a limit price for these price types')
        self.limitPrice = limit_price

        self.reserveOrder = reserve_order
        if reserve_order and reserve_quantity is None:
            raise Exception('need reserve quantity')
        self.reserveQuantity = reserve_quantity

        self.orderTerm = order_term.value
        self.allOrNone = all_or_none

        if self.allOrNone:
            if price_type not in [EnumEquityPriceType.LIMIT, EnumEquityPriceType.STOP_LIMIT]:
                raise Exception('only limit or stop limit with all or none')
            if quantity < 300:
                raise Exception('quantity of 300 or more with all or none')

        self.clientOrderId = str(uuid.uuid1()).upper().replace('-', '')[:20]
        self.previewId = None

        if order_term in [EnumOrderTerm.IMMEDIATE_OR_CANCEL, EnumOrderTerm.FILL_OR_KILL] \
                and price_type not in [EnumEquityPriceType.LIMIT, EnumEquityPriceType.STOP_LIMIT]:
            raise Exception('only limit orders with order term immediate_or_cancel or fill_or_kill')

    def get_prop_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}


class EquityOrderProps(_OrderPropsBase):
    def __init__(
            self,
            account_id,
            quantity,
            symbol,
            order_action,
            market_session=EnumMarketSession.REGULAR,
            routing_destination=EnumRoutingDestination.AUTO,
            **kwargs):
        """
        Equity order properties

        :param account_id: account id
        :type account_id: int
        :param quantity: quantity
        :type quantity: int
        :param symbol: symbol
        :type symbol: str
        :param order_action: order action
        :type order_action: EnumEquityOrderAction
        :param market_session: market session
        :type market_session: EnumMarketSession
        :param routing_destination: routing destination
        :type routing_destination: EnumRoutingDestination
        :param kwargs: kwargs
        :type kwargs: dict
        :return:
        """
        assert isinstance(account_id, int)
        assert isinstance(quantity, int)
        assert isinstance(symbol, str)
        assert isinstance(order_action, EnumEquityOrderAction)
        assert isinstance(market_session, EnumMarketSession)
        assert isinstance(routing_destination, EnumRoutingDestination)
        super().__init__(account_id, quantity, **kwargs)
        self.symbol = symbol.upper()
        self.orderAction = order_action.value
        self.marketSession = market_session.value
        self.routingDestination = routing_destination.value


class EquityOrderChangeProps(_OrderPropsBase):
    def __init__(self, account_id, quantity, order_num, **kwargs):
        """
        Equity order change properties

        :param account_id: account id
        :type account_id: int
        :param quantity: quantity
        :type quantity: int
        :param order_num: order number
        :type order_num: int
        :param kwargs: kwargs
        :type kwargs: dict
        :return:
        """
        assert isinstance(account_id, int)
        assert isinstance(quantity, int)
        assert isinstance(order_num, int)
        super().__init__(account_id, quantity, **kwargs)
        self.orderNum = order_num


class OptionOrderProps(_OrderPropsBase):
    def __init__(
            self,
            account_id,
            quantity,
            symbol,
            order_action,
            stop_limit_price,
            call_or_put,
            strike_price,
            expiration_year,
            expiration_month,
            expiration_day,
            market_session=EnumMarketSession.REGULAR,
            routing_destination=EnumRoutingDestination.AUTO,
            **kwargs):

        """
        Option order properties

        :param account_id: account id
        :type account_id: int
        :param quantity: quantity
        :type quantity: int order_enums
        :param symbol: symbol
        :type symbol: str
        :param order_action: order action
        :type order_action: EnumOptionOrderAction
        :param stop_limit_price: stop limit price
        :type stop_limit_price: int|float
        :param call_or_put: call or put
        :type call_or_put: EnumCallOrPut
        :param strike_price: strike price
        :type strike_price: int|float
        :param expiration_year: expiration year
        :type expiration_year: int
        :param expiration_month: expiration month
        :type expiration_month: int
        :param expiration_day: expiration day
        :type expiration_day: int
        :param market_session: market session
        :type market_session: EnumMarketSession
        :param routing_destination: routing destination
        :type routing_destination: EnumRoutingDestination
        :param kwargs: kwargs
        :type kwargs: dict
        :return:
        """
        assert isinstance(call_or_put, EnumCallOrPut)
        assert isinstance(symbol, str)
        assert isinstance(order_action, EnumOptionOrderAction)
        assert isinstance(strike_price, (float, int,))
        assert isinstance(stop_limit_price, (float, int,))
        assert isinstance(expiration_year, int)
        assert isinstance(expiration_month, int)
        assert isinstance(expiration_day, int)
        assert isinstance(market_session, EnumMarketSession)
        assert isinstance(routing_destination, EnumRoutingDestination)
        super().__init__(account_id, quantity, **kwargs)
        self.orderAction = order_action.value
        self.marketSession = market_session.value
        self.stopLimitPrice = stop_limit_price
        self.symbolInfo = dict({
            'symbol': symbol.upper(),
            'callOrPut': call_or_put.value,
            'strikePrice': strike_price,
            'expirationYear': expiration_year,
            'expirationMonth': expiration_month,
            'expirationDay': expiration_day
        })


class OptionOrderChangeProps(_OrderPropsBase):
    def __init__(self, account_id, quantity, order_num, stop_limit_price=None, **kwargs):
        """
        Option order change properties

        :param account_id: account id
        :type account_id: int
        :param quantity: quantity
        :type quantity: int
        :param order_num: order number
        :type order_num: int
        :param stop_limit_price: stop limit price
        :type stop_limit_price: int|float
        :param kwargs: kwargs
        :type kwargs: dict
        :return:
        """
        assert isinstance(account_id, int)
        assert isinstance(quantity, int)
        assert isinstance(order_num, int)
        assert isinstance(stop_limit_price, (float, int, type(None)))
        super().__init__(account_id, quantity, **kwargs)
        self.orderNum = order_num
        self.stopLimitPrice = stop_limit_price
