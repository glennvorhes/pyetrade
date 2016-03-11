from ._response_base import ResponseBase as _ResponseBase
from .. import account


class _Account:
    def __init__(self, account_desc=None, account_id=None, margin_level=None, net_account_value=None,
                 registration_type=None):
        self.account_desc = account_desc
        self.account_id = account_id
        self.margin_level = margin_level
        self.net_account_value = net_account_value
        self.registration_type = registration_type


class AccountList(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self._wrap_dict_in_list('response')

        self.accounts = [_Account(**a) for a in self._inner_dict['response']]
        """
        :type: list of _Account
        """


class _AccountBalanceInfo:
    def __init__(self, cash_available_for_withdrawal=None, funds_withheld_from_withdrawal=None, net_account_value=None,
                 net_cash=None, sweep_deposit_amount=None, total_long_value=None, total_securities_mkt_value=None):
        self.cash_available_for_withdrawal = cash_available_for_withdrawal
        self.funds_withheld_from_withdrawal = funds_withheld_from_withdrawal
        self.net_account_value = net_account_value
        self.net_cash = net_cash
        self.sweep_deposit_amount = sweep_deposit_amount
        self.total_long_value = total_long_value
        self.total_securities_mkt_value = total_securities_mkt_value


class _MarginAccountBalanceInfo:
    def __init__(self, margin_balance=None, margin_balance_withdrawal=None, margin_equity=None,
                 marginable_securities=None, max_available_for_withdrawal=None,
                 non_marginable_securities_and_options=None, short_reserve=None):
        self.margin_balance = margin_balance
        self.margin_balance_withdrawal = margin_balance_withdrawal
        self.margin_equity = margin_equity
        self.marginable_securities = marginable_securities
        self.max_available_for_withdrawal = max_available_for_withdrawal
        self.non_marginable_securities_and_options = non_marginable_securities_and_options
        self.short_reserve = short_reserve


class AccountBalance(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self.account_balance = _AccountBalanceInfo(**self._inner_dict['account_balance'])
        self.account_id = self._inner_dict['account_id']
        self.account_type = self._inner_dict['account_type']
        if 'margin_account_balance' not in self._inner_dict:
            self._inner_dict['margin_account_balance'] = {}
        self.margin_account_balance = _MarginAccountBalanceInfo(**self._inner_dict['margin_account_balance'])
        self.option_level = self._inner_dict['option_level']


class _PositionProductId:
    def __init__(self, call_put=None, exp_day=None, exp_month=None, exp_year=None, strike_price=None, symbol=None,
                 type_code=None):
        self.call_put = call_put
        self.exp_day = exp_day
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.strike_price = strike_price
        self.symbol = symbol
        self.type_code = type_code


class _Position:
    def __init__(self, cost_basis=None, current_price=None, description=None, long_or_short=None, market_value=None,
                 product_id=None, qty=None):
        self.cost_basis = cost_basis
        self.current_price = current_price
        self.description = description
        self.long_or_short = long_or_short
        self.market_value = market_value
        if not isinstance(product_id, dict):
            product_id = {}
        self.product_id = _PositionProductId(**product_id)
        self.qty = qty


class AccountPositions(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self.account_id = self._inner_dict['account_id']
        self.count = self._inner_dict['count']
        self.marker = self._inner_dict['marker']

        self._wrap_dict_in_list('response')

        self.positions = [_Position(**p) for p in self._inner_dict['response']]
        """
        :type: list of _Position
        """


class Alert:
    def __init__(self, alert_id=None, date_time=None, read_flag=None, subject=None, symbol=None):
        self.alert_id = alert_id
        self.date_time = date_time
        self.read_flag = read_flag
        self.subject = subject
        self.symbol = symbol

    def read(self):
        """

        :return:
        :rtype: AlertRead
        """
        return account.read_alert(self.alert_id)

    def delete(self):
        """

        :return:
        :rtype: AlertDelete
        """
        return account.delete_alert(self.alert_id)


class AccountAlerts(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self._wrap_dict_in_list('response')

        self.alerts = [Alert(**a) for a in self._inner_dict['response']]
        """
        :type: list of Alert
        """


class AlertRead(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self.alert_id = self._inner_dict['alert_id']
        # TODO parse the date
        self.create_date = self._inner_dict['create_date']
        self.msg_text = self._inner_dict['msg_text']
        self.read_date = self._inner_dict['read_date']
        self.subject = self._inner_dict['subject']


class AlertDelete(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)
        self.result = self._inner_dict['result']


class _TransactionInfo:
    def __init__(self, amount=None, description=None, details=None, transaction_date=None, transaction_id=None,
                 transaction_short_desc=None):
        self.amount = amount
        self.description = description
        self.details = details
        self.transaction_date = transaction_date
        self.transaction_id = transaction_id
        self.transaction_short_desc = transaction_short_desc

    @property
    def info(self):
        """

        :return:
        :rtype: TransactionDetails
        """
        return account.get_transaction_details(known_url=self.details)


class TransactionsResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self.account_id = self._inner_dict['account_id']
        self.count = self._inner_dict['count']
        self.next_ = self._inner_dict['next_']

        self._wrap_dict_in_list('transaction_list')

        self.transactions = [_TransactionInfo(**t) for t in self._inner_dict['transaction_list']]


class TransactionDetails(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self.account_order_no = self._inner_dict['account_order_no']
        self.amount = self._inner_dict['amount']
        self.category = self._inner_dict['category']
        self.commission = self._inner_dict['commission']
        self.display_symbol = self._inner_dict['display_symbol']
        self.payment_currency = self._inner_dict['payment_currency']
        self.price = self._inner_dict['price']

        self.product_id = _PositionProductId(**self._inner_dict['product_id'])

        self.quantity = self._inner_dict['quantity']
        self.settlement_currency = self._inner_dict['settlement_currency']
        self.settlement_date = self._inner_dict['settlement_date']
        self.transaction_date = self._inner_dict['transaction_date']
        self.transaction_description = self._inner_dict['transaction_description']
        self.transaction_type = self._inner_dict['transaction_type']
        self.underlying_product_id = self._inner_dict['underlying_product_id']
        self.user_description = self._inner_dict['user_description']
