# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceFlavor"]


class InferenceFlavor(BaseModel):
    cpu: float
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/cpu'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.cpu"
    """

    description: str
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/description'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.description"
    """

    gpu: int
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/gpu'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.gpu"
    """

    gpu_compute_capability: str
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/gpu_compute_capability'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.gpu_compute_capability"
    """

    gpu_memory: float
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/gpu_memory'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.gpu_memory"
    """

    gpu_model: str
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/gpu_model'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.gpu_model"
    """

    is_gpu_shared: bool
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/is_gpu_shared'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.is_gpu_shared"
    """

    memory: float
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/memory'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.memory"
    """

    name: str
    """
    '#/components/schemas/InferenceFlavorOutSerializerV3/properties/name'
    "$.components.schemas.InferenceFlavorOutSerializerV3.properties.name"
    """
