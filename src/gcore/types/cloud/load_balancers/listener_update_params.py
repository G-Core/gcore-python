# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ListenerUpdateParams", "UserList"]


class ListenerUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    allowed_cidrs: Optional[List[str]]
    """Network CIDRs from which service will be accessible"""

    connection_limit: int
    """Limit of simultaneous connections"""

    name: str
    """Load balancer listener name"""

    secret_id: Optional[str]
    """
    ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
    PROMETHEUS load balancer
    """

    sni_secret_id: Optional[List[str]]
    """
    List of secret's ID containing PKCS12 format certificate/key bundfles for
    `TERMINATED_HTTPS` or PROMETHEUS listeners
    """

    timeout_client_data: Optional[int]
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int]
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int]
    """Backend member inactivity timeout in milliseconds"""

    user_list: Optional[Iterable[UserList]]
    """Load balancer listener users list"""


class UserList(TypedDict, total=False):
    encrypted_password: Required[str]
    """Encrypted password to auth via Basic Authentication"""

    username: Required[str]
    """Username to auth via Basic Authentication"""
