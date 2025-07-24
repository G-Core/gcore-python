# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Ffprobes", "Data"]


class Data(BaseModel):
    avg_bitrate: float

    max_fps: float

    max_height: int

    max_keyframe_interval: int

    sum_frames: int

    time: str


class Ffprobes(BaseModel):
    data: Optional[List[Data]] = None
