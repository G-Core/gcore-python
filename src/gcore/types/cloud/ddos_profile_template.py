# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ddos_profile_template_field import DDOSProfileTemplateField

__all__ = ["DDOSProfileTemplate"]


class DDOSProfileTemplate(BaseModel):
    id: int
    """Unique identifier for the DDoS protection template"""

    description: Optional[str] = None
    """Detailed description explaining the template's purpose and use cases"""

    fields: List[DDOSProfileTemplateField]
    """List of configurable fields that define the template's protection parameters"""

    name: str
    """Human-readable name of the protection template"""
