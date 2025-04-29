# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["L7Rule"]


class L7Rule(BaseModel):
    id: Optional[str] = None
    """
    '#/components/schemas/L7RuleSchema/properties/id'
    "$.components.schemas.L7RuleSchema.properties.id"
    """

    compare_type: Optional[Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"]] = None
    """
    '#/components/schemas/L7RuleSchema/properties/compare_type'
    "$.components.schemas.L7RuleSchema.properties.compare_type"
    """

    invert: Optional[bool] = None
    """
    '#/components/schemas/L7RuleSchema/properties/invert'
    "$.components.schemas.L7RuleSchema.properties.invert"
    """

    key: Optional[str] = None
    """
    '#/components/schemas/L7RuleSchema/properties/key'
    "$.components.schemas.L7RuleSchema.properties.key"
    """

    operating_status: Optional[Literal["DEGRADED", "DRAINING", "ERROR", "NO_MONITOR", "OFFLINE", "ONLINE"]] = None
    """
    '#/components/schemas/L7RuleSchema/properties/operating_status'
    "$.components.schemas.L7RuleSchema.properties.operating_status"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/L7RuleSchema/properties/project_id'
    "$.components.schemas.L7RuleSchema.properties.project_id"
    """

    provisioning_status: Optional[
        Literal["ACTIVE", "DELETED", "ERROR", "PENDING_CREATE", "PENDING_DELETE", "PENDING_UPDATE"]
    ] = None
    """
    '#/components/schemas/L7RuleSchema/properties/provisioning_status'
    "$.components.schemas.L7RuleSchema.properties.provisioning_status"
    """

    region: Optional[str] = None
    """
    '#/components/schemas/L7RuleSchema/properties/region'
    "$.components.schemas.L7RuleSchema.properties.region"
    """

    region_id: Optional[int] = None
    """
    '#/components/schemas/L7RuleSchema/properties/region_id'
    "$.components.schemas.L7RuleSchema.properties.region_id"
    """

    tags: Optional[List[str]] = None
    """
    '#/components/schemas/L7RuleSchema/properties/tags'
    "$.components.schemas.L7RuleSchema.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/L7RuleSchema/properties/task_id'
    "$.components.schemas.L7RuleSchema.properties.task_id"
    """

    type: Optional[
        Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ]
    ] = None
    """
    '#/components/schemas/L7RuleSchema/properties/type'
    "$.components.schemas.L7RuleSchema.properties.type"
    """

    value: Optional[str] = None
    """
    '#/components/schemas/L7RuleSchema/properties/value'
    "$.components.schemas.L7RuleSchema.properties.value"
    """
