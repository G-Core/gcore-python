# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AppliedPresetFields"]


class AppliedPresetFields(BaseModel):
    """
    Preset applied to the object and the list of object fields that are managed by the preset.
    """

    id: Optional[int] = None
    """ID of the applied preset."""

    deletable: Optional[bool] = None
    """
    Defines whether the applied preset can be unapplied from the object by the
    current user.
    """

    fields: Optional[List[str]] = None
    """Object fields managed by the preset.

    Option fields are prefixed with `options.`.
    """

    name: Optional[str] = None
    """Name of the applied preset."""
