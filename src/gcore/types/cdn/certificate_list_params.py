# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CertificateListParams"]


class CertificateListParams(TypedDict, total=False):
    automated: bool
    """How the SSL certificate was issued.

    Possible values:

    - **true** – Certificate was issued automatically.
    - **false** – Certificate was added by a user.
    """

    limit: int
    """Maximum number of items to return in the response. Cannot exceed 1000."""

    offset: int
    """Number of items to skip from the beginning of the list."""

    resource_id: int
    """CDN resource ID for which certificates are requested."""

    validity_not_after_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Date and time when the certificate become untrusted (ISO 8601/RFC 3339 format,
    UTC.)

    Response will contain only certificates valid until the specified time.
    """
