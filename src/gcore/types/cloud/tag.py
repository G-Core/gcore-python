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
    """Tag key.

    Maximum 255 characters. Cannot contain spaces, tabs, newlines, empty string or
    '=' character.
    """

    read_only: bool
    """If true, the tag is read-only and cannot be modified by the user"""

    value: str
    """Tag value.

    Maximum 255 characters. Cannot contain spaces, tabs, newlines, empty string or
    '=' character.
    """
