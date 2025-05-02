# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ContainerProbeExecCreateParam"]


class ContainerProbeExecCreateParam(TypedDict, total=False):
    command: Required[List[str]]
    """
    '#/components/schemas/ContainerProbeExecConfigSerializerV2/properties/command'
    "$.components.schemas.ContainerProbeExecConfigSerializerV2.properties.command"
    """
