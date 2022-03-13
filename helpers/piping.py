from functools import reduce


def pipe(*sequence):
    """Combines a sequence of an input arg and following functions,
    from left-to-right. The output from the first function is the input
    for the next one"""
    return reduce(lambda arg, fn: fn(arg), sequence[1:], sequence[0])
