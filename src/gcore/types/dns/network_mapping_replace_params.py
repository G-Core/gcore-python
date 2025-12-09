# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .dns_mapping_entry_param import DNSMappingEntryParam

__all__ = ["NetworkMappingReplaceParams"]


class NetworkMappingReplaceParams(TypedDict, total=False):
    body_id: Annotated[int, PropertyInfo(alias="id")]

    mapping: Iterable[DNSMappingEntryParam]

    name: str
