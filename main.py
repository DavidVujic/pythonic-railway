import sys

import app
import railway

default_path = "./data/example.csv"


def main(path):
    res = app.run(path)

    if railway.failed(res):
        print("Function name", res.name)
        print("Exception", repr(res.exception) if res.exception else None)
        print("args", res.args)
        print("kwargs", res.kwargs)
        return "FAIL"
    else:
        return f"The result is: {res}"


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) >= 2 else default_path
    res = main(path)
    print(res)
