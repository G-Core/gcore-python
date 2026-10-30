# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CertificateCreateParams", "CreateSslPayload", "CreateLetsEncryptSslPayload"]


class CreateSslPayload(TypedDict, total=False):
    name: Required[str]
    """SSL certificate name.

    It must be unique.
    """

    ssl_certificate: Required[Annotated[str, PropertyInfo(alias="sslCertificate")]]
    """Public part of the SSL certificate.

    All chain of the SSL certificate should be added.
    """

    ssl_private_key: Required[Annotated[str, PropertyInfo(alias="sslPrivateKey")]]
    """Private key of the SSL certificate."""

    automated: Literal[False]
    """Must be **false** or omitted for a certificate you upload."""

    validate_root_ca: bool
    """
    Defines whether to check the SSL certificate for a signature from a trusted
    certificate authority.

    Possible values:

    - **true** - SSL certificate must be verified to be signed by a trusted
      certificate authority.
    - **false** - SSL certificate will not be verified to be signed by a trusted
      certificate authority.
    """


class CreateLetsEncryptSslPayload(TypedDict, total=False):
    automated: Required[Literal[True]]
    """Must be **true** to issue certificate automatically."""

    name: Required[str]
    """SSL certificate name. It must be unique."""


CertificateCreateParams: TypeAlias = Union[CreateSslPayload, CreateLetsEncryptSslPayload]
