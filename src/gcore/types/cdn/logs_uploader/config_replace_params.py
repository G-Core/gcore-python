# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ConfigReplaceParams"]


class ConfigReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the config."""

    policy: Required[int]
    """ID of the policy that should be assigned to given config."""

    target: Required[int]
    """ID of the target to which logs should be uploaded."""

    enabled: bool
    """Enables or disables the config."""

    for_all_resources: bool
    """
    If set to true, the config will be applied to all CDN resources. If set to
    false, the config will be applied to the resources specified in the `resources`
    field.
    """

    resources: Iterable[int]
    """List of resource IDs to which the config should be applied."""
