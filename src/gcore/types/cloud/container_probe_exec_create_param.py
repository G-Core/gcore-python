# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ContainerProbeExecCreateParam"]


class ContainerProbeExecCreateParam(TypedDict, total=False):
    command: Required[List[str]]
    """Command to be executed inside the running container."""
