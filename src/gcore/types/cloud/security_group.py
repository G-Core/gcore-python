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
    """Tags for a security group"""

    updated_at: datetime
    """Datetime when the security group was last updated"""

    description: Optional[str] = None
    """Security group description"""

    security_group_rules: Optional[List[SecurityGroupRule]] = None
    """Security group rules"""
