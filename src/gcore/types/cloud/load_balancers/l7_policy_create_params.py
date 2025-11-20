# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "L7PolicyCreateParams",
    "CreateL7PolicyRedirectToURLSerializer",
    "CreateL7PolicyRedirectPrefixSerializer",
    "CreateL7PolicyRedirectToPoolSerializer",
    "CreateL7PolicyRejectSerializer",
]


class CreateL7PolicyRedirectToURLSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REDIRECT_TO_URL"]]
    """Action"""

    listener_id: Required[str]
    """Listener ID"""

    redirect_url: Required[str]
    """Requests matching this policy will be redirected to this URL."""

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


class CreateL7PolicyRedirectPrefixSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REDIRECT_PREFIX"]]
    """Action"""

    listener_id: Required[str]
    """Listener ID"""

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


class CreateL7PolicyRedirectToPoolSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REDIRECT_TO_POOL"]]
    """Action"""

    listener_id: Required[str]
    """Listener ID"""

    redirect_pool_id: Required[str]
    """Requests matching this policy will be redirected to the pool with this ID."""

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener"""

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the resource."""


class CreateL7PolicyRejectSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["REJECT"]]
    """Action"""

    listener_id: Required[str]
    """Listener ID"""

    name: str
    """Human-readable name of the policy"""

    position: int
    """The position of this policy on the listener"""

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the resource."""


L7PolicyCreateParams: TypeAlias = Union[
    CreateL7PolicyRedirectToURLSerializer,
    CreateL7PolicyRedirectPrefixSerializer,
    CreateL7PolicyRedirectToPoolSerializer,
    CreateL7PolicyRejectSerializer,
]
