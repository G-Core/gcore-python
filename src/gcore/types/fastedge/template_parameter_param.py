# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateParameterParam"]


class TemplateParameterParam(TypedDict, total=False):
    data_type: Required[Literal["string", "number", "date", "time", "secret", "store", "bool", "json", "enum"]]
    """
    Parameter type determines validation and UI rendering:
    string - text input
    number - numeric input
    date - date picker
    time - time picker
    secret - references a secret
    store - references an edge store
    bool - boolean toggle
    json - JSON editor or multiline text area with JSON validation
    enum - dropdown/select with allowed values defined via parameter metadata
    """

    mandatory: Required[bool]
    """If true, this parameter must be provided when instantiating the template"""

    name: Required[str]
    """
    Parameter name used as a placeholder in template (e.g., `API_KEY`,
    `DATABASE_URL`)
    """

    descr: str
    """Human-readable explanation of what this parameter controls"""

    metadata: str
    """
    Optional JSON-encoded string for additional parameter metadata, such as allowed
    values for enum types
    """
