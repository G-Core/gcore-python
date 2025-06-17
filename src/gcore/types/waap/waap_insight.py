# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from ..._models import BaseModel
from .waap_insight_status import WaapInsightStatus

__all__ = ["WaapInsight"]


class WaapInsight(BaseModel):
    id: str
    """A generated unique identifier for the insight"""

    description: str
    """The description of the insight"""

    first_seen: datetime
    """The date and time the insight was first seen in ISO 8601 format"""

    insight_type: str
    """The type of the insight represented as a slug"""

    labels: Dict[str, str]
    """A hash table of label names and values that apply to the insight"""

    last_seen: datetime
    """The date and time the insight was last seen in ISO 8601 format"""

    last_status_change: datetime
    """The date and time the insight was last seen in ISO 8601 format"""

    recommendation: str
    """The recommended action to perform to resolve the insight"""

    status: WaapInsightStatus
    """The different statuses an insight can have"""
