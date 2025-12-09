# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DNSMappingEntryParam"]


class DNSMappingEntryParam(TypedDict, total=False):
    cidr4: Iterable[object]

    cidr6: Iterable[object]

    tags: SequenceNotStr[str]
