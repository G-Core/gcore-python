# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CDNAccountLimits"]


class CDNAccountLimits(BaseModel):
    id: Optional[int] = None
    """Account ID."""

    origins_in_group_limit: Optional[int] = None
    """
    Maximum number of origins that can be added to the origin group on your tariff
    plan.
    """

    prefetch_pattern_limit: Optional[int] = None
    """Maximum number of patterns per prefetch request."""

    prefetch_request_limit: Optional[str] = None
    """Rate limit for prefetch requests."""

    purge_by_urls_request_limit: Optional[str] = None
    """Rate limit for purge-by-URL requests."""

    purge_max_urls_limit: Optional[int] = None
    """Maximum number of URLs per purge-by-URL request."""

    purge_pattern_limit: Optional[int] = None
    """Maximum number of patterns per purge request."""

    purge_request_limit: Optional[str] = None
    """Rate limit for purge-by-pattern requests."""

    resources_limit: Optional[int] = None
    """Maximum number of CDN resources that can be created on your tariff plan."""

    rules_limit: Optional[int] = None
    """
    Maximum number of rules that can be created per CDN resource on your tariff
    plan.
    """

    secondary_hostnames_limit: Optional[int] = None
    """Maximum number of secondary hostnames (additional CNAMEs) per CDN resource."""
