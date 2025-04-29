# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["L7PolicyReplaceParams"]


class L7PolicyReplaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/0/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/1/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[1].schema"
    """

    action: Required[Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"]]
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/action'
    "$.components.schemas.UpdateL7PolicySchema.properties.action"
    """

    name: str
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/name'
    "$.components.schemas.UpdateL7PolicySchema.properties.name"
    """

    position: int
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/position'
    "$.components.schemas.UpdateL7PolicySchema.properties.position"
    """

    redirect_http_code: int
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/redirect_http_code'
    "$.components.schemas.UpdateL7PolicySchema.properties.redirect_http_code"
    """

    redirect_pool_id: str
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/redirect_pool_id'
    "$.components.schemas.UpdateL7PolicySchema.properties.redirect_pool_id"
    """

    redirect_prefix: str
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/redirect_prefix'
    "$.components.schemas.UpdateL7PolicySchema.properties.redirect_prefix"
    """

    redirect_url: str
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/redirect_url'
    "$.components.schemas.UpdateL7PolicySchema.properties.redirect_url"
    """

    tags: List[str]
    """
    '#/components/schemas/UpdateL7PolicySchema/properties/tags'
    "$.components.schemas.UpdateL7PolicySchema.properties.tags"
    """
