from . import result


def try_catch(fn, *args, **kwargs):
    """A try-catch two-tracks adapter"""
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return result.Fail(fn=fn, exception=e)


def true_false(fn, *args, **kwargs):
    """A boolean two-tracks adapter"""
    res = fn(*args, **kwargs)

    if res is False:
        return result.Fail(fn=fn)
    return res
