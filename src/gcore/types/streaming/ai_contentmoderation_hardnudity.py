# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AIContentmoderationHardnudity"]


class AIContentmoderationHardnudity(BaseModel):
    category: Literal["hard_nudity", "sport", "nsfw", "soft_nudity"]
    """AI content moderation with "`hard_nudity`" algorithm"""

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

    stop_objects: Optional[
        Literal[
            "ANUS_EXPOSED",
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
    ] = None
    """
    Comma separated objects, and probabilities, that will cause the processing to
    stop immediatelly after finding.
    """
