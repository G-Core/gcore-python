# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .alias import Alias
from ..._models import BaseModel

__all__ = ["AliasDetail", "AliasDetailSslProvisioning", "AliasDetailSslProvisioningAcmeDelegation"]


class AliasDetailSslProvisioningAcmeDelegation(BaseModel):
    """CNAME record to create so validation can be completed for the hostname."""

    cname_name: Optional[str] = None
    """Hostname to create the CNAME record for."""

    cname_target: Optional[str] = None
    """Value the CNAME record must point to."""


class AliasDetailSslProvisioning(BaseModel):
    """DNS record delegating Let's Encrypt domain validation for the alias hostname.

    It is `null` for an
    alias serving a certificate you added yourself, and until a delegation record has been prepared
    for the hostname.
    """

    acme_delegation: Optional[AliasDetailSslProvisioningAcmeDelegation] = None
    """CNAME record to create so validation can be completed for the hostname."""


class AliasDetail(Alias):
    ssl_provisioning: Optional[AliasDetailSslProvisioning] = None
    """DNS record delegating Let's Encrypt domain validation for the alias hostname.

    It is `null` for an alias serving a certificate you added yourself, and until a
    delegation record has been prepared for the hostname.
    """
