# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SecretUploadTlsCertificateResponse"]


class SecretUploadTlsCertificateResponse(BaseModel):
    tasks: Optional[List[str]] = None
    """Task list"""
