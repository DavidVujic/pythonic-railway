# A Pythonic Railway

This is an attempt to implement a lightweight, or perhaps a sloppy,
version of Railway Oriented Programming in Python.

What I'm trying to achieve with the example code in this repo,
is to use the functional concepts of Railway Oriented Programming,
but still keep a Pythonic mindset.

## What's in this repo?
Turn a single track function, into a two-track Railway by using decorators.

before:

``` python
def get_headers(data):
    return data[0].keys()
```

after:

``` python
@railway.tracks
def get_headers(data):
    return data[0].keys()
```

The `tracks` decorator will turn the `get_headers` function into a two-tracked railway,
by wrapping the function call using an adapter. If the function call causes an Exception,
an object of `Fail` type will be returned.

If all goes well, the data will be returned as without the decorator.

_Side note: In a proper Railway Oriented Programming implementation,
a `Success` object should be returned. But I think that
just returning the data has a nice keep it simple approach._

There's also a `true-false` adapter for boolean functions. This one could be used to
take the failed railway track, bypassing the rest of the flow, when the return value from
the decorated function is `False`.

## Some syntactic sugar
In the `funcs` module contains functionality to implement a functions pipeline.
This one is inspired by threading macros in Clojure.

The first argument to `pipe` is the input value to the first function in the sequence.
The output from the first function is the input to the next one.
``` python
res = funcs.pipe(arg, func1, func2, func3)
```

If something has gone wrong somewhere in the sequence, `res` will be a `Fail` object.
Otherwise it will be the output from the last function in the sequence.


## References
Don't miss the NDC London talk
[Railway oriented programming: Error handling in functional languages by Scott Wlaschin](https://vimeo.com/113707214)

Do you want to go all-in functional Python? Have a look at (returns)[https://returns.readthedocs.io/en/latest/index.html]
