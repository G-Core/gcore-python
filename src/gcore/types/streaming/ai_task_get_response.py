# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .ai_task import AITask
from ..._models import BaseModel

__all__ = [
    "AITaskGetResponse",
    "AITaskGetResponseProcessingTime",
    "AITaskGetResponseResult",
    "AITaskGetResponseResultAIResultsTranscribe",
    "AITaskGetResponseResultAIResultsTranscribeSubtitle",
    "AITaskGetResponseResultAIResultsContentmoderationSport",
    "AITaskGetResponseResultAIResultsContentmoderationSportFrame",
    "AITaskGetResponseResultAIResultsContentmoderationNsfw",
    "AITaskGetResponseResultAIResultsContentmoderationNsfwFrame",
    "AITaskGetResponseResultAIResultsContentmoderationHardnudity",
    "AITaskGetResponseResultAIResultsContentmoderationHardnudityFrame",
    "AITaskGetResponseResultAIResultsContentmoderationSoftnudity",
    "AITaskGetResponseResultAIResultsContentmoderationSoftnudityFrame",
    "AITaskGetResponseResultAIResultsFailure",
]


class AITaskGetResponseProcessingTime(BaseModel):
    completed_at: Optional[str] = None
    """Video processing end time. Format is date time in ISO 8601"""

    started_at: Optional[str] = None
    """Video processing start time. Format is date time in ISO 8601"""

    total_time_sec: Optional[float] = None
    """Duration of video processing in seconds"""


class AITaskGetResponseResultAIResultsTranscribeSubtitle(BaseModel):
    end_time: Optional[str] = None
    """End time of the phrase, when it ends in the video. Format is "HH:mm:ss.fff"."""

    start_time: Optional[str] = None
    """Start time of the phrase when it is heard in the video.

    Format is "HH:mm:ss.fff".
    """

    text: Optional[str] = None
    """A complete phrase that sounds during a specified period of time."""


class AITaskGetResponseResultAIResultsTranscribe(BaseModel):
    concatenated_text: Optional[str] = None
    """Full text of the analyzed video. The value is unstructured, unformatted text."""

    languages: Optional[List[str]] = None
    """An array of language codes that were discovered and/or used in transcription.

    If the audio or subtitle language was explicitly specified in the initial
    parameters, it will be copied here. For automatic detection the identified
    languages will be displayed here. Also please note that for multilingual audio,
    the first 5 languages are displayed in order of frequency of use.
    """

    speech_detected: Optional[bool] = None
    """Determines whether speech was detected or not.

    Please note: If the task is in "SUCCESS" status and speech was not found in the
    entire file, then "false" will be indicated here and the `subtitles` field will
    be empty.
    """

    subtitles: Optional[List[AITaskGetResponseResultAIResultsTranscribeSubtitle]] = None
    """An array of phrases divided into time intervals, in the format "json".

    Suitable when you need to display the result in chronometric form, or transfer
    the text for further processing.
    """

    vtt_content: Optional[str] = FieldInfo(alias="vttContent", default=None)
    """Auto generated subtitles in WebVTT format."""


class AITaskGetResponseResultAIResultsContentmoderationSportFrame(BaseModel):
    confidence: Optional[float] = None
    """Percentage of probability of identifying the activity"""

    frame_number: Optional[int] = FieldInfo(alias="frame-number", default=None)
    """Video frame number where activity was found"""

    label: Optional[str] = None
    """Type of detected activity"""


class AITaskGetResponseResultAIResultsContentmoderationSport(BaseModel):
    detection_results: Optional[
        List[
            Literal[
                "archery",
                "arm wrestling",
                "playing badminton",
                "playing baseball",
                "basketball dunk",
                "bowling",
                "boxing punch",
                "boxing speed bag",
                "catching or throwing baseball",
                "catching or throwing softball",
                "cricket",
                "curling",
                "disc golfing",
                "dodgeball",
                "fencing",
                "football",
                "golf chipping",
                "golf driving",
                "golf putting",
                "hitting baseball",
                "hockey stop",
                "ice skating",
                "javelin throw",
                "juggling soccer ball",
                "kayaking",
                "kicking field goal",
                "kicking soccer ball",
                "playing cricket",
                "playing field hockey",
                "playing ice hockey",
                "playing kickball",
                "playing lacrosse",
                "playing ping pong",
                "playing polo",
                "playing squash or racquetball",
                "playing tennis",
                "playing volleyball",
                "pole vault",
                "riding a bike",
                "riding or walking with horse",
                "roller skating",
                "rowing",
                "sailing",
                "shooting goal (soccer)",
                "skateboarding",
                "skiing",
            ]
        ]
    ] = None

    frames: Optional[List[AITaskGetResponseResultAIResultsContentmoderationSportFrame]] = None

    sport_detected: Optional[bool] = None
    """A boolean value whether any sports were detected"""


class AITaskGetResponseResultAIResultsContentmoderationNsfwFrame(BaseModel):
    confidence: Optional[float] = None
    """Percentage of probability of identifying the object"""

    frame_number: Optional[int] = FieldInfo(alias="frame-number", default=None)
    """Video frame number where object was found"""

    label: Optional[str] = None
    """Type of detected object"""


class AITaskGetResponseResultAIResultsContentmoderationNsfw(BaseModel):
    detection_results: Optional[List[Literal["nsfw"]]] = None

    frames: Optional[List[AITaskGetResponseResultAIResultsContentmoderationNsfwFrame]] = None

    nsfw_detected: Optional[bool] = None
    """A boolean value whether any Not Safe For Work content was detected"""


class AITaskGetResponseResultAIResultsContentmoderationHardnudityFrame(BaseModel):
    confidence: Optional[float] = None
    """Percentage of probability of identifying the object"""

    frame_number: Optional[int] = FieldInfo(alias="frame-number", default=None)
    """Video frame number where object was found"""

    label: Optional[str] = None
    """Type of detected object"""


class AITaskGetResponseResultAIResultsContentmoderationHardnudity(BaseModel):
    detection_results: Optional[
        List[
            Literal[
                "ANUS_EXPOSED",
                "BUTTOCKS_EXPOSED",
                "FEMALE_BREAST_EXPOSED",
                "FEMALE_GENITALIA_EXPOSED",
                "MALE_BREAST_EXPOSED",
                "MALE_GENITALIA_EXPOSED",
            ]
        ]
    ] = None

    frames: Optional[List[AITaskGetResponseResultAIResultsContentmoderationHardnudityFrame]] = None

    porn_detected: Optional[bool] = None
    """A boolean value whether any nudity was detected"""


class AITaskGetResponseResultAIResultsContentmoderationSoftnudityFrame(BaseModel):
    confidence: Optional[float] = None
    """Percentage of probability of identifying the object"""

    frame_number: Optional[int] = FieldInfo(alias="frame-number", default=None)
    """Video frame number where object was found"""

    label: Optional[str] = None
    """Type of detected object"""


class AITaskGetResponseResultAIResultsContentmoderationSoftnudity(BaseModel):
    detection_results: Optional[
        List[
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
        ]
    ] = None

    frames: Optional[List[AITaskGetResponseResultAIResultsContentmoderationSoftnudityFrame]] = None

    porn_detected: Optional[bool] = None
    """A boolean value whether any nudity and other body part was detected"""


class AITaskGetResponseResultAIResultsFailure(BaseModel):
    error: str


AITaskGetResponseResult: TypeAlias = Union[
    AITaskGetResponseResultAIResultsTranscribe,
    AITaskGetResponseResultAIResultsContentmoderationSport,
    AITaskGetResponseResultAIResultsContentmoderationNsfw,
    AITaskGetResponseResultAIResultsContentmoderationHardnudity,
    AITaskGetResponseResultAIResultsContentmoderationSoftnudity,
    AITaskGetResponseResultAIResultsFailure,
]


class AITaskGetResponse(AITask):
    processing_time: Optional[AITaskGetResponseProcessingTime] = None

    result: Optional[AITaskGetResponseResult] = None
