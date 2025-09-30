# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LogSettings", "Folder"]


class Folder(BaseModel):
    id: Optional[int] = None
    """Parameter meaning depends on the value of the "`storage_type`" value:

    - **s3** - S3 bucket ID.
    - **ftp/sftp** - FTP/SFTP folder ID.
    """

    bucket: Optional[str] = None
    """S3 bucket name.

    The field is required if "`storage_type`": **s3**.
    """

    cdn_resource: Optional[int] = None
    """CDN resource ID."""

    folder: Optional[str] = None
    """Parameter meaning depends on the value of the "`storage_type`" value:

    - **s3** - S3 bucket sub-folder name (optional.)
    - **ftp/sftp** - FTP/SFTP folder name (required.)
    """


class LogSettings(BaseModel):
    all_resources_bucket: Optional[str] = None
    """Name of the S3 bucket to which logs of all CDN resources are delivered.

    Applicable for "`storage_type`": S3.
    """

    all_resources_folder: Optional[str] = None
    """Parameter meaning depends on the value of the "`storage_type`" value:

    - **s3** - Name of the S3 bucket sub-folder to which logs for all CDN resources
      are delivered.
    - **ftp/sftp** - Name of the folder (or path) to which logs for all CDN
      resources are delivered.
    """

    archive_size_mb: Optional[int] = None
    """
    The size of a single piece of the archive in MB. In case of **null** value logs
    are delivered without slicing.
    """

    client: Optional[int] = None
    """Client ID."""

    comment: Optional[str] = None
    """System comment on the status of settings, if they are suspended."""

    enabled: Optional[bool] = None
    """Enables or disables a log forwarding feature.

    Possible values:

    - **true** - log forwarding feature is active.
    - **false** - log forwarding feature is deactivated.
    """

    folders: Optional[List[Folder]] = None
    """List of folders/buckets for receiving CDN resources logs."""

    for_all_resources: Optional[bool] = None
    """
    Defines whether logs of all CDN resources are delivered to one folder/bucket or
    to separate ones.

    Possible values:

    - **true** - Logs of all CDN resources are delivered to one folder/bucket.
    - **false** - Logs of CDN resources are delivered to separate folders/buckets.
    """

    ftp_hostname: Optional[str] = None
    """FTP storage hostname."""

    ftp_login: Optional[str] = None
    """FTP storage login."""

    ftp_prepend_folder: Optional[str] = None
    """Name of prepend FTP folder for log delivery."""

    ignore_empty_logs: Optional[bool] = None
    """Enables or disables the forwarding of empty logs.

    Possible values:

    - **true** - Empty logs are not sent.
    - **false** - Empty logs are sent.
    """

    s3_access_key_id: Optional[str] = None
    """Access key ID for the S3 account.

    Access Key ID is 20 alpha-numeric characters like 022QF06E7MXBSH9DHM02
    """

    s3_aws_region: Optional[str] = None
    """Amazon AWS region."""

    s3_bucket_location: Optional[str] = None
    """S3 storage location.

    Restrictions:

    - Maximum 255 symbols.
    - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores
      (.:\\__-).
    """

    s3_host_bucket: Optional[str] = None
    """S3 storage bucket hostname.

    Restrictions:

    - Maximum 255 symbols.
    - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores.
    """

    s3_hostname: Optional[str] = None
    """S3 storage hostname."""

    s3_type: Optional[str] = None
    """Storage type compatible with S3.

    Possible values:

    - **amazon** – AWS S3 storage.
    - **other** – Other (not AWS) S3 compatible storage.
    """

    sftp_hostname: Optional[str] = None
    """SFTP storage hostname."""

    sftp_login: Optional[str] = None
    """SFTP storage login."""

    sftp_prepend_folder: Optional[str] = None
    """Name of prepend SFTP folder for log delivery."""

    status: Optional[str] = None
    """Log delivery status.

    Possible values:

    - **ok** – All/part of attempts to deliver logs were successful.
    - **failed** – All attempts to deliver logs failed.
    - **pending** - No logs delivery attempts yet.
    - **disabled** - Log delivery is disabled.
    """

    storage_type: Optional[str] = None
    """Storage type.

    Possible values:

    - **ftp**
    - **sftp**
    - **s3**
    """
