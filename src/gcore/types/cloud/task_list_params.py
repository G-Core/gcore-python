# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    from_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/0/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[0].schema.anyOf[0]"
    """

    is_acknowledged: Optional[bool]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/1/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[1].schema.anyOf[0]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/2'
    "$.paths['/cloud/v1/tasks'].get.parameters[2]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/3'
    "$.paths['/cloud/v1/tasks'].get.parameters[3]"
    """

    project_id: Optional[Iterable[int]]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/4/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[4].schema.anyOf[0]"
    """

    region_id: Optional[Iterable[int]]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/5/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[5].schema.anyOf[0]"
    """

    sorting: Optional[Literal["asc", "desc"]]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/6/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[6].schema.anyOf[0]"
    """

    state: Optional[List[Literal["ERROR", "FINISHED", "NEW", "RUNNING"]]]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/7/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[7].schema.anyOf[0]"
    """

    task_type: Optional[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/8/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[8].schema.anyOf[0]"
    """

    to_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks/get/parameters/9/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks'].get.parameters[9].schema.anyOf[0]"
    """
