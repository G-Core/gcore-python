# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FlavorHardwareDescription"]


class FlavorHardwareDescription(BaseModel):
    cpu: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/cpu/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.cpu.anyOf[0]"
    """

    disk: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/disk/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.disk.anyOf[0]"
    """

    ephemeral: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/ephemeral/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.ephemeral.anyOf[0]"
    """

    gpu: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/gpu/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.gpu.anyOf[0]"
    """

    ipu: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/ipu/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.ipu.anyOf[0]"
    """

    network: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/network/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.network.anyOf[0]"
    """

    poplar_count: Optional[int] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/poplar_count/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.poplar_count.anyOf[0]"
    """

    ram: Optional[str] = None
    """
    '#/components/schemas/FlavorHardwareDescriptionSerializer/properties/ram/anyOf/0'
    "$.components.schemas.FlavorHardwareDescriptionSerializer.properties.ram.anyOf[0]"
    """
