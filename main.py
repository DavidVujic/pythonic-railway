from rails import railway, result, funcs


@railway.tracks
def fn1(arg) -> float:
    return 4.2


@railway.tracks
def fn2(arg) -> tuple:
    # raise Exception("KABOOM")
    return "Hello", arg


@railway.true_false_tracks
def fn3(arg) -> bool:
    return True


@railway.tracks
def fn4(args) -> str:
    return f"{args} Hello World"


def print_result(res):
    if result.has_failed(res):
        print(f"Failed at: {res.fn.__name__}. Exception? {res.exception}")
    else:
        print(f"The result is: {res} and the type is {type(res)}")


def with_piped_functions():
    res = funcs.pipe(fn1, fn2, fn3, fn4)

    print_result(res)


def with_functions_one_by_one():
    a = fn1(None)
    b = fn2(a)
    c = fn3(b)
    d = fn4(c)

    print_result(d)


# with_piped_functions()
# with_functions_one_by_one()
