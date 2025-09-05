# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CredentialRecreateParams"]


class CredentialRecreateParams(TypedDict, total=False):
    delete_sftp_password: bool
    """Remove the SFTP password, disabling password authentication.

    Only applicable to SFTP storage type.
    """

    generate_s3_keys: bool
    """Generate new S3 access and secret keys for S3 storage.

    Only applicable to S3 storage type.
    """

    generate_sftp_password: bool
    """Generate a new random password for SFTP access.

    Only applicable to SFTP storage type.
    """

    reset_sftp_keys: bool
    """Reset/remove all SSH keys associated with the SFTP storage.

    Only applicable to SFTP storage type.
    """

    sftp_password: str
    """Set a custom password for SFTP access. Only applicable to SFTP storage type."""
