# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapRuleBlockedRequests"]


class WaapRuleBlockedRequests(BaseModel):
    action: str
    """The action taken by the rule"""

    count: int
    """The number of requests blocked by the rule"""

    rule_name: str
    """The name of the rule that blocked the request"""
