# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: int
    """Project ID, which is automatically generated upon creation."""

    client_id: int
    """ID associated with the client."""

    created_at: datetime
    """Datetime of creation, which is automatically generated."""

    is_default: bool
    """Indicates if the project is the default one.

    Each client always has one default project.
    """

    name: str
    """Unique project name for a client."""

    state: str
    """The state of the project."""

    deleted_at: Optional[datetime] = None
    """
    Datetime of deletion, which is automatically generated if the project is
    deleted.
    """

    description: Optional[str] = None
    """Description of the project."""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
