# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["APIDiscoveryUpdateSettingsParams"]


class APIDiscoveryUpdateSettingsParams(TypedDict, total=False):
    description_file_location: Annotated[Optional[str], PropertyInfo(alias="descriptionFileLocation")]
    """The URL of the API description file.

    This will be periodically scanned if `descriptionFileScanEnabled` is enabled.
    Supported formats are YAML and JSON, and it must adhere to OpenAPI versions 2,
    3, or 3.1.
    """

    description_file_scan_enabled: Annotated[Optional[bool], PropertyInfo(alias="descriptionFileScanEnabled")]
    """Indicates if periodic scan of the description file is enabled"""

    description_file_scan_interval_hours: Annotated[
        Optional[int], PropertyInfo(alias="descriptionFileScanIntervalHours")
    ]
    """The interval in hours for scanning the description file"""

    traffic_scan_enabled: Annotated[Optional[bool], PropertyInfo(alias="trafficScanEnabled")]
    """Indicates if traffic scan is enabled"""

    traffic_scan_interval_hours: Annotated[Optional[int], PropertyInfo(alias="trafficScanIntervalHours")]
    """The interval in hours for scanning the traffic"""
