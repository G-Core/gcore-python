# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SecretListParams"]


class SecretListParams(TypedDict, total=False):
    app_id: int
    """App ID"""

    secret_name: str
    """Secret name"""
