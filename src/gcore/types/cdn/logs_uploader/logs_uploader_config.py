# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ..logs_uploader_validation import LogsUploaderValidation

__all__ = ["LogsUploaderConfig", "Status"]


class Status(LogsUploaderValidation):
    """Validation status of the logs uploader config."""

    pass


class LogsUploaderConfig(BaseModel):
    id: Optional[int] = None

    client_id: Optional[int] = None
    """Client that owns the config."""

    created: Optional[datetime] = None
    """Time when the config was created."""

    enabled: Optional[bool] = None
    """Enables or disables the config."""

    for_all_resources: Optional[bool] = None
    """
    If set to true, the config will be applied to all CDN resources. If set to
    false, the config will be applied to the resources specified in the `resources`
    field.
    """

    name: Optional[str] = None
    """Name of the config."""

    policy: Optional[int] = None
    """ID of the policy that should be assigned to given config."""

    resources: Optional[List[int]] = None
    """List of resource IDs to which the config should be applied."""

    status: Optional[Status] = None
    """Validation status of the logs uploader config."""

    target: Optional[int] = None
    """ID of the target to which logs should be uploaded."""

    updated: Optional[datetime] = None
    """Time when the config was updated."""
