# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_rule_set import WaapRuleSet

__all__ = ["DomainListRuleSetsResponse"]

DomainListRuleSetsResponse: TypeAlias = List[WaapRuleSet]
