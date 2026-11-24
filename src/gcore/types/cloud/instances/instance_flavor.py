# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InstanceFlavor"]


class InstanceFlavor(BaseModel):
    architecture: Literal["aarch64", "unknown", "x86_64"]
    """Flavor architecture type."""

    available: bool
    """Whether a new server of this flavor can be created in this region now.

    The value is false when the flavor is disabled in the region or is out of stock
    there.
    """

    name: str
    """Flavor name."""

    os_type: Literal["linux", "unknown", "windows"]
    """Flavor operating system."""

    ram_mib: int
    """RAM size in MiB."""

    region_id: int
    """Region ID."""

    vcpus: int
    """Virtual CPU count."""
