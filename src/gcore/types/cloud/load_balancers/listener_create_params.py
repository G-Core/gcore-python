# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..lb_listener_protocol import LbListenerProtocol

__all__ = ["ListenerCreateParams", "UserList"]


class ListenerCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    loadbalancer_id: Required[str]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/loadbalancer_id'
    "$.components.schemas.CreateLbListenerSerializer.properties.loadbalancer_id"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/name'
    "$.components.schemas.CreateLbListenerSerializer.properties.name"
    """

    protocol: Required[LbListenerProtocol]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/protocol'
    "$.components.schemas.CreateLbListenerSerializer.properties.protocol"
    """

    protocol_port: Required[int]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/protocol_port'
    "$.components.schemas.CreateLbListenerSerializer.properties.protocol_port"
    """

    allowed_cidrs: Optional[List[str]]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/allowed_cidrs/anyOf/0'
    "$.components.schemas.CreateLbListenerSerializer.properties.allowed_cidrs.anyOf[0]"
    """

    connection_limit: int
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/connection_limit'
    "$.components.schemas.CreateLbListenerSerializer.properties.connection_limit"
    """

    insert_x_forwarded: bool
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/insert_x_forwarded'
    "$.components.schemas.CreateLbListenerSerializer.properties.insert_x_forwarded"
    """

    secret_id: str
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.CreateLbListenerSerializer.properties.secret_id.anyOf[0]"
    """

    sni_secret_id: List[str]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/sni_secret_id'
    "$.components.schemas.CreateLbListenerSerializer.properties.sni_secret_id"
    """

    timeout_client_data: Optional[int]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.CreateLbListenerSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.CreateLbListenerSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.CreateLbListenerSerializer.properties.timeout_member_data.anyOf[0]"
    """

    user_list: Iterable[UserList]
    """
    '#/components/schemas/CreateLbListenerSerializer/properties/user_list'
    "$.components.schemas.CreateLbListenerSerializer.properties.user_list"
    """


class UserList(TypedDict, total=False):
    encrypted_password: Required[str]
    """
    '#/components/schemas/UserListItem/properties/encrypted_password'
    "$.components.schemas.UserListItem.properties.encrypted_password"
    """

    username: Required[str]
    """
    '#/components/schemas/UserListItem/properties/username'
    "$.components.schemas.UserListItem.properties.username"
    """
