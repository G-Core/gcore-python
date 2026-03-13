# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .template_parameter import TemplateParameter

__all__ = ["Template"]


class Template(BaseModel):
    api_type: str
    """Wasm API type"""

    binary_id: int
    """ID of the WebAssembly binary to use for this template"""

    name: str
    """Unique name for the template (used for identification and searching)"""

    owned: bool
    """Is the template owned by user?"""

    params: List[TemplateParameter]
    """Parameters"""

    long_descr: Optional[str] = None
    """Detailed markdown description explaining template features and usage"""

    short_descr: Optional[str] = None
    """Brief one-line description displayed in template listings"""
