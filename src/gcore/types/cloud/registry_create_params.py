# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegistryCreateParams"]


class RegistryCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    name: Required[str]
    """
    A name for the container registry. Should be in lowercase, consisting only of
    numbers, letters and -, with maximum length of 24 characters
    """

    storage_limit: int
    """Registry storage limit, GiB"""
