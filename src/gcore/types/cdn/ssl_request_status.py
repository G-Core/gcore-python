# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SslRequestStatus", "LatestStatus", "Status"]


class LatestStatus(BaseModel):
    """Detailed information about last attempt to issue a Let's Encrypt certificate."""

    id: Optional[int] = None
    """ID of the attempt to issue the Let's Encrypt certificate."""

    created: Optional[str] = None
    """
    Date and time when the issuing attempt status was created (ISO 8601/RFC 3339
    format, UTC).
    """

    details: Optional[str] = None
    """
    Detailed description of the error that occurred when trying to issue a Let's
    Encrypt certificate.
    """

    error: Optional[str] = None
    """
    Brief description of the error that occurred when trying to issue a Let's
    Encrypt certificate.
    """

    retry_after: Optional[str] = None
    """
    Date indicating when the certificate issuance limit will be lifted (ISO 8601/RFC
    3339 format, UTC).

    It is filled in only if error = RateLimited.
    """

    status: Optional[str] = None
    """Status of the attempt to issue the Let's Encrypt certificate.

    Possible values:

    - **Done** - Attempt is successful. Let's Encrypt certificate was issued.
    - **Failed** - Attempt failed. Let's Encrypt certificate was not issued.
    - **Cancelled** - Attempt is canceled. Let's Encrypt certificate was not issued.
    """


class Status(BaseModel):
    id: Optional[int] = None
    """ID of the attempt to issue the Let's Encrypt certificate."""

    created: Optional[str] = None
    """
    Date and time when the issuing attempt status was created (ISO 8601/RFC 3339
    format, UTC).
    """

    details: Optional[str] = None
    """
    Detailed description of the error that occurred when trying to issue a Let's
    Encrypt certificate.
    """

    error: Optional[str] = None
    """
    Brief description of the error that occurred when trying to issue a Let's
    Encrypt certificate.
    """

    retry_after: Optional[str] = None
    """
    Date indicating when the certificate issuance limit will be lifted (ISO 8601/RFC
    3339 format, UTC).

    It is filled in only if error = RateLimited.
    """

    status: Optional[str] = None
    """Status of the attempt to issue the Let's Encrypt certificate.

    Possible values:

    - **Done** - Attempt is successful. Let's Encrypt certificate was issued.
    - **Failed** - Attempt failed. Let's Encrypt certificate was not issued.
    - **Cancelled** - Attempt is canceled. Let's Encrypt certificate was not issued.
    """


class SslRequestStatus(BaseModel):
    id: Optional[int] = None
    """ID of the attempt to issue a Let's Encrypt certificate."""

    active: Optional[bool] = None
    """Defines whether the Let's Encrypt certificate issuing process is active.

    Possible values:

    - **true** - Issuing process is active.
    - **false** - Issuing process is completed.
    """

    attempts_count: Optional[int] = None
    """Number of attempts to issue the Let's Encrypt certificate."""

    finished: Optional[str] = None
    """
    Date when the process of issuing a Let's Encrypt certificate was finished (ISO
    8601/RFC 3339 format, UTC).

    The field is **null** if the issuing process is not finished.
    """

    latest_status: Optional[LatestStatus] = None
    """Detailed information about last attempt to issue a Let's Encrypt certificate."""

    next_attempt_time: Optional[str] = None
    """
    Time of the next scheduled attempt to issue the Let's Encrypt certificate (ISO
    8601/RFC 3339 format, UTC).
    """

    resource: Optional[int] = None
    """CDN resource ID."""

    started: Optional[str] = None
    """
    Date when the process of issuing a Let's Encrypt certificate was started (ISO
    8601/RFC 3339 format, UTC).
    """

    statuses: Optional[List[Status]] = None
    """Detailed information about attempts to issue a Let's Encrypt certificate."""
