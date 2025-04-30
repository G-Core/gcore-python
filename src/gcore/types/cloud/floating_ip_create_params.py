# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .tag_update_list_param import TagUpdateListParam

__all__ = ["FloatingIPCreateParams"]


class FloatingIPCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    fixed_ip_address: Optional[str]
    """
    '#/components/schemas/CreateFloatingIPSerializer/properties/fixed_ip_address/anyOf/0'
    "$.components.schemas.CreateFloatingIPSerializer.properties.fixed_ip_address.anyOf[0]"
    """

    port_id: Optional[str]
    """
    '#/components/schemas/CreateFloatingIPSerializer/properties/port_id/anyOf/0'
    "$.components.schemas.CreateFloatingIPSerializer.properties.port_id.anyOf[0]"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/CreateFloatingIPSerializer/properties/tags'
    "$.components.schemas.CreateFloatingIPSerializer.properties.tags"
    """
