# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContainerProbeTcpSocketCreateParam"]


class ContainerProbeTcpSocketCreateParam(TypedDict, total=False):
    port: Required[int]
    """Port number to check if it's open."""
