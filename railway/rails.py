from functools import partial
from railway.funcs import true_false, try_catch
from railway.result import failed


def wrapper(rail_fn, fn, *args, **kwargs):
    if len(args) and failed(args[0]):
        return args[0]

    return rail_fn(fn, *args, **kwargs)


def tracks(fn):
    """Railway Oriented Programming decorator

    Wraps a function into a two-tracked function.

    Taking the Fail track when there is an exception.
    """

    return partial(wrapper, try_catch, fn)


def tracks_boolean(fn):
    """Railway Oriented Programming decorator

    Wraps a function into a two-tracked function.

    Taking the Fail track when the result from a function is False.
    """

    return partial(wrapper, true_false, fn)
