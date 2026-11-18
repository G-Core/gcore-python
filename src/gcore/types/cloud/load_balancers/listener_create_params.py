# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr
from ..lb_listener_protocol import LbListenerProtocol

__all__ = ["ListenerCreateParams", "UserList"]


class ListenerCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    load_balancer_id: Required[str]
    """ID of already existent Load Balancer."""

    name: Required[str]
    """Load balancer listener name"""

    protocol: Required[LbListenerProtocol]
    """Load balancer listener protocol"""

    protocol_port: Required[int]
    """Protocol port"""

    allowed_cidrs: Optional[SequenceNotStr[str]]
    """Network CIDRs from which service will be accessible. Order-insensitive."""

    connection_limit: int
    """Limit of the simultaneous connections.

    If -1 is provided, it is translated to the default value 100000.
    """

    default_pool_id: str
    """ID of already existent Load Balancer Pool to attach listener to."""

    insert_x_forwarded: bool
    """Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests.

    Only used with HTTP or `TERMINATED_HTTPS` protocols.
    """

    secret_id: Literal[""]
    """
    ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
    PROMETHEUS listener
    """

    sni_secret_id: SequenceNotStr[str]
    """
    List of secrets IDs containing PKCS12 format certificate/key bundles for
    `TERMINATED_HTTPS` or PROMETHEUS listeners
    """

    timeout_client_data: Optional[int]
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int]
    """Backend member connection timeout in milliseconds.

    We are recommending to use `pool.timeout_member_connect` instead.
    """

    timeout_member_data: Optional[int]
    """Backend member inactivity timeout in milliseconds.

    We are recommending to use `pool.timeout_member_data` instead.
    """

    user_list: Iterable[UserList]
    """Load balancer listener list of username and encrypted password items"""


class UserList(TypedDict, total=False):
    encrypted_password: Required[str]
    """
    Password hash for HTTP basic authentication in crypt(3) format, for example
    SHA-256 ($5$) or bcrypt ($2b$). Do not send the password as plain text. Do not
    use the $apr1$ format.
    """

    username: Required[str]
    """Username for HTTP basic authentication.

    Use 3 to 32 letters, digits, periods, underscores or hyphens. Start with a
    letter or a digit. Do not end with a hyphen. Do not use spaces.
    """
