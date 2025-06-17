# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapUserAgentDetails"]


class WaapUserAgentDetails(BaseModel):
    base_browser: str
    """User agent browser"""

    base_browser_version: str
    """User agent browser version"""

    client: str
    """Client from User agent header"""

    client_type: str
    """User agent client type"""

    client_version: str
    """User agent client version"""

    cpu: str
    """User agent cpu"""

    device: str
    """User agent device"""

    device_type: str
    """User agent device type"""

    full_string: str
    """User agent"""

    os: str
    """User agent os"""

    rendering_engine: str
    """User agent engine"""
