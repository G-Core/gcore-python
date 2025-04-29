# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .l7_rule import L7Rule
from ..._models import BaseModel

__all__ = ["L7Policy"]


class L7Policy(BaseModel):
    id: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/id'
    "$.components.schemas.L7PolicySchema.properties.id"
    """

    action: Optional[Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"]] = None
    """
    '#/components/schemas/L7PolicySchema/properties/action'
    "$.components.schemas.L7PolicySchema.properties.action"
    """

    listener_id: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/listener_id'
    "$.components.schemas.L7PolicySchema.properties.listener_id"
    """

    name: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/name'
    "$.components.schemas.L7PolicySchema.properties.name"
    """

    operating_status: Optional[Literal["DEGRADED", "DRAINING", "ERROR", "NO_MONITOR", "OFFLINE", "ONLINE"]] = None
    """
    '#/components/schemas/L7PolicySchema/properties/operating_status'
    "$.components.schemas.L7PolicySchema.properties.operating_status"
    """

    position: Optional[int] = None
    """
    '#/components/schemas/L7PolicySchema/properties/position'
    "$.components.schemas.L7PolicySchema.properties.position"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/L7PolicySchema/properties/project_id'
    "$.components.schemas.L7PolicySchema.properties.project_id"
    """

    provisioning_status: Optional[
        Literal["ACTIVE", "DELETED", "ERROR", "PENDING_CREATE", "PENDING_DELETE", "PENDING_UPDATE"]
    ] = None
    """
    '#/components/schemas/L7PolicySchema/properties/provisioning_status'
    "$.components.schemas.L7PolicySchema.properties.provisioning_status"
    """

    redirect_http_code: Optional[int] = None
    """
    '#/components/schemas/L7PolicySchema/properties/redirect_http_code'
    "$.components.schemas.L7PolicySchema.properties.redirect_http_code"
    """

    redirect_pool_id: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/redirect_pool_id'
    "$.components.schemas.L7PolicySchema.properties.redirect_pool_id"
    """

    redirect_prefix: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/redirect_prefix'
    "$.components.schemas.L7PolicySchema.properties.redirect_prefix"
    """

    redirect_url: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/redirect_url'
    "$.components.schemas.L7PolicySchema.properties.redirect_url"
    """

    region: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/region'
    "$.components.schemas.L7PolicySchema.properties.region"
    """

    region_id: Optional[int] = None
    """
    '#/components/schemas/L7PolicySchema/properties/region_id'
    "$.components.schemas.L7PolicySchema.properties.region_id"
    """

    rules: Optional[List[L7Rule]] = None
    """
    '#/components/schemas/L7PolicySchema/properties/rules'
    "$.components.schemas.L7PolicySchema.properties.rules"
    """

    tags: Optional[List[str]] = None
    """
    '#/components/schemas/L7PolicySchema/properties/tags'
    "$.components.schemas.L7PolicySchema.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/L7PolicySchema/properties/task_id'
    "$.components.schemas.L7PolicySchema.properties.task_id"
    """
