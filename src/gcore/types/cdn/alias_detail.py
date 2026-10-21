# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .alias import Alias
from ..._models import BaseModel

__all__ = [
    "AliasDetail",
    "AliasDetailSslProvisioning",
    "AliasDetailSslProvisioningAcmeDelegation",
    "AliasDetailSslProvisioningHTTPValidation",
]


class AliasDetailSslProvisioningAcmeDelegation(BaseModel):
    """CNAME record to create so validation can be completed for the hostname.

    Returned when `challenge_type` is `dns_01`.
    """

    cname_name: Optional[str] = None
    """Hostname to create the CNAME record for."""

    cname_target: Optional[str] = None
    """Value the CNAME record must point to."""


class AliasDetailSslProvisioningHTTPValidation(BaseModel):
    """CNAME record pointing the alias hostname to your CDN CNAME.

    Returned when `challenge_type` is `http_01`; `null` until a CDN CNAME is assigned to your account.
    """

    cname_name: Optional[str] = None
    """Hostname to create the CNAME record for."""

    cname_target: Optional[str] = None
    """Value the CNAME record must point to."""


class AliasDetailSslProvisioning(BaseModel):
    """DNS record needed for Let's Encrypt domain validation of the alias hostname.

    It is `null` when `automated` is `false`, and when `challenge_type` is `dns_01` until a delegation record has been prepared for the hostname.
    """

    acme_delegation: Optional[AliasDetailSslProvisioningAcmeDelegation] = None
    """CNAME record to create so validation can be completed for the hostname.

    Returned when `challenge_type` is `dns_01`.
    """

    http_validation: Optional[AliasDetailSslProvisioningHTTPValidation] = None
    """CNAME record pointing the alias hostname to your CDN CNAME.

    Returned when `challenge_type` is `http_01`; `null` until a CDN CNAME is
    assigned to your account.
    """


class AliasDetail(Alias):
    ssl_provisioning: Optional[AliasDetailSslProvisioning] = None
    """DNS record needed for Let's Encrypt domain validation of the alias hostname.

    It is `null` when `automated` is `false`, and when `challenge_type` is `dns_01`
    until a delegation record has been prepared for the hostname.
    """
