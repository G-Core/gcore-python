# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TemplateShort"]


class TemplateShort(BaseModel):
    id: int
    """Template ID"""

    api_type: str
    """Wasm API type"""

    name: str
    """Name of the template"""

    owned: bool
    """Is the template owned by user?"""

    long_descr: Optional[str] = None
    """Long description of the template"""

    short_descr: Optional[str] = None
    """Short description of the template"""
