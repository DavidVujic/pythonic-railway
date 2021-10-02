class Fail:
    def __init__(self, fn=None, exception=None):
        self.fn = fn
        self.exception: Exception = exception
