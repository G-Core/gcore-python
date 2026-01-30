# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ShieldReplaceParams"]


class ShieldReplaceParams(TypedDict, total=False):
    shielding_pop: Optional[int]
    """Shielding location ID.

    If origin shielding is disabled, the parameter value is **null**.
    """
