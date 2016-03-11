from unittest import TestCase
from datetime import date
from pyetrade import etrade_config

from pyetrade import account

__author__ = 'glenn'

acount_id = 83405188
alert_id = 1108
transaction_id = 345678


class TestAccounts(TestCase):
    def setUp(self):
        etrade_config.init_props(sandbox=True)

    def test_account_list(self):
        return

        resp = account.list_accounts()
        print(resp.accounts[0].account_desc)

    def test_get_balance(self):
        return
        bal = account.get_balance(acount_id)
        print(bal.margin_account_balance.short_reserve)

    def test_get_positions(self):
        return
        pas = account.get_positions(acount_id)
        print(pas.positions[0].product_id.symbol)
        # print

    def test_get_alerts(self):
        return
        al = account.get_alerts()

        al.alerts[0].read()
        al.alerts[0].delete()

    def test_read_alert(self):
        return
        read = account.read_alert(alert_id)

    def test_delete_alert(self):
        # return
        delet = account.delete_alert(alert_id)

    def test_transaction_history(self):
        # return
        trans = account.get_transaction_history(83405188,
                                                transaction_group=account.EnumTransactionGroup.TRADES,
                                                asset_type=account.EnumTransactionAssetType.EQ,
                                                transaction_type_s=account.EnumTransactionTypeTrade.ALL,
                                                ticker_symbol=None,
                                                start_date=None,
                                                end_date=None,
                                                count=None,
                                                marker=None)

        g = trans.transactions[0].info
        print(g)
        print(g.product_id.symbol)

    def test_get_transaction_details(self):
        return

        deets = account.get_transaction_details(acount_id, transaction_id)

        print(deets.product_id.symbol)




        # def test_accounts(self):
        #     # print(account.list_accounts())
        #     # print(account.get_balance(83405188))
        #     # print(account.get_positions(83405188))
        #     # print(account.get_alerts())
        #     # print(account.read_alert(1108))
        #     # print(account.delete_alert(1108))
        #
        #     # print(account.get_transaction_history(83405188))
        #     # print(account.get_transaction_history(83405188, account_enums.TransactionGroup.TRADES))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=TranactionAssetType.EQ,
        #                                           transaction_type_s=TransactionTypeTrade.ALL,
        #                                           ticker_symbol='goog',
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=TranactionAssetType.EQ,
        #                                           transaction_type_s=TransactionTypeTrade.ALL,
        #                                           ticker_symbol=None,
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=TranactionAssetType.EQ,
        #                                           transaction_type_s=None,
        #                                           ticker_symbol='goog',
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=TranactionAssetType.EQ,
        #                                           transaction_type_s=[TransactionTypeTrade.ASSSIGNMENT, TransactionTypeTrade.EXCERCISE],
        #                                           ticker_symbol='goog',
        #                                           start_date=date.today(),
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #
        #     # return
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.WITHDRAWALS,
        #                                           asset_type=None,
        #                                           transaction_type_s=TransactionTypeWithdrawal.ATM,
        #                                           ticker_symbol=None,
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #     # return
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=None,
        #                                           asset_type=None,
        #                                           transaction_type_s=TransactionTypeOther.CURRENCY_XCH,
        #                                           ticker_symbol=None,
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #     # return
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.DEPOSITS,
        #                                           asset_type=None,
        #                                           transaction_type_s=[TransactionTypeDeposit.CHECK, TransactionTypeDeposit.DEPOSIT],
        #                                           ticker_symbol=None,
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #     #
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=None,
        #                                           transaction_type_s=[TransactionTypeTrade.EXPIRATION],
        #                                           ticker_symbol='goog',
        #                                           start_date=date.today(),
        #                                           end_date=date.today(),
        #                                           count=5,
        #                                           marker=0))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=None,
        #                                           transaction_type_s=[TransactionTypeTrade.EXPIRATION],
        #                                           ticker_symbol='goog',
        #                                           start_date=date.today(),
        #                                           end_date=date.today(),
        #                                           count=5,
        #                                           marker=0))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=None,
        #                                           transaction_type_s=[TransactionTypeTrade.EXPIRATION],
        #                                           ticker_symbol='goog',
        #                                           start_date=date.today(),
        #                                           end_date=date.today(),
        #                                           count=5,
        #                                           marker=0))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=TransactionGroup.TRADES,
        #                                           asset_type=TranactionAssetType.MF,
        #                                           transaction_type_s=[TransactionTypeTrade.EXPIRATION, TransactionTypeTrade.ALL],
        #                                           ticker_symbol='goog',
        #                                           start_date=date.today(),
        #                                           end_date=date.today(),
        #                                           count=5,
        #                                           marker=0))
        #     print(account.get_transaction_history(83405188,
        #                                           transaction_group=None,
        #                                           asset_type=None,
        #                                           transaction_type_s=None,
        #                                           ticker_symbol=None,
        #                                           start_date=None,
        #                                           end_date=None,
        #                                           count=None,
        #                                           marker=None))
        #
        #
        #
        #     # print(account.get_transaction_history(
        #     # 83405188,
        #     #     account_enums.TransactionGroup.TRADES,
        #     #     account_enums.TransactionAssetType.EQ,
        #     #     account_enums.TransactionTypeTrade.ALL,
        #     #     ticker_symbol='goog'
        #     # ))
        #
        #     # print(account.get_transaction_details(83405188, 345678))
        #
        #
        #     # self.fail()
