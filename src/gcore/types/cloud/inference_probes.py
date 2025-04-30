# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_probe_config import ContainerProbeConfig

__all__ = ["InferenceProbes"]


class InferenceProbes(BaseModel):
    liveness_probe: Optional[ContainerProbeConfig] = None
    """
    '#/components/schemas/InferenceInstanceProbesOutSerializerV2/properties/liveness_probe/anyOf/0'
    "$.components.schemas.InferenceInstanceProbesOutSerializerV2.properties.liveness_probe.anyOf[0]"
    """

    readiness_probe: Optional[ContainerProbeConfig] = None
    """
    '#/components/schemas/InferenceInstanceProbesOutSerializerV2/properties/readiness_probe/anyOf/0'
    "$.components.schemas.InferenceInstanceProbesOutSerializerV2.properties.readiness_probe.anyOf[0]"
    """

    startup_probe: Optional[ContainerProbeConfig] = None
    """
    '#/components/schemas/InferenceInstanceProbesOutSerializerV2/properties/startup_probe/anyOf/0'
    "$.components.schemas.InferenceInstanceProbesOutSerializerV2.properties.startup_probe.anyOf[0]"
    """
