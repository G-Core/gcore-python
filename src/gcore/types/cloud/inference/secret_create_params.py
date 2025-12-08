# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretCreateParams", "Data"]


class SecretCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    data: Required[Data]
    """Secret data."""

    name: Required[str]
    """Secret name."""

    type: Required[str]
    """Secret type. Currently only `aws-iam` is supported."""


class Data(TypedDict, total=False):
    """Secret data."""

    aws_access_key_id: Required[str]
    """AWS IAM key ID."""

    aws_secret_access_key: Required[str]
    """AWS IAM secret key."""
