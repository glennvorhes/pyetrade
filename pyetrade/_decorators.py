from . import _error
from json.decoder import JSONDecodeError
import json
from ._auth import auth

__author__ = 'glenn'


class ProcessResult(object):
    """
    decorator for all etrade interaction
    """
    def __init__(self, response_class):
        """

        :param response_class: the response class used to construct the return value
        """
        self._response_class = response_class

    def __call__(self, f):

        def wrapped_f(*args, **kwargs):
            """
            wrap the function

            :param args:
            :param kwargs:
            :return: error or response object
            :rtype ResponseBase|EtradeError
            """

            response = f(*args, **kwargs)

            if response.status_code == 404:
                return _error.EtradeError(_error.ErrorType.PAGE_NOT_FOUND, '404')
            try:
                response_json = response.json()
                if 'Error' in response_json:
                    error_json = response_json['Error']
                    etrade_err = _error.EtradeError(
                        _error.ErrorType.ETRADE_DEFINED.KEYERROR,
                        error_json['message'] if 'message' in error_json else '',
                        error_json['errorCode'] if 'errorCode' in error_json else None
                    )
                    return etrade_err
                    # if etrade_err.msg.find('oauth_problem') > -1:
                    #     auth.reauthorize()
                    #     return wrapped_f(*args, **kwargs)
                    # else:
                    #     return etrade_err
                else:
                    return self._response_class(response_json)
            except JSONDecodeError:
                return _error.EtradeError(_error.ErrorType.BAD_JSON, 'poorly formed json response')
            except KeyError as ex:
                return _error.EtradeError(_error.ErrorType.KEYERROR, ex.args)

        return wrapped_f
