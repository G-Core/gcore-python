# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AnalyticsGetFiltersResponse"]


class AnalyticsGetFiltersResponse(BaseModel):
    """A supported analytics filter value with its observed occurrence count."""

    count: int
    """Number of times this value was observed in the requested range."""

    value: str
    """Value to use in an analytics query for the required filter parameter."""
