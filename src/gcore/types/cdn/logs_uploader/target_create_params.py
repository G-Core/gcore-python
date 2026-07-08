# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TargetCreateParams",
    "Config",
    "ConfigS3GcoreConfig",
    "ConfigBaseS3Config",
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
    "ConfigAzureBlobConfig",
    "ConfigAzureBlobConfigAuth",
    "ConfigAzureBlobConfigAuthConfig",
    "ConfigAzureBlobConfigAuthConfigAccountKey",
    "ConfigAzureBlobConfigAuthConfigToken",
    "ConfigSlsConfig",
    "ConfigSlsConfigAuth",
    "ConfigSlsConfigAuthConfig",
]


class TargetCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Config for specific storage type."""

    storage_type: Required[
        Literal["s3_gcore", "s3_amazon", "s3_oss", "s3_other", "s3_v1", "ftp", "sftp", "http", "azure_blob", "sls"]
    ]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class ConfigS3GcoreConfig(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: str

    region: str

    secret_access_key: str

    use_path_style: bool


class ConfigBaseS3Config(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]


class ConfigS3OssConfig(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: Optional[str]

    region: Optional[str]

    secret_access_key: str


class ConfigS3OtherConfig(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: str

    region: str

    secret_access_key: str

    use_path_style: bool


class ConfigS3V1Config(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: str

    region: str

    secret_access_key: str

    use_path_style: bool


class ConfigFtpConfig(TypedDict, total=False):
    directory: Optional[str]

    hostname: str

    password: str

    timeout_seconds: int

    user: str


class ConfigSftpConfig(TypedDict, total=False):
    directory: Optional[str]

    hostname: str

    key_passphrase: Optional[str]

    password: Optional[str]

    private_key: Optional[str]

    timeout_seconds: int

    user: str


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


class ConfigAzureBlobConfigAuthConfigAccountKey(TypedDict, total=False):
    account_key: Required[str]
    """Azure Blob Storage account key."""


class ConfigAzureBlobConfigAuthConfigToken(TypedDict, total=False):
    token: Required[str]
    """Azure Blob Storage SAS token."""


ConfigAzureBlobConfigAuthConfig: TypeAlias = Union[
    ConfigAzureBlobConfigAuthConfigAccountKey, ConfigAzureBlobConfigAuthConfigToken
]


class ConfigAzureBlobConfigAuth(TypedDict, total=False):
    config: Required[ConfigAzureBlobConfigAuthConfig]
    """Authentication credentials."""

    type: Required[Literal["shared_key", "sas_token"]]
    """Authentication type."""


class ConfigAzureBlobConfig(TypedDict, total=False):
    account_name: str
    """Azure Blob Storage account name."""

    auth: ConfigAzureBlobConfigAuth

    container_name: str
    """Azure Blob Storage container name."""

    directory: Optional[str]
    """Directory path within the container."""

    endpoint: Optional[str]
    """Custom Azure Blob Storage endpoint URL."""


class ConfigSlsConfigAuthConfig(TypedDict, total=False):
    """Authentication credentials."""

    access_key_id: Required[str]
    """Alibaba access key ID."""

    secret_access_key: Required[str]
    """Alibaba secret access key."""


class ConfigSlsConfigAuth(TypedDict, total=False):
    config: Required[ConfigSlsConfigAuthConfig]
    """Authentication credentials."""

    type: Required[Literal["ak_sk"]]
    """Authentication type."""


class ConfigSlsConfig(TypedDict, total=False):
    auth: ConfigSlsConfigAuth

    endpoint: Optional[str]
    """SLS endpoint.

    Optional — derived from the region as `{region}.log.aliyuncs.com` when omitted.
    """

    log_store: str
    """SLS logstore name.

    3-36 characters; lowercase letters, digits, hyphens, and underscores.
    """

    project: str
    """SLS project name. 3-63 characters; lowercase letters, digits, and hyphens."""

    region: str
    """SLS region (e.g. `eu-central-1`)."""

    topic: Optional[str]
    """Optional SLS topic (0-128 characters)."""


Config: TypeAlias = Union[
    ConfigS3GcoreConfig,
    ConfigBaseS3Config,
    ConfigS3OssConfig,
    ConfigS3OtherConfig,
    ConfigS3V1Config,
    ConfigFtpConfig,
    ConfigSftpConfig,
    ConfigHTTPConfig,
    ConfigAzureBlobConfig,
    ConfigSlsConfig,
]
