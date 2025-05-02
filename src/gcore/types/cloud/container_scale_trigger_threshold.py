# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContainerScaleTriggerThreshold"]


class ContainerScaleTriggerThreshold(BaseModel):
    threshold: int
    """Threshold value for the trigger in percentage"""
