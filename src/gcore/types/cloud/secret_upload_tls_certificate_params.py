# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretUploadTlsCertificateParams", "Payload"]


class SecretUploadTlsCertificateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v2/secrets/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v2/secrets/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateSecretSerializerV2/properties/name'
    "$.components.schemas.CreateSecretSerializerV2.properties.name"
    """

    payload: Required[Payload]
    """
    '#/components/schemas/CreateSecretSerializerV2/properties/payload'
    "$.components.schemas.CreateSecretSerializerV2.properties.payload"
    """

    expiration: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    '#/components/schemas/CreateSecretSerializerV2/properties/expiration/anyOf/0'
    "$.components.schemas.CreateSecretSerializerV2.properties.expiration.anyOf[0]"
    """


class Payload(TypedDict, total=False):
    certificate: Required[str]
    """
    '#/components/schemas/CreateSecretPayloadSerializer/properties/certificate'
    "$.components.schemas.CreateSecretPayloadSerializer.properties.certificate"
    """

    certificate_chain: Required[str]
    """
    '#/components/schemas/CreateSecretPayloadSerializer/properties/certificate_chain'
    "$.components.schemas.CreateSecretPayloadSerializer.properties.certificate_chain"
    """

    private_key: Required[str]
    """
    '#/components/schemas/CreateSecretPayloadSerializer/properties/private_key'
    "$.components.schemas.CreateSecretPayloadSerializer.properties.private_key"
    """
