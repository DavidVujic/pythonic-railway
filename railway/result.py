from dataclasses import dataclass
from typing import Any


@dataclass
class Fail:
    exception: Exception | None = None
    name: str | None = None
    args: Any = None
    kwargs: Any = None


def failed(res) -> bool:
    return isinstance(res, Fail)


def succeeded(res) -> bool:
    return not failed(res)
