# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Console", "RemoteConsole"]


class RemoteConsole(BaseModel):
    protocol: str
    """
    '#/components/schemas/RemoteConsoleData/properties/protocol'
    "$.components.schemas.RemoteConsoleData.properties.protocol"
    """

    type: str
    """
    '#/components/schemas/RemoteConsoleData/properties/type'
    "$.components.schemas.RemoteConsoleData.properties.type"
    """

    url: str
    """
    '#/components/schemas/RemoteConsoleData/properties/url'
    "$.components.schemas.RemoteConsoleData.properties.url"
    """


class Console(BaseModel):
    remote_console: RemoteConsole
    """
    '#/components/schemas/RemoteConsoleSerializer/properties/remote_console'
    "$.components.schemas.RemoteConsoleSerializer.properties.remote_console"
    """
