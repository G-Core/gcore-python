# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateParameter"]


class TemplateParameter(BaseModel):
    data_type: Literal["string", "number", "date", "time", "secret"]
    """Parameter type"""

    mandatory: bool
    """Is this field mandatory?"""

    name: str
    """Parameter name"""

    descr: Optional[str] = None
    """Parameter description"""
