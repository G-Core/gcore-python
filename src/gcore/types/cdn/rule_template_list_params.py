# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RuleTemplateListParams"]


class RuleTemplateListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return in the response. Cannot exceed 1000."""

    offset: int
    """Number of items to skip from the beginning of the list."""
