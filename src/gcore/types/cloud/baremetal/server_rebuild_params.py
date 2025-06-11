# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ServerRebuildParams"]


class ServerRebuildParams(TypedDict, total=False):
    project_id: int

    region_id: int

    image_id: str
    """Image ID"""

    user_data: str
    """String in base64 format.

    Must not be passed together with 'username' or 'password'. Examples of the
    `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """
