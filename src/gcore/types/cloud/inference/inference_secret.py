# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..aws_iam_data import AwsIamData

__all__ = ["InferenceSecret"]


class InferenceSecret(BaseModel):
    data: AwsIamData
    """
    '#/components/schemas/InferenceBoxSecretsSerializer/properties/data'
    "$.components.schemas.InferenceBoxSecretsSerializer.properties.data"
    """

    name: str
    """
    '#/components/schemas/InferenceBoxSecretsSerializer/properties/name'
    "$.components.schemas.InferenceBoxSecretsSerializer.properties.name"
    """

    type: str
    """
    '#/components/schemas/InferenceBoxSecretsSerializer/properties/type'
    "$.components.schemas.InferenceBoxSecretsSerializer.properties.type"
    """
