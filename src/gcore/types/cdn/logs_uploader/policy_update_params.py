# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "PolicyUpdateParams",
    "FieldConversions",
    "FieldConversionsConversion",
    "FieldConversionsConversionScaleFieldConversion",
    "FieldConversionsConversionScaleFieldConversionConfig",
    "FieldConversionsConversionReplaceFieldConversion",
    "FieldConversionsConversionReplaceFieldConversionConfig",
]


class PolicyUpdateParams(TypedDict, total=False):
    date_format: str
    """Date format for logs."""

    description: str
    """Description of the policy."""

    escape_special_characters: bool
    """
    When set to true, the service sanitizes string values by escaping characters
    that may be unsafe for transport, logging, or downstream processing.

    The following categories of characters are escaped:

    - Control and non-printable characters
    - Quotation marks and escape characters
    - Characters outside the standard ASCII range

    The resulting output contains only printable ASCII characters.
    """

    field_conversions: Dict[str, FieldConversions]
    """Per-field value conversions for exported logs.

    Maps a canonical Gcore field name to the pipeline applied to its values. Field
    names are limited to 255 characters and must not be empty. Each key must be
    present in `fields`, and each conversion type must be listed in that field's
    `allowed_conversions` from `/cdn/v2/logs_uploader/policies/fields`. Conversions
    in a pipeline are applied in array order. Values are converted independently of
    `field_remap`, which renames the exported field: both are keyed on the canonical
    field name.
    """

    field_delimiter: str
    """Field delimiter for logs."""

    field_remap: Dict[str, str]
    """Per-field output-name remap for exported logs.

    Maps a canonical Gcore field name (from `/cdn/logs_uploader/policies/fields`,
    and must be present in `fields`) to the field name it should have in the
    exported logs. Unmapped fields keep their canonical name. Output names (after
    remapping) must be unique.
    """

    field_separator: str
    """Field separator for logs."""

    fields: SequenceNotStr[str]
    """List of fields to include in logs.

    Duplicate names are allowed for plain text output, but rejected when
    `format_type` is `json` or a `field_remap` is set (each field becomes a distinct
    output key).
    """

    file_name_template: str
    """Template for log file name."""

    format_type: Literal["json", ""]
    """Format type for logs.

    Possible values:

    - **""** - empty, it means it will apply the format configurations from the
      policy.
    - **"json"** - output the logs as json lines.
    """

    include_empty_logs: bool
    """Include empty logs in the upload."""

    include_shield_logs: bool
    """Include logs from origin shielding in the upload."""

    log_sample_rate: float
    """Sampling rate for logs.

    A value between 0 and 1 that determines the fraction of log entries to collect.

    - **1** - collect all logs (default).
    - **0.5** - collect approximately 50% of logs.
    - **0** - collect no logs (effectively disables logging without removing the
      policy).
    """

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


class FieldConversionsConversionScaleFieldConversionConfig(TypedDict, total=False):
    factor: Required[float]
    """Multiplier applied to the field value."""

    precision: Optional[int]
    """Optional number of decimal places in the converted value.

    Must be specified together with `rounding`; returned as `null` when unspecified.
    """

    rounding: Optional[Literal["nearest", "down", "up"]]
    """Optional rounding mode.

    Must be specified together with `precision`; returned as `null` when
    unspecified.
    """


class FieldConversionsConversionScaleFieldConversion(TypedDict, total=False):
    config: Required[FieldConversionsConversionScaleFieldConversionConfig]

    type: Required[Literal["scale"]]


class FieldConversionsConversionReplaceFieldConversionConfig(TypedDict, total=False):
    values: Required[Dict[str, str]]
    """Exact, case-sensitive replacements, matched and written without trimming.

    Keys must not be empty and are limited to 255 characters; values are limited to
    100 characters and may be empty.
    """

    default: str
    """Value used when the input does not match any key in `values`."""


class FieldConversionsConversionReplaceFieldConversion(TypedDict, total=False):
    config: Required[FieldConversionsConversionReplaceFieldConversionConfig]

    type: Required[Literal["replace"]]


FieldConversionsConversion: TypeAlias = Union[
    FieldConversionsConversionScaleFieldConversion, FieldConversionsConversionReplaceFieldConversion
]


class FieldConversions(TypedDict, total=False):
    conversions: Required[Iterable[FieldConversionsConversion]]
