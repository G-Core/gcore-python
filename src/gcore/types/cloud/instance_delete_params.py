# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["InstanceDeleteParams"]


class InstanceDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    all_floating_ips: bool
    """Delete all associated floating IPs (default: preserve)."""

    all_ports: bool
    """Delete all attached ports (default: preserve)."""

    all_volumes: bool
    """Delete all attached volumes (default: preserve)."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    floating_ip_ids: SequenceNotStr[str]
    """Delete only these floating IP IDs (mutually exclusive with `all_floating_ips`)."""

    port_ids: SequenceNotStr[str]
    """Delete only these port IDs (mutually exclusive with `all_ports`)."""

    volume_ids: SequenceNotStr[str]
    """Delete only these volume IDs (mutually exclusive with `all_volumes`)."""
