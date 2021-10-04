# A Pythonic Railway

This is an attempt to implement a lightweight, or perhaps sloppy, version of Railway Oriented Programming in Python.

What I'm trying to achieve with the example code in this repo, is to use the functional concepts of Railway Oriented Programming,
but still keep a Pythonic mindset.

## Functions

``` python
def parse(path_to_csv_file):
    with open(path_to_csv_file, mode="r") as f:
        return list(csv.DictReader(f))


def get_headers(data):
    return data[0].keys()


def has_valid_headers(headers):
    true_or_false = map(lambda header: True if header else False, headers)
    return False not in set(true_or_false)
```
