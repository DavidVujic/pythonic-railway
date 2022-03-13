from dataclasses import dataclass


@dataclass
class Fail:
    exception: Exception | None
    name: str


def failed(res) -> bool:
    return isinstance(res, Fail)


def succeeded(res) -> bool:
    return not failed(res)
