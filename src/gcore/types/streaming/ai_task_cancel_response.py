# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AITaskCancelResponse"]


class AITaskCancelResponse(BaseModel):
    result: Optional[str] = None
    """A textual explicit description of the result of the operation"""
