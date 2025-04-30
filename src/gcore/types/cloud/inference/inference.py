# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..logging import Logging
from .container import Container
from ...._models import BaseModel
from ..inference_probes import InferenceProbes
from ..ingress_opts_out import IngressOptsOut

__all__ = ["Inference"]


class Inference(BaseModel):
    address: Optional[str] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/address/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.address.anyOf[0]"
    """

    auth_enabled: bool
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/auth_enabled'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.auth_enabled"
    """

    command: Optional[str] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/command/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.command.anyOf[0]"
    """

    containers: List[Container]
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/containers'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.containers"
    """

    created_at: Optional[str] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/created_at/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.created_at.anyOf[0]"
    """

    credentials_name: str
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/credentials_name'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.credentials_name"
    """

    description: str
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/description'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.description"
    """

    envs: Optional[Dict[str, str]] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/envs/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.envs.anyOf[0]"
    """

    flavor_name: str
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/flavor_name'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.flavor_name"
    """

    image: str
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/image'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.image"
    """

    ingress_opts: Optional[IngressOptsOut] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/ingress_opts/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.ingress_opts.anyOf[0]"
    """

    listening_port: int
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/listening_port'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.listening_port"
    """

    logging: Optional[Logging] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/logging/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.logging.anyOf[0]"
    """

    name: str
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/name'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.name"
    """

    probes: Optional[InferenceProbes] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/probes/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.probes.anyOf[0]"
    """

    project_id: int
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/project_id'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.project_id"
    """

    status: Literal["ACTIVE", "DELETING", "DEPLOYING", "DISABLED", "PARTIALLYDEPLOYED"]
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/status'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.status"
    """

    timeout: Optional[int] = None
    """
    '#/components/schemas/InferenceInstanceOutSerializerV3/properties/timeout/anyOf/0'
    "$.components.schemas.InferenceInstanceOutSerializerV3.properties.timeout.anyOf[0]"
    """
