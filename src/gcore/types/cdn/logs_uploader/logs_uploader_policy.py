# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["LogsUploaderPolicy"]


class LogsUploaderPolicy(BaseModel):
    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the policy."""

    created: Optional[datetime] = None
    """Time when logs uploader policy was created."""

    date_format: Optional[str] = None
    """Date format for logs."""

    description: Optional[str] = None
    """Description of the policy."""

    field_delimiter: Optional[str] = None
    """Field delimiter for logs."""

    field_separator: Optional[str] = None
    """Field separator for logs."""

    fields: Optional[List[str]] = None
    """List of fields to include in logs."""

    file_name_template: Optional[str] = None
    """Template for log file name."""

    format_type: Optional[str] = None
    """Format type for logs."""

    include_empty_logs: Optional[bool] = None
    """Include empty logs in the upload."""

    include_shield_logs: Optional[bool] = None
    """Include logs from origin shielding in the upload."""

    name: Optional[str] = None
    """Name of the policy."""

    related_uploader_configs: Optional[List[int]] = None
    """List of logs uploader configs that use this policy."""

    retry_interval_minutes: Optional[int] = None
    """Interval in minutes to retry failed uploads."""

    rotate_interval_minutes: Optional[int] = None
    """Interval in minutes to rotate logs."""

    rotate_threshold_lines: Optional[int] = None
    """Threshold in lines to rotate logs."""

    rotate_threshold_mb: Optional[int] = None
    """Threshold in MB to rotate logs."""

    tags: Optional[Dict[str, str]] = None
    """
    Tags allow for dynamic decoration of logs by adding predefined fields to the log
    format. These tags serve as customizable key-value pairs that can be included in
    log entries to enhance context and readability.
    """

    updated: Optional[datetime] = None
    """Time when logs uploader policy was updated."""
