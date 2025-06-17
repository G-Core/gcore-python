# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["APIDiscoveryGetSettingsResponse"]


class APIDiscoveryGetSettingsResponse(BaseModel):
    description_file_location: Optional[str] = FieldInfo(alias="descriptionFileLocation", default=None)
    """The URL of the API description file.

    This will be periodically scanned if `descriptionFileScanEnabled` is enabled.
    Supported formats are YAML and JSON, and it must adhere to OpenAPI versions 2,
    3, or 3.1.
    """

    description_file_scan_enabled: Optional[bool] = FieldInfo(alias="descriptionFileScanEnabled", default=None)
    """Indicates if periodic scan of the description file is enabled"""

    description_file_scan_interval_hours: Optional[int] = FieldInfo(
        alias="descriptionFileScanIntervalHours", default=None
    )
    """The interval in hours for scanning the description file"""

    traffic_scan_enabled: Optional[bool] = FieldInfo(alias="trafficScanEnabled", default=None)
    """Indicates if traffic scan is enabled.

    Traffic scan is used to discover undocumented APIs
    """

    traffic_scan_interval_hours: Optional[int] = FieldInfo(alias="trafficScanIntervalHours", default=None)
    """The interval in hours for scanning the traffic"""
