# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PortConvertParams"]


class PortConvertParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    target_type: Required[Literal["floating_ip"]]
    """Resource type to convert the port to"""
