# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "StreamStartRecordingResponse",
    "Data",
    "DataStream",
    "DataStreamClient",
    "Warning",
    "WarningMeta",
    "WarningSourceObject",
]


class DataStreamClient(BaseModel):
    id: Optional[int] = None
    """Client ID"""

    storage_limit_mb: Optional[int] = None
    """Current storage limit for client by megabytes"""

    storage_usage_mb: Optional[float] = None
    """Current storage usage for client by megabytes"""


class DataStream(BaseModel):
    id: Optional[int] = None
    """Stream ID"""

    client: Optional[DataStreamClient] = None


class Data(BaseModel):
    """Stream data"""

    stream: Optional[DataStream] = None


class WarningMeta(BaseModel):
    """storage usage state for client"""

    storage_limit_mb: Optional[int] = None
    """Current storage limit for client by megabytes"""

    storage_usage_mb: Optional[float] = None
    """Current storage usage for client by megabytes"""


class WarningSourceObject(BaseModel):
    """Warning source object"""

    id: Optional[int] = None
    """Client ID"""

    type: Optional[Literal["client"]] = None
    """Object type (class)"""


class Warning(BaseModel):
    key: Optional[Literal["client_storage_almost_exceeded"]] = None
    """current warning key"""

    meta: Optional[WarningMeta] = None
    """storage usage state for client"""

    source_object: Optional[WarningSourceObject] = None
    """Warning source object"""


class StreamStartRecordingResponse(BaseModel):
    data: Optional[Data] = None
    """Stream data"""

    errors: Optional[List[object]] = None
    """List of errors received on attempt to start recording process"""

    warnings: Optional[List[Warning]] = None
    """List of warnings received on starting recording process"""
