# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["PolicyUpdateParams"]


class PolicyUpdateParams(TypedDict, total=False):
    date_format: str
    """Date format for logs."""

    description: str
    """Description of the policy."""

    field_delimiter: str
    """Field delimiter for logs."""

    field_separator: str
    """Field separator for logs."""

    fields: SequenceNotStr[str]
    """List of fields to include in logs."""

    file_name_template: str
    """Template for log file name."""

    format_type: str
    """Format type for logs."""

    include_empty_logs: bool
    """Include empty logs in the upload."""

    include_shield_logs: bool
    """Include logs from origin shielding in the upload."""

    name: str
    """Name of the policy."""

    retry_interval_minutes: int
    """Interval in minutes to retry failed uploads."""

    rotate_interval_minutes: int
    """Interval in minutes to rotate logs."""

    rotate_threshold_lines: int
    """Threshold in lines to rotate logs."""

    rotate_threshold_mb: Optional[int]
    """Threshold in MB to rotate logs."""

    tags: Dict[str, str]
    """
    Tags allow for dynamic decoration of logs by adding predefined fields to the log
    format. These tags serve as customizable key-value pairs that can be included in
    log entries to enhance context and readability.
    """
