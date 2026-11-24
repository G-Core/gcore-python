# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BaremetalFlavor", "HardwareDescription", "NetworkingCapabilities"]


class HardwareDescription(BaseModel):
    """Hardware of the flavor, as text to show to a person.

    `disk` gives the disk layout. `license` marks a Windows flavor. The value is null for a flavor
    with no hardware text.
    """

    cpu: str
    """CPU model and core count."""

    disk: str
    """Disk layout, including count and RAID level."""

    license: str
    """Bundled license, empty for the Linux variants."""

    network: str
    """Network interfaces."""

    ram: str
    """Memory size."""


class NetworkingCapabilities(BaseModel):
    """What ports attached to a server of this flavor support."""

    allowed_address_pairs: bool
    """Whether ports on this flavor accept allowed address pairs."""

    port_security: bool
    """Whether ports on this flavor accept port security."""

    security_groups: bool
    """Whether ports on this flavor accept security groups."""


class BaremetalFlavor(BaseModel):
    architecture: Literal["aarch64", "unknown", "x86_64"]
    """Flavor architecture type."""

    capacity: int
    """
    How many servers of this flavor the client can build in this region now, after
    reservations. 0 also means the count is unavailable.
    """

    cpu_threads: int
    """CPU thread count. The server is dedicated, so nothing is oversubscribed."""

    hardware_description: Optional[HardwareDescription] = None
    """Hardware of the flavor, as text to show to a person.

    `disk` gives the disk layout. `license` marks a Windows flavor. The value is
    null for a flavor with no hardware text.
    """

    name: str
    """Flavor name."""

    networking_capabilities: NetworkingCapabilities
    """What ports attached to a server of this flavor support."""

    os_type: Literal["linux", "unknown", "windows"]
    """Flavor operating system."""

    ram_mib: int
    """RAM size in MiB."""

    region_id: int
    """Region ID."""

    reserved_capacity: int
    """How many of `capacity` exist only because of the client's own reservations."""

    resource_class: Optional[str] = None
    """Hardware class the flavor is served from.

    The value is null if the flavor has no resource class.
    """
