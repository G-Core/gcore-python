# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["InferenceApplicationTemplate", "Components", "ComponentsParameters", "ComponentsSuitableFlavor"]


class ComponentsParameters(BaseModel):
    default_value: str
    """Default value assigned if not provided"""

    description: str
    """Description of the parameter's purpose"""

    display_name: str
    """User-friendly name of the parameter"""

    enum_values: Optional[List[str]] = None
    """Allowed values when type is "enum" """

    max_value: Optional[str] = None
    """Maximum value (applies to integer and float types)"""

    min_value: Optional[str] = None
    """Minimum value (applies to integer and float types)"""

    pattern: Optional[str] = None
    """Regexp pattern when type is "string" """

    required: bool
    """Indicates is parameter mandatory"""

    type: Literal["enum", "float", "integer", "string"]
    """Determines the type of the parameter"""


class ComponentsSuitableFlavor(BaseModel):
    name: str
    """Name of the flavor"""


class Components(BaseModel):
    description: str
    """Summary of the component's functionality"""

    display_name: str
    """Human-readable name of the component"""

    exposable: bool
    """
    Indicates whether this component can expose a public-facing endpoint (e.g., for
    inference or API access).
    """

    license_url: str
    """URL to the component's license information"""

    parameters: Dict[str, ComponentsParameters]
    """Configurable parameters for the component"""

    readme: str
    """Detailed documentation or usage instructions"""

    required: bool
    """Specifies if the component is required for the application"""

    suitable_flavors: List[ComponentsSuitableFlavor]
    """List of compatible flavors or configurations"""


class InferenceApplicationTemplate(BaseModel):
    components: Dict[str, Components]
    """Configurable components of the application"""

    cover_url: str
    """URL to the application's cover image"""

    description: str
    """Brief overview of the application"""

    display_name: str
    """Human-readable name of the application"""

    name: str
    """Unique application identifier in the catalog"""

    readme: str
    """Detailed documentation or instructions"""

    tags: Dict[str, str]
    """Categorization key-value pairs"""
