from enum import Enum


class ErrorType(Enum):
    PAGE_NOT_FOUND = 'PAGE NOT FOUND'
    BAD_JSON = "BAD JSON"
    ETRADE_DEFINED = 'ETRADE DEFINED'
    KEYERROR = 'KEYERROR'


class EtradeError:

    def __init__(self, error_type=None, msg=None, code=None):
        """

        :param error_type:
        :param msg:
        :type error_type: ErrorType
        :type msg: str
        :return:
        """
        self.error_type = error_type
        self.msg = msg
        self.code = code
