# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .template_parameter import TemplateParameter

__all__ = ["Template"]


class Template(BaseModel):
    api_type: str
    """Wasm API type"""

    binary_id: int
    """Binary ID"""

    name: str
    """Name of the template"""

    owned: bool
    """Is the template owned by user?"""

    params: List[TemplateParameter]
    """Parameters"""

    long_descr: Optional[str] = None
    """Long description of the template"""

    short_descr: Optional[str] = None
    """Short description of the template"""
