# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Capacity"]


class Capacity(BaseModel):
    capacity: int
    """Available capacity."""

    flavor_name: str
    """Flavor name."""
