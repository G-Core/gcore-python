# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["L7PolicyCreateParams"]


class L7PolicyCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    action: Required[Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"]]
    """Action"""

    listener_id: Required[str]
    """Listener ID"""

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener. Positions start at 1."""

    redirect_http_code: int
    """
    Requests matching this policy will be redirected to the specified URL or Prefix
    URL with the HTTP response code. Valid if action is `REDIRECT_TO_URL` or
    `REDIRECT_PREFIX`. Valid options are 301, 302, 303, 307, or 308. Default is 302.
    """

    redirect_pool_id: str
    """Requests matching this policy will be redirected to the pool withthis ID.

    Only valid if action is `REDIRECT_TO_POOL`.
    """

    redirect_prefix: str
    """Requests matching this policy will be redirected to this Prefix URL.

    Only valid if action is `REDIRECT_PREFIX`.
    """

    redirect_url: str
    """Requests matching this policy will be redirected to this URL.

    Only valid if action is `REDIRECT_TO_URL`.
    """

    tags: List[str]
    """A list of simple strings assigned to the resource."""
