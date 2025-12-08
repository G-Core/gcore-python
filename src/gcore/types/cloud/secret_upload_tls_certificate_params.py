# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretUploadTlsCertificateParams", "Payload"]


class SecretUploadTlsCertificateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """Secret name"""

    payload: Required[Payload]
    """Secret payload."""

    expiration: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Datetime when the secret will expire. Defaults to None"""


class Payload(TypedDict, total=False):
    """Secret payload."""

    certificate: Required[str]
    """SSL certificate in PEM format."""

    certificate_chain: Required[str]
    """SSL certificate chain of intermediates and root certificates in PEM format."""

    private_key: Required[str]
    """SSL private key in PEM format."""
