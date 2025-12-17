# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DNSMappingEntryParam"]


class DNSMappingEntryParam(TypedDict, total=False):
    cidr4: SequenceNotStr[str]

    cidr6: SequenceNotStr[str]

    tags: SequenceNotStr[str]
