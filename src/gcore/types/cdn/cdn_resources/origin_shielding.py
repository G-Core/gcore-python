# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["OriginShielding"]


class OriginShielding(BaseModel):
    shielding_pop: Optional[int] = None
    """Shielding location ID.

    If origin shielding is disabled, the parameter value is **null**.
    """
