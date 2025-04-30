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
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/attachment_id'
    "$.components.schemas.VolumeAttachmentSerializer.properties.attachment_id"
    """

    volume_id: str
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/volume_id'
    "$.components.schemas.VolumeAttachmentSerializer.properties.volume_id"
    """

    attached_at: Optional[datetime] = None
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/attached_at/anyOf/0'
    "$.components.schemas.VolumeAttachmentSerializer.properties.attached_at.anyOf[0]"
    """

    device: Optional[str] = None
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/device/anyOf/0'
    "$.components.schemas.VolumeAttachmentSerializer.properties.device.anyOf[0]"
    """

    flavor_id: Optional[str] = None
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/flavor_id/anyOf/0'
    "$.components.schemas.VolumeAttachmentSerializer.properties.flavor_id.anyOf[0]"
    """

    instance_name: Optional[str] = None
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/instance_name/anyOf/0'
    "$.components.schemas.VolumeAttachmentSerializer.properties.instance_name.anyOf[0]"
    """

    server_id: Optional[str] = None
    """
    '#/components/schemas/VolumeAttachmentSerializer/properties/server_id/anyOf/0'
    "$.components.schemas.VolumeAttachmentSerializer.properties.server_id.anyOf[0]"
    """


class LimiterStats(BaseModel):
    iops_base_limit: int
    """
    '#/components/schemas/VolumeLimiterStatsSerializer/properties/iops_base_limit'
    "$.components.schemas.VolumeLimiterStatsSerializer.properties.iops_base_limit"
    """

    iops_burst_limit: int
    """
    '#/components/schemas/VolumeLimiterStatsSerializer/properties/iops_burst_limit'
    "$.components.schemas.VolumeLimiterStatsSerializer.properties.iops_burst_limit"
    """

    m_bps_base_limit: int = FieldInfo(alias="MBps_base_limit")
    """
    '#/components/schemas/VolumeLimiterStatsSerializer/properties/MBps_base_limit'
    "$.components.schemas.VolumeLimiterStatsSerializer.properties.MBps_base_limit"
    """

    m_bps_burst_limit: int = FieldInfo(alias="MBps_burst_limit")
    """
    '#/components/schemas/VolumeLimiterStatsSerializer/properties/MBps_burst_limit'
    "$.components.schemas.VolumeLimiterStatsSerializer.properties.MBps_burst_limit"
    """


class Volume(BaseModel):
    id: str
    """
    '#/components/schemas/VolumeSerializer/properties/id'
    "$.components.schemas.VolumeSerializer.properties.id"
    """

    bootable: bool
    """
    '#/components/schemas/VolumeSerializer/properties/bootable'
    "$.components.schemas.VolumeSerializer.properties.bootable"
    """

    created_at: datetime
    """
    '#/components/schemas/VolumeSerializer/properties/created_at'
    "$.components.schemas.VolumeSerializer.properties.created_at"
    """

    is_root_volume: bool
    """
    '#/components/schemas/VolumeSerializer/properties/is_root_volume'
    "$.components.schemas.VolumeSerializer.properties.is_root_volume"
    """

    name: str
    """
    '#/components/schemas/VolumeSerializer/properties/name'
    "$.components.schemas.VolumeSerializer.properties.name"
    """

    project_id: int
    """
    '#/components/schemas/VolumeSerializer/properties/project_id'
    "$.components.schemas.VolumeSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/VolumeSerializer/properties/region'
    "$.components.schemas.VolumeSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/VolumeSerializer/properties/region_id'
    "$.components.schemas.VolumeSerializer.properties.region_id"
    """

    size: int
    """
    '#/components/schemas/VolumeSerializer/properties/size'
    "$.components.schemas.VolumeSerializer.properties.size"
    """

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
    """
    '#/components/schemas/VolumeSerializer/properties/status'
    "$.components.schemas.VolumeSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/VolumeSerializer/properties/tags'
    "$.components.schemas.VolumeSerializer.properties.tags"
    """

    volume_type: str
    """
    '#/components/schemas/VolumeSerializer/properties/volume_type'
    "$.components.schemas.VolumeSerializer.properties.volume_type"
    """

    attachments: Optional[List[Attachment]] = None
    """
    '#/components/schemas/VolumeSerializer/properties/attachments/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.attachments.anyOf[0]"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/VolumeSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.creator_task_id.anyOf[0]"
    """

    limiter_stats: Optional[LimiterStats] = None
    """
    '#/components/schemas/VolumeSerializer/properties/limiter_stats/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.limiter_stats.anyOf[0]"
    """

    snapshot_ids: Optional[List[str]] = None
    """
    '#/components/schemas/VolumeSerializer/properties/snapshot_ids/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.snapshot_ids.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/VolumeSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.task_id.anyOf[0]"
    """

    updated_at: Optional[datetime] = None
    """
    '#/components/schemas/VolumeSerializer/properties/updated_at/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.updated_at.anyOf[0]"
    """

    volume_image_metadata: Optional[Dict[str, str]] = None
    """
    '#/components/schemas/VolumeSerializer/properties/volume_image_metadata/anyOf/0'
    "$.components.schemas.VolumeSerializer.properties.volume_image_metadata.anyOf[0]"
    """
