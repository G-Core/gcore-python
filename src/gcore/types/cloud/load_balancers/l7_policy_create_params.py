# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["L7PolicyCreateParams"]


class L7PolicyCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    action: Required[Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"]]
    """
    '#/components/schemas/CreateL7PolicySchema/properties/action'
    "$.components.schemas.CreateL7PolicySchema.properties.action"
    """

    listener_id: Required[str]
    """
    '#/components/schemas/CreateL7PolicySchema/properties/listener_id'
    "$.components.schemas.CreateL7PolicySchema.properties.listener_id"
    """

    name: str
    """
    '#/components/schemas/CreateL7PolicySchema/properties/name'
    "$.components.schemas.CreateL7PolicySchema.properties.name"
    """

    position: int
    """
    '#/components/schemas/CreateL7PolicySchema/properties/position'
    "$.components.schemas.CreateL7PolicySchema.properties.position"
    """

    redirect_http_code: int
    """
    '#/components/schemas/CreateL7PolicySchema/properties/redirect_http_code'
    "$.components.schemas.CreateL7PolicySchema.properties.redirect_http_code"
    """

    redirect_pool_id: str
    """
    '#/components/schemas/CreateL7PolicySchema/properties/redirect_pool_id'
    "$.components.schemas.CreateL7PolicySchema.properties.redirect_pool_id"
    """

    redirect_prefix: str
    """
    '#/components/schemas/CreateL7PolicySchema/properties/redirect_prefix'
    "$.components.schemas.CreateL7PolicySchema.properties.redirect_prefix"
    """

    redirect_url: str
    """
    '#/components/schemas/CreateL7PolicySchema/properties/redirect_url'
    "$.components.schemas.CreateL7PolicySchema.properties.redirect_url"
    """

    tags: List[str]
    """
    '#/components/schemas/CreateL7PolicySchema/properties/tags'
    "$.components.schemas.CreateL7PolicySchema.properties.tags"
    """
