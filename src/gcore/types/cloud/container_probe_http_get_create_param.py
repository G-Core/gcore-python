# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContainerProbeHTTPGetCreateParam"]


class ContainerProbeHTTPGetCreateParam(TypedDict, total=False):
    port: Required[int]
    """
    '#/components/schemas/ContainerProbeHttpGetConfigSerializerV2/properties/port'
    "$.components.schemas.ContainerProbeHttpGetConfigSerializerV2.properties.port"
    """

    headers: Dict[str, str]
    """
    '#/components/schemas/ContainerProbeHttpGetConfigSerializerV2/properties/headers'
    "$.components.schemas.ContainerProbeHttpGetConfigSerializerV2.properties.headers"
    """

    host: Optional[str]
    """
    '#/components/schemas/ContainerProbeHttpGetConfigSerializerV2/properties/host/anyOf/0'
    "$.components.schemas.ContainerProbeHttpGetConfigSerializerV2.properties.host.anyOf[0]"
    """

    path: str
    """
    '#/components/schemas/ContainerProbeHttpGetConfigSerializerV2/properties/path'
    "$.components.schemas.ContainerProbeHttpGetConfigSerializerV2.properties.path"
    """

    schema: str
    """
    '#/components/schemas/ContainerProbeHttpGetConfigSerializerV2/properties/schema'
    "$.components.schemas.ContainerProbeHttpGetConfigSerializerV2.properties.schema"
    """
