# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .inference_application_template import InferenceApplicationTemplate

__all__ = ["InferenceApplicationTemplateList"]


class InferenceApplicationTemplateList(BaseModel):
    count: int
    """Number of objects"""

    results: List[InferenceApplicationTemplate]
    """Objects"""
