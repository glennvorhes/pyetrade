import datetime
from enum import Enum
import re
import requests
from ._urls import accounts_urls
from ._auth import auth as _auth
from ._decorators import ProcessResult
from ._responses import account_response

__author__ = 'glenn'


def _format_date_to_mmddyyyy(input_date):
    """
    Format the date to mmddyyy

    :param input_date: str|None
    :return: date formated string
    :rtype: str
    """
    if input_date is None:
        return None
    elif input_date is str:
        # regex for start and end dates
        assert re.search('^[0,1][0-9][0,1,2,3][0-9][2][0][0-9][0-9]$', input_date)
        return input_date
    elif type(input_date) in (datetime.datetime, datetime.date):
        return input_date.strftime('%m%d%Y')
    else:
        raise AssertionError('wrong type')


class EnumTransactionGroup(Enum):
    DEPOSITS = 'DEPOSITS'
    WITHDRAWALS = 'WITHDRAWALS'
    TRADES = 'TRADES'


class EnumTransactionAssetType(Enum):
    EQ = 'EQ'
    OPTN = 'OPTN'
    MMF = 'MMF'
    MF = 'MF'
    BOND = 'BOND'
    ALL = 'ALL'


class EnumTransactionTypeTrade(Enum):
    ALL = 'ALL'
    # A balance adjustment as the result of another party exercising an option.
    ASSSIGNMENT = 'ASSSIGNMENT'
    # A balance adjustment as the result of exercising an option
    EXCERCISE = 'EXCERCISE'
    '''
    The date on which an option, right, or warrant expires and becomes
    worthless if not exercised. Also, the date on which an agreement is no
    longer in effect.
    '''
    EXPIRATION = 'EXPIRATION'


class EnumTransactionTypeWithdrawal(Enum):
    ALL = 'ALL'
    """Common to Withdrawal and Deposit"""
    # Service charge from automated teller machines
    ATM = 'ATM'
    # Check deposit or withdrawal
    CHECK = 'CHECK'
    # Contribution
    CONTRIBUTION = 'CONTRIBUTION'
    # Money taken out of retirement fund
    DISTRIBUTION = 'DISTRIBUTION'
    # Point of sale debit
    POS = 'POS'
    # Cash transfer (in or out)
    TRANSFER = 'TRANSFER'
    # Cash wire (in or out)
    WIRE = 'WIRE'

    """specific to withdrawals"""
    # List of transactions that decrease assets
    DEBIT = 'DEBIT'
    # Decrease of assets
    DIRECT_DEBIT = 'DIRECT_DEBIT'
    # Service fees
    FEE = 'FEE'


class EnumTransactionTypeDeposit(Enum):
    ALL = 'ALL'
    """Common to Withdrawal and Deposit"""
    # Service charge from automated teller machines
    ATM = 'ATM'
    # Check deposit or withdrawal
    CHECK = 'CHECK'
    # Contribution
    CONTRIBUTION = 'CONTRIBUTION'
    # Money taken out of retirement fund
    DISTRIBUTION = 'DISTRIBUTION'
    # Point of sale debit
    POS = 'POS'
    # Cash transfer (in or out)
    TRANSFER = 'TRANSFER'
    # Cash wire (in or out)
    WIRE = 'WIRE'

    """Specific to Deposit"""
    # List of transactions that Increase assets
    DEPOSIT = 'DEPOSIT'
    # Increase of assets
    DIRECT_DEPOSIT = 'DIRECT_DEPOSIT'
    # Dividend paid
    DIVIDEND = 'DIVIDEND'
    # Interest charged
    INTEREST = 'INTEREST'


class EnumTransactionTypeOther(Enum):
    ALL = 'ALL'
    # Split, merger, or acquisition
    CORPORATE_ACTIONS = 'CORPORATE_ACTIONS'
    # Currency exchange
    CURRENCY_XCH = 'CURRENCY_XCH'
    # Sweep Deposit
    SWEEP = 'SWEEP'


@ProcessResult(account_response.AccountList)
def list_accounts():
    """
    Return accounts

    :return: account list
    :rtype: account_response.AccountList|EtradeError
    """
    return requests.get(accounts_urls.account_list(), auth=_auth.get_current)


@ProcessResult(account_response.AccountBalance)
def get_balance(account_id):
    """
    Get account balance

    :param account_id: account id
    :type account_id: int
    :return: account balance
    :rtype: account_response.AccountBalance|EtradeError
    """
    assert isinstance(account_id, int)
    return requests.get(accounts_urls.account_balance(account_id), auth=_auth.get_current)


@ProcessResult(account_response.AccountPositions)
def get_positions(account_id):
    """
    Get account positions

    :param account_id: account id
    :type account_id: int
    :return: account positions
    :rtype: account_response.AccountPositions|EtradeError
    """
    assert isinstance(account_id, int)
    return requests.get(accounts_urls.account_positions(account_id), auth=_auth.get_current)


@ProcessResult(account_response.AccountAlerts)
def get_alerts():
    """
    Get alerts

    :return: alerts
    :rtype: account_response.AccountAlerts|EtradeError
    """
    return requests.get(accounts_urls.account_alerts(), auth=_auth.get_current)


@ProcessResult(account_response.AlertRead)
def read_alert(alert_id):
    """
    Read alert

    :param alert_id: alert id
    :type alert_id: int
    :return: the alert
    :rtype: account_response.AlertRead|EtradeError
    """
    assert isinstance(alert_id, int)
    return requests.get(accounts_urls.account_read_delete_alert(alert_id), auth=_auth.get_current)


@ProcessResult(account_response.AlertDelete)
def delete_alert(alert_id):
    """
    Delete an alert by id

    :param alert_id: the alert id
    :type alert_id: int
    :return: the delete response
    :rtype: account_response.AlertDelete|EtradeError
    """
    assert isinstance(alert_id, int)
    return requests.delete(accounts_urls.account_read_delete_alert(alert_id), auth=_auth.get_current)


@ProcessResult(account_response.TransactionsResponse)
def get_transaction_history(account_id,
                            transaction_group=None,
                            asset_type=None,
                            transaction_type_s=None,
                            ticker_symbol=None,
                            start_date=None,
                            end_date=None,
                            count=None,
                            marker=None):
    """
    Get the transaction history

    :param account_id: account id
    :type account_id: int
    :param transaction_group: the transaction group
    :type transaction_group: EnumTransactionGroup|None
    :param asset_type: the asset type
    :type asset_type: EnumTransactionAssetType|None
    :param transaction_type_s: the transaction types as a single enum or a list
    :type transaction_type_s:
    EnumTransactionTypeTrade|EnumTransactionTypeWithdrawal|EnumTransactionTypeDeposit|EnumTransactionTypeOther|list|None
    :param ticker_symbol: the ticker symbol
    :type ticker_symbol: str|None
    :param start_date: the start date
    :type start_date: str|datetime.datetime|datetime.date|None
    :param end_date: the end date
    :type end_date: str|datetime.datetime|datetime.date|None
    :param count: the count to return
    :type count: int|None
    :param marker: the marker, check more documentation
    :type marker: int|None
    :return: the recent transactions
    :rtype: account_response.TransactionsResponse|EtradeError
    """

    '''
    handle all assertions here before parameters are passed to the url generator
    start with the start, end dates and count/marker parameters that are not
    passed to the url generator
    '''

    assert isinstance(account_id, int)
    assert isinstance(transaction_group, (EnumTransactionGroup, type(None),))
    assert isinstance(transaction_type_s, (
        EnumTransactionTypeTrade, EnumTransactionTypeWithdrawal, EnumTransactionTypeDeposit,
        EnumTransactionTypeOther, list, type(None),))
    assert isinstance(asset_type, (EnumTransactionAssetType, type(None),))
    assert isinstance(ticker_symbol, (str, type(None),))
    assert isinstance(start_date, (str, datetime.datetime, datetime.date, type(None),))
    assert isinstance(end_date, (str, datetime.datetime, datetime.date, type(None),))
    assert isinstance(count, (int, type(None),))
    assert isinstance(marker, (int, type(None),))

    start_date = _format_date_to_mmddyyyy(start_date)
    end_date = _format_date_to_mmddyyyy(end_date)

    # if the transaction group is TRADES, can define an asset type and ticker
    if transaction_group is not None and transaction_group == EnumTransactionGroup.TRADES:
        asset_type = None if asset_type is None else asset_type.value

        if ticker_symbol is str:
            if len(ticker_symbol) == 0:
                ticker_symbol = None

    # otherwise, asset_type, ticker_symbol must be None
    else:
        assert asset_type is None
        assert ticker_symbol is None

    # transaction types pertain to transaction groups with the exception of
    # CORPORATE_ACTIONS, CURRENCY_XCH, and SWEEP
    # if transaction group is not defined, the type may be one or none of these
    if transaction_group is None:
        assert isinstance(transaction_type_s, (EnumTransactionTypeOther, type(None),))
        if isinstance(transaction_type_s, EnumTransactionTypeOther):
            transaction_type_s = transaction_type_s.value
        else:
            transaction_type_s = None
    else:
        type_lookup = dict({
            EnumTransactionGroup.TRADES: EnumTransactionTypeTrade,
            EnumTransactionGroup.DEPOSITS: EnumTransactionTypeDeposit,
            EnumTransactionGroup.WITHDRAWALS: EnumTransactionTypeWithdrawal
        })
        valid_type = type_lookup[transaction_group]
        assert isinstance(transaction_type_s, (valid_type, list, type(None),))
        if isinstance(transaction_type_s, valid_type):
            transaction_type_s = transaction_type_s.value
        elif isinstance(transaction_type_s, list):
            check_list = [isinstance(t, valid_type) for t in transaction_type_s]
            for chk in check_list:
                assert chk
            transaction_type_s = ','.join([t.value for t in transaction_type_s])

    # transaction group is one account_enum.TransactionGroup or None
    transaction_group = None if transaction_group is None else transaction_group.value

    params = dict()
    params['startDate'] = start_date
    params['endDate'] = end_date
    params['count'] = count
    params['marker'] = marker

    return requests.get(accounts_urls.account_transaction_history(
        account_id, transaction_group, asset_type, transaction_type_s, ticker_symbol
    ), params=params, auth=_auth.get_current)


@ProcessResult(account_response.TransactionDetails)
def get_transaction_details(account_id=None, transaction_id=None, known_url=None):
    """
    Get the transaction details

    :param account_id: the account id
    :type account_id: int
    :param transaction_id: the transaction id
    :type transaction_id: int
    :param known_url: the known url to the transaction details
    :type known_url: str|None
    :return: the transaction details
    :rtype: account_response.TransactionDetails|EtradeError
    """
    if account_id and transaction_id:
        return requests.get(accounts_urls.account_transaction_details(account_id, transaction_id),
                            auth=_auth.get_current)
    elif known_url:
        known_url = known_url.strip()
        if not known_url.endswith('.json'):
            known_url += '.json'
        return requests.get(known_url, auth=_auth.get_current)
    else:
        print('problem with input parameters')
        return None



