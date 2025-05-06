# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LoadBalancerL7Rule"]


class LoadBalancerL7Rule(BaseModel):
    id: Optional[str] = None
    """L7Rule ID"""

    compare_type: Optional[Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"]] = None
    """The comparison type for the L7 rule"""

    invert: Optional[bool] = None
    """When true the logic of the rule is inverted.

    For example, with invert true, 'equal to' would become 'not equal to'. Default
    is false.
    """

    key: Optional[str] = None
    """The key to use for the comparison.

    For example, the name of the cookie to evaluate.
    """

    operating_status: Optional[Literal["DEGRADED", "DRAINING", "ERROR", "NO_MONITOR", "OFFLINE", "ONLINE"]] = None
    """L7 policy operating status"""

    project_id: Optional[int] = None
    """Project ID"""

    provisioning_status: Optional[
        Literal["ACTIVE", "DELETED", "ERROR", "PENDING_CREATE", "PENDING_DELETE", "PENDING_UPDATE"]
    ] = None

    region: Optional[str] = None
    """Region name"""

    region_id: Optional[int] = None
    """Region ID"""

    tags: Optional[List[str]] = None
    """A list of simple strings assigned to the l7 rule"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
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
    """The L7 rule type"""

    value: Optional[str] = None
    """The value to use for the comparison. For example, the file type to compare."""
