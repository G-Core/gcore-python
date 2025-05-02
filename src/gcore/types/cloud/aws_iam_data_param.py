# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AwsIamDataParam"]


class AwsIamDataParam(TypedDict, total=False):
    aws_access_key_id: Required[str]
    """AWS IAM key ID."""

    aws_secret_access_key: Required[str]
    """AWS IAM secret key."""
