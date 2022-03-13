import sys

import app
import railway

default_path = "./data/example.csv"


def main(path):
    res = app.run(path)

    if railway.failed(res):
        return f"Function={res.name} Error={repr(res.exception) if res.exception else 'empty'}"
    else:
        return f"The result is: {res}"


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) >= 2 else default_path
    res = main(path)
    print(res)
