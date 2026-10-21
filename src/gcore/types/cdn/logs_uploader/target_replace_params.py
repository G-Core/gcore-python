# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TargetReplaceParams",
    "PutLogsUploaderTargetS3Gcore",
    "PutLogsUploaderTargetS3GcoreConfig",
    "PutLogsUploaderTargetS3GcoreConfigS3GcoreConfig",
    "PutLogsUploaderTargetS3GcoreConfigS3GcoreBoundConfigPut",
    "PutLogsUploaderTargetS3Amazon",
    "PutLogsUploaderTargetS3AmazonConfig",
    "PutLogsUploaderTargetS3Oss",
    "PutLogsUploaderTargetS3OssConfig",
    "PutLogsUploaderTargetS3Other",
    "PutLogsUploaderTargetS3OtherConfig",
    "PutLogsUploaderTargetS3V1",
    "PutLogsUploaderTargetS3V1Config",
    "PutLogsUploaderTargetFtp",
    "PutLogsUploaderTargetFtpConfig",
    "PutLogsUploaderTargetSftp",
    "PutLogsUploaderTargetSftpConfig",
    "PutLogsUploaderTargetHTTP",
    "PutLogsUploaderTargetHTTPConfig",
    "PutLogsUploaderTargetHTTPConfigUpload",
    "PutLogsUploaderTargetHTTPConfigUploadResponseAction",
    "PutLogsUploaderTargetHTTPConfigAppend",
    "PutLogsUploaderTargetHTTPConfigAppendResponseAction",
    "PutLogsUploaderTargetHTTPConfigAuth",
    "PutLogsUploaderTargetHTTPConfigAuthConfig",
    "PutLogsUploaderTargetHTTPConfigRetry",
    "PutLogsUploaderTargetHTTPConfigRetryResponseAction",
    "PutLogsUploaderTargetAzureBlob",
    "PutLogsUploaderTargetAzureBlobConfig",
    "PutLogsUploaderTargetAzureBlobConfigAuth",
    "PutLogsUploaderTargetAzureBlobConfigAuthConfig",
    "PutLogsUploaderTargetAzureBlobConfigAuthConfigAccountKey",
    "PutLogsUploaderTargetAzureBlobConfigAuthConfigToken",
    "PutLogsUploaderTargetSls",
    "PutLogsUploaderTargetSlsConfig",
    "PutLogsUploaderTargetSlsConfigAuth",
    "PutLogsUploaderTargetSlsConfigAuthConfig",
]


class PutLogsUploaderTargetS3Gcore(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetS3GcoreConfig]
    """Config for the `s3_gcore` storage type."""

    storage_type: Required[Literal["s3_gcore"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetS3GcoreConfigS3GcoreConfig(TypedDict, total=False):
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


class PutLogsUploaderTargetS3GcoreConfigS3GcoreBoundConfigPut(TypedDict, total=False):
    """`storage_id` keeps its current value when omitted.

    To bind a target that is not bound yet, or
    one that uses another storage type, send both `storage_id` and `bucket_name`.
    """

    bucket_name: Required[str]
    """Name of a bucket in the selected storage."""

    directory: Optional[str]

    storage_id: int
    """ID of your Gcore Object Storage.

    The storage must be active and of the Standard type.
    """


PutLogsUploaderTargetS3GcoreConfig: TypeAlias = Union[
    PutLogsUploaderTargetS3GcoreConfigS3GcoreConfig, PutLogsUploaderTargetS3GcoreConfigS3GcoreBoundConfigPut
]


class PutLogsUploaderTargetS3Amazon(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetS3AmazonConfig]

    storage_type: Required[Literal["s3_amazon"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetS3AmazonConfig(TypedDict, total=False):
    access_key_id: Required[str]

    bucket_name: Required[str]

    region: Required[str]

    secret_access_key: Required[str]

    directory: Optional[str]


class PutLogsUploaderTargetS3Oss(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetS3OssConfig]

    storage_type: Required[Literal["s3_oss"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetS3OssConfig(TypedDict, total=False):
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


class PutLogsUploaderTargetS3Other(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetS3OtherConfig]

    storage_type: Required[Literal["s3_other"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetS3OtherConfig(TypedDict, total=False):
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


class PutLogsUploaderTargetS3V1(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetS3V1Config]

    storage_type: Required[Literal["s3_v1"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetS3V1Config(TypedDict, total=False):
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


class PutLogsUploaderTargetFtp(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetFtpConfig]

    storage_type: Required[Literal["ftp"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetFtpConfig(TypedDict, total=False):
    directory: Optional[str]

    hostname: str

    password: str

    timeout_seconds: int

    user: str


class PutLogsUploaderTargetSftp(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetSftpConfig]

    storage_type: Required[Literal["sftp"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetSftpConfig(TypedDict, total=False):
    directory: Optional[str]

    hostname: str

    key_passphrase: Optional[str]

    password: Optional[str]

    private_key: Optional[str]

    timeout_seconds: int

    user: str


class PutLogsUploaderTargetHTTP(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetHTTPConfig]

    storage_type: Required[Literal["http"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetHTTPConfigUploadResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class PutLogsUploaderTargetHTTPConfigUpload(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[PutLogsUploaderTargetHTTPConfigUploadResponseAction]

    timeout_seconds: int

    use_compression: bool


class PutLogsUploaderTargetHTTPConfigAppendResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class PutLogsUploaderTargetHTTPConfigAppend(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[PutLogsUploaderTargetHTTPConfigAppendResponseAction]

    timeout_seconds: int

    use_compression: bool


class PutLogsUploaderTargetHTTPConfigAuthConfig(TypedDict, total=False):
    token: Required[str]

    header_name: Required[str]


class PutLogsUploaderTargetHTTPConfigAuth(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetHTTPConfigAuthConfig]

    type: Required[Literal["token"]]


class PutLogsUploaderTargetHTTPConfigRetryResponseAction(TypedDict, total=False):
    action: Required[Literal["drop", "retry", "append"]]

    description: str

    match_payload: str

    match_status_code: int


class PutLogsUploaderTargetHTTPConfigRetry(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]

    method: Literal["POST", "PUT"]

    response_actions: Iterable[PutLogsUploaderTargetHTTPConfigRetryResponseAction]

    timeout_seconds: int

    use_compression: bool


class PutLogsUploaderTargetHTTPConfig(TypedDict, total=False):
    upload: Required[PutLogsUploaderTargetHTTPConfigUpload]

    append: PutLogsUploaderTargetHTTPConfigAppend

    auth: PutLogsUploaderTargetHTTPConfigAuth

    content_type: Literal["json", "text"]

    retry: PutLogsUploaderTargetHTTPConfigRetry


class PutLogsUploaderTargetAzureBlob(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetAzureBlobConfig]

    storage_type: Required[Literal["azure_blob"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetAzureBlobConfigAuthConfigAccountKey(TypedDict, total=False):
    account_key: Required[str]
    """Azure Blob Storage account key."""


class PutLogsUploaderTargetAzureBlobConfigAuthConfigToken(TypedDict, total=False):
    token: Required[str]
    """Azure Blob Storage SAS token."""


PutLogsUploaderTargetAzureBlobConfigAuthConfig: TypeAlias = Union[
    PutLogsUploaderTargetAzureBlobConfigAuthConfigAccountKey, PutLogsUploaderTargetAzureBlobConfigAuthConfigToken
]


class PutLogsUploaderTargetAzureBlobConfigAuth(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetAzureBlobConfigAuthConfig]
    """Authentication credentials."""

    type: Required[Literal["shared_key", "sas_token"]]
    """Authentication type."""


class PutLogsUploaderTargetAzureBlobConfig(TypedDict, total=False):
    account_name: str
    """Azure Blob Storage account name."""

    auth: PutLogsUploaderTargetAzureBlobConfigAuth

    container_name: str
    """Azure Blob Storage container name."""

    directory: Optional[str]
    """Directory path within the container."""

    endpoint: Optional[str]
    """Custom Azure Blob Storage endpoint URL."""


class PutLogsUploaderTargetSls(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetSlsConfig]

    storage_type: Required[Literal["sls"]]
    """Type of storage for logs."""

    description: str
    """Description of the target."""

    name: str
    """Name of the target."""


class PutLogsUploaderTargetSlsConfigAuthConfig(TypedDict, total=False):
    """Authentication credentials."""

    access_key_id: Required[str]
    """Alibaba access key ID."""

    secret_access_key: Required[str]
    """Alibaba secret access key."""


class PutLogsUploaderTargetSlsConfigAuth(TypedDict, total=False):
    config: Required[PutLogsUploaderTargetSlsConfigAuthConfig]
    """Authentication credentials."""

    type: Required[Literal["ak_sk"]]
    """Authentication type."""


class PutLogsUploaderTargetSlsConfig(TypedDict, total=False):
    auth: PutLogsUploaderTargetSlsConfigAuth

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


TargetReplaceParams: TypeAlias = Union[
    PutLogsUploaderTargetS3Gcore,
    PutLogsUploaderTargetS3Amazon,
    PutLogsUploaderTargetS3Oss,
    PutLogsUploaderTargetS3Other,
    PutLogsUploaderTargetS3V1,
    PutLogsUploaderTargetFtp,
    PutLogsUploaderTargetSftp,
    PutLogsUploaderTargetHTTP,
    PutLogsUploaderTargetAzureBlob,
    PutLogsUploaderTargetSls,
]
