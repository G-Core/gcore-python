# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHKeyCreateParams"]


class SSHKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """User-defined name for the SSH key"""

    public_key: Required[str]
    """The SSH public key content (ssh-rsa or ssh-ed25519 format)"""
