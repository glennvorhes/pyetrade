from .. import etrade_config


def request_token():
    return 'https://etws.etrade.com/oauth/request_token'


def authorize(oauth_token):
    return 'https://us.etrade.com/e/t/etws/authorize?key={0}&token={1}'.format(
        etrade_config.oauth_consumer_key, oauth_token
    )

def access():
    return 'https://etws.etrade.com/oauth/access_token'
