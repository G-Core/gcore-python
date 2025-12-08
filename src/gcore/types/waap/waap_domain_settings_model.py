# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .waap_domain_api_settings import WaapDomainAPISettings
from .waap_domain_ddos_settings import WaapDomainDDOSSettings

__all__ = ["WaapDomainSettingsModel"]


class WaapDomainSettingsModel(BaseModel):
    """Settings for a domain."""

    api: WaapDomainAPISettings
    """API settings of a domain"""

    ddos: WaapDomainDDOSSettings
    """DDoS settings for a domain."""
