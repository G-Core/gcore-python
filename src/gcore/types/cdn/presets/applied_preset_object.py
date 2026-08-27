# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["AppliedPresetObject"]


class AppliedPresetObject(BaseModel):
    """A single object the preset is applied to."""

    object_id: int
    """
    ID of the object (CDN resource or rule, according to the preset `object_type`)
    the preset is applied to.
    """

    preset_id: int
    """ID of the preset that is applied to the object.

    Matches the `preset_id` path parameter.
    """
