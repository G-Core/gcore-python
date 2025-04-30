# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContainerProbeHTTPGet"]


class ContainerProbeHTTPGet(BaseModel):
    headers: Dict[str, str]
    """
    '#/components/schemas/ContainerProbeHttpGetConfigOutSerializerV2/properties/headers'
    "$.components.schemas.ContainerProbeHttpGetConfigOutSerializerV2.properties.headers"
    """

    host: Optional[str] = None
    """
    '#/components/schemas/ContainerProbeHttpGetConfigOutSerializerV2/properties/host/anyOf/0'
    "$.components.schemas.ContainerProbeHttpGetConfigOutSerializerV2.properties.host.anyOf[0]"
    """

    path: str
    """
    '#/components/schemas/ContainerProbeHttpGetConfigOutSerializerV2/properties/path'
    "$.components.schemas.ContainerProbeHttpGetConfigOutSerializerV2.properties.path"
    """

    port: int
    """
    '#/components/schemas/ContainerProbeHttpGetConfigOutSerializerV2/properties/port'
    "$.components.schemas.ContainerProbeHttpGetConfigOutSerializerV2.properties.port"
    """

    schema_: str = FieldInfo(alias="schema")
    """
    '#/components/schemas/ContainerProbeHttpGetConfigOutSerializerV2/properties/schema'
    "$.components.schemas.ContainerProbeHttpGetConfigOutSerializerV2.properties.schema"
    """
