# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .container_probe_create_param import ContainerProbeCreateParam

__all__ = ["ContainerProbeConfigCreateParam"]


class ContainerProbeConfigCreateParam(TypedDict, total=False):
    enabled: Required[bool]
    """
    '#/components/schemas/InferenceInstanceContainerProbeConfigurationSerializerV2/properties/enabled'
    "$.components.schemas.InferenceInstanceContainerProbeConfigurationSerializerV2.properties.enabled"
    """

    probe: Optional[ContainerProbeCreateParam]
    """
    '#/components/schemas/InferenceInstanceContainerProbeConfigurationSerializerV2/properties/probe/anyOf/0'
    "$.components.schemas.InferenceInstanceContainerProbeConfigurationSerializerV2.properties.probe.anyOf[0]"
    """
