# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContainerScaleTriggerRate"]


class ContainerScaleTriggerRate(BaseModel):
    rate: int
    """
    '#/components/schemas/ContainerScaleTriggersRateOutSerializer/properties/rate'
    "$.components.schemas.ContainerScaleTriggersRateOutSerializer.properties.rate"
    """

    window: int
    """
    '#/components/schemas/ContainerScaleTriggersRateOutSerializer/properties/window'
    "$.components.schemas.ContainerScaleTriggersRateOutSerializer.properties.window"
    """
