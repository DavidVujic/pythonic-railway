from functools import reduce, partial
from . import adapter


def _two_tracked(fn, runner, *args, **kwargs):
    if len(args) and isinstance(args[0], adapter.Fail):
        return args[0]

    return runner(fn, *args, **kwargs)


def tracks(fn):
    """Wraps a plain function in a Railway two-tracks function."""
    return partial(_two_tracked, fn, adapter.try_catch)


def boolean_tracks(fn):
    """Wraps a plain function in a Railway two-tracks function."""
    return partial(_two_tracked, fn, adapter.true_false)


def pipe(*functions):
    """Combines functions from left-to-right.
    The output from a function is the input for the next one"""
    return reduce(lambda arg, fn: fn(arg), functions, None)
