# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ssl_request_status import SslRequestStatus

__all__ = ["AliasCertificateStatus", "AliasCertificateStatusCnameRecord"]


class AliasCertificateStatusCnameRecord(BaseModel):
    cname_name: Optional[str] = None
    """Hostname to create the CNAME record for."""

    cname_target: Optional[str] = None
    """Value the CNAME record must point to."""


class AliasCertificateStatus(SslRequestStatus):
    challenge_type: Optional[str] = None
    """The domain validation method this attempt uses.

    Possible values:

    - **`dns_01`** - Validation via a DNS record.
    - **`http_01`** - Validation via an HTTP request.
    """

    cname_records: Optional[List[AliasCertificateStatusCnameRecord]] = None
    """
    CNAME records to create so Let's Encrypt domain validation can complete for the
    alias hostname.
    """

    reason: Optional[str] = None
    """Why this attempt was opened.

    Possible values:

    - **initial** - First attempt to issue a certificate.
    - **renewal** - A scheduled renewal of an existing certificate.
    - **manual** - Manually triggered, for example via a retry.
    - **switch** - Switching from your own certificate to a Let's Encrypt
      certificate.
    - **extend** - Extending the set of domains covered by the certificate.
    """

    requested_domains: Optional[List[str]] = None
    """Domains this attempt requested a certificate for."""

    validation_state: Optional[str] = None
    """State of the domain validation for this attempt.

    Possible values:

    - **PENDING** - Validation has not started yet.
    - **`AWAITING_CNAME`** - Waiting for the CNAME records below to be created.
    - **VALIDATING** - Validation is in progress.
    - **COMPLETED** - Validation succeeded.
    - **FAILED** - Validation did not succeed.
    """
