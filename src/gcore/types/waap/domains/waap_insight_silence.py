# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["WaapInsightSilence"]


class WaapInsightSilence(BaseModel):
    id: str
    """A generated unique identifier for the silence"""

    author: str
    """The author of the silence"""

    comment: str
    """A comment explaining the reason for the silence"""

    expire_at: Optional[datetime] = None
    """The date and time the silence expires in ISO 8601 format"""

    insight_type: str
    """The slug of the insight type"""

    labels: Dict[str, str]
    """A hash table of label names and values that apply to the insight silence"""
