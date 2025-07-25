# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AITaskGetAISettingsResponse"]


class AITaskGetAISettingsResponse(BaseModel):
    supported: Optional[bool] = None
    """Is the given language pair supported for transcription and translation?"""
