# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ..logs_uploader_validation import LogsUploaderValidation

__all__ = [
    "LogsUploaderTarget",
    "Config",
    "ConfigS3GcoreConfigResponse",
    "ConfigS3AmazonConfigResponse",
    "ConfigUnionMember2",
    "ConfigBaseFtpConfig",
    "ConfigSftpConfigResponse",
    "ConfigHTTPConfigResponse",
    "ConfigHTTPConfigResponseAppend",
    "ConfigHTTPConfigResponseAppendResponseAction",
    "ConfigHTTPConfigResponseAuth",
    "ConfigHTTPConfigResponseAuthConfig",
    "ConfigHTTPConfigResponseRetry",
    "ConfigHTTPConfigResponseRetryResponseAction",
    "ConfigHTTPConfigResponseUpload",
    "ConfigHTTPConfigResponseUploadResponseAction",
    "Status",
]


class ConfigS3GcoreConfigResponse(BaseModel):
    access_key_id: Optional[str] = None

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    endpoint: Optional[str] = None

    region: Optional[str] = None

    use_path_style: Optional[bool] = None


class ConfigS3AmazonConfigResponse(BaseModel):
    access_key_id: Optional[str] = None

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    region: Optional[str] = None


class ConfigUnionMember2(BaseModel):
    access_key_id: Optional[str] = None

    bucket_name: Optional[str] = None

    directory: Optional[str] = None

    region: Optional[str] = None


class ConfigBaseFtpConfig(BaseModel):
    directory: Optional[str] = None

    hostname: Optional[str] = None

    timeout_seconds: Optional[int] = None

    user: Optional[str] = None


class ConfigSftpConfigResponse(BaseModel):
    hostname: str

    user: str

    directory: Optional[str] = None

    key_passphrase: Optional[str] = None

    password: Optional[str] = None

    private_key: Optional[str] = None

    timeout_seconds: Optional[int] = None


class ConfigHTTPConfigResponseAppendResponseAction(BaseModel):
    action: Optional[Literal["drop", "retry", "append"]] = None

    description: Optional[str] = None

    match_payload: Optional[str] = None

    match_status_code: Optional[int] = None


class ConfigHTTPConfigResponseAppend(BaseModel):
    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["POST", "PUT"]] = None

    response_actions: Optional[List[ConfigHTTPConfigResponseAppendResponseAction]] = None

    timeout_seconds: Optional[int] = None

    url: Optional[str] = None

    use_compression: Optional[bool] = None


class ConfigHTTPConfigResponseAuthConfig(BaseModel):
    token: Optional[str] = None

    header_name: Optional[str] = None


class ConfigHTTPConfigResponseAuth(BaseModel):
    config: Optional[ConfigHTTPConfigResponseAuthConfig] = None

    type: Optional[Literal["token"]] = None


class ConfigHTTPConfigResponseRetryResponseAction(BaseModel):
    action: Optional[Literal["drop", "retry", "append"]] = None

    description: Optional[str] = None

    match_payload: Optional[str] = None

    match_status_code: Optional[int] = None


class ConfigHTTPConfigResponseRetry(BaseModel):
    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["POST", "PUT"]] = None

    response_actions: Optional[List[ConfigHTTPConfigResponseRetryResponseAction]] = None

    timeout_seconds: Optional[int] = None

    url: Optional[str] = None

    use_compression: Optional[bool] = None


class ConfigHTTPConfigResponseUploadResponseAction(BaseModel):
    action: Optional[Literal["drop", "retry", "append"]] = None

    description: Optional[str] = None

    match_payload: Optional[str] = None

    match_status_code: Optional[int] = None


class ConfigHTTPConfigResponseUpload(BaseModel):
    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["POST", "PUT"]] = None

    response_actions: Optional[List[ConfigHTTPConfigResponseUploadResponseAction]] = None

    timeout_seconds: Optional[int] = None

    url: Optional[str] = None

    use_compression: Optional[bool] = None


class ConfigHTTPConfigResponse(BaseModel):
    append: Optional[ConfigHTTPConfigResponseAppend] = None

    auth: Optional[ConfigHTTPConfigResponseAuth] = None

    content_type: Optional[Literal["json", "text"]] = None

    retry: Optional[ConfigHTTPConfigResponseRetry] = None

    upload: Optional[ConfigHTTPConfigResponseUpload] = None


Config: TypeAlias = Union[
    ConfigS3GcoreConfigResponse,
    ConfigS3AmazonConfigResponse,
    ConfigUnionMember2,
    ConfigS3GcoreConfigResponse,
    ConfigS3GcoreConfigResponse,
    ConfigBaseFtpConfig,
    ConfigSftpConfigResponse,
    ConfigHTTPConfigResponse,
]


class Status(LogsUploaderValidation):
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    pass


class LogsUploaderTarget(BaseModel):
    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the target."""

    config: Optional[Config] = None
    """Config for specific storage type."""

    created: Optional[datetime] = None
    """Time when logs uploader target was created."""

    description: Optional[str] = None
    """Description of the target."""

    name: Optional[str] = None
    """Name of the target."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this target."""

    status: Optional[Status] = None
    """Validation status of the logs uploader target.

    Informs if the specified target is reachable.
    """

    storage_type: Optional[Literal["s3_gcore", "s3_amazon", "s3_oss", "s3_other", "s3_v1", "ftp", "sftp", "http"]] = (
        None
    )
    """Type of storage for logs."""

    updated: Optional[datetime] = None
    """Time when logs uploader target was updated."""
