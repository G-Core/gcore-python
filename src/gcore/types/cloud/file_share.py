# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .tag import Tag
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "FileShare",
    "Network",
    "ShareSettings",
    "ShareSettingsStandardShareSettingsOutputSerializer",
    "ShareSettingsDdnShareSettingsOutputSerializer",
    "ShareSettingsVastShareSettingsOutputSerializer",
    "ShareSettingsVastShareSettingsOutputSerializerQuota",
    "ShareSettingsVastShareSettingsOutputSerializerQuotaDefaultGroupQuota",
    "ShareSettingsVastShareSettingsOutputSerializerQuotaDefaultUserQuota",
    "ShareSettingsVastShareSettingsOutputSerializerQuotaOverride",
]


class Network(BaseModel):
    """Network and subnet of the file share."""

    network_id: str
    """Network ID."""

    network_name: str
    """Network name."""

    subnet_id: str
    """ID of the subnet that the file share uses."""

    subnet_name: str
    """Subnet name."""


class ShareSettingsStandardShareSettingsOutputSerializer(BaseModel):
    type_name: Literal["standard"]
    """Standard file share type"""


class ShareSettingsDdnShareSettingsOutputSerializer(BaseModel):
    gid: Optional[int] = None
    """Group ID being owner of the share"""

    projid: Optional[int] = None
    """Exascaler project ID"""

    type_name: Literal["ddn"]
    """DDN file share type"""

    uid: Optional[int] = None
    """User ID being owner of the share"""


class ShareSettingsVastShareSettingsOutputSerializerQuotaDefaultGroupQuota(BaseModel):
    """Quota for each group without an override.

    The value is `null` if there is no default.
    """

    grace_period: Optional[str] = None
    """Time after the usage goes above `soft_limit`, in the `D HH:MM:SS` format."""

    hard_limit: Optional[int] = None
    """Maximum capacity in bytes.

    Write operations fail when the usage reaches this limit.
    """

    soft_limit: Optional[int] = None
    """Capacity in bytes that starts the grace period."""


class ShareSettingsVastShareSettingsOutputSerializerQuotaDefaultUserQuota(BaseModel):
    """Quota for each user without an override.

    The value is `null` if there is no default.
    """

    grace_period: Optional[str] = None
    """Time after the usage goes above `soft_limit`, in the `D HH:MM:SS` format."""

    hard_limit: Optional[int] = None
    """Maximum capacity in bytes.

    Write operations fail when the usage reaches this limit.
    """

    soft_limit: Optional[int] = None
    """Capacity in bytes that starts the grace period."""


class ShareSettingsVastShareSettingsOutputSerializerQuotaOverride(BaseModel):
    grace_period: Optional[str] = None
    """Time after the usage goes above `soft_limit`, in the `D HH:MM:SS` format."""

    hard_limit: Optional[int] = None
    """Maximum capacity in bytes.

    Write operations fail when the usage reaches this limit.
    """

    identifier: int
    """Numeric user ID or group ID."""

    identifier_type: Literal["gid", "uid"]
    """Type of `identifier`. The value `uid` is for a user and `gid` is for a group."""

    soft_limit: Optional[int] = None
    """Capacity in bytes that starts the grace period."""

    state: Literal[
        "FAILED",
        "GRACE_EXPIRED",
        "HARD_BOTH_EXCEEDED",
        "HARD_EXCEEDED",
        "INODE_HARD_EXCEEDED",
        "INODE_SOFT_EXCEEDED",
        "OK",
        "SOFT_BOTH_EXCEEDED",
        "SOFT_EXCEEDED",
        "UNKNOWN",
    ]
    """Usage state of the quota.

    `OK` means that the usage is below the limits. `SOFT_EXCEEDED`,
    `INODE_SOFT_EXCEEDED` and `SOFT_BOTH_EXCEEDED` mean that the capacity, the
    number of files or both are above the soft limit. `GRACE_EXPIRED` means that the
    grace period is over and write operations fail. `HARD_EXCEEDED`,
    `INODE_HARD_EXCEEDED` and `HARD_BOTH_EXCEEDED` mean that the capacity, the
    number of files or both are at the hard limit and write operations fail.
    `FAILED` means that the system cannot get the state. `UNKNOWN` means that the
    state is not available.
    """


class ShareSettingsVastShareSettingsOutputSerializerQuota(BaseModel):
    """User and group quotas of the file share.

    The value is `null` if quotas are disabled or if the quotas are not available.
    """

    default_group_quota: Optional[ShareSettingsVastShareSettingsOutputSerializerQuotaDefaultGroupQuota] = None
    """Quota for each group without an override.

    The value is `null` if there is no default.
    """

    default_user_quota: Optional[ShareSettingsVastShareSettingsOutputSerializerQuotaDefaultUserQuota] = None
    """Quota for each user without an override.

    The value is `null` if there is no default.
    """

    overrides: List[ShareSettingsVastShareSettingsOutputSerializerQuotaOverride]
    """Quotas for specified users and groups."""


class ShareSettingsVastShareSettingsOutputSerializer(BaseModel):
    allowed_characters: Optional[Literal["LCD", "NPL"]] = None

    path_length: Optional[Literal["LCD", "NPL"]] = None

    quota: Optional[ShareSettingsVastShareSettingsOutputSerializerQuota] = None
    """User and group quotas of the file share.

    The value is `null` if quotas are disabled or if the quotas are not available.
    """

    root_squash: bool
    """Enables or disables root squash for NFS clients.

    - If `true`, root squash is enabled: the root user is mapped to nobody for all
      file and folder management operations on the export.
    - If `false`, root squash is disabled: the NFS client `root` user retains root
      privileges.
    """

    trash_access: bool
    """
    Shows whether clients within the share's access range can move files and folders
    to the hidden `.vast_trash` folder for asynchronous deletion.
    """

    type_name: Literal["vast"]
    """Vast file share type"""


ShareSettings: TypeAlias = Annotated[
    Union[
        ShareSettingsStandardShareSettingsOutputSerializer,
        ShareSettingsDdnShareSettingsOutputSerializer,
        ShareSettingsVastShareSettingsOutputSerializer,
    ],
    PropertyInfo(discriminator="type_name"),
]


class FileShare(BaseModel):
    id: str
    """File share ID"""

    connection_point: Optional[str] = None
    """Connection point. Can be null during File share creation"""

    created_at: str
    """Datetime when the file share was created"""

    creator_task_id: str
    """Task that created this entity"""

    name: str
    """File share name"""

    network: Network
    """Network and subnet of the file share."""

    network_id: str
    """Deprecated. Use `network.network_id` instead. Network ID."""

    network_name: str
    """Deprecated. Use `network.network_name` instead. Network name."""

    project_id: int
    """Project ID"""

    protocol: str
    """File share protocol"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    share_network_name: Optional[str] = None
    """Share network name.

    May be null if the file share was created with volume type VAST
    """

    share_settings: ShareSettings
    """Share settings specific to the file share type"""

    size: int
    """File share size in GiB"""

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
    """File share status"""

    subnet_id: str
    """Deprecated. Use `network.subnet_id` instead. Subnet ID."""

    subnet_name: str
    """Deprecated. Use `network.subnet_name` instead. Subnet name."""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    type_name: Literal["ddn", "standard", "vast"]
    """File share type name"""

    volume_type: Literal["ddn_share_type", "default_share_type", "vast_share_type"]
    """Deprecated. Use `type_name` instead. File share disk type"""
