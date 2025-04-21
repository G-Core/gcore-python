# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSHKeyCreated"]


class SSHKeyCreated(BaseModel):
    id: str
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/id'
    "$.components.schemas.CreatedSSHKeySerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/created_at'
    "$.components.schemas.CreatedSSHKeySerializer.properties.created_at"
    """

    fingerprint: str
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/fingerprint'
    "$.components.schemas.CreatedSSHKeySerializer.properties.fingerprint"
    """

    name: str
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/name'
    "$.components.schemas.CreatedSSHKeySerializer.properties.name"
    """

    private_key: Optional[str] = None
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/private_key/anyOf/0'
    "$.components.schemas.CreatedSSHKeySerializer.properties.private_key.anyOf[0]"
    """

    project_id: int
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/project_id'
    "$.components.schemas.CreatedSSHKeySerializer.properties.project_id"
    """

    public_key: str
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/public_key'
    "$.components.schemas.CreatedSSHKeySerializer.properties.public_key"
    """

    shared_in_project: bool
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/shared_in_project'
    "$.components.schemas.CreatedSSHKeySerializer.properties.shared_in_project"
    """

    state: Literal["ACTIVE", "DELETING"]
    """
    '#/components/schemas/CreatedSSHKeySerializer/properties/state'
    "$.components.schemas.CreatedSSHKeySerializer.properties.state"
    """
