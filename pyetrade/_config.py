import os
# TODO Make sure certain properties have been defined


class _EtradeConfig(object):
    """
    configuration object
    """

    def __init__(self):
        self.changed = False

        self._user_name = self._user_pwd = None
        self._consumer_key_sandbox = self._consumer_secret_sandbox = None
        self._consumer_key_production = self._consumer_secret_production = None

        self._browser = None
        self._auth_dir = os.getcwd()
        self._sandbox = False
        """
        flag to use the sandbox urls and authorization
        """

        self.init_env()
        self.init_props(browser='firefox')

    def init_env(self, user_name='ETRADE_USER', user_pwd='ETRADE_PWD',
                 key_sandbox='ETRADE_KEY_SANDBOX', secret_sandbox='ETRADE_SECRET_SANDBOX',
                 key_prod='ETRADE_KEY', secret_prod='ETRADE_SECRET'):
        self._user_name = None if user_name not in os.environ else os.environ[user_name]
        self._user_pwd = None if user_pwd not in os.environ else os.environ[user_pwd]

        self._consumer_key_sandbox = None if key_sandbox not in os.environ else os.environ[key_sandbox]
        self._consumer_secret_sandbox = None if secret_sandbox not in os.environ else os.environ[secret_sandbox]

        self._consumer_key_production = None if key_prod not in os.environ else os.environ[key_prod]
        self._consumer_secret_production = None if secret_prod not in os.environ else os.environ[secret_prod]

    def init_props(self, sandbox=False, browser=None, auth_dir=None, user_name=None, user_pwd=None,
                   key_sandbox=None, secret_sandbox=None, key_prod=None, secret_prod=None):
        self._sandbox = sandbox

        self._browser = browser or self._browser
        self._auth_dir = auth_dir or self._auth_dir

        self._user_name = user_name or self._user_name
        self._user_pwd = user_pwd or self._user_pwd

        self._consumer_key_sandbox = key_sandbox or self._consumer_key_sandbox
        self._consumer_secret_sandbox = secret_sandbox or self._consumer_secret_sandbox
        self._consumer_key_production = key_prod or self._consumer_key_production
        self._consumer_secret_production = secret_prod or self._consumer_secret_production

    def _change_helper(self, key, value, set_changed=True):
        if self.__getattribute__(key) != value:
            self.changed = set_changed
            self.__setattr__(key, value)

    @property
    def user_name(self) -> str:
        return self._user_name

    @user_name.setter
    def user_name(self, new_username):
        """

        :param new_username:
        :type new_username: str
        """
        self._change_helper('_user_name', new_username)

    @property
    def user_pwd(self) -> str:
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, new_password):
        """

        :param new_password:
        :type new_password: str
        """
        self._change_helper('_user_pwd', new_password)

    @property
    def browser(self) -> str:
        return self._browser

    @browser.setter
    def browser(self, new_browser):
        self._change_helper('_browser', new_browser)

    @property
    def sandbox(self) -> bool:
        return self._sandbox

    @sandbox.setter
    def sandbox(self, use_sandbox):
        self._change_helper('_sandbox', use_sandbox)

    @property
    def auth_file_directory(self) -> str:
        return self._auth_dir

    @auth_file_directory.setter
    def auth_file_directory(self, auth_directory):
        self._change_helper('_auth_file_directory', auth_directory)

    @property
    def consumer_key_sandbox(self) -> str:
        return self._consumer_key_sandbox

    @consumer_key_sandbox.setter
    def consumer_key_sandbox(self, key):
        self._change_helper('_oauth_consumer_key_sandbox', key, self.sandbox)

    @property
    def consumer_secret_sandbox(self) -> str:
        return self._consumer_secret_sandbox

    @consumer_secret_sandbox.setter
    def consumer_secret_sandbox(self, secret):
        self._change_helper('_oauth_consumer_secret_sandbox', secret, self.sandbox)

    @property
    def consumer_key(self) -> str:
        return self._consumer_key_production

    @consumer_key.setter
    def consumer_key(self, key):
        self._change_helper('_oauth_consumer_key_production', key, not self.sandbox)

    @property
    def consumer_secret(self) -> str:
        return self._consumer_secret_production

    @consumer_secret.setter
    def consumer_secret(self, secret):
        self._change_helper('_oauth_consumer_secret_production', secret, not self.sandbox)

    @property
    def auth_file_path(self):
        return os.path.join(self._auth_dir, 'auth{0}.json'.format('_sandbox' if self.sandbox else ''))

    @property
    def oauth_consumer_key(self) -> str:
        """
        property to get the consumer key

        :return: consumer key
        """

        return self._consumer_key_sandbox if self.sandbox else self._consumer_key_production

    @property
    def oath_consumer_secret(self) -> str:
        """
        property to get the consumer secret

        :return: consumer secret
        """
        return self._consumer_secret_sandbox if self.sandbox else self._consumer_secret_production


etrade_config = _EtradeConfig()
