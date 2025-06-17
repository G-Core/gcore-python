# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WaapInsightSortBy"]

WaapInsightSortBy: TypeAlias = Literal[
    "id",
    "-id",
    "insight_type",
    "-insight_type",
    "first_seen",
    "-first_seen",
    "last_seen",
    "-last_seen",
    "last_status_change",
    "-last_status_change",
    "status",
    "-status",
]
