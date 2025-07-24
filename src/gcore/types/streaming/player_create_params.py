# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .player_param import PlayerParam

__all__ = ["PlayerCreateParams"]


class PlayerCreateParams(TypedDict, total=False):
    player: PlayerParam
    """Set of properties for displaying videos.

    All parameters may be blank to inherit their values from default Streaming
    player.
    """
