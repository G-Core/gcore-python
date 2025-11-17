# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["TaskIDList"]


class TaskIDList(BaseModel):
    tasks: List[str]
    """List of task IDs representing asynchronous operations.

    Use these IDs to monitor operation progress:

    - `GET /v1/tasks/{task_id}` - Check individual task status and details Poll task
      status until completion (`FINISHED`/`ERROR`) before proceeding with dependent
      operations.
    """
