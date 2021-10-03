from functools import reduce


def pipe(*functions):
    """Combines functions from left-to-right.
    The output from a function is the input for the next one"""
    return reduce(lambda arg, fn: fn(arg), functions, None)
