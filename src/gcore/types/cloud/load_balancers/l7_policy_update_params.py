# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "L7PolicyUpdateParams",
    "UpdateL7PolicyRedirectToURLSerializer",
    "UpdateL7PolicyRedirectPrefixSerializer",
    "UpdateL7PolicyRedirectToPoolSerializer",
    "UpdateL7PolicyRejectSerializer",
]


class UpdateL7PolicyRedirectToURLSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REDIRECT_TO_URL"]]
    """Action"""

    redirect_url: Required[str]
    """Requests matching this policy will be redirected to this URL.

    Only valid if action is `REDIRECT_TO_URL`.
    """

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener"""

    redirect_http_code: int
    """
    Requests matching this policy will be redirected to the specified URL or Prefix
    URL with the HTTP response code. Valid if action is `REDIRECT_TO_URL` or
    `REDIRECT_PREFIX`. Valid options are 301, 302, 303, 307, or 308. Default is 302.
    """

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the resource."""


class UpdateL7PolicyRedirectPrefixSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REDIRECT_PREFIX"]]
    """Action"""

    redirect_prefix: Required[str]
    """Requests matching this policy will be redirected to this Prefix URL."""

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener"""

    redirect_http_code: int
    """
    Requests matching this policy will be redirected to the specified URL or Prefix
    URL with the HTTP response code. Valid options are 301, 302, 303, 307, or 308.
    Default is 302.
    """

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the resource."""


class UpdateL7PolicyRedirectToPoolSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REDIRECT_TO_POOL"]]
    """Action"""

    redirect_pool_id: Required[str]
    """Requests matching this policy will be redirected to the pool with this ID."""

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener"""

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the resource."""


class UpdateL7PolicyRejectSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REJECT"]]
    """Action"""

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener"""

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the resource."""


L7PolicyUpdateParams: TypeAlias = Union[
    UpdateL7PolicyRedirectToURLSerializer,
    UpdateL7PolicyRedirectPrefixSerializer,
    UpdateL7PolicyRedirectToPoolSerializer,
    UpdateL7PolicyRejectSerializer,
]
