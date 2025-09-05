# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProfileReplaceParams", "Field"]


class ProfileReplaceParams(TypedDict, total=False):
    fields: Required[Iterable[Field]]

    profile_template: Required[int]

    ip_address: Optional[str]

    site: str


class Field(TypedDict, total=False):
    base_field: Required[int]

    field_value: Optional[Dict[str, object]]
