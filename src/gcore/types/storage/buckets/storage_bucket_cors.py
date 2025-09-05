# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["StorageBucketCors", "Data"]


class Data(BaseModel):
    allowed_origins: Optional[List[str]] = FieldInfo(alias="allowedOrigins", default=None)


class StorageBucketCors(BaseModel):
    data: Optional[Data] = None
