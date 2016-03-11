import json
import time
from datetime import datetime, timedelta

import os
from requests_oauthlib import OAuth1Session, OAuth1
from splinter import Browser
from ._urls import auth_urls as _auth_urls

from . import etrade_config

__author__ = 'glenn'

_time_format = '%m-%d-%Y %H:%M:%S'


class _Auth(object):
    def __init__(self):
        """
        The authorization object, has a property to get current
        """

        self._authorization = None
        self._last_used = datetime.utcnow() - timedelta(hours=10)

        self._resource_owner_key = None
        self._resource_owner_secret = None

        self._consumer_key = etrade_config.oauth_consumer_key
        self._consumer_secret = etrade_config.oath_consumer_secret

        self._auth_file_path = etrade_config.auth_file_path
        self._user_name = etrade_config.user_name
        self._user_pwd = etrade_config.user_pwd

    def force_expire(self):
        self._authorization = None

    def _write_auth_txt(self):
        # output the owner key and secret to the file
        with open(etrade_config.auth_file_path, 'w') as f:
            json.dump(
                {
                    "resourceOwnerKey": self._resource_owner_key,
                    "resourceOwnerSecret": self._resource_owner_secret,
                    "utcTime": self._last_used.strftime(_time_format)
                }, f, indent=4, sort_keys=True)

    def _load_saved_auth(self):

        if os.path.isfile(etrade_config.auth_file_path):
            with open(etrade_config.auth_file_path, 'r') as f:
                auth_props = json.load(f)
            self._resource_owner_key = auth_props['resourceOwnerKey']
            self._resource_owner_secret = auth_props['resourceOwnerSecret']
            self._last_used = datetime.strptime(auth_props['utcTime'], _time_format)
        else:
            self._write_auth_txt()

        self._authorization = OAuth1(etrade_config.oauth_consumer_key,
                                     client_secret=etrade_config.oath_consumer_secret,
                                     resource_owner_key=self._resource_owner_key,
                                     resource_owner_secret=self._resource_owner_secret)

    def _reauthorize(self):
        print('need to create new authorization')

        """create an oauth session using the consumer key/secret combination and for
        some reason the callback parameter 'oob'"""
        oauth = OAuth1Session(
            etrade_config.oauth_consumer_key,
            client_secret=etrade_config.oath_consumer_secret,
            callback_uri='oob'
        )

        request_dict = oauth.fetch_request_token(_auth_urls.request_token())
        del oauth

        # request dict now contains the request token and secret
        # pass the token and the consumer key as url parameters to the
        # authorize application url

        # this is not a rest interface so there is no typical response
        # instead, need to use browser automation with selenium, splinter, and phantomjs
        # or other driver (eg firefox)

        if etrade_config.browser == 'firefox':
            browser = Browser('firefox', )
        elif etrade_config.browser == 'phantomjs':
            browser = Browser('phantomjs', service_args=['--ssl-protocol=tlsv1'])
        else:
            print('check browser')
            raise ValueError()

        browser.visit(_auth_urls.authorize(request_dict['oauth_token']))
        time.sleep(1)

        # add user name and password and click the login button
        user_input_elements = browser.find_by_name('USER')
        if len(user_input_elements) > 0:
            user_input_elements[0].type(self._user_name)
            print('user id element found')
            # print(browser.html)
        else:
            print('user id element not found')
            print(browser.html)
            exit()
        time.sleep(1)

        pwd_input_elements = browser.find_by_id('txtPassword')
        if len(pwd_input_elements) > 0:
            pwd_input_elements[0].type(self._user_pwd)
            print('password element found')
        else:
            print('password element not found')
            exit()
        time.sleep(1)

        logon_button = browser.find_by_css('.log-on-btn')

        if len(logon_button) > 0:
            logon_button[0].click()
            print('logon button found')
        else:
            print('logon button not found')
            exit()
        # print(len(logon_button))
        # exit()
        time.sleep(1)
        # exit()first.click()

        # Of the input elements, get the one with the value of "Accept" license aggrement
        input_element_list = [inp for inp in browser.find_by_css('input') if inp.value == 'Accept']
        time.sleep(1)

        # Be sure there was at least one input element meeting the criteria of being
        # an input element with a value of 'Accept' before proceeding
        if len(input_element_list) > 0:
            # Invoke a click on the element which will take to the next page
            input_element_list[0].click()
            time.sleep(1)
            """ phantomjs adds an extra space on the end of the verifier
            that is found at the first and only input element on the
            page now visited
            Remove this with .strip()
            """
            # Variable to contain the verifier
            oauth_verifier = browser.find_by_css('input').first.value.strip()
            time.sleep(1)
            browser.quit()
        else:
            # something went wrong if there was no matching element
            # Freak out and exit if this is the case
            raise Exception('can not find the right element to click on')
        print('verifier:', oauth_verifier)

        # Session using everything, consumer token/secret, request token/secret, and verifier
        oauth = OAuth1Session(etrade_config.oauth_consumer_key,
                              client_secret=etrade_config.oath_consumer_secret,
                              resource_owner_key=request_dict['oauth_token'],
                              resource_owner_secret=request_dict['oauth_token_secret'],
                              verifier=oauth_verifier)

        access_dict = oauth.fetch_access_token(_auth_urls.access())
        del oauth

        self._resource_owner_key = access_dict['oauth_token']
        self._resource_owner_secret = access_dict['oauth_token_secret']

        # the authorization object that can be used with all subsequent requests
        self._authorization = OAuth1(
            etrade_config.oauth_consumer_key,
            client_secret=etrade_config.oath_consumer_secret,
            resource_owner_key=self._resource_owner_key,
            resource_owner_secret=self._resource_owner_secret
        )

        etrade_config.changed = False

    @property
    def get_current(self):
        """
        Get a current OAuth1, renew if necessary

        :return: the current authorization
        :rtype: OAuth1
        """

        self._load_saved_auth()
        utc_now = datetime.utcnow()

        # can reuse if not more than 2 hours since last use and in the same day
        if self._authorization and self._last_used + timedelta(hours=2) > utc_now and \
                self._last_used.day == utc_now.day and not etrade_config.changed:
            pass
            print('can use existing authorization properties')
        else:
            self._reauthorize()

        # update last used time
        self._last_used = datetime.utcnow()
        self._write_auth_txt()

        # return the authorization, new or reused
        return self._authorization

auth = _Auth()
