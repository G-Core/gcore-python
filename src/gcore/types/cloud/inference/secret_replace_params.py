# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..aws_iam_data_param import AwsIamDataParam

__all__ = ["SecretReplaceParams"]


class SecretReplaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/put/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].put.parameters[0].schema"
    """

    data: Required[AwsIamDataParam]
    """
    '#/components/schemas/InferenceSecretInUpdateSerializer/properties/data'
    "$.components.schemas.InferenceSecretInUpdateSerializer.properties.data"
    """

    type: Required[str]
    """
    '#/components/schemas/InferenceSecretInUpdateSerializer/properties/type'
    "$.components.schemas.InferenceSecretInUpdateSerializer.properties.type"
    """
