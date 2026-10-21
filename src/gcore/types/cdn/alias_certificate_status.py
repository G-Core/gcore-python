# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AliasCertificateStatus", "Challenge", "CnameRecord", "LatestStatus", "Status"]


class Challenge(BaseModel):
    challenge_type: Optional[str] = None
    """Domain validation method of the challenge.

    Possible values:

    - `dns_01` – Validation via a DNS record.
    - `http_01` – Validation via an HTTP request.
    """

    domain: Optional[str] = None
    """Domain the challenge validates."""

    error: Optional[str] = None
    """Why the challenge failed. Empty unless `state` is `invalid`."""

    state: Optional[str] = None
    """State of the challenge.

    Possible values:

    - `pending` – The challenge has not been checked yet.
    - `processing` – Let's Encrypt is validating the challenge.
    - `valid` – The challenge passed.
    - `invalid` – The challenge failed; see `error`.
    """


class CnameRecord(BaseModel):
    cname_name: Optional[str] = None
    """Hostname to create the CNAME record for."""

    cname_target: Optional[str] = None
    """Value the CNAME record must point to."""


class LatestStatus(BaseModel):
    """Detailed information about last attempt to issue a Let's Encrypt certificate.

    The field is `null` until the first attempt of the issuing process has been recorded.
    """

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

    - `DONE` – Attempt is successful. Let's Encrypt certificate was issued.
    - `FAILED` – Attempt failed. Let's Encrypt certificate was not issued.
    - `CANCELLED` – Attempt is cancelled. Let's Encrypt certificate was not issued.
    - `FORBIDDEN` – Issuing of Let's Encrypt certificates is disabled for your
      account. Let's Encrypt certificate was not issued.
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

    - `DONE` – Attempt is successful. Let's Encrypt certificate was issued.
    - `FAILED` – Attempt failed. Let's Encrypt certificate was not issued.
    - `CANCELLED` – Attempt is cancelled. Let's Encrypt certificate was not issued.
    - `FORBIDDEN` – Issuing of Let's Encrypt certificates is disabled for your
      account. Let's Encrypt certificate was not issued.
    """


class AliasCertificateStatus(BaseModel):
    id: Optional[int] = None
    """ID of the attempt to issue a Let's Encrypt certificate."""

    active: Optional[bool] = None
    """Defines whether the Let's Encrypt certificate issuing process is active.

    Possible values:

    - `true` – Issuing process is active.
    - `false` – Issuing process is completed.
    """

    attempts_count: Optional[int] = None
    """Number of attempts to issue the Let's Encrypt certificate."""

    challenge_type: Optional[str] = None
    """The domain validation method this attempt uses.

    Possible values:

    - `dns_01` – Validation via a DNS record.
    - `http_01` – Validation via an HTTP request.
    """

    challenges: Optional[List[Challenge]] = None
    """
    Domain validation challenges of the latest order placed with Let's Encrypt, one
    per domain.
    """

    cname_records: Optional[List[CnameRecord]] = None
    """
    CNAME records to create so Let's Encrypt domain validation can complete for the
    alias hostname. Empty when the attempt uses `http_01`.
    """

    finished: Optional[str] = None
    """
    Date when the process of issuing a Let's Encrypt certificate was finished (ISO
    8601/RFC 3339 format, UTC).

    The field is `null` if the issuing process is not finished.
    """

    latest_status: Optional[LatestStatus] = None
    """Detailed information about last attempt to issue a Let's Encrypt certificate.

    The field is `null` until the first attempt of the issuing process has been
    recorded.
    """

    next_attempt_time: Optional[str] = None
    """
    Time of the next scheduled attempt to issue the Let's Encrypt certificate (ISO
    8601/RFC 3339 format, UTC).
    """

    reason: Optional[str] = None
    """Why this attempt was opened.

    Possible values:

    - `initial` – First attempt to issue a certificate.
    - `renewal` – A scheduled renewal of an existing certificate.
    - `manual` – Manually triggered, for example via a retry.
    - `switch` – Switching from your own certificate to a Let's Encrypt certificate.
    - `extend` – Extending the set of domains covered by the certificate.
    """

    requested_domains: Optional[List[str]] = None
    """Domains this attempt requested a certificate for."""

    resource: Optional[int] = None
    """Always `null` for an alias."""

    started: Optional[str] = None
    """
    Date when the process of issuing a Let's Encrypt certificate was started (ISO
    8601/RFC 3339 format, UTC).
    """

    statuses: Optional[List[Status]] = None
    """Detailed information about attempts to issue a Let's Encrypt certificate."""

    validation_state: Optional[str] = None
    """State of the domain validation for this attempt.

    Possible values:

    - `PENDING` – Validation has not started yet.
    - `AWAITING_CNAME` – Waiting for the CNAME records below to be created.
    - `VALIDATING` – Validation is in progress.
    - `COMPLETED` – Validation succeeded.
    - `FAILED` – Validation did not succeed.
    """
