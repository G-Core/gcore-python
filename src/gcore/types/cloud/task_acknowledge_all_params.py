# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TaskAcknowledgeAllParams"]


class TaskAcknowledgeAllParams(TypedDict, total=False):
    project_id: Optional[int]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks%2Facknowledge_all/post/parameters/0/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks/acknowledge_all'].post.parameters[0].schema.anyOf[0]"
    """

    region_id: Optional[int]
    """
    '#/paths/%2Fcloud%2Fv1%2Ftasks%2Facknowledge_all/post/parameters/1/schema/anyOf/0'
    "$.paths['/cloud/v1/tasks/acknowledge_all'].post.parameters[1].schema.anyOf[0]"
    """
