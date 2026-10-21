# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from ..logs_uploader_validation import LogsUploaderValidation

__all__ = [
    "LogsUploaderTarget",
    "LogsUploaderTargetResponseS3Gcore",
    "LogsUploaderTargetResponseS3GcoreConfig",
    "LogsUploaderTargetResponseS3GcoreConfigS3GcoreConfigResponse",
    "LogsUploaderTargetResponseS3GcoreConfigS3GcoreBoundConfigResponse",
    "LogsUploaderTargetResponseS3GcoreStatus",
    "LogsUploaderTargetResponseS3Amazon",
    "LogsUploaderTargetResponseS3AmazonConfig",
    "LogsUploaderTargetResponseS3AmazonStatus",
    "LogsUploaderTargetResponseS3Oss",
    "LogsUploaderTargetResponseS3OssConfig",
    "LogsUploaderTargetResponseS3OssStatus",
    "LogsUploaderTargetResponseS3Other",
    "LogsUploaderTargetResponseS3OtherConfig",
    "LogsUploaderTargetResponseS3OtherStatus",
    "LogsUploaderTargetResponseS3V1",
    "LogsUploaderTargetResponseS3V1Config",
    "LogsUploaderTargetResponseS3V1Status",
    "LogsUploaderTargetResponseFtp",
    "LogsUploaderTargetResponseFtpConfig",
    "LogsUploaderTargetResponseFtpStatus",
    "LogsUploaderTargetResponseSftp",
    "LogsUploaderTargetResponseSftpConfig",
    "LogsUploaderTargetResponseSftpStatus",
    "LogsUploaderTargetResponseHTTP",
    "LogsUploaderTargetResponseHTTPConfig",
    "LogsUploaderTargetResponseHTTPConfigAppend",
    "LogsUploaderTargetResponseHTTPConfigAppendResponseAction",
    "LogsUploaderTargetResponseHTTPConfigAuth",
    "LogsUploaderTargetResponseHTTPConfigAuthConfig",
    "LogsUploaderTargetResponseHTTPConfigRetry",
    "LogsUploaderTargetResponseHTTPConfigRetryResponseAction",
    "LogsUploaderTargetResponseHTTPConfigUpload",
    "LogsUploaderTargetResponseHTTPConfigUploadResponseAction",
    "LogsUploaderTargetResponseHTTPStatus",
    "LogsUploaderTargetResponseAzureBlob",
    "LogsUploaderTargetResponseAzureBlobConfig",
    "LogsUploaderTargetResponseAzureBlobConfigAuth",
    "LogsUploaderTargetResponseAzureBlobConfigAuthConfig",
    "LogsUploaderTargetResponseAzureBlobConfigAuthConfigAccountKey",
    "LogsUploaderTargetResponseAzureBlobConfigAuthConfigToken",
    "LogsUploaderTargetResponseAzureBlobStatus",
    "LogsUploaderTargetResponseSls",
    "LogsUploaderTargetResponseSlsConfig",
    "LogsUploaderTargetResponseSlsConfigAuth",
    "LogsUploaderTargetResponseSlsConfigAuthConfig",
    "LogsUploaderTargetResponseSlsStatus",
]


class LogsUploaderTargetResponseS3GcoreConfigS3GcoreConfigResponse(BaseModel):
    access_key_id: str

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    endpoint: Optional[str] = None

    region: Optional[str] = None

    use_path_style: Optional[bool] = None


class LogsUploaderTargetResponseS3GcoreConfigS3GcoreBoundConfigResponse(BaseModel):
    """A target bound to your Gcore Object Storage.

    The CDN manages the connection, so its settings
    are not returned.
    """

    bucket_name: str

    storage_id: int
    """ID of your Gcore Object Storage."""

    directory: Optional[str] = None


LogsUploaderTargetResponseS3GcoreConfig: TypeAlias = Union[
    LogsUploaderTargetResponseS3GcoreConfigS3GcoreConfigResponse,
    LogsUploaderTargetResponseS3GcoreConfigS3GcoreBoundConfigResponse,
]


class LogsUploaderTargetResponseS3GcoreStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseS3Gcore(BaseModel):
    storage_type: Literal["s3_gcore"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseS3GcoreConfig] = None
    """Config for the `s3_gcore` storage type."""

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseS3GcoreStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseS3AmazonConfig(BaseModel):
    access_key_id: Optional[str] = None

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    region: Optional[str] = None


class LogsUploaderTargetResponseS3AmazonStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseS3Amazon(BaseModel):
    storage_type: Literal["s3_amazon"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseS3AmazonConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseS3AmazonStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseS3OssConfig(BaseModel):
    access_key_id: Optional[str] = None

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    endpoint: Optional[str] = None

    region: Optional[str] = None


class LogsUploaderTargetResponseS3OssStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseS3Oss(BaseModel):
    storage_type: Literal["s3_oss"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseS3OssConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseS3OssStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseS3OtherConfig(BaseModel):
    access_key_id: str

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    endpoint: Optional[str] = None

    region: Optional[str] = None

    use_path_style: Optional[bool] = None


class LogsUploaderTargetResponseS3OtherStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseS3Other(BaseModel):
    storage_type: Literal["s3_other"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseS3OtherConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseS3OtherStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseS3V1Config(BaseModel):
    access_key_id: str

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    endpoint: Optional[str] = None

    region: Optional[str] = None

    use_path_style: Optional[bool] = None


class LogsUploaderTargetResponseS3V1Status(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseS3V1(BaseModel):
    storage_type: Literal["s3_v1"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseS3V1Config] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseS3V1Status] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseFtpConfig(BaseModel):
    directory: Optional[str] = None

    hostname: Optional[str] = None

    timeout_seconds: Optional[int] = None

    user: Optional[str] = None


class LogsUploaderTargetResponseFtpStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseFtp(BaseModel):
    storage_type: Literal["ftp"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseFtpConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseFtpStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseSftpConfig(BaseModel):
    directory: Optional[str] = None

    hostname: Optional[str] = None

    key_passphrase: Optional[str] = None

    password: Optional[str] = None

    private_key: Optional[str] = None

    timeout_seconds: Optional[int] = None

    user: Optional[str] = None


class LogsUploaderTargetResponseSftpStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseSftp(BaseModel):
    storage_type: Literal["sftp"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseSftpConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseSftpStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseHTTPConfigAppendResponseAction(BaseModel):
    action: Optional[Literal["drop", "retry", "append"]] = None

    description: Optional[str] = None

    match_payload: Optional[str] = None

    match_status_code: Optional[int] = None


class LogsUploaderTargetResponseHTTPConfigAppend(BaseModel):
    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["POST", "PUT"]] = None

    response_actions: Optional[List[LogsUploaderTargetResponseHTTPConfigAppendResponseAction]] = None

    timeout_seconds: Optional[int] = None

    url: Optional[str] = None

    use_compression: Optional[bool] = None


class LogsUploaderTargetResponseHTTPConfigAuthConfig(BaseModel):
    token: Optional[str] = None

    header_name: Optional[str] = None


class LogsUploaderTargetResponseHTTPConfigAuth(BaseModel):
    config: Optional[LogsUploaderTargetResponseHTTPConfigAuthConfig] = None

    type: Optional[Literal["token"]] = None


class LogsUploaderTargetResponseHTTPConfigRetryResponseAction(BaseModel):
    action: Optional[Literal["drop", "retry", "append"]] = None

    description: Optional[str] = None

    match_payload: Optional[str] = None

    match_status_code: Optional[int] = None


class LogsUploaderTargetResponseHTTPConfigRetry(BaseModel):
    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["POST", "PUT"]] = None

    response_actions: Optional[List[LogsUploaderTargetResponseHTTPConfigRetryResponseAction]] = None

    timeout_seconds: Optional[int] = None

    url: Optional[str] = None

    use_compression: Optional[bool] = None


class LogsUploaderTargetResponseHTTPConfigUploadResponseAction(BaseModel):
    action: Optional[Literal["drop", "retry", "append"]] = None

    description: Optional[str] = None

    match_payload: Optional[str] = None

    match_status_code: Optional[int] = None


class LogsUploaderTargetResponseHTTPConfigUpload(BaseModel):
    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["POST", "PUT"]] = None

    response_actions: Optional[List[LogsUploaderTargetResponseHTTPConfigUploadResponseAction]] = None

    timeout_seconds: Optional[int] = None

    url: Optional[str] = None

    use_compression: Optional[bool] = None


class LogsUploaderTargetResponseHTTPConfig(BaseModel):
    append: Optional[LogsUploaderTargetResponseHTTPConfigAppend] = None

    auth: Optional[LogsUploaderTargetResponseHTTPConfigAuth] = None

    content_type: Optional[Literal["json", "text"]] = None

    retry: Optional[LogsUploaderTargetResponseHTTPConfigRetry] = None

    upload: Optional[LogsUploaderTargetResponseHTTPConfigUpload] = None


class LogsUploaderTargetResponseHTTPStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseHTTP(BaseModel):
    storage_type: Literal["http"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseHTTPConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseHTTPStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseAzureBlobConfigAuthConfigAccountKey(BaseModel):
    account_key: str
    """Masked secret value."""


class LogsUploaderTargetResponseAzureBlobConfigAuthConfigToken(BaseModel):
    token: str
    """Masked secret value."""


LogsUploaderTargetResponseAzureBlobConfigAuthConfig: TypeAlias = Union[
    LogsUploaderTargetResponseAzureBlobConfigAuthConfigAccountKey,
    LogsUploaderTargetResponseAzureBlobConfigAuthConfigToken,
]


class LogsUploaderTargetResponseAzureBlobConfigAuth(BaseModel):
    config: LogsUploaderTargetResponseAzureBlobConfigAuthConfig
    """Authentication credentials. Secret fields are masked with '**\\****'."""

    type: Literal["shared_key", "sas_token"]
    """Authentication type."""


class LogsUploaderTargetResponseAzureBlobConfig(BaseModel):
    account_name: Optional[str] = None
    """Azure Blob Storage account name."""

    auth: Optional[LogsUploaderTargetResponseAzureBlobConfigAuth] = None

    container_name: Optional[str] = None
    """Azure Blob Storage container name."""

    directory: Optional[str] = None
    """Directory path within the container."""

    endpoint: Optional[str] = None
    """Custom Azure Blob Storage endpoint URL."""


class LogsUploaderTargetResponseAzureBlobStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseAzureBlob(BaseModel):
    storage_type: Literal["azure_blob"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseAzureBlobConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseAzureBlobStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


class LogsUploaderTargetResponseSlsConfigAuthConfig(BaseModel):
    """Authentication credentials. Secret fields are masked with '*****'."""

    access_key_id: Optional[str] = None
    """Alibaba access key ID."""

    secret_access_key: Optional[str] = None
    """Masked secret value."""


class LogsUploaderTargetResponseSlsConfigAuth(BaseModel):
    config: LogsUploaderTargetResponseSlsConfigAuthConfig
    """Authentication credentials. Secret fields are masked with '**\\****'."""

    type: Literal["ak_sk"]
    """Authentication type."""


class LogsUploaderTargetResponseSlsConfig(BaseModel):
    auth: Optional[LogsUploaderTargetResponseSlsConfigAuth] = None

    endpoint: Optional[str] = None
    """SLS endpoint.

    Optional — derived from the region as `{region}.log.aliyuncs.com` when omitted.
    """

    log_store: Optional[str] = None
    """SLS logstore name.

    3-36 characters; lowercase letters, digits, hyphens, and underscores.
    """

    project: Optional[str] = None
    """SLS project name. 3-63 characters; lowercase letters, digits, and hyphens."""

    region: Optional[str] = None
    """SLS region (e.g. `eu-central-1`)."""

    topic: Optional[str] = None
    """Optional SLS topic (0-128 characters)."""


class LogsUploaderTargetResponseSlsStatus(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTargetResponseSls(BaseModel):
    storage_type: Literal["sls"]
    """Type of storage for logs."""

    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[LogsUploaderTargetResponseSlsConfig] = None

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[LogsUploaderTargetResponseSlsStatus] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""


LogsUploaderTarget: TypeAlias = Annotated[
    Union[
        LogsUploaderTargetResponseS3Gcore,
        LogsUploaderTargetResponseS3Amazon,
        LogsUploaderTargetResponseS3Oss,
        LogsUploaderTargetResponseS3Other,
        LogsUploaderTargetResponseS3V1,
        LogsUploaderTargetResponseFtp,
        LogsUploaderTargetResponseSftp,
        LogsUploaderTargetResponseHTTP,
        LogsUploaderTargetResponseAzureBlob,
        LogsUploaderTargetResponseSls,
    ],
    PropertyInfo(discriminator="storage_type"),
]
