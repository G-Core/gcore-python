# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TargetCreateParams",
    "CreateLogsUploaderTargetS3Gcore",
    "CreateLogsUploaderTargetS3GcoreConfig",
    "CreateLogsUploaderTargetS3GcoreConfigS3GcoreConfig",
    "CreateLogsUploaderTargetS3GcoreConfigS3GcoreBoundConfig",
    "CreateLogsUploaderTargetS3Amazon",
    "CreateLogsUploaderTargetS3AmazonConfig",
    "CreateLogsUploaderTargetS3Oss",
    "CreateLogsUploaderTargetS3OssConfig",
    "CreateLogsUploaderTargetS3Other",
    "CreateLogsUploaderTargetS3OtherConfig",
    "CreateLogsUploaderTargetS3V1",
    "CreateLogsUploaderTargetS3V1Config",
    "CreateLogsUploaderTargetFtp",
    "CreateLogsUploaderTargetFtpConfig",
    "CreateLogsUploaderTargetSftp",
    "CreateLogsUploaderTargetSftpConfig",
    "CreateLogsUploaderTargetHTTP",
    "CreateLogsUploaderTargetHTTPConfig",
    "CreateLogsUploaderTargetHTTPConfigUpload",
    "CreateLogsUploaderTargetHTTPConfigUploadResponseAction",
    "CreateLogsUploaderTargetHTTPConfigAppend",
    "CreateLogsUploaderTargetHTTPConfigAppendResponseAction",
    "CreateLogsUploaderTargetHTTPConfigAuth",
    "CreateLogsUploaderTargetHTTPConfigAuthConfig",
    "CreateLogsUploaderTargetHTTPConfigRetry",
    "CreateLogsUploaderTargetHTTPConfigRetryResponseAction",
    "CreateLogsUploaderTargetAzureBlob",
    "CreateLogsUploaderTargetAzureBlobConfig",
    "CreateLogsUploaderTargetAzureBlobConfigAuth",
    "CreateLogsUploaderTargetAzureBlobConfigAuthConfig",
    "CreateLogsUploaderTargetAzureBlobConfigAuthConfigAccountKey",
    "CreateLogsUploaderTargetAzureBlobConfigAuthConfigToken",
    "CreateLogsUploaderTargetSls",
    "CreateLogsUploaderTargetSlsConfig",
    "CreateLogsUploaderTargetSlsConfigAuth",
    "CreateLogsUploaderTargetSlsConfigAuthConfig",
]


class CreateLogsUploaderTargetS3Gcore(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetS3GcoreConfig]
    """Config for the `s3_gcore` storage type."""

    storage_type: Required[Literal["s3_gcore"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetS3GcoreConfigS3GcoreConfig(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: str
    """S3 storage endpoint URL.

    Must be a public address: private and reserved IP addresses, `localhost`, and
    hostnames that resolve to them are rejected.
    """

    region: str

    secret_access_key: str

    use_path_style: bool


class CreateLogsUploaderTargetS3GcoreConfigS3GcoreBoundConfig(TypedDict, total=False):
    """Deliver logs to a bucket in your Gcore Object Storage.

    Select the storage and bucket, and the
    CDN configures the connection for you.
    """

    bucket_name: Required[str]
    """Name of a bucket in the selected storage."""

    storage_id: Required[int]
    """ID of your Gcore Object Storage.

    The storage must be active and of the Standard type.
    """

    directory: Optional[str]


CreateLogsUploaderTargetS3GcoreConfig: TypeAlias = Union[
    CreateLogsUploaderTargetS3GcoreConfigS3GcoreConfig, CreateLogsUploaderTargetS3GcoreConfigS3GcoreBoundConfig
]


class CreateLogsUploaderTargetS3Amazon(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetS3AmazonConfig]

    storage_type: Required[Literal["s3_amazon"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetS3AmazonConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]


class CreateLogsUploaderTargetS3Oss(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetS3OssConfig]

    storage_type: Required[Literal["s3_oss"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetS3OssConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]

    endpoint: Optional[str]
    """S3 storage endpoint URL.

    Must be a public address: private and reserved IP addresses, `localhost`, and
    hostnames that resolve to them are rejected.
    """

    region: Optional[str]


class CreateLogsUploaderTargetS3Other(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetS3OtherConfig]

    storage_type: Required[Literal["s3_other"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetS3OtherConfig(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: str
    """S3 storage endpoint URL.

    Must be a public address: private and reserved IP addresses, `localhost`, and
    hostnames that resolve to them are rejected.
    """

    region: str

    secret_access_key: str

    use_path_style: bool


class CreateLogsUploaderTargetS3V1(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetS3V1Config]

    storage_type: Required[Literal["s3_v1"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetS3V1Config(TypedDict, total=False):
    access_key_id: str

    bucket_name: str

    directory: Optional[str]

    endpoint: str
    """S3 storage endpoint URL.

    Must be a public address: private and reserved IP addresses, `localhost`, and
    hostnames that resolve to them are rejected.
    """

    region: str

    secret_access_key: str

    use_path_style: bool


class CreateLogsUploaderTargetFtp(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetFtpConfig]

    storage_type: Required[Literal["ftp"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetFtpConfig(TypedDict, total=False):
    directory: Optional[str]

    hostname: str

    password: str

    timeout_seconds: int

    user: str


class CreateLogsUploaderTargetSftp(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetSftpConfig]

    storage_type: Required[Literal["sftp"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetSftpConfig(TypedDict, total=False):
    directory: Optional[str]

    hostname: str

    key_passphrase: Optional[str]

    password: Optional[str]

    private_key: Optional[str]

    timeout_seconds: int

    user: str


class CreateLogsUploaderTargetHTTP(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetHTTPConfig]

    storage_type: Required[Literal["http"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetHTTPConfigUploadResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class CreateLogsUploaderTargetHTTPConfigUpload(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[CreateLogsUploaderTargetHTTPConfigUploadResponseAction]

    timeout_seconds: int

    use_compression: bool


class CreateLogsUploaderTargetHTTPConfigAppendResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class CreateLogsUploaderTargetHTTPConfigAppend(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[CreateLogsUploaderTargetHTTPConfigAppendResponseAction]

    timeout_seconds: int

    use_compression: bool


class CreateLogsUploaderTargetHTTPConfigAuthConfig(TypedDict, total=False):
    token: Required[str]

    header_name: Required[str]


class CreateLogsUploaderTargetHTTPConfigAuth(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetHTTPConfigAuthConfig]

    type: Required[Literal["token"]]


class CreateLogsUploaderTargetHTTPConfigRetryResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class CreateLogsUploaderTargetHTTPConfigRetry(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[CreateLogsUploaderTargetHTTPConfigRetryResponseAction]

    timeout_seconds: int

    use_compression: bool


class CreateLogsUploaderTargetHTTPConfig(TypedDict, total=False):
    upload: Required[CreateLogsUploaderTargetHTTPConfigUpload]

    append: CreateLogsUploaderTargetHTTPConfigAppend

    auth: CreateLogsUploaderTargetHTTPConfigAuth

    content_type: Literal["json", "text"]

    retry: CreateLogsUploaderTargetHTTPConfigRetry


class CreateLogsUploaderTargetAzureBlob(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetAzureBlobConfig]

    storage_type: Required[Literal["azure_blob"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetAzureBlobConfigAuthConfigAccountKey(TypedDict, total=False):
    account_key: Required[str]
    """Azure Blob Storage account key."""


class CreateLogsUploaderTargetAzureBlobConfigAuthConfigToken(TypedDict, total=False):
    token: Required[str]
    """Azure Blob Storage SAS token."""


CreateLogsUploaderTargetAzureBlobConfigAuthConfig: TypeAlias = Union[
    CreateLogsUploaderTargetAzureBlobConfigAuthConfigAccountKey, CreateLogsUploaderTargetAzureBlobConfigAuthConfigToken
]


class CreateLogsUploaderTargetAzureBlobConfigAuth(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetAzureBlobConfigAuthConfig]
    """Authentication credentials."""

    type: Required[Literal["shared_key", "sas_token"]]
    """Authentication type."""


class CreateLogsUploaderTargetAzureBlobConfig(TypedDict, total=False):
    account_name: str
    """Azure Blob Storage account name."""

    auth: CreateLogsUploaderTargetAzureBlobConfigAuth

    container_name: str
    """Azure Blob Storage container name."""

    directory: Optional[str]
    """Directory path within the container."""

    endpoint: Optional[str]
    """Custom Azure Blob Storage endpoint URL."""


class CreateLogsUploaderTargetSls(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetSlsConfig]

    storage_type: Required[Literal["sls"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class CreateLogsUploaderTargetSlsConfigAuthConfig(TypedDict, total=False):
    """Authentication credentials."""

    access_key_id: Required[str]
    """Alibaba access key ID."""

    secret_access_key: Required[str]
    """Alibaba secret access key."""


class CreateLogsUploaderTargetSlsConfigAuth(TypedDict, total=False):
    config: Required[CreateLogsUploaderTargetSlsConfigAuthConfig]
    """Authentication credentials."""

    type: Required[Literal["ak_sk"]]
    """Authentication type."""


class CreateLogsUploaderTargetSlsConfig(TypedDict, total=False):
    auth: CreateLogsUploaderTargetSlsConfigAuth

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


TargetCreateParams: TypeAlias = Union[
    CreateLogsUploaderTargetS3Gcore,
    CreateLogsUploaderTargetS3Amazon,
    CreateLogsUploaderTargetS3Oss,
    CreateLogsUploaderTargetS3Other,
    CreateLogsUploaderTargetS3V1,
    CreateLogsUploaderTargetFtp,
    CreateLogsUploaderTargetSftp,
    CreateLogsUploaderTargetHTTP,
    CreateLogsUploaderTargetAzureBlob,
    CreateLogsUploaderTargetSls,
]
