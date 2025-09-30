# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TargetReplaceParams",
    "Config",
    "ConfigS3GcoreConfig",
    "ConfigS3AmazonConfig",
    "ConfigS3OssConfig",
    "ConfigS3OtherConfig",
    "ConfigS3V1Config",
    "ConfigFtpConfig",
    "ConfigSftpConfig",
    "ConfigHTTPConfig",
    "ConfigHTTPConfigUpload",
    "ConfigHTTPConfigUploadResponseAction",
    "ConfigHTTPConfigAppend",
    "ConfigHTTPConfigAppendResponseAction",
    "ConfigHTTPConfigAuth",
    "ConfigHTTPConfigAuthConfig",
    "ConfigHTTPConfigRetry",
    "ConfigHTTPConfigRetryResponseAction",
]


class TargetReplaceParams(TypedDict, total=False):
    config: Required[Config]
    """Config for specific storage type."""

    storage_type: Required[Literal["s3_gcore", "s3_amazon", "s3_oss", "s3_other", "s3_v1", "ftp", "sftp", "http"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class ConfigS3GcoreConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    endpoint: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]

    use_path_style: bool


class ConfigS3AmazonConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]


class ConfigS3OssConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]

    region: Optional[str]


class ConfigS3OtherConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    endpoint: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]

    use_path_style: bool


class ConfigS3V1Config(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    endpoint: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]

    use_path_style: bool


class ConfigFtpConfig(TypedDict, total=False):
    hostname: Required[str]

    password: Required[str]

    user: Required[str]

    directory: Optional[str]

    timeout_seconds: int


class ConfigSftpConfig(TypedDict, total=False):
    hostname: Required[str]

    user: Required[str]

    directory: Optional[str]

    key_passphrase: Optional[str]

    password: Optional[str]

    private_key: Optional[str]

    timeout_seconds: int


class ConfigHTTPConfigUploadResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class ConfigHTTPConfigUpload(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[ConfigHTTPConfigUploadResponseAction]

    timeout_seconds: int

    use_compression: bool


class ConfigHTTPConfigAppendResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class ConfigHTTPConfigAppend(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[ConfigHTTPConfigAppendResponseAction]

    timeout_seconds: int

    use_compression: bool


class ConfigHTTPConfigAuthConfig(TypedDict, total=False):
    token: Required[str]

    header_name: Required[str]


class ConfigHTTPConfigAuth(TypedDict, total=False):
    config: Required[ConfigHTTPConfigAuthConfig]

    type: Required[Literal["token"]]


class ConfigHTTPConfigRetryResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class ConfigHTTPConfigRetry(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[ConfigHTTPConfigRetryResponseAction]

    timeout_seconds: int

    use_compression: bool


class ConfigHTTPConfig(TypedDict, total=False):
    upload: Required[ConfigHTTPConfigUpload]

    append: ConfigHTTPConfigAppend

    auth: ConfigHTTPConfigAuth

    content_type: Literal["json", "text"]

    retry: ConfigHTTPConfigRetry


Config: TypeAlias = Union[
    ConfigS3GcoreConfig,
    ConfigS3AmazonConfig,
    ConfigS3OssConfig,
    ConfigS3OtherConfig,
    ConfigS3V1Config,
    ConfigFtpConfig,
    ConfigSftpConfig,
    ConfigHTTPConfig,
]
