from . import _error
from json.decoder import JSONDecodeError

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
                    etrade_err = _error.EtradeError(
                        _error.ErrorType.ETRADE_DEFINED,
                        response_json['Error']['message'],
                        response_json['Error']['errorCode']
                    )
                    print(self._response_class.__name__)
                    print(etrade_err.msg)
                    return etrade_err
                else:
                    return self._response_class(response_json)
            except JSONDecodeError:
                return _error.EtradeError(_error.ErrorType.BAD_JSON, 'poorly formed json response')
            except KeyError as ex:
                return _error.EtradeError(_error.ErrorType.KEYERROR, ex.args)

        return wrapped_f
