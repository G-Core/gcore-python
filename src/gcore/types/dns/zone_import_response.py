# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ZoneImportResponse", "Imported"]


class Imported(BaseModel):
    """ImportedRRSets - import statistics"""

    qtype: Optional[int] = None

    resource_records: Optional[int] = None

    rrsets: Optional[int] = None

    skipped_resource_records: Optional[int] = None


class ZoneImportResponse(BaseModel):
    imported: Optional[Imported] = None
    """ImportedRRSets - import statistics"""

    success: Optional[bool] = None

    warnings: Optional[Dict[str, Dict[str, str]]] = None
