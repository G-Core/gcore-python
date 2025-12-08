# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = [
    "DeploymentCreateParams",
    "ComponentsConfiguration",
    "ComponentsConfigurationScale",
    "ComponentsConfigurationParameterOverrides",
]


class DeploymentCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    application_name: Required[str]
    """Identifier of the application from the catalog"""

    components_configuration: Required[Dict[str, ComponentsConfiguration]]
    """Mapping of component names to their configuration (e.g., `"model": {...}`)"""

    name: Required[str]
    """Desired name for the new deployment"""

    regions: Required[Iterable[int]]
    """Geographical regions where the deployment should be created"""

    api_keys: SequenceNotStr[str]
    """List of API keys for the application"""


class ComponentsConfigurationScale(TypedDict, total=False):
    """Scaling parameters of the component"""

    max: Required[int]
    """Maximum number of replicas the container can be scaled up to"""

    min: Required[int]
    """Minimum number of replicas the component can be scaled down to"""


class ComponentsConfigurationParameterOverrides(TypedDict, total=False):
    value: Required[str]
    """New value assigned to the overridden parameter"""


class ComponentsConfiguration(TypedDict, total=False):
    exposed: Required[bool]
    """
    Whether the component should be exposed via a public endpoint (e.g., for
    external inference/API access).
    """

    flavor: Required[str]
    """
    Specifies the compute configuration (e.g., CPU/GPU size) to be used for the
    component.
    """

    scale: Required[ComponentsConfigurationScale]
    """Scaling parameters of the component"""

    parameter_overrides: Dict[str, ComponentsConfigurationParameterOverrides]
    """Map of parameter overrides for customization"""
