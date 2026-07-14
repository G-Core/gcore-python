# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PresetDetail"]


class PresetDetail(BaseModel):
    id: Optional[int] = None
    """Preset ID."""

    name: Optional[str] = None
    """Preset name."""

    object_type: Optional[Literal["CDNResource", "Rule"]] = None
    """Type of object the preset can be applied to.

    Possible values:

    - **CDNResource** - Preset is applied to a CDN resource.
    - **Rule** - Preset is applied to a rule.
    """

    preset_settings: Optional[Dict[str, object]] = None
    """
    CDN resource or rule settings that the preset applies to the target object,
    including the **options** object.

    The available keys match the writable fields of the object type the preset
    targets (`object_type`). Options included in the preset cannot be edited on the
    object while the preset is applied.
    """

    service: Optional[Literal["cdn"]] = None
    """Service the preset belongs to."""
