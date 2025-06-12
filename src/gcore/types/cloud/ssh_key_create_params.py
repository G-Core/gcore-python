# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHKeyCreateParams"]


class SSHKeyCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    name: Required[str]
    """SSH key name"""

    public_key: str
    """The public part of an SSH key is the shareable portion of an SSH key pair.

    It can be safely sent to servers or services to grant access. It does not
    contain sensitive information.

    - If you’re uploading your own key, provide the public part here (usually found
      in a file like `id_ed25519.pub`).
    - If you want the platform to generate an Ed25519 key pair for you, leave this
      field empty — the system will return the private key in the response **once
      only**.
    """

    shared_in_project: bool
    """SSH key is shared with all users in the project"""
