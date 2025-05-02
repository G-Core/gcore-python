# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ddos_profile_template_field import DDOSProfileTemplateField

__all__ = ["DDOSProfileTemplate"]


class DDOSProfileTemplate(BaseModel):
    id: int

    name: str

    description: Optional[str] = None

    fields: Optional[List[DDOSProfileTemplateField]] = None
