# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Restream"]


class Restream(BaseModel):
    active: Optional[bool] = None
    """Enables/Disables restream. Has two possible values:

    - **true** — restream is enabled and can be started
    - **false** — restream is disabled.

    Default is true
    """

    client_user_id: Optional[int] = None
    """Custom field where you can specify user ID in your system"""

    live: Optional[bool] = None
    """Indicates that the stream is being published. Has two possible values:

    - **true** — stream is being published
    - **false** — stream isn't published
    """

    name: Optional[str] = None
    """Restream name"""

    stream_id: Optional[int] = None
    """ID of the stream to restream"""

    uri: Optional[str] = None
    """A URL to push the stream to"""
