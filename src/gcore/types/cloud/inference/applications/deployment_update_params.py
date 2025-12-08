# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = [
    "DeploymentUpdateParams",
    "ComponentsConfiguration",
    "ComponentsConfigurationParameterOverrides",
    "ComponentsConfigurationScale",
]


class DeploymentUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    api_keys: SequenceNotStr[str]
    """List of API keys for the application"""

    components_configuration: Dict[str, Optional[ComponentsConfiguration]]
    """Mapping of component names to their configuration (e.g., `"model": {...}`)"""

    regions: Iterable[int]
    """Geographical regions to be updated for the deployment"""


class ComponentsConfigurationParameterOverrides(TypedDict, total=False):
    value: Required[str]
    """New value assigned to the overridden parameter"""


class ComponentsConfigurationScale(TypedDict, total=False):
    """Scaling parameters of the component"""

    max: int
    """Maximum number of replicas the container can be scaled up to"""

    min: int
    """Minimum number of replicas the component can be scaled down to"""


class ComponentsConfiguration(TypedDict, total=False):
    exposed: bool
    """
    Whether the component should be exposed via a public endpoint (e.g., for
    external inference/API access).
    """

    flavor: str
    """
    Specifies the compute configuration (e.g., CPU/GPU size) to be used for the
    component.
    """

    parameter_overrides: Dict[str, Optional[ComponentsConfigurationParameterOverrides]]
    """Map of parameter overrides for customization"""

    scale: ComponentsConfigurationScale
    """Scaling parameters of the component"""
