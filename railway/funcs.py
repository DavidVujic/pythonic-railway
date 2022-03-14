from railway.result import Fail


def try_catch(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return Fail(exception=e, name=fn.__name__, args=args, kwargs=kwargs)


def true_false(fn, *args, **kwargs):
    res = fn(*args, **kwargs)

    return Fail(name=fn.__name__, args=args, kwargs=kwargs) if res is False else res
