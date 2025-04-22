# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FloatingIPAssignParams"]


class FloatingIPAssignParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bfloating_ip_id%7D%2Fassign/post/parameters/0/schema'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/assign'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bfloating_ip_id%7D%2Fassign/post/parameters/1/schema'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/assign'].post.parameters[1].schema"
    """

    port_id: Required[str]
    """
    '#/components/schemas/AssignFloatingIPSerializer/properties/port_id'
    "$.components.schemas.AssignFloatingIPSerializer.properties.port_id"
    """

    fixed_ip_address: Optional[str]
    """
    '#/components/schemas/AssignFloatingIPSerializer/properties/fixed_ip_address/anyOf/0'
    "$.components.schemas.AssignFloatingIPSerializer.properties.fixed_ip_address.anyOf[0]"
    """
