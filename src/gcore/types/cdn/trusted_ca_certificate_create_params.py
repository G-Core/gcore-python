# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrustedCaCertificateCreateParams"]


class TrustedCaCertificateCreateParams(TypedDict, total=False):
    name: Required[str]
    """CA certificate name.

    It must be unique.
    """

    ssl_certificate: Required[Annotated[str, PropertyInfo(alias="sslCertificate")]]
    """Public part of the CA certificate.

    It must be in the PEM format.
    """
