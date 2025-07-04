# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceSecret", "Data"]


class Data(BaseModel):
    aws_access_key_id: str
    """AWS IAM key ID."""

    aws_secret_access_key: str
    """AWS IAM secret key."""


class InferenceSecret(BaseModel):
    data: Data
    """Secret data."""

    name: str
    """Secret name."""

    type: str
    """Secret type."""
