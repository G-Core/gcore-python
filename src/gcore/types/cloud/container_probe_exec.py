# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ContainerProbeExec"]


class ContainerProbeExec(BaseModel):
    command: List[str]
    """
    '#/components/schemas/ContainerProbeExecConfigOutSerializerV2/properties/command'
    "$.components.schemas.ContainerProbeExecConfigOutSerializerV2.properties.command"
    """
