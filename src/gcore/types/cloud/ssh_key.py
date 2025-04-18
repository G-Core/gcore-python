# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSHKey"]


class SSHKey(BaseModel):
    id: str
    """
    '#/components/schemas/SSHKeySerializer/properties/id'
    "$.components.schemas.SSHKeySerializer.properties.id"
    """

    created_at: Optional[datetime] = None
    """
    '#/components/schemas/SSHKeySerializer/properties/created_at/anyOf/0'
    "$.components.schemas.SSHKeySerializer.properties.created_at.anyOf[0]"
    """

    fingerprint: str
    """
    '#/components/schemas/SSHKeySerializer/properties/fingerprint'
    "$.components.schemas.SSHKeySerializer.properties.fingerprint"
    """

    name: str
    """
    '#/components/schemas/SSHKeySerializer/properties/name'
    "$.components.schemas.SSHKeySerializer.properties.name"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/SSHKeySerializer/properties/project_id/anyOf/0'
    "$.components.schemas.SSHKeySerializer.properties.project_id.anyOf[0]"
    """

    public_key: str
    """
    '#/components/schemas/SSHKeySerializer/properties/public_key'
    "$.components.schemas.SSHKeySerializer.properties.public_key"
    """

    shared_in_project: bool
    """
    '#/components/schemas/SSHKeySerializer/properties/shared_in_project'
    "$.components.schemas.SSHKeySerializer.properties.shared_in_project"
    """

    state: Literal["ACTIVE", "DELETING"]
    """
    '#/components/schemas/SSHKeySerializer/properties/state'
    "$.components.schemas.SSHKeySerializer.properties.state"
    """
