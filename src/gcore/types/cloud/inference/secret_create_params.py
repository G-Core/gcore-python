# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..aws_iam_data_param import AwsIamDataParam

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    data: Required[AwsIamDataParam]
    """Secret data."""

    name: Required[str]
    """Secret name."""

    type: Required[str]
    """Secret type. Currently only `aws-iam` is supported."""
