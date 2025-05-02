# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..aws_iam_data import AwsIamData

__all__ = ["InferenceSecret"]


class InferenceSecret(BaseModel):
    data: AwsIamData
    """Secret data."""

    name: str
    """Secret name."""

    type: str
    """Secret type."""
