# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LaasIndexRetentionPolicyParam"]


class LaasIndexRetentionPolicyParam(TypedDict, total=False):
    period: Required[Optional[int]]
    """Duration of days for which logs must be kept."""
