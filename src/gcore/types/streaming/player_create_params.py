# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .create_player_param import CreatePlayerParam

__all__ = ["PlayerCreateParams"]


class PlayerCreateParams(TypedDict, total=False):
    player: CreatePlayerParam
    """Set of properties for displaying videos.

    All parameters may be blank to inherit their values from default Streaming
    player.
    """
