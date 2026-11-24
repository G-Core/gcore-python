# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConsoleGetParams"]


class ConsoleGetParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    console_type: Literal["serial", "vnc"]
    """Console type you expect the server to give.

    The server hardware sets the available types. A value that the hardware does not
    give causes an error. Omit this parameter to accept the type of the server.
    """
