# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FlavorListParams", "Name", "RamMib", "Vcpus"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    architectures: List[Literal["aarch64", "unknown", "x86_64"]]
    """Filter by flavor architecture type(s)."""

    available: bool
    """Set to true to return only the available flavors.

    Set to false to return only the flavors that are disabled in their region or out
    of stock there. Omit it to return all flavors.
    """

    compatible_with_boot_volume_id: str
    """Return only the flavors that can boot from this volume, from its image metadata.

    An unknown volume matches no flavor. A non-bootable volume or one without image
    metadata is a 400. At most one `compatible_with_`\\** parameter per request.
    """

    compatible_with_image_id: str
    """
    Return only the flavors that can boot this image: its region, OS type and CPU
    architecture. An unknown image matches no flavor. At most one
    `compatible_with_`\\** parameter per request.
    """

    compatible_with_snapshot_id: str
    """
    Return only the flavors that can boot from this snapshot, resolved through its
    parent volume's image metadata. An unknown snapshot matches no flavor. A parent
    volume with no image metadata is a 400. At most one `compatible_with_`\\**
    parameter per request.
    """

    limit: int
    """Max items to return."""

    name: Name
    """Operator flavor name filter, e.g. name[prefix]=g2-."""

    offset: int
    """Items to skip."""

    order_by: Literal[
        "name.asc",
        "name.desc",
        "ram_mib.asc",
        "ram_mib.desc",
        "region_id.asc",
        "region_id.desc",
        "vcpus.asc",
        "vcpus.desc",
    ]
    """Sort field and direction."""

    os_types: List[Literal["linux", "unknown", "windows"]]
    """Filter by flavor operating system(s)."""

    ram_mib: RamMib
    """Range filter on RAM size in MiB."""

    region_ids: Iterable[int]
    """Filter by region ID(s). Omit = all regions."""

    vcpus: Vcpus
    """Range filter on virtual CPU count."""


class Name(TypedDict, total=False):
    """Operator flavor name filter, e.g. name[prefix]=g2-."""

    contains: SequenceNotStr[str]
    """Case-insensitive substring, e.g.

    `[contains]=web`. Repeat the key to match any substring.
    """

    exact: SequenceNotStr[str]
    """Case-insensitive exact match, e.g.

    `[exact]=web-1`. Repeat the key to match any of several.
    """

    prefix: SequenceNotStr[str]
    """Case-insensitive starts-with, e.g.

    `[prefix]=prod-`. Repeat the key to match any prefix.
    """

    suffix: SequenceNotStr[str]
    """Case-insensitive ends-with, e.g.

    `[suffix]=-db`. Repeat the key to match any suffix.
    """


class RamMib(TypedDict, total=False):
    """Range filter on RAM size in MiB."""

    gt: int
    """Strictly greater than, e.g. `[gt]=1`."""

    gte: int
    """Greater than or equal, e.g. `[gte]=2`."""

    lt: int
    """Strictly less than, e.g. `[lt]=8`."""

    lte: int
    """Less than or equal, e.g. `[lte]=4`."""


class Vcpus(TypedDict, total=False):
    """Range filter on virtual CPU count."""

    gt: int
    """Strictly greater than, e.g. `[gt]=1`."""

    gte: int
    """Greater than or equal, e.g. `[gte]=2`."""

    lt: int
    """Strictly less than, e.g. `[lt]=8`."""

    lte: int
    """Less than or equal, e.g. `[lte]=4`."""
