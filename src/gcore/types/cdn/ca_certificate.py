# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CaCertificate"]


class CaCertificate(BaseModel):
    id: Optional[int] = None
    """CA certificate ID."""

    cert_issuer: Optional[str] = None
    """Name of the certification center that issued the CA certificate."""

    cert_subject_alt: Optional[str] = None
    """Alternative domain names that the CA certificate secures."""

    cert_subject_cn: Optional[str] = None
    """Domain name that the CA certificate secures."""

    deleted: Optional[bool] = None
    """Defines whether the certificate has been deleted. Parameter is **deprecated**.

    Possible values:

    - **true** - Certificate has been deleted.
    - **false** - Certificate has not been deleted.
    """

    has_related_resources: Optional[bool] = FieldInfo(alias="hasRelatedResources", default=None)
    """Defines whether the CA certificate is used by a CDN resource.

    Possible values:

    - **true** - Certificate is used by a CDN resource.
    - **false** - Certificate is not used by a CDN resource.
    """

    name: Optional[str] = None
    """CA certificate name."""

    ssl_certificate_chain: Optional[str] = FieldInfo(alias="sslCertificateChain", default=None)
    """Parameter is **deprecated**."""

    validity_not_after: Optional[str] = None
    """Date when the CA certificate become untrusted (ISO 8601/RFC 3339 format, UTC.)"""

    validity_not_before: Optional[str] = None
    """Date when the CA certificate become valid (ISO 8601/RFC 3339 format, UTC.)"""
