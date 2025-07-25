# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["QualitySets", "Live", "LiveQuality", "Vod", "VodQuality"]


class LiveQuality(BaseModel):
    id: Optional[int] = None
    """ID of the quality"""

    name: Optional[str] = None
    """Name of the quality"""


class Live(BaseModel):
    id: Optional[int] = None
    """ID of the custom quality set"""

    default: Optional[bool] = None
    """States if this preset is default for a client profile"""

    name: Optional[str] = None
    """Human readable name of the quality set"""

    qualities: Optional[List[LiveQuality]] = None
    """Array of associated qualities"""


class VodQuality(BaseModel):
    id: Optional[int] = None
    """ID of the quality"""

    name: Optional[str] = None
    """Name of the quality"""


class Vod(BaseModel):
    id: Optional[int] = None
    """ID of the custom quality set"""

    default: Optional[bool] = None
    """States if this preset is default for a client profile"""

    name: Optional[str] = None
    """Human readable name of the quality set"""

    qualities: Optional[List[VodQuality]] = None
    """Array of associated qualities"""


class QualitySets(BaseModel):
    live: Optional[List[Live]] = None

    vod: Optional[List[Vod]] = None
