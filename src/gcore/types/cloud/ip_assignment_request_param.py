# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPAssignmentRequestParam"]


class IPAssignmentRequestParam(TypedDict, total=False):
    subnet_id: Required[str]
    """ID of the subnet"""

    ip_address: str
    """IP address to assign.

    Omit it to get any free address of the subnet, which is the only option when the
    subnet's free addresses are not known to the caller.
    """
