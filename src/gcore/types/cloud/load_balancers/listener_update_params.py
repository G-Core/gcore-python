# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ListenerUpdateParams", "UserList"]


class ListenerUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[1].schema"
    """

    allowed_cidrs: Optional[List[str]]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/allowed_cidrs/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.allowed_cidrs.anyOf[0]"
    """

    connection_limit: int
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/connection_limit'
    "$.components.schemas.PatchLbListenerSerializer.properties.connection_limit"
    """

    name: str
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/name'
    "$.components.schemas.PatchLbListenerSerializer.properties.name"
    """

    secret_id: Optional[str]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.secret_id.anyOf[0]"
    """

    sni_secret_id: Optional[List[str]]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/sni_secret_id/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.sni_secret_id.anyOf[0]"
    """

    timeout_client_data: Optional[int]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.timeout_member_data.anyOf[0]"
    """

    user_list: Optional[Iterable[UserList]]
    """
    '#/components/schemas/PatchLbListenerSerializer/properties/user_list/anyOf/0'
    "$.components.schemas.PatchLbListenerSerializer.properties.user_list.anyOf[0]"
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
