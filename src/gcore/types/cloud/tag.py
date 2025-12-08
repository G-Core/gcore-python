# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    """
    A tag is a key-value pair that can be associated with a resource,
    enabling efficient filtering and grouping for better organization and management.
    Some tags are read-only and cannot be modified by the user.
    Tags are also integrated with cost reports, allowing cost data to be filtered based on tag keys or values.
    """

    key: str
    """Tag key. The maximum size for a key is 255 characters."""

    read_only: bool
    """If true, the tag is read-only and cannot be modified by the user"""

    value: str
    """Tag value. The maximum size for a value is 255 characters."""
