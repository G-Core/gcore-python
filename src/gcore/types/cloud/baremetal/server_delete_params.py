# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["ServerDeleteParams"]


class ServerDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    all_floating_ips: bool
    """Delete all floating IPs associated with the server's ports.

    Default preserves them (disassociate only). Mutually exclusive with
    `floating_ip_ids`.
    """

    all_ports: bool
    """Delete all ports attached to the bare metal server.

    Default preserves them (detach only; the trunk is dissolved but every port
    survives, reusable elsewhere). Mutually exclusive with `port_ids`.
    """

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    floating_ip_ids: SequenceNotStr[str]
    """Floating IP IDs to delete; the rest are preserved.

    Mutually exclusive with `all_floating_ips`.
    """

    port_ids: SequenceNotStr[str]
    """Port IDs to delete; the rest are preserved.

    Mutually exclusive with `all_ports`.
    """
