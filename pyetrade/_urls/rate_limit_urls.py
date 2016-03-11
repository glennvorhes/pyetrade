from .. import etrade_config as _config
from urllib.parse import urlencode


def rate_limit(params):
    out_url = 'https://etwssandbox.etrade.com/statuses/sandbox/rest/limits.json' \
        if _config.sandbox else \
        'https://etws.etrade.com/statuses/rest/limits.json'

    return out_url + '?' + urlencode(params)
