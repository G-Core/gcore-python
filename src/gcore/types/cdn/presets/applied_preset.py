# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["AppliedPreset", "AppliedObjects", "NoAppliedObjects"]


class AppliedObjects(BaseModel):
    object_ids: Optional[List[int]] = None
    """IDs of the objects the preset is currently applied to."""

    object_type: Optional[str] = None
    """Type of objects the preset is applied to."""


class NoAppliedObjects(BaseModel):
    message: Optional[str] = None


AppliedPreset: TypeAlias = Union[AppliedObjects, NoAppliedObjects]
