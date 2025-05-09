# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .waap_api_urls import WaapAPIURLs
from .waap_domain_ddos_settings import WaapDomainDDOSSettings

__all__ = ["WaapDomainSettings"]


class WaapDomainSettings(BaseModel):
    api: WaapAPIURLs
    """API settings of a domain"""

    ddos: WaapDomainDDOSSettings
    """DDoS settings for a domain."""
