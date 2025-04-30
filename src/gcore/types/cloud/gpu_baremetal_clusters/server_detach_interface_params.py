# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerDetachInterfaceParams"]


class ServerDetachInterfaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/0/schema'
    "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fdetach_interface/post/parameters/1/schema'
    "$.paths['/cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface'].post.parameters[1].schema"
    """

    ip_address: Required[str]
    """
    '#/components/schemas/PortIdWithIpSchema/properties/ip_address'
    "$.components.schemas.PortIdWithIpSchema.properties.ip_address"
    """

    port_id: Required[str]
    """
    '#/components/schemas/PortIdWithIpSchema/properties/port_id'
    "$.components.schemas.PortIdWithIpSchema.properties.port_id"
    """
