from __future__ import annotations

from typing import cast

from httpx import Timeout

from .._constants import DEFAULT_TIMEOUT


def extract_timeout_value(timeout: float | Timeout | None) -> float:
    if isinstance(timeout, float):
        return timeout
    elif isinstance(timeout, Timeout):
        return cast(float, timeout.read)
    elif timeout is None:
        return cast(float, DEFAULT_TIMEOUT.read)
    raise ValueError(
        f"Expected a float or Timeout for timeout, but received {timeout!r}. If you want to use the default timeout, pass None."
    )
