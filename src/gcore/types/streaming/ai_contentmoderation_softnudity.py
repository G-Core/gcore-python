# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AIContentmoderationSoftnudity"]


class AIContentmoderationSoftnudity(BaseModel):
    category: Literal["soft_nudity", "sport", "nsfw", "hard_nudity"]
    """AI content moderation with "`soft_nudity`" algorithm"""

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
            "ANUS_COVERED",
            "ANUS_EXPOSED",
            "ARMPITS_COVERED",
            "ARMPITS_EXPOSED",
            "BELLY_COVERED",
            "BELLY_EXPOSED",
            "BUTTOCKS_COVERED",
            "BUTTOCKS_EXPOSED",
            "FACE_FEMALE",
            "FACE_MALE",
            "FEET_COVERED",
            "FEET_EXPOSED",
            "FEMALE_BREAST_COVERED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_COVERED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
    ] = None
    """
    Comma separated objects, and probabilities, that will cause the processing to
    stop immediatelly after finding.
    """
