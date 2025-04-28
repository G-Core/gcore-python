# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .access_rule import AccessRule

__all__ = ["AccessRuleList"]


class AccessRuleList(BaseModel):
    count: int
    """
    '#/components/schemas/AccessRuleCollectionSerializer/properties/count'
    "$.components.schemas.AccessRuleCollectionSerializer.properties.count"
    """

    results: List[AccessRule]
    """
    '#/components/schemas/AccessRuleCollectionSerializer/properties/results'
    "$.components.schemas.AccessRuleCollectionSerializer.properties.results"
    """
