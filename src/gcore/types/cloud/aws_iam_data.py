# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AwsIamData"]


class AwsIamData(BaseModel):
    aws_access_key_id: str
    """
    '#/components/schemas/AwsIamData/properties/aws_access_key_id'
    "$.components.schemas.AwsIamData.properties.aws_access_key_id"
    """

    aws_secret_access_key: str
    """
    '#/components/schemas/AwsIamData/properties/aws_secret_access_key'
    "$.components.schemas.AwsIamData.properties.aws_secret_access_key"
    """
