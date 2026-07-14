# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AppliedApplyParams"]


class AppliedApplyParams(TypedDict, total=False):
    object_id: Required[int]
    """
    ID of the object (CDN resource or rule, according to the preset `object_type`)
    to apply the preset to.
    """
