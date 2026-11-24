# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ServerCreateParams", "Interface"]


class ServerCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    flavor_name: Required[str]
    """Name of a bare metal flavor.

    The flavor sets the CPU, the memory, the disks and the network cards of the
    server. `GET /v1/projects/{project_id}/baremetal/flavors` lists the flavors.
    """

    image_id: Required[str]
    """OS image to write to the server's local disk."""

    interfaces: Required[Iterable[Interface]]
    """Pre-created ports to attach, in NIC/boot order."""

    region_id: Required[int]
    """Region to provision the server in."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    name: str
    """Server name. Auto-generated if omitted."""

    password: str
    """Password of the default user.

    No response returns it. A Windows image needs a password. For a Windows image,
    the create checks these rules: the password has a minimum of 6 characters, it
    contains no word 'admin', and it contains 3 of these character types: digits,
    lowercase letters, uppercase letters, other characters. For a Linux image, the
    password enables SSH login with a password. Send `password` or `user_data`, not
    both.
    """

    ssh_key_id: str
    """ID of the SSH key to add to the default user."""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Tag keys and values
    cannot contain characters from U+0080 to U+00FF. Some tags are read-only and
    cannot be modified by the user. Tags are also integrated with cost reports,
    allowing cost data to be filtered based on tag keys or values.
    """

    user_data: str
    """cloud-init user data (raw or base64).

    Windows: may be combined with password (password sets the Administrator
    account). Linux: mutually exclusive with password.
    """


class Interface(TypedDict, total=False):
    port_id: Required[str]
    """Existing port to attach. Array order is the NIC/boot order."""

    port_group: int
    """0-based bond/trunk group, dense across all interfaces.

    Omitted defaults to group 0. Must be omitted on DPU/SmartNIC flavors.
    """
