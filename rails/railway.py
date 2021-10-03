from functools import partial
from . import adapter, result


def _two_tracked(fn, runner, *args, **kwargs):
    if len(args) and isinstance(args[0], result.Fail):
        return args[0]

    return runner(fn, *args, **kwargs)


def tracks(fn):
    "Wraps a plain function in a Railway two-tracks function."
    return partial(_two_tracked, fn, adapter.try_catch)


def true_false_tracks(fn):
    "Wraps a plain function in a Railway two-tracks function."
    return partial(_two_tracked, fn, adapter.true_false)
