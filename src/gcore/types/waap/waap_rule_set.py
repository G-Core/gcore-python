# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .waap_domain_policy import WaapDomainPolicy

__all__ = ["WaapRuleSet", "Tag"]


class Tag(BaseModel):
    id: int
    """Identifier of the tag."""

    description: str
    """Detailed description of the tag."""

    name: str
    """Name of the tag."""


class WaapRuleSet(BaseModel):
    id: int
    """Identifier of the rule set."""

    description: str
    """Detailed description of the rule set."""

    is_active: bool
    """Indicates if the rule set is currently active."""

    name: str
    """Name of the rule set."""

    tags: List[Tag]
    """Collection of tags associated with the rule set."""

    resource_slug: Optional[str] = None
    """The resource slug associated with the rule set."""

    rules: Optional[List[WaapDomainPolicy]] = None
