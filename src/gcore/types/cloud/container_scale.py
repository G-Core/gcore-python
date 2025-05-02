# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_scale_triggers import ContainerScaleTriggers

__all__ = ["ContainerScale"]


class ContainerScale(BaseModel):
    cooldown_period: Optional[int] = None
    """Cooldown period between scaling actions in seconds"""

    max: int
    """Maximum scale for the container"""

    min: int
    """Minimum scale for the container"""

    polling_interval: Optional[int] = None
    """Polling interval for scaling triggers in seconds"""

    triggers: ContainerScaleTriggers
    """Triggers for scaling actions"""
