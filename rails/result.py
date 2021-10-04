class Fail:
    def __init__(self, fn=None, exception=None):
        self.fn = fn
        self.exception: Exception = exception


def failed(res) -> bool:
    return isinstance(res, Fail)


def succeeded(res) -> bool:
    return not failed(res)
