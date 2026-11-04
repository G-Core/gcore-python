# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SSHKeyCreateParams"]


class SSHKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """User-defined name for the SSH key"""

    public_key: Required[str]
    """The SSH public key content (ssh-rsa or ssh-ed25519 format)"""

    accept_language: Annotated[str, PropertyInfo(alias="Accept-Language")]
