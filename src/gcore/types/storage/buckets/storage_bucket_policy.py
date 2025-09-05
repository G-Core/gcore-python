# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["StorageBucketPolicy"]


class StorageBucketPolicy(BaseModel):
    enabled_http_access: Optional[bool] = FieldInfo(alias="enabledHttpAccess", default=None)
