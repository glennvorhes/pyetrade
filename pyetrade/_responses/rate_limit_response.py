from ._response_base import ResponseBase as _ResponseBase


class RateLimitResponse(_ResponseBase):
    def __init__(self, input_dict):
        super().__init__(input_dict)

        self.consumer_key = self._inner_dict['consumer_key']
        self.limit_interval_in_seconds = self._inner_dict['limit_interval_in_seconds']
        self.requests_limit = self._inner_dict['requests_limit']
        self.requests_remaining = self._inner_dict['requests_remaining']
        self.reset_time = self._inner_dict['reset_time']
        self.reset_time_epoch_seconds = self._inner_dict['reset_time_epoch_seconds']
