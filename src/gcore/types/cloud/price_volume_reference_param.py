# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PriceVolumeReferenceParam"]


class PriceVolumeReferenceParam(TypedDict, total=False):
    volume_id: Required[str]
    """Existing volume."""
