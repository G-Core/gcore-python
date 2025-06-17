# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InsightSilenceCreateParams"]


class InsightSilenceCreateParams(TypedDict, total=False):
    author: Required[str]
    """The author of the silence"""

    comment: Required[str]
    """A comment explaining the reason for the silence"""

    insight_type: Required[str]
    """The slug of the insight type"""

    labels: Required[Dict[str, str]]
    """A hash table of label names and values that apply to the insight silence"""

    expire_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date and time the silence expires in ISO 8601 format"""
