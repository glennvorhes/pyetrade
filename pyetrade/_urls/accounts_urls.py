from .. import etrade_config as _config


def account_list():
    return 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/accountlist.json'


def account_balance(account_id):
    out = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountbalance/{0}.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/accountbalance/{0}.json'
    return out.format(account_id)


def account_positions(account_id):
    out = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountpositions/{0}.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/accountpositions/{0}.json'
    return out.format(account_id)


def account_alerts():
    return 'https://etwssandbox.etrade.com/accounts/sandbox/rest/alerts.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/alerts.json'


def account_read_delete_alert(alert_id):
    out = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/alerts/{0}.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/alerts/{0}.json'
    return out.format(alert_id)


def account_transaction_history(
        account_id, group=None, asset_type=None, transaction_type_s=None, ticker_symbol=None):
    out_url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/{accountId}/transactions.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/{accountId}/transactions.json'

    format_dict = dict(accountId=account_id)

    if isinstance(group, str):
        format_dict['Group'] = group
        out_url = out_url[:out_url.find('.json')] + '/{Group}' + '.json'

    if isinstance(asset_type, str):
        format_dict['AssetType'] = asset_type
        out_url = out_url[:out_url.find('.json')] + '/{AssetType}' + '.json'

    if isinstance(transaction_type_s, str):
        format_dict['TransactionType'] = transaction_type_s
        out_url = out_url[:out_url.find('.json')] + '/{TransactionType}' + '.json'

    if isinstance(ticker_symbol, str):
        format_dict['TickerSymbol'] = ticker_symbol
        out_url = out_url[:out_url.find('.json')] + '/{TickerSymbol}' + '.json'

    return out_url.format(**format_dict)


def account_transaction_details(account_id, transaction_id):
    """
    get the transaction details url by account id an transaction id
    :param account_id: the account id
    :type account_id: int
    :param transaction_id: the transaction id
    :type transaction_id: int
    :return: the get transaction details url
    :rtype: str
    """
    out_url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/{accountId}/transactions/{transactionId}.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/accounts/rest/{accountId}/transactions/{transactionId}.json'
    return out_url.format(accountId=account_id, transactionId=transaction_id)
