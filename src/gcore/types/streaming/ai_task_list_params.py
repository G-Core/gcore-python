# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AITaskListParams"]


class AITaskListParams(TypedDict, total=False):
    date_created: str
    """Time when task was created. Datetime in ISO 8601 format."""

    limit: int
    """Number of results to return per page."""

    ordering: Literal["task_id", "status", "task_name", "started_at"]
    """
    Which field to use when ordering the results: `task_id`, status, and
    `task_name`. Sorting is done in ascending (ASC) order.

    If parameter is omitted then "`started_at` DESC" is used for ordering by
    default.
    """

    page: int
    """Page to view from task list, starting from 1"""

    search: str
    """
    This is an field for combined text search in the following fields: `task_id`,
    `task_name`, status, and `task_data`.

    Both full and partial searches are possible inside specified above fields. For
    example, you can filter tasks of a certain category, or tasks by a specific
    original file.

    Example:

    - To filter tasks of Content Moderation NSFW method:
      `GET /streaming/ai/tasks?search=nsfw`
    - To filter tasks of processing video from a specific origin:
      `GET /streaming/ai/tasks?search=s3.eu-west-1.amazonaws.com`
    """

    status: Literal["FAILURE", "PENDING", "RECEIVED", "RETRY", "REVOKED", "STARTED", "SUCCESS"]
    """Task status"""

    task_id: str
    """The task unique identifier to fiund"""

    task_name: Literal["transcription", "content-moderation"]
    """Type of the AI task.

    Reflects the original API method that was used to create the AI task.
    """
