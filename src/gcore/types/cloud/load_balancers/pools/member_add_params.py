# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MemberAddParams"]


class MemberAddParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/0/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fmember/post/parameters/1/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member'].post.parameters[1].schema"
    """

    address: Required[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/address'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.address"
    """

    protocol_port: Required[int]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/protocol_port'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.protocol_port"
    """

    admin_state_up: Optional[bool]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/admin_state_up/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.admin_state_up.anyOf[0]"
    """

    instance_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/instance_id/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.instance_id.anyOf[0]"
    """

    monitor_address: Optional[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_address/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_address.anyOf[0]"
    """

    monitor_port: Optional[int]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_port/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_port.anyOf[0]"
    """

    subnet_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/subnet_id/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.subnet_id.anyOf[0]"
    """

    weight: Optional[int]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/weight/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.weight.anyOf[0]"
    """
