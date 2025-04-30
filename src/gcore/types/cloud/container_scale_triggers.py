# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_scale_trigger_sqs import ContainerScaleTriggerSqs
from .container_scale_trigger_rate import ContainerScaleTriggerRate
from .container_scale_trigger_threshold import ContainerScaleTriggerThreshold

__all__ = ["ContainerScaleTriggers"]


class ContainerScaleTriggers(BaseModel):
    cpu: Optional[ContainerScaleTriggerThreshold] = None
    """
    '#/components/schemas/ContainerScaleTriggersOutSerializer/properties/cpu/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersOutSerializer.properties.cpu.anyOf[0]"
    """

    gpu_memory: Optional[ContainerScaleTriggerThreshold] = None
    """
    '#/components/schemas/ContainerScaleTriggersOutSerializer/properties/gpu_memory/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersOutSerializer.properties.gpu_memory.anyOf[0]"
    """

    gpu_utilization: Optional[ContainerScaleTriggerThreshold] = None
    """
    '#/components/schemas/ContainerScaleTriggersOutSerializer/properties/gpu_utilization/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersOutSerializer.properties.gpu_utilization.anyOf[0]"
    """

    http: Optional[ContainerScaleTriggerRate] = None
    """
    '#/components/schemas/ContainerScaleTriggersOutSerializer/properties/http/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersOutSerializer.properties.http.anyOf[0]"
    """

    memory: Optional[ContainerScaleTriggerThreshold] = None
    """
    '#/components/schemas/ContainerScaleTriggersOutSerializer/properties/memory/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersOutSerializer.properties.memory.anyOf[0]"
    """

    sqs: Optional[ContainerScaleTriggerSqs] = None
    """
    '#/components/schemas/ContainerScaleTriggersOutSerializer/properties/sqs/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersOutSerializer.properties.sqs.anyOf[0]"
    """
