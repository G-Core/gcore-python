# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["DNSLocationTranslations"]


class DNSLocationTranslations(BaseModel):
    names: Optional[Dict[str, str]] = None
