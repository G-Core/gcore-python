# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CertificateListParams"]


class CertificateListParams(TypedDict, total=False):
    automated: bool
    """How the SSL certificate was issued.

    Possible values:

    - **true** – Certificate was issued automatically.
    - **false** – Certificate was added by a user.
    """

    resource_id: int
    """CDN resource ID for which certificates are requested."""

    validity_not_after_lte: str
    """
    Date and time when the certificate become untrusted (ISO 8601/RFC 3339 format,
    UTC.)

    Response will contain only certificates valid until the specified time.
    """
