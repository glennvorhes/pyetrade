from ._response_base import ResponseBase as _ResponseBase


class NotificationResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self._gen_class()

