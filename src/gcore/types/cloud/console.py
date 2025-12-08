# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Console", "RemoteConsole"]


class RemoteConsole(BaseModel):
    """Remote console information"""

    protocol: str

    type: str

    url: str


class Console(BaseModel):
    remote_console: RemoteConsole
    """Remote console information"""
