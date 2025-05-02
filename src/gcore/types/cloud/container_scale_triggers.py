# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_scale_trigger_sqs import ContainerScaleTriggerSqs
from .container_scale_trigger_rate import ContainerScaleTriggerRate
from .container_scale_trigger_threshold import ContainerScaleTriggerThreshold

__all__ = ["ContainerScaleTriggers"]


class ContainerScaleTriggers(BaseModel):
    cpu: Optional[ContainerScaleTriggerThreshold] = None
    """CPU trigger configuration"""

    gpu_memory: Optional[ContainerScaleTriggerThreshold] = None
    """GPU memory trigger configuration.

    Calculated by DCGM_FI_DEV_MEM_COPY_UTIL metric
    """

    gpu_utilization: Optional[ContainerScaleTriggerThreshold] = None
    """GPU utilization trigger configuration.

    Calculated by DCGM_FI_DEV_GPU_UTIL metric
    """

    http: Optional[ContainerScaleTriggerRate] = None
    """HTTP trigger configuration"""

    memory: Optional[ContainerScaleTriggerThreshold] = None
    """Memory trigger configuration"""

    sqs: Optional[ContainerScaleTriggerSqs] = None
    """SQS trigger configuration"""
