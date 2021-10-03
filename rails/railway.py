from functools import partial
from .result import Fail
from .adapter import try_catch, true_false


def _two_tracked(fn, runner, *args, **kwargs):
    if len(args) and isinstance(args[0], Fail):
        return args[0]

    return runner(fn, *args, **kwargs)


def tracks(fn):
    "Wraps a plain function in a Railway two-tracks function."
    return partial(_two_tracked, fn, try_catch)


def true_false_tracks(fn):
    "Wraps a plain function in a Railway two-tracks function."
    return partial(_two_tracked, fn, true_false)
