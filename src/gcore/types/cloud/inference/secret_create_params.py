# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..aws_iam_data_param import AwsIamDataParam

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/post/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/secrets'].post.parameters[0].schema"
    """

    data: Required[AwsIamDataParam]
    """
    '#/components/schemas/InferenceBoxSecretsInSerializer/properties/data'
    "$.components.schemas.InferenceBoxSecretsInSerializer.properties.data"
    """

    name: Required[str]
    """
    '#/components/schemas/InferenceBoxSecretsInSerializer/properties/name'
    "$.components.schemas.InferenceBoxSecretsInSerializer.properties.name"
    """

    type: Required[str]
    """
    '#/components/schemas/InferenceBoxSecretsInSerializer/properties/type'
    "$.components.schemas.InferenceBoxSecretsInSerializer.properties.type"
    """
