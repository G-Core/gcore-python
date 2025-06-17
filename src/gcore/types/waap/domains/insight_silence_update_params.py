# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InsightSilenceUpdateParams"]


class InsightSilenceUpdateParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    author: Required[str]
    """The author of the silence"""

    comment: Required[str]
    """A comment explaining the reason for the silence"""

    expire_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]
    """The date and time the silence expires in ISO 8601 format"""

    labels: Dict[str, str]
    """A hash table of label names and values that apply to the insight silence"""
