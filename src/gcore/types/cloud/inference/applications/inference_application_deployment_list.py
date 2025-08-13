# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .inference_application_deployment import InferenceApplicationDeployment

__all__ = ["InferenceApplicationDeploymentList"]


class InferenceApplicationDeploymentList(BaseModel):
    count: int
    """Number of objects"""

    results: List[InferenceApplicationDeployment]
    """Objects"""
