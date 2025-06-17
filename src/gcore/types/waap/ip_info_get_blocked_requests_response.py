# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_rule_blocked_requests import WaapRuleBlockedRequests

__all__ = ["IPInfoGetBlockedRequestsResponse"]

IPInfoGetBlockedRequestsResponse: TypeAlias = List[WaapRuleBlockedRequests]
