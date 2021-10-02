from rail.railway import pipe, Fail


def fn1(arg) -> float:
    return 4.2


def fn2(arg) -> tuple:
    raise Exception("KABOOM")
    return round(arg * 10), "hello"


def fn3(args) -> str:
    val = args[0]
    message = args[1]
    return f"{message} world {val}"


res = pipe(fn1, fn2, fn3)

if isinstance(res, Fail):
    print(f"Failed at: {res.fn.__name__}. Exception: {res.exception}")
else:
    print(f"The result is: {res}")
