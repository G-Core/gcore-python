# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Storage", "Credentials", "CredentialsKey", "CredentialsS3"]


class CredentialsKey(BaseModel):
    id: Optional[int] = None
    """Unique identifier for the SSH key"""

    created_at: Optional[str] = None
    """ISO 8601 timestamp when the SSH key was created"""

    name: Optional[str] = None
    """User-defined name for the SSH key"""


class CredentialsS3(BaseModel):
    access_key: Optional[str] = None
    """S3-compatible access key identifier for authentication"""

    secret_key: Optional[str] = None
    """S3-compatible secret key for authentication (keep secure)"""


class Credentials(BaseModel):
    keys: Optional[List[CredentialsKey]] = None
    """SSH public keys associated with SFTP storage for passwordless authentication"""

    s3: Optional[CredentialsS3] = None

    sftp_password: Optional[str] = None
    """
    Generated or user-provided password for SFTP access (only present for SFTP
    storage type)
    """


class Storage(BaseModel):
    id: int
    """Unique identifier for the storage instance"""

    address: str
    """Full hostname/address for accessing the storage endpoint"""

    client_id: int
    """Client identifier who owns this storage"""

    created_at: str
    """ISO 8601 timestamp when the storage was created"""

    location: str
    """Geographic location code where the storage is provisioned"""

    name: str
    """User-defined name for the storage instance"""

    provisioning_status: Literal["creating", "ok", "updating", "deleting", "deleted"]
    """Current provisioning status of the storage instance"""

    reseller_id: int
    """Reseller technical client ID associated with the client"""

    type: Literal["sftp", "s3"]
    """
    Storage protocol type - either S3-compatible object storage or SFTP file
    transfer
    """

    can_restore: Optional[bool] = None
    """
    Whether this storage can be restored if deleted (S3 storages only, within 2
    weeks)
    """

    credentials: Optional[Credentials] = None

    custom_config_file: Optional[bool] = None
    """Whether custom configuration file is used for this storage"""

    deleted_at: Optional[str] = None
    """
    ISO 8601 timestamp when the storage was deleted (only present for deleted
    storages)
    """

    disable_http: Optional[bool] = None
    """Whether HTTP access is disabled for this storage (HTTPS only)"""

    expires: Optional[str] = None
    """ISO 8601 timestamp when the storage will expire (if set)"""

    rewrite_rules: Optional[Dict[str, str]] = None
    """Custom URL rewrite rules for the storage (admin-configurable)"""

    server_alias: Optional[str] = None
    """Custom domain alias for accessing the storage"""
