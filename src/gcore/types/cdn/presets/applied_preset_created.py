# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AppliedPresetCreated"]


class AppliedPresetCreated(BaseModel):
    object_id: int
    """
    ID of the object (CDN resource or rule, according to the preset `object_type`)
    the preset is applied to.
    """

    preset_id: int
    """ID of the preset that is applied to the object.

    Matches the `preset_id` path parameter.
    """

    message: Optional[str] = None
    """Deprecated.

    Use `preset_id` and `object_id` instead. This field is kept for backward
    compatibility and will be removed in a future version.
    """
