# A Pythonic Railway

This is an attempt to implement a lightweight, or perhaps a sloppy,
version of Railway Oriented Programming in Python.

What I'm trying to achieve with the example code in this repo,
is to use the functional concepts of Railway Oriented Programming.
At the same time I want to keep a Pythonic mindset, and not go all-in functional.

## Why Railways?
As I understand Railway Oriented Programming, it is about adding error handling and still keeping a "happy path" style in the code.
This is done by wrapping or decorating functions.

The functions are wrapped (or decorated, as in the examples in this repo) to catch failures. The output of a failed function call will
be the input to the next one. The next function will choose track based on the input: the success track or the fail track.

By using a two-tracked approach in functions, the error handling will be separated from the program.

Functions will be less cluttered with `try except` error handling and also `if else` flow control clauses. In many cases,
this will mean that the amount of code within functions will be a lot less. Less is more.


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
by wrapping the function call. If the code in the function causes an 💥 Exception 💥 (such as an IndexError or TypeError),
an object of `Fail` type will be returned. The following functions will be bypassed when a `Fail`
object is passed in as an argument.

If all goes well, the data will be returned, just as it would without the decorator.

_Side note: In a proper Railway Oriented Programming implementation,
a `Success` object should be returned. But I think that
just returning the data has a nice keep-it-simple approach._

There's also a `true-false` wrapper for boolean functions. This one can be used when
a `False` result should exit the sequence. The wrapper creates a two-track function that will
return a `Fail` object if the result is `False`. The following functions in the sequence will be
bypassed.

``` python
@railway.tracks_boolean
def has_valid_headers(headers):
    true_or_false = map(lambda header: True if header else False, headers)

    return False not in set(true_or_false)
```

## Some syntactic sugar
In the `funcs` module contains functionality to implement a functions pipeline.
This one is inspired by threading macros in Clojure.

The first argument to `pipe` is the input value to the first function in the sequence.
The output from the first function is the input to the next one.
``` python
res = pipe("path/to/file.csv", parse, get_headers, has_valid_headers)
```

Or, without the pipe function:

``` python
data = parse("path/to/file.csv")
headers = get_headers(data)
is_valid = has_valid_headers(headers)
```

If something has gone wrong somewhere in the sequence, `res` will be a `Fail` object.
Otherwise it will be the output from the last function in the sequence.

## References
Don't miss the NDC London talk
[Railway oriented programming: Error handling in functional languages by Scott Wlaschin](https://vimeo.com/113707214)

Do you want to go all-in functional Python? Have a look at [returns](https://returns.readthedocs.io/en/latest/index.html)
and [toolz](https://github.com/pytoolz/toolz)
