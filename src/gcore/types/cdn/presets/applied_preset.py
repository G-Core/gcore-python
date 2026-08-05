# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AppliedPreset"]


class AppliedPreset(BaseModel):
    object_ids: List[int]
    """IDs of the objects the preset is currently applied to.

    Empty when the preset is not applied to anything.
    """

    object_type: str
    """Type of objects the preset is applied to."""

    message: Optional[str] = None
    """Deprecated.

    Present only when `object_ids` is empty. Check `object_ids` instead. This field
    is kept for backward compatibility and will be removed in a future version.
    """
