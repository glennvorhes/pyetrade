from .. import etrade_config as _config
from urllib.parse import urlencode


def market_quote(symbols):
    out_url = 'https://etwssandbox.etrade.com/market/sandbox/rest/quote/{0}.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/market/rest/quote/{0}.json'

    symbol_list = []
    if type(symbols) is str:
        symbol_list.append(symbols)
    elif type(symbols) is list:
        symbol_list.extend(symbols)
    else:
        raise TypeError('wrong type passed as param')

    symbol_list = [s.upper() for s in symbol_list]

    for i in range(len(symbol_list)):
        try:
            assert isinstance(symbol_list[i], str)
        # except
        except Exception as exc:
            print(exc.args)

        symbol_list[i] = symbol_list[i].upper()

    if len(symbol_list) > 25:
        raise ValueError('maximum of 25 quotes in one request')

    return out_url.format(','.join(symbol_list))


def market_lookup(param_dict):
    out_url = 'https://etwssandbox.etrade.com/market/sandbox/rest/productlookup.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/market/rest/productlookup.json'

    return out_url + '?' + urlencode(param_dict)


def market_option_chains(param_dict):
    out_url = 'https://etwssandbox.etrade.com/market/sandbox/rest/optionchains.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/market/rest/optionchains.json'

    return out_url + '?' + urlencode(param_dict)


def market_option_expire_date(param_dict):
    out_url = 'https://etwssandbox.etrade.com/market/sandbox/rest/optionexpiredate.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/market/rest/optionexpiredate.json'

    return out_url + '?' + urlencode(param_dict)
