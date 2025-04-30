# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_scale_triggers import ContainerScaleTriggers

__all__ = ["ContainerScale"]


class ContainerScale(BaseModel):
    cooldown_period: Optional[int] = None
    """
    '#/components/schemas/ContainerScaleOutSerializerV3/properties/cooldown_period/anyOf/0'
    "$.components.schemas.ContainerScaleOutSerializerV3.properties.cooldown_period.anyOf[0]"
    """

    max: int
    """
    '#/components/schemas/ContainerScaleOutSerializerV3/properties/max'
    "$.components.schemas.ContainerScaleOutSerializerV3.properties.max"
    """

    min: int
    """
    '#/components/schemas/ContainerScaleOutSerializerV3/properties/min'
    "$.components.schemas.ContainerScaleOutSerializerV3.properties.min"
    """

    polling_interval: Optional[int] = None
    """
    '#/components/schemas/ContainerScaleOutSerializerV3/properties/polling_interval/anyOf/0'
    "$.components.schemas.ContainerScaleOutSerializerV3.properties.polling_interval.anyOf[0]"
    """

    triggers: ContainerScaleTriggers
    """
    '#/components/schemas/ContainerScaleOutSerializerV3/properties/triggers'
    "$.components.schemas.ContainerScaleOutSerializerV3.properties.triggers"
    """
