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

    - **pending** – A certificate attempt is in progress.
    - **issued** – The latest attempt succeeded.
    - **failed** – The latest attempt ended without a certificate.
    - **null** – No certificate is managed for the alias: the alias uses a
      certificate you provided, or is automated and has never opened an attempt.
    """

    status: Optional[Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"]] = None
    """Alias status.

    Possible values:

    - **pending** – The certificate has not been issued yet; the alias is not
      served.
    - **active** – The alias is served with its certificate.
    - **`ssl_issuing`** – A new certificate is being issued; the current one keeps
      being served.
    - **`ssl_error`** – Certificate issuance failed; a previously issued certificate
      keeps being served.
    - **inactive** – The alias or its CDN resource is disabled; the alias is not
      served.
    """


class Exist(BaseModel):
    id: Optional[int] = None
    """Alias ID."""

    cname: Optional[str] = None
    """Alias hostname."""

    ssl_status: Optional[Literal["pending", "issued", "failed"]] = None
    """Outcome of the certificate we manage for the alias.

    Possible values:

    - **pending** – A certificate attempt is in progress.
    - **issued** – The latest attempt succeeded.
    - **failed** – The latest attempt ended without a certificate.
    - **null** – No certificate is managed for the alias: the alias uses a
      certificate you provided, or is automated and has never opened an attempt.
    """

    status: Optional[Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"]] = None
    """Alias status.

    Possible values:

    - **pending** – The certificate has not been issued yet; the alias is not
      served.
    - **active** – The alias is served with its certificate.
    - **`ssl_issuing`** – A new certificate is being issued; the current one keeps
      being served.
    - **`ssl_error`** – Certificate issuance failed; a previously issued certificate
      keeps being served.
    - **inactive** – The alias or its CDN resource is disabled; the alias is not
      served.
    """


class AliasCreateMultipleResponse(BaseModel):
    created: Optional[List[Created]] = None
    """Aliases created by this request."""

    exists: Optional[List[Exist]] = None
    """Items whose hostname was already an alias of the CDN resource.

    Nothing was changed for them.
    """
