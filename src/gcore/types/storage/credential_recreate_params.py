# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CredentialRecreateParams"]


class CredentialRecreateParams(TypedDict, total=False):
    delete_sftp_password: bool

    generate_s3_keys: bool

    generate_sftp_password: bool

    reset_sftp_keys: bool

    sftp_password: str
