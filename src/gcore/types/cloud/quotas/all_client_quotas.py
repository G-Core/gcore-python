# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .global_quotas import GlobalQuotas
from .regional_quotas import RegionalQuotas

__all__ = ["AllClientQuotas"]


class AllClientQuotas(BaseModel):
    global_quotas: Optional[GlobalQuotas] = None
    """Global entity quotas"""

    regional_quotas: Optional[List[RegionalQuotas]] = None
    """Regional entity quotas. Only contains initialized quotas."""
