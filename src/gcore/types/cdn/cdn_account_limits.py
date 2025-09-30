# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CdnAccountLimits"]


class CdnAccountLimits(BaseModel):
    id: Optional[int] = None
    """Account ID."""

    origins_in_group_limit: Optional[int] = None
    """
    Maximum number of origins that can be added to the origin group on your tariff
    plan.
    """

    resources_limit: Optional[int] = None
    """Maximum number of CDN resources that can be created on your tariff plan."""

    rules_limit: Optional[int] = None
    """
    Maximum number of rules that can be created per CDN resource on your tariff
    plan.
    """
