# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel
from .security_group_rule import SecurityGroupRule

__all__ = ["SecurityGroup"]


class SecurityGroup(BaseModel):
    id: str
    """
    '#/components/schemas/SecurityGroupSerializer/properties/id'
    "$.components.schemas.SecurityGroupSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/SecurityGroupSerializer/properties/created_at'
    "$.components.schemas.SecurityGroupSerializer.properties.created_at"
    """

    name: str
    """
    '#/components/schemas/SecurityGroupSerializer/properties/name'
    "$.components.schemas.SecurityGroupSerializer.properties.name"
    """

    project_id: int
    """
    '#/components/schemas/SecurityGroupSerializer/properties/project_id'
    "$.components.schemas.SecurityGroupSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/SecurityGroupSerializer/properties/region'
    "$.components.schemas.SecurityGroupSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/SecurityGroupSerializer/properties/region_id'
    "$.components.schemas.SecurityGroupSerializer.properties.region_id"
    """

    revision_number: int
    """
    '#/components/schemas/SecurityGroupSerializer/properties/revision_number'
    "$.components.schemas.SecurityGroupSerializer.properties.revision_number"
    """

    updated_at: datetime
    """
    '#/components/schemas/SecurityGroupSerializer/properties/updated_at'
    "$.components.schemas.SecurityGroupSerializer.properties.updated_at"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/SecurityGroupSerializer/properties/description/anyOf/0'
    "$.components.schemas.SecurityGroupSerializer.properties.description.anyOf[0]"
    """

    metadata: Optional[List[Tag]] = None
    """
    '#/components/schemas/SecurityGroupSerializer/properties/metadata'
    "$.components.schemas.SecurityGroupSerializer.properties.metadata"
    """

    security_group_rules: Optional[List[SecurityGroupRule]] = None
    """
    '#/components/schemas/SecurityGroupSerializer/properties/security_group_rules'
    "$.components.schemas.SecurityGroupSerializer.properties.security_group_rules"
    """

    tags: Optional[List[str]] = None
    """
    '#/components/schemas/SecurityGroupSerializer/properties/tags/anyOf/0'
    "$.components.schemas.SecurityGroupSerializer.properties.tags.anyOf[0]"
    """
