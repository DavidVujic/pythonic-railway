from rails import railway, result, funcs
import csv

CSV_PATH = "./data/example.csv"


@railway.tracks
def parse(path_to_csv_file):
    with open(path_to_csv_file, mode="r") as f:
        return list(csv.DictReader(f))


@railway.tracks
def get_headers(data):
    return data[0].keys()


@railway.true_false_tracks
def has_valid_headers(headers):
    true_or_false = map(lambda header: True if header else False, headers)

    return False not in set(true_or_false)


def print_result(res):
    if result.has_failed(res):
        print(f"Failed at: {res.fn.__name__}. Exception? {res.exception}")
    else:
        print(f"The result is: {res} and the type is {type(res)}")


def with_piped_functions():
    res = funcs.pipe(CSV_PATH, parse, get_headers, has_valid_headers)

    print_result(res)


def with_functions_one_by_one():
    data = parse(CSV_PATH)
    headers = get_headers(data)
    is_valid = has_valid_headers(headers)

    print_result(is_valid)


with_piped_functions()
with_functions_one_by_one()
