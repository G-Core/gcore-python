# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InferenceApikeySecret"]


class InferenceApikeySecret(BaseModel):
    secret: str
    """
    '#/components/schemas/InferenceInstanceApikeySecretSerializerV3/properties/secret'
    "$.components.schemas.InferenceInstanceApikeySecretSerializerV3.properties.secret"
    """

    status: Literal["PENDING", "READY"]
    """
    '#/components/schemas/InferenceInstanceApikeySecretSerializerV3/properties/status'
    "$.components.schemas.InferenceInstanceApikeySecretSerializerV3.properties.status"
    """
