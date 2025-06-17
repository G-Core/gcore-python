# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .waap_advanced_rule_descriptor import WaapAdvancedRuleDescriptor

__all__ = ["WaapAdvancedRuleDescriptorList"]


class WaapAdvancedRuleDescriptorList(BaseModel):
    version: str
    """The descriptor's version"""

    objects: Optional[List[WaapAdvancedRuleDescriptor]] = None
