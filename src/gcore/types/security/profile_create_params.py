# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ProfileCreateParams", "Field"]


class ProfileCreateParams(TypedDict, total=False):
    fields: Required[Iterable[Field]]

    profile_template: Required[int]

    site: Required[str]
    """Region where the protection profiles will be deployed"""

    ip_address: str
    """Required for Universal template only. Optional for all others."""


class Field(TypedDict, total=False):
    base_field: Required[int]

    field_value: object
