# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["WaapInsightType"]


class WaapInsightType(BaseModel):
    description: str
    """The description of the insight type"""

    insight_frequency: int
    """The frequency of the insight type"""

    insight_grouping_dimensions: List[str]
    """The grouping dimensions of the insight type"""

    insight_template: str
    """The insight template"""

    labels: List[str]
    """The labels of the insight type"""

    name: str
    """The name of the insight type"""

    recommendation_template: str
    """The recommendation template"""

    slug: str
    """The slug of the insight type"""
