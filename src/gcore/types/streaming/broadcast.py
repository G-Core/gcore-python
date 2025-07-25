# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Broadcast"]


class Broadcast(BaseModel):
    name: str
    """Broadcast name"""

    ad_id: Optional[int] = None
    """ID of ad to be displayed in a live stream.

    If empty the default ad is show. If there is no default ad, no ad is shown
    """

    custom_iframe_url: Optional[str] = None
    """Custom URL of iframe for video player to be shared via sharing button in player.

    Auto generated iframe URL is provided by default
    """

    pending_message: Optional[str] = None
    """A custom message that is shown if broadcast status is set to pending.

    If empty, a default message is shown
    """

    player_id: Optional[int] = None
    """ID of player to be used with a broadcast. If empty the default player is used"""

    poster: Optional[str] = None
    """Uploaded poster file"""

    share_url: Optional[str] = None
    """
    Custom URL or iframe displayed in the link field when a user clicks on a sharing
    button in player. If empty, the link field and social network sharing is
    disabled
    """

    show_dvr_after_finish: Optional[bool] = None
    """Regulates if a DVR record is shown once a broadcast is finished.

    Has two possible values:

    - **true** — record is shown
    - **false** — record isn't shown

    Default is false
    """

    status: Optional[str] = None
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

    stream_ids: Optional[List[int]] = None
    """IDs of streams used in a broadcast"""
