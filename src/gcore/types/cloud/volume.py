# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .tag import Tag
from ..._models import BaseModel

__all__ = ["Volume", "Attachment", "LimiterStats"]


class Attachment(BaseModel):
    attachment_id: str
    """The unique identifier of the attachment object."""

    volume_id: str
    """The unique identifier of the attached volume."""

    attached_at: Optional[datetime] = None
    """The date and time when the attachment was created."""

    device: Optional[str] = None
    """The block device name inside the guest instance."""

    flavor_id: Optional[str] = None
    """The flavor ID of the instance."""

    instance_name: Optional[str] = None
    """The name of the instance if attached and the server name is known."""

    server_id: Optional[str] = None
    """The unique identifier of the instance."""


class LimiterStats(BaseModel):
    """Schema representing the Quality of Service (QoS) parameters for a volume."""

    iops_base_limit: int
    """The sustained IOPS (Input/Output Operations Per Second) limit."""

    iops_burst_limit: int
    """The burst IOPS limit."""

    m_bps_base_limit: int = FieldInfo(alias="MBps_base_limit")
    """The sustained bandwidth limit in megabytes per second (MBps)."""

    m_bps_burst_limit: int = FieldInfo(alias="MBps_burst_limit")
    """The burst bandwidth limit in megabytes per second (MBps)."""


class Volume(BaseModel):
    id: str
    """The unique identifier of the volume."""

    bootable: bool
    """Indicates whether the volume is bootable."""

    created_at: datetime
    """The date and time when the volume was created."""

    is_root_volume: bool
    """Indicates whether this is a root volume."""

    name: str
    """The name of the volume."""

    project_id: int
    """Project ID."""

    region: str
    """The region where the volume is located."""

    region_id: int
    """The identifier of the region."""

    size: int
    """The size of the volume in gibibytes (GiB)."""

    status: Literal[
        "attaching",
        "available",
        "awaiting-transfer",
        "backing-up",
        "creating",
        "deleting",
        "detaching",
        "downloading",
        "error",
        "error_backing-up",
        "error_deleting",
        "error_extending",
        "error_restoring",
        "extending",
        "in-use",
        "maintenance",
        "reserved",
        "restoring-backup",
        "retyping",
        "reverting",
        "uploading",
    ]
    """The current status of the volume."""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    volume_type: str
    """The type of volume storage."""

    attachments: Optional[List[Attachment]] = None
    """List of attachments associated with the volume."""

    creator_task_id: Optional[str] = None
    """The ID of the task that created this volume."""

    limiter_stats: Optional[LimiterStats] = None
    """Schema representing the Quality of Service (QoS) parameters for a volume."""

    snapshot_ids: Optional[List[str]] = None
    """List of snapshot IDs associated with this volume."""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    updated_at: Optional[datetime] = None
    """The date and time when the volume was last updated."""

    volume_image_metadata: Optional[Dict[str, str]] = None
    """Image metadata for volumes created from an image."""
