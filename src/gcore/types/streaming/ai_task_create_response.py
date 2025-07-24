# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AITaskCreateResponse"]


class AITaskCreateResponse(BaseModel):
    task_id: str
    """ID of the created AI task, from which you can get the execution result"""
