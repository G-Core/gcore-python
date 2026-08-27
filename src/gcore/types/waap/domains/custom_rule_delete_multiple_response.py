# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["CustomRuleDeleteMultipleResponse"]


class CustomRuleDeleteMultipleResponse(BaseModel):
    deleted_ids: Optional[List[int]] = None
    """Rules IDs deleted by the operation"""
