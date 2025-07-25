# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DirectUploadParameters"]


class DirectUploadParameters(BaseModel):
    token: Optional[str] = None
    """Token"""

    servers: Optional[List[object]] = None
    """An array which contains information about servers you can upload a video to.

    **Server;** type — object.

    ---

    Server has the following fields:

    - **id;** type — integer
       Server ID
    - **hostname;** type — string
       Server hostname
    """

    video: Optional[object] = None
    """Contains information about the created video.

    See the full description in the Get video request
    """
