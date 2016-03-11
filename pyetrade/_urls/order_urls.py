from .. import etrade_config as _config


def orders_list(account_id):
    out_url = 'https://etwssandbox.etrade.com/order/sandbox/rest/orderlist/{accountId}.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/orderlist/{accountId}.json'
    return out_url.format(accountId=account_id)


def orders_equity_preview():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/previewequityorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/previewequityorder.json'


def orders_equity_place():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/placeequityorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/placeequityorder.json'


def orders_equity_change_preview():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/previewchangeequityorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/previewchangeequityorder.json'


def orders_equity_change_place():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/placechangeequityorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/placechangeequityorder.json'


def orders_option_preview():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/previewoptionorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/previewoptionorder.json'


def orders_option_place():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/placeoptionorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/placeoptionorder.json'


def orders_option_change_preview():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/previewchangeoptionorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/previewchangeoptionorder.json'


def orders_option_change_place():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/placechangeoptionorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/placechangeoptionorder.json'


def orders_cancel():
    return 'https://etwssandbox.etrade.com/order/sandbox/rest/cancelorder.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/order/rest/cancelorder.json'
