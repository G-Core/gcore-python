# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CdnAvailableFeatures", "FreeFeature", "PaidFeature"]


class FreeFeature(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8601/RFC 3339 format, UTC.)"""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Feature name."""


class PaidFeature(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8601/RFC 3339 format, UTC.)"""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Feature name."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""


class CdnAvailableFeatures(BaseModel):
    id: Optional[int] = None
    """Account ID."""

    free_features: Optional[List[FreeFeature]] = None
    """Free features available for your account."""

    paid_features: Optional[List[PaidFeature]] = None
    """Paid features available for your account."""
