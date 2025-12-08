# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = [
    "InferenceApplicationDeployment",
    "ComponentsConfiguration",
    "ComponentsConfigurationParameterOverrides",
    "ComponentsConfigurationScale",
    "Status",
    "StatusComponentInferences",
    "StatusExposeAddresses",
    "StatusRegion",
    "StatusRegionComponents",
]


class ComponentsConfigurationParameterOverrides(BaseModel):
    value: str
    """New value assigned to the overridden parameter"""


class ComponentsConfigurationScale(BaseModel):
    """Scaling parameters of the component"""

    max: int
    """Maximum number of replicas the container can be scaled up to"""

    min: int
    """Minimum number of replicas the component can be scaled down to"""


class ComponentsConfiguration(BaseModel):
    exposed: bool
    """Indicates if the component will obtain a public address"""

    flavor: str
    """Chosen flavor or variant of the component"""

    parameter_overrides: Dict[str, ComponentsConfigurationParameterOverrides]
    """Map of parameter overrides for customization"""

    scale: ComponentsConfigurationScale
    """Scaling parameters of the component"""


class StatusComponentInferences(BaseModel):
    flavor: str
    """Flavor of the inference"""

    name: str
    """Name of the inference"""


class StatusExposeAddresses(BaseModel):
    address: str
    """Global access endpoint for the component"""


class StatusRegionComponents(BaseModel):
    error: str
    """Error message if the component is in an error state"""

    status: str
    """Current state of the component in a specific region"""


class StatusRegion(BaseModel):
    components: Dict[str, StatusRegionComponents]
    """Mapping of component names to their status in the region"""

    region_id: int
    """Region ID"""

    status: str
    """Current state of the deployment in a specific region"""


class Status(BaseModel):
    """Current state of the deployment across regions"""

    component_inferences: Dict[str, StatusComponentInferences]
    """Map of components and their inferences"""

    consolidated_status: Literal["Active", "Failed", "PartiallyDeployed", "Unknown"]
    """High-level summary of the deployment status across all regions"""

    expose_addresses: Dict[str, StatusExposeAddresses]
    """Map of component keys to their global access endpoints"""

    regions: List[StatusRegion]
    """Status details for each deployment region"""


class InferenceApplicationDeployment(BaseModel):
    api_keys: List[str]
    """List of API keys for the application"""

    application_name: str
    """Identifier of the application template from the catalog"""

    components_configuration: Dict[str, ComponentsConfiguration]
    """Mapping of component names to their configuration (e.g., `"model": {...}`)"""

    name: str
    """Unique identifier of the deployment"""

    regions: List[int]
    """Geographical regions where the deployment is active"""

    status: Status
    """Current state of the deployment across regions"""
