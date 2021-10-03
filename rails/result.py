class Fail:
    def __init__(self, fn=None, exception=None):
        self.fn = fn
        self.exception: Exception = exception


def has_failed(res) -> bool:
    return isinstance(res, Fail)
