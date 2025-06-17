# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..waap_insight_status import WaapInsightStatus

__all__ = ["InsightReplaceParams"]


class InsightReplaceParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    status: Required[WaapInsightStatus]
    """The different statuses an insight can have"""
