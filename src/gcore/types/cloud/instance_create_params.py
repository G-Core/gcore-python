# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["InstanceCreateParams", "Interface"]


class InstanceCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    boot_volume_id: Required[str]
    """Pre-created boot volume UUID."""

    flavor_name: Required[str]
    """Name of an instance flavor with no GPU.

    Use `GET /v1/projects/{project_id}/instances/flavors` to list them.
    """

    interfaces: Required[Iterable[Interface]]
    """Pre-created ports to attach, in NIC/boot order."""

    region_id: Required[int]
    """Region to provision the instance in."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    data_volume_ids: SequenceNotStr[str]
    """Pre-created data volume UUIDs to attach."""

    name: str
    """Instance name.

    If you omit it, the name template of the account gives the name. Without a
    template, the name is generated. The account can forbid custom names. Then the
    name must be equal to the name that the template gives.
    """

    password: str
    """Password of the default user.

    No response returns it. A Windows image needs a password. For a Windows image,
    the create checks these rules: the password has a minimum of 6 characters, it
    contains no word 'admin', and it contains 3 of these character types: digits,
    lowercase letters, uppercase letters, other characters. For a Linux image, the
    password enables SSH login with a password. Send `password` or `user_data`, not
    both.
    """

    placement_group_id: str
    """Pre-created placement group UUID for affinity/anti-affinity."""

    ssh_key_id: str
    """ID of the SSH key to add to the default user."""

    tags: Dict[str, str]
    """Customer-owned key-value tags."""

    user_data: str
    """cloud-init user data, raw or base64. Up to 65535 bytes once decoded."""


class Interface(TypedDict, total=False):
    port_id: Required[str]
    """Existing port to attach. Array order is the NIC/boot order."""
