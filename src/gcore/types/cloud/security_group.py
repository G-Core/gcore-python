# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel
from .security_group_rule import SecurityGroupRule

__all__ = ["SecurityGroup"]


class SecurityGroup(BaseModel):
    id: str
    """Security group ID"""

    created_at: datetime
    """Datetime when the security group was created"""

    name: str
    """Security group name"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    revision_number: int
    """The number of revisions"""

    tags_v2: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    updated_at: datetime
    """Datetime when the security group was last updated"""

    description: Optional[str] = None
    """Security group description"""

    security_group_rules: Optional[List[SecurityGroupRule]] = None
    """Security group rules"""
