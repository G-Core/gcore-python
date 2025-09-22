# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AIContentmoderationSport"]


class AIContentmoderationSport(BaseModel):
    category: Literal["sport", "nsfw", "hard_nudity", "soft_nudity"]
    """AI content moderation with types of sports activity detection"""

    task_name: Literal["content-moderation"]
    """Name of the task to be performed"""

    url: str
    """URL to the MP4 file to analyse.

    File must be publicly accessible via HTTP/HTTPS.
    """

    client_entity_data: Optional[str] = None
    """
    Meta parameter, designed to store your own extra information about a video
    entity: video source, video id, etc. It is not used in any way in video
    processing.

    For example, if an AI-task was created automatically when you uploaded a video
    with the AI auto-processing option (nudity detection, etc), then the ID of the
    associated video for which the task was performed will be explicitly indicated
    here.
    """

    client_user_id: Optional[str] = None
    """Meta parameter, designed to store your own identifier.

    Can be used by you to tag requests from different end-users. It is not used in
    any way in video processing.
    """
