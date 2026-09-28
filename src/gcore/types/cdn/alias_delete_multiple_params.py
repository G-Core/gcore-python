# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["AliasDeleteMultipleParams"]


class AliasDeleteMultipleParams(TypedDict, total=False):
    cnames: SequenceNotStr[str]
    """Hostnames of the aliases to delete."""

    ids: Iterable[int]
    """IDs of the aliases to delete."""
