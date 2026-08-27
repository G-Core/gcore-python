# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServerApplySettingsParams"]


class ServerApplySettingsParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cluster_id: Required[str]
    """Cluster unique identifier"""

    max_disruption: Literal["none", "rebuild"]
    """
    The most disruptive operation the request is permitted to perform on existing
    servers. Applying settings re-images the servers, so this must be set to
    'rebuild' to proceed. The default 'none' always fails with a validation error
    and exists only to prevent accidental destructive applies.
    """
