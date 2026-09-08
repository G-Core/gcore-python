# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "LogsUploaderPolicy",
    "FieldConversions",
    "FieldConversionsConversion",
    "FieldConversionsConversionScaleFieldConversion",
    "FieldConversionsConversionScaleFieldConversionConfig",
    "FieldConversionsConversionReplaceFieldConversion",
    "FieldConversionsConversionReplaceFieldConversionConfig",
]


class FieldConversionsConversionScaleFieldConversionConfig(BaseModel):
    factor: float
    """Multiplier applied to the field value."""

    precision: Optional[int] = None
    """Optional number of decimal places in the converted value.

    Must be specified together with `rounding`; returned as `null` when unspecified.
    """

    rounding: Optional[Literal["nearest", "down", "up"]] = None
    """Optional rounding mode.

    Must be specified together with `precision`; returned as `null` when
    unspecified.
    """


class FieldConversionsConversionScaleFieldConversion(BaseModel):
    config: FieldConversionsConversionScaleFieldConversionConfig

    type: Literal["scale"]


class FieldConversionsConversionReplaceFieldConversionConfig(BaseModel):
    values: Dict[str, str]
    """Exact, case-sensitive replacements, matched and written without trimming.

    Keys must not be empty and are limited to 255 characters; values are limited to
    100 characters and may be empty.
    """

    default: Optional[str] = None
    """Value used when the input does not match any key in `values`."""


class FieldConversionsConversionReplaceFieldConversion(BaseModel):
    config: FieldConversionsConversionReplaceFieldConversionConfig

    type: Literal["replace"]


FieldConversionsConversion: TypeAlias = Annotated[
    Union[FieldConversionsConversionScaleFieldConversion, FieldConversionsConversionReplaceFieldConversion],
    PropertyInfo(discriminator="type"),
]


class FieldConversions(BaseModel):
    conversions: List[FieldConversionsConversion]


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

    escape_special_characters: Optional[bool] = None
    """
    When set to true, the service sanitizes string values by escaping characters
    that may be unsafe for transport, logging, or downstream processing.

    The following categories of characters are escaped:

    - Control and non-printable characters
    - Quotation marks and escape characters
    - Characters outside the standard ASCII range

    The resulting output contains only printable ASCII characters.
    """

    field_conversions: Optional[Dict[str, FieldConversions]] = None
    """Per-field value conversions for exported logs.

    Maps a canonical Gcore field name to the pipeline applied to its values. Field
    names are limited to 255 characters and must not be empty. Each key must be
    present in `fields`, and each conversion type must be listed in that field's
    `allowed_conversions` from `/cdn/v2/logs_uploader/policies/fields`. Conversions
    in a pipeline are applied in array order. Values are converted independently of
    `field_remap`, which renames the exported field: both are keyed on the canonical
    field name.
    """

    field_delimiter: Optional[str] = None
    """Field delimiter for logs."""

    field_remap: Optional[Dict[str, str]] = None
    """Per-field output-name remap for exported logs.

    Maps a canonical Gcore field name (from `/cdn/logs_uploader/policies/fields`,
    and must be present in `fields`) to the field name it should have in the
    exported logs. Unmapped fields keep their canonical name. Output names (after
    remapping) must be unique.
    """

    field_separator: Optional[str] = None
    """Field separator for logs."""

    fields: Optional[List[str]] = None
    """List of fields to include in logs.

    Duplicate names are allowed for plain text output, but rejected when
    `format_type` is `json` or a `field_remap` is set (each field becomes a distinct
    output key).
    """

    file_name_template: Optional[str] = None
    """Template for log file name."""

    format_type: Optional[Literal["json", ""]] = None
    """Format type for logs.

    Possible values:

    - **""** - empty, it means it will apply the format configurations from the
      policy.
    - **"json"** - output the logs as json lines.
    """

    include_empty_logs: Optional[bool] = None
    """Include empty logs in the upload."""

    include_shield_logs: Optional[bool] = None
    """Include logs from origin shielding in the upload."""

    log_sample_rate: Optional[float] = None
    """Sampling rate for logs.

    A value between 0 and 1 that determines the fraction of log entries to collect.

    - **1** - collect all logs (default).
    - **0.5** - collect approximately 50% of logs.
    - **0** - collect no logs (effectively disables logging without removing the
      policy).
    """

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
