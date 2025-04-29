# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = ["FileShare"]


class FileShare(BaseModel):
    id: str
    """
    '#/components/schemas/FileShareSerializer/properties/id'
    "$.components.schemas.FileShareSerializer.properties.id"
    """

    connection_point: Optional[str] = None
    """
    '#/components/schemas/FileShareSerializer/properties/connection_point/anyOf/0'
    "$.components.schemas.FileShareSerializer.properties.connection_point.anyOf[0]"
    """

    created_at: str
    """
    '#/components/schemas/FileShareSerializer/properties/created_at'
    "$.components.schemas.FileShareSerializer.properties.created_at"
    """

    creator_task_id: str
    """
    '#/components/schemas/FileShareSerializer/properties/creator_task_id'
    "$.components.schemas.FileShareSerializer.properties.creator_task_id"
    """

    metadata: Dict[str, str]
    """
    '#/components/schemas/FileShareSerializer/properties/metadata'
    "$.components.schemas.FileShareSerializer.properties.metadata"
    """

    metadata_detailed: List[Tag]
    """
    '#/components/schemas/FileShareSerializer/properties/metadata_detailed'
    "$.components.schemas.FileShareSerializer.properties.metadata_detailed"
    """

    name: str
    """
    '#/components/schemas/FileShareSerializer/properties/name'
    "$.components.schemas.FileShareSerializer.properties.name"
    """

    network_id: str
    """
    '#/components/schemas/FileShareSerializer/properties/network_id'
    "$.components.schemas.FileShareSerializer.properties.network_id"
    """

    network_name: str
    """
    '#/components/schemas/FileShareSerializer/properties/network_name'
    "$.components.schemas.FileShareSerializer.properties.network_name"
    """

    project_id: int
    """
    '#/components/schemas/FileShareSerializer/properties/project_id'
    "$.components.schemas.FileShareSerializer.properties.project_id"
    """

    protocol: str
    """
    '#/components/schemas/FileShareSerializer/properties/protocol'
    "$.components.schemas.FileShareSerializer.properties.protocol"
    """

    region: str
    """
    '#/components/schemas/FileShareSerializer/properties/region'
    "$.components.schemas.FileShareSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/FileShareSerializer/properties/region_id'
    "$.components.schemas.FileShareSerializer.properties.region_id"
    """

    share_network_name: Optional[str] = None
    """
    '#/components/schemas/FileShareSerializer/properties/share_network_name/anyOf/0'
    "$.components.schemas.FileShareSerializer.properties.share_network_name.anyOf[0]"
    """

    size: int
    """
    '#/components/schemas/FileShareSerializer/properties/size'
    "$.components.schemas.FileShareSerializer.properties.size"
    """

    status: Literal[
        "available",
        "awaiting_transfer",
        "backup_creating",
        "backup_restoring",
        "backup_restoring_error",
        "creating",
        "creating_from_snapshot",
        "deleted",
        "deleting",
        "ensuring",
        "error",
        "error_deleting",
        "extending",
        "extending_error",
        "inactive",
        "manage_error",
        "manage_starting",
        "migrating",
        "migrating_to",
        "replication_change",
        "reverting",
        "reverting_error",
        "shrinking",
        "shrinking_error",
        "shrinking_possible_data_loss_error",
        "unmanage_error",
        "unmanage_starting",
        "unmanaged",
    ]
    """
    '#/components/schemas/FileShareSerializer/properties/status'
    "$.components.schemas.FileShareSerializer.properties.status"
    """

    subnet_id: str
    """
    '#/components/schemas/FileShareSerializer/properties/subnet_id'
    "$.components.schemas.FileShareSerializer.properties.subnet_id"
    """

    subnet_name: str
    """
    '#/components/schemas/FileShareSerializer/properties/subnet_name'
    "$.components.schemas.FileShareSerializer.properties.subnet_name"
    """

    tags: List[Tag]
    """
    '#/components/schemas/FileShareSerializer/properties/tags'
    "$.components.schemas.FileShareSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/FileShareSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.FileShareSerializer.properties.task_id.anyOf[0]"
    """

    volume_type: Literal["default_share_type", "vast_share_type"]
    """
    '#/components/schemas/FileShareSerializer/properties/volume_type'
    "$.components.schemas.FileShareSerializer.properties.volume_type"
    """
