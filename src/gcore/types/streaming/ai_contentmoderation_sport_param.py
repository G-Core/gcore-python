# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIContentmoderationSportParam"]


class AIContentmoderationSportParam(TypedDict, total=False):
    category: Required[Literal["sport"]]
    """AI content moderation with types of sports activity detection"""

    task_name: Required[Literal["content-moderation"]]
    """Name of the task to be performed"""

    url: Required[str]
    """URL to the MP4 file to analyze.

    File must be publicly accessible via HTTP/HTTPS.
    """

    client_entity_data: str
    """
    Meta parameter, designed to store your own extra information about a video
    entity: video source, video id, etc. It is not used in any way in video
    processing.

    For example, if an AI-task was created automatically when you uploaded a video
    with the AI auto-processing option (nudity detection, etc), then the ID of the
    associated video for which the task was performed will be explicitly indicated
    here.
    """

    client_user_id: str
    """Meta parameter, designed to store your own identifier.

    Can be used by you to tag requests from different end-users. It is not used in
    any way in video processing.
    """
