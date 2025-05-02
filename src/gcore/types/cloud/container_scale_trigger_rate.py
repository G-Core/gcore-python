# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContainerScaleTriggerRate"]


class ContainerScaleTriggerRate(BaseModel):
    rate: int
    """Request count per 'window' seconds for the http trigger"""

    window: int
    """Time window for rate calculation in seconds"""
