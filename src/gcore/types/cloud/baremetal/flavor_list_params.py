# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FlavorListParams", "CPUThreads", "Name", "RamMib"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    architectures: List[Literal["aarch64", "unknown", "x86_64"]]
    """Filter by flavor architecture type(s)."""

    compatible_with_image_id: str
    """
    Return only the flavors that can boot this image: its region, OS type and CPU
    architecture, minus the flavors registered as incompatible with its OS release.
    An unknown image matches no flavor.
    """

    cpu_threads: CPUThreads
    """Range filter on CPU thread count."""

    limit: int
    """Max items to return."""

    name: Name
    """Operator flavor name filter, e.g. name[prefix]=bm2-."""

    offset: int
    """Items to skip."""

    order_by: Literal[
        "cpu_threads.asc",
        "cpu_threads.desc",
        "name.asc",
        "name.desc",
        "ram_mib.asc",
        "ram_mib.desc",
        "region_id.asc",
        "region_id.desc",
    ]
    """Sort field and direction."""

    os_types: List[Literal["linux", "unknown", "windows"]]
    """Filter by flavor operating system(s)."""

    ram_mib: RamMib
    """Range filter on RAM size in MiB."""

    region_ids: Iterable[int]
    """Filter by region ID(s). Omit = all regions."""


class CPUThreads(TypedDict, total=False):
    """Range filter on CPU thread count."""

    gt: int
    """Strictly greater than, e.g. `[gt]=1`."""

    gte: int
    """Greater than or equal, e.g. `[gte]=2`."""

    lt: int
    """Strictly less than, e.g. `[lt]=8`."""

    lte: int
    """Less than or equal, e.g. `[lte]=4`."""


class Name(TypedDict, total=False):
    """Operator flavor name filter, e.g. name[prefix]=bm2-."""

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
