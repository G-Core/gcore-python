# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileTemplateListParams"]


class ProfileTemplateListParams(TypedDict, total=False):
    accepts_ip_address: bool
    """
    Keep only templates that require a protected `ip_address` per profile (true), or
    only templates whose protected addresses are hardcoded (false). Omit to get
    every template.
    """
