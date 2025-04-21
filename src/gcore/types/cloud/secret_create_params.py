# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateSecretSerializer/properties/name'
    "$.components.schemas.CreateSecretSerializer.properties.name"
    """

    payload: Required[str]
    """
    '#/components/schemas/CreateSecretSerializer/properties/payload'
    "$.components.schemas.CreateSecretSerializer.properties.payload"
    """

    payload_content_encoding: Required[Literal["base64"]]
    """
    '#/components/schemas/CreateSecretSerializer/properties/payload_content_encoding'
    "$.components.schemas.CreateSecretSerializer.properties.payload_content_encoding"
    """

    payload_content_type: Required[str]
    """
    '#/components/schemas/CreateSecretSerializer/properties/payload_content_type'
    "$.components.schemas.CreateSecretSerializer.properties.payload_content_type"
    """

    secret_type: Required[Literal["certificate", "opaque", "passphrase", "private", "public", "symmetric"]]
    """
    '#/components/schemas/CreateSecretSerializer/properties/secret_type'
    "$.components.schemas.CreateSecretSerializer.properties.secret_type"
    """

    algorithm: Optional[str]
    """
    '#/components/schemas/CreateSecretSerializer/properties/algorithm/anyOf/0'
    "$.components.schemas.CreateSecretSerializer.properties.algorithm.anyOf[0]"
    """

    bit_length: Optional[int]
    """
    '#/components/schemas/CreateSecretSerializer/properties/bit_length/anyOf/0'
    "$.components.schemas.CreateSecretSerializer.properties.bit_length.anyOf[0]"
    """

    expiration: Optional[str]
    """
    '#/components/schemas/CreateSecretSerializer/properties/expiration/anyOf/0'
    "$.components.schemas.CreateSecretSerializer.properties.expiration.anyOf[0]"
    """

    mode: Optional[str]
    """
    '#/components/schemas/CreateSecretSerializer/properties/mode/anyOf/0'
    "$.components.schemas.CreateSecretSerializer.properties.mode.anyOf[0]"
    """
