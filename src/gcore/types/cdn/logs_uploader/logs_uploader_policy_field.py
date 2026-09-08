# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["LogsUploaderPolicyField"]


class LogsUploaderPolicyField(BaseModel):
    allowed_conversions: List[Literal["scale", "replace"]]
    """Conversion types this field permits in `field_conversions`.

    Empty when the field permits none.
    """

    name: str
    """
    Canonical Gcore field name, or `-` as the skipped-column placeholder, selectable
    in a policy's `fields`.
    """
