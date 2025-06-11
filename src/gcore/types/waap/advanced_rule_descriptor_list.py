# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .advanced_rule_descriptor import AdvancedRuleDescriptor

__all__ = ["AdvancedRuleDescriptorList"]


class AdvancedRuleDescriptorList(BaseModel):
    version: str
    """The descriptor's version"""

    objects: Optional[List[AdvancedRuleDescriptor]] = None
