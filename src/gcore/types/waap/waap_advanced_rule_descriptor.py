# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WaapAdvancedRuleDescriptor", "Attr", "AttrArg"]


class AttrArg(BaseModel):
    name: str
    """The argument's name"""

    type: str
    """The argument's type"""

    description: Optional[str] = None
    """The argument's description"""


class Attr(BaseModel):
    name: str
    """The attribute's name"""

    type: str
    """The attribute's type"""

    args: Optional[List[AttrArg]] = None
    """A list of arguments for the attribute"""

    description: Optional[str] = None
    """The attribute's description"""

    hint: Optional[str] = None
    """The attribute's hint"""


class WaapAdvancedRuleDescriptor(BaseModel):
    name: str
    """The object's name"""

    type: str
    """The object's type"""

    attrs: Optional[List[Attr]] = None
    """The object's attributes list"""

    description: Optional[str] = None
    """The object's description"""
