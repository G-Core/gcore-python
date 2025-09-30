# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CertificateReplaceParams"]


class CertificateReplaceParams(TypedDict, total=False):
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
