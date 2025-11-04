# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomConfigurationValidateParams"]


class CustomConfigurationValidateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    pg_conf: Required[str]
    """PostgreSQL configuration"""

    version: Required[str]
    """PostgreSQL version"""
