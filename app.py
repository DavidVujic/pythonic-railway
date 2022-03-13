import csv

import railway
from helpers import piping


@railway.tracks
def _parse(path_to_csv_file):
    with open(path_to_csv_file, mode="r") as f:
        return list(csv.DictReader(f))


@railway.tracks
def _get_headers(data):
    return data[0].keys()


@railway.tracks_boolean
def _has_valid_headers(headers):
    true_or_false = map(lambda header: True if header else False, headers)

    return False not in set(true_or_false)


def run(path):
    return piping.pipe(path, _parse, _get_headers, _has_valid_headers)


def run_each_function_one_by_one(path):
    data = _parse(path)
    headers = _get_headers(data)
    is_valid = _has_valid_headers(headers)

    return is_valid
