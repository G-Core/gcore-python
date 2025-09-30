# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SettingUpdateParams", "Folder"]


class SettingUpdateParams(TypedDict, total=False):
    all_resources_bucket: Required[str]
    """Name of the S3 bucket to which logs for all CDN resources are delivered."""

    all_resources_folder: Required[str]
    """Parameter meaning depends on the value of the "`storage_type`" value:

    - If "`storage_type`": s3 - Name of the S3 bucket sub-folder to which logs for
      all CDN resources are delivered.
    - If "`storage_type`": ftp/sftp - Name of the folder (or path) to which logs for
      all CDN resources are delivered.
    """

    folders: Required[Iterable[Folder]]
    """List of folders/buckets for receiving CDN resources logs."""

    for_all_resources: Required[bool]
    """
    Defines whether logs of all CDN resources are delivered to one folder/bucket or
    to separate ones.

    Possible values:

    - **true** - Logs of all CDN resources are delivered to one folder/bucket.
    - **false** - Logs of different CDN resources are delivered to separate
      folders/buckets.
    """

    ftp_hostname: Required[str]
    """FTP storage hostname."""

    ftp_login: Required[str]
    """FTP storage login."""

    ftp_password: Required[str]
    """FTP storage password."""

    s3_access_key_id: Required[str]
    """Access key ID for the S3 account.

    Access Key ID is 20 alpha-numeric characters like 022QF06E7MXBSH9DHM02
    """

    s3_hostname: Required[str]
    """S3 storage hostname.

    It is required if "`s3_type`": other.
    """

    s3_secret_key: Required[str]
    """Secret access key for the S3 account.

    Secret Access Key is 20-50 alpha-numeric-slash-plus characters like
    kWcrlUX5JEDGM/LtmEENI/aVmYvHNif5zB+d9+ct
    """

    s3_type: Required[str]
    """Storage type compatible with S3.

    Possible values:

    - **amazon** – AWS S3 storage.
    - **other** – Other (not AWS) S3 compatible storage.
    """

    sftp_hostname: Required[str]
    """SFTP storage hostname."""

    sftp_login: Required[str]
    """SFTP storage login."""

    sftp_password: Required[str]
    """SFTP storage password.

    It should be empty if "`sftp_private_key`" is set.
    """

    storage_type: Required[str]
    """Storage type.

    Possible values:

    - **ftp**
    - **sftp**
    - **s3**
    """

    archive_size_mb: Optional[int]
    """
    The size of a single piece of the archive in MB. In case of **null** value logs
    are delivered without slicing.
    """

    enabled: bool
    """Enables or disables a log forwarding feature.

    Possible values:

    - **true** - log forwarding feature is active.
    - **false** - log forwarding feature is deactivated.
    """

    ftp_prepend_folder: str
    """Name of the FTP prepend folder for log delivery.

    **Null** is allowed.
    """

    ignore_empty_logs: bool
    """Enables or disables the forwarding of empty logs.

    Possible values:

    - **true** - Empty logs are not sent.
    - **false** - Empty logs are sent.
    """

    s3_aws_region: int
    """Amazon AWS region."""

    s3_bucket_location: str
    """Location of S3 storage.

    Restrictions:

    - Maximum of 255 symbols.
    - Latin letters (A-Z, a-z), digits (0-9), dots, colons, dashes, and underscores
      (.:\\__-).
    """

    s3_host_bucket: str
    """S3 bucket hostname.

    Restrictions:

    - Maximum of 255 symbols.
    - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores.
    - Required if "`s3_type`": other.
    """

    sftp_key_passphrase: str
    """Passphrase for SFTP private key.

    Restrictions:

    - Should be set if private key encoded with passphrase.
    - Should be empty if "`sftp_password`" is set.
    """

    sftp_prepend_folder: str
    """Name of the SFTP prepend folder for log delivery.

    **Null** is allowed.
    """

    sftp_private_key: str
    """Private key for SFTP authorization.

    Possible values:

    - **RSA**
    - **ED25519**

    It should be empty if "`sftp_password`" is set.
    """


class Folder(TypedDict, total=False):
    id: int
    """Parameter meaning depends on the value of the "`storage_type`" value:

    - **s3** - S3 bucket ID.
    - **ftp/sftp** - FTP/SFTP folder ID.
    """

    bucket: str
    """S3 bucket name.

    The field is required if "`storage_type`": **s3**.
    """

    cdn_resource: int
    """CDN resource ID."""

    folder: str
    """Parameter meaning depends on the value of the "`storage_type`" value:

    - **s3** - S3 bucket sub-folder name (optional.)
    - **ftp/sftp** - FTP/SFTP folder name (required.)
    """
