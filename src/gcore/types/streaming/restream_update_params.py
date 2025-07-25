# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RestreamUpdateParams", "Restream"]


class RestreamUpdateParams(TypedDict, total=False):
    restream: Restream


class Restream(TypedDict, total=False):
    active: bool
    """Enables/Disables restream. Has two possible values:

    - **true** — restream is enabled and can be started
    - **false** — restream is disabled.

    Default is true
    """

    client_user_id: int
    """Custom field where you can specify user ID in your system"""

    live: bool
    """Indicates that the stream is being published. Has two possible values:

    - **true** — stream is being published
    - **false** — stream isn't published
    """

    name: str
    """Restream name"""

    stream_id: int
    """ID of the stream to restream"""

    uri: str
    """A URL to push the stream to"""
