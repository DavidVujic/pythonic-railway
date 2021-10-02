from rail import railway, result


@railway.tracks
def fn1(arg) -> float:
    return 4.2


@railway.tracks
def fn2(arg) -> tuple:
    # raise Exception("KABOOM")
    return "Hello", arg


@railway.boolean_tracks
def fn3(arg) -> bool:
    return True


@railway.tracks
def fn4(args) -> str:
    return f"{args} Hello World"


res = railway.pipe(fn1, fn2, fn3, fn4)

if isinstance(res, result.Fail):
    print(f"Failed at: {res.fn.__name__}. Exception? {res.exception}")
else:
    print(f"The result is: {res}")
