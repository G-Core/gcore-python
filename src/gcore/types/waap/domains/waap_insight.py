# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WaapInsight"]


class WaapInsight(BaseModel):
    id: str
    """A generated unique identifier for the insight"""

    description: str
    """The description of the insight"""

    first_seen: datetime
    """The date and time the insight was first seen in ISO 8601 format"""

    insight_type: str
    """The slug of the insight type"""

    labels: Dict[str, str]
    """A hash table of label names and values that apply to the insight"""

    last_seen: datetime
    """The date and time the insight was last seen in ISO 8601 format"""

    last_status_change: datetime
    """The date and time the insight was last seen in ISO 8601 format"""

    recommendation: str
    """The recommended action to perform to resolve the insight"""

    status: Literal["OPEN", "ACKED", "CLOSED"]
    """The status of the insight"""
