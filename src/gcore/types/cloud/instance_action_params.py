# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceActionParams"]


class InstanceActionParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    action: Required[Literal["reboot", "reboot_hard", "resume", "start", "stop", "suspend"]]
    """Power action to run on the instance.

    `reboot_hard` replaces the legacy `powercycle` action.
    """

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """
