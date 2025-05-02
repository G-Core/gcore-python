# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AwsIamData"]


class AwsIamData(BaseModel):
    aws_access_key_id: str
    """AWS IAM key ID."""

    aws_secret_access_key: str
    """AWS IAM secret key."""
