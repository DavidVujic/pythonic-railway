import sys
import app
from rails import result

default_path = "./data/example.csv"


def main(path):
    res = app.run(path)

    if result.failed(res):
        return (
            f"Failed at: {res.fn.__name__}. "
            f"{repr(res.exception) if res.exception else ''}"
        )
    else:
        return f"The result is: {res} and the type is {type(res)}"


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) >= 2 else default_path
    res = main(path)
    print(res)
