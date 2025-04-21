# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Secret"]


class Secret(BaseModel):
    id: str
    """
    '#/components/schemas/SecretSerializer/properties/id'
    "$.components.schemas.SecretSerializer.properties.id"
    """

    name: str
    """
    '#/components/schemas/SecretSerializer/properties/name'
    "$.components.schemas.SecretSerializer.properties.name"
    """

    secret_type: Literal["certificate", "opaque", "passphrase", "private", "public", "symmetric"]
    """
    '#/components/schemas/SecretSerializer/properties/secret_type'
    "$.components.schemas.SecretSerializer.properties.secret_type"
    """

    status: str
    """
    '#/components/schemas/SecretSerializer/properties/status'
    "$.components.schemas.SecretSerializer.properties.status"
    """

    algorithm: Optional[str] = None
    """
    '#/components/schemas/SecretSerializer/properties/algorithm/anyOf/0'
    "$.components.schemas.SecretSerializer.properties.algorithm.anyOf[0]"
    """

    bit_length: Optional[int] = None
    """
    '#/components/schemas/SecretSerializer/properties/bit_length/anyOf/0'
    "$.components.schemas.SecretSerializer.properties.bit_length.anyOf[0]"
    """

    content_types: Optional[Dict[str, str]] = None
    """
    '#/components/schemas/SecretSerializer/properties/content_types/anyOf/0'
    "$.components.schemas.SecretSerializer.properties.content_types.anyOf[0]"
    """

    created: Optional[datetime] = None
    """
    '#/components/schemas/SecretSerializer/properties/created/anyOf/0'
    "$.components.schemas.SecretSerializer.properties.created.anyOf[0]"
    """

    expiration: Optional[datetime] = None
    """
    '#/components/schemas/SecretSerializer/properties/expiration/anyOf/0'
    "$.components.schemas.SecretSerializer.properties.expiration.anyOf[0]"
    """

    mode: Optional[str] = None
    """
    '#/components/schemas/SecretSerializer/properties/mode/anyOf/0'
    "$.components.schemas.SecretSerializer.properties.mode.anyOf[0]"
    """
