# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_probe import ContainerProbe

__all__ = ["ContainerProbeConfig"]


class ContainerProbeConfig(BaseModel):
    enabled: bool
    """
    '#/components/schemas/InferenceInstanceContainerProbeConfigurationOutSerializerV2/properties/enabled'
    "$.components.schemas.InferenceInstanceContainerProbeConfigurationOutSerializerV2.properties.enabled"
    """

    probe: Optional[ContainerProbe] = None
    """
    '#/components/schemas/InferenceInstanceContainerProbeConfigurationOutSerializerV2/properties/probe/anyOf/0'
    "$.components.schemas.InferenceInstanceContainerProbeConfigurationOutSerializerV2.properties.probe.anyOf[0]"
    """
