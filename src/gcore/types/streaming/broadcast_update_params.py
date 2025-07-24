# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BroadcastUpdateParams", "Broadcast"]


class BroadcastUpdateParams(TypedDict, total=False):
    broadcast: Broadcast


class Broadcast(TypedDict, total=False):
    name: Required[str]
    """Broadcast name"""

    ad_id: int
    """ID of ad to be displayed in a live stream.

    If empty the default ad is show. If there is no default ad, no ad is shown
    """

    custom_iframe_url: str
    """Custom URL of iframe for video player to be shared via sharing button in player.

    Auto generated iframe URL is provided by default
    """

    pending_message: str
    """A custom message that is shown if broadcast status is set to pending.

    If empty, a default message is shown
    """

    player_id: int
    """ID of player to be used with a broadcast. If empty the default player is used"""

    poster: str
    """Uploaded poster file"""

    share_url: str
    """
    Custom URL or iframe displayed in the link field when a user clicks on a sharing
    button in player. If empty, the link field and social network sharing is
    disabled
    """

    show_dvr_after_finish: bool
    """Regulates if a DVR record is shown once a broadcast is finished.

    Has two possible values:

    - **true** — record is shown
    - **false** — record isn't shown

    Default is false
    """

    status: str
    """
    Broadcast statuses:
     **Pending** — default “Broadcast isn’t started yet” or custom message (see `pending_message`
    parameter) is shown, users don't see the live stream
     **Live** — broadcast is live, and viewers can see it
     **Paused** — “Broadcast is paused” message is shown, users don't see the live stream

    **Finished** — “Broadcast is finished” message is shown, users don't see the
    live stream
     The users' browsers start displaying the message/stream immediately after you change
    the broadcast status
    """

    stream_ids: Iterable[int]
    """IDs of streams used in a broadcast"""
