# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AliasCreateMultipleResponse", "Created", "Exist"]


class Created(BaseModel):
    id: Optional[int] = None
    """Alias ID."""

    cname: Optional[str] = None
    """Alias hostname."""

    ssl_status: Optional[Literal["pending", "issued", "failed"]] = None
    """Outcome of the certificate we manage for the alias.

    Possible values:

    - `pending` – A certificate attempt is in progress, or was stopped by pausing
      the alias and starts again after it is resumed.
    - `issued` – The latest attempt succeeded.
    - `failed` – The latest attempt ended without a certificate.
    - `null` – No certificate is managed for the alias: the alias uses a certificate
      you provided, or is automated and has never opened an attempt.
    """

    status: Optional[Literal["inactive", "pending", "http_only", "active"]] = None
    """Alias status.

    Possible values:

    - `inactive` – The alias or its CDN resource is disabled; the alias is not
      served.
    - `pending` – The alias configuration has not reached the CDN yet.
    - `http_only` – The alias is served over HTTP only.
    - `active` – The alias is served over HTTP and HTTPS.
    """


class Exist(BaseModel):
    id: Optional[int] = None
    """Alias ID."""

    cname: Optional[str] = None
    """Alias hostname."""

    ssl_status: Optional[Literal["pending", "issued", "failed"]] = None
    """Outcome of the certificate we manage for the alias.

    Possible values:

    - `pending` – A certificate attempt is in progress, or was stopped by pausing
      the alias and starts again after it is resumed.
    - `issued` – The latest attempt succeeded.
    - `failed` – The latest attempt ended without a certificate.
    - `null` – No certificate is managed for the alias: the alias uses a certificate
      you provided, or is automated and has never opened an attempt.
    """

    status: Optional[Literal["inactive", "pending", "http_only", "active"]] = None
    """Alias status.

    Possible values:

    - `inactive` – The alias or its CDN resource is disabled; the alias is not
      served.
    - `pending` – The alias configuration has not reached the CDN yet.
    - `http_only` – The alias is served over HTTP only.
    - `active` – The alias is served over HTTP and HTTPS.
    """


class AliasCreateMultipleResponse(BaseModel):
    created: Optional[List[Created]] = None
    """Aliases created by this request."""

    exists: Optional[List[Exist]] = None
    """Items whose hostname was already an alias of the CDN resource.

    Nothing was changed for them.
    """
