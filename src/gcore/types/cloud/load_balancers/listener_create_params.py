# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..lb_listener_protocol import LbListenerProtocol

__all__ = ["ListenerCreateParams", "UserList"]


class ListenerCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    loadbalancer_id: Required[str]
    """Load balancer ID"""

    name: Required[str]
    """Load balancer listener name"""

    protocol: Required[LbListenerProtocol]
    """Load balancer listener protocol"""

    protocol_port: Required[int]
    """Protocol port"""

    allowed_cidrs: Optional[List[str]]
    """Network CIDRs from which service will be accessible"""

    connection_limit: int
    """Limit of the simultaneous connections"""

    insert_x_forwarded: bool
    """Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests.

    Only used with HTTP or `TERMINATED_HTTPS` protocols.
    """

    secret_id: str
    """
    ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
    PROMETHEUS listener
    """

    sni_secret_id: List[str]
    """
    List of secrets IDs containing PKCS12 format certificate/key bundles for
    `TERMINATED_HTTPS` or PROMETHEUS listeners
    """

    timeout_client_data: Optional[int]
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int]
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int]
    """Backend member inactivity timeout in milliseconds"""

    user_list: Iterable[UserList]
    """Load balancer listener list of username and encrypted password items"""


class UserList(TypedDict, total=False):
    encrypted_password: Required[str]
    """Encrypted password to auth via Basic Authentication"""

    username: Required[str]
    """Username to auth via Basic Authentication"""
