# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StorageCreateParams"]


class StorageCreateParams(TypedDict, total=False):
    location: Required[str]
    """Geographic location where the storage will be provisioned.

    Each location represents a specific data center region.
    """

    name: Required[str]
    """Unique storage name identifier.

    Must contain only letters, numbers, dashes, and underscores. Cannot be empty and
    must be less than 256 characters.
    """

    type: Required[Literal["sftp", "s3"]]
    """Storage protocol type.

    Choose 's3' for S3-compatible object storage with API access, or `sftp` for SFTP
    file transfer protocol.
    """

    generate_sftp_password: bool
    """Automatically generate a secure password for SFTP storage access.

    Only applicable when type is `sftp`. When `true`, a random password will be
    generated and returned in the response.
    """

    sftp_password: str
    """Custom password for SFTP storage access.

    Only applicable when type is `sftp`. If not provided and
    `generate_sftp_password` is `false`, no password authentication will be
    available.
    """
