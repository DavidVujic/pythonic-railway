from functools import reduce


class Fail:
    def __init__(self, fn=None, exception=None):
        self.fn = fn
        self.exception: Exception = exception


def run(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return Fail(fn=fn, exception=e)


def wrap(fn):
    def two_tracked_fn(*args, **kwargs):
        if len(args) and isinstance(args[0], Fail):
            return args[0]

        return run(fn, *args, **kwargs)

    return two_tracked_fn


def pipe(*functions):
    functions = map(wrap, functions)

    return reduce(lambda arg, fn: fn(arg), functions, None)
