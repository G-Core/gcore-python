# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..deploy_status import DeployStatus
from ..container_scale import ContainerScale

__all__ = ["Container"]


class Container(BaseModel):
    address: Optional[str] = None
    """
    '#/components/schemas/ContainerOutSerializerV3/properties/address/anyOf/0'
    "$.components.schemas.ContainerOutSerializerV3.properties.address.anyOf[0]"
    """

    deploy_status: DeployStatus
    """
    '#/components/schemas/ContainerOutSerializerV3/properties/deploy_status'
    "$.components.schemas.ContainerOutSerializerV3.properties.deploy_status"
    """

    error_message: Optional[str] = None
    """
    '#/components/schemas/ContainerOutSerializerV3/properties/error_message/anyOf/0'
    "$.components.schemas.ContainerOutSerializerV3.properties.error_message.anyOf[0]"
    """

    region_id: int
    """
    '#/components/schemas/ContainerOutSerializerV3/properties/region_id'
    "$.components.schemas.ContainerOutSerializerV3.properties.region_id"
    """

    scale: ContainerScale
    """
    '#/components/schemas/ContainerOutSerializerV3/properties/scale'
    "$.components.schemas.ContainerOutSerializerV3.properties.scale"
    """
