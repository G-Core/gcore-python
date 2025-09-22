# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoListParams"]


class VideoListParams(TypedDict, total=False):
    id: str
    """IDs of the videos to find.

    You can specify one or more identifiers separated by commas. Example,
    ?id=1,101,1001
    """

    client_user_id: int
    """Find videos where "`client_user_id`" meta field is equal to the search value"""

    fields: str
    """
    Restriction to return only the specified attributes, instead of the entire
    dataset. Specify, if you need to get short response. The following fields are
    available for specifying: id, name, duration, status, `created_at`,
    `updated_at`, `hls_url`, screenshots, `converted_videos`, priority, `stream_id`.
    Example, ?fields=id,name,`hls_url`
    """

    page: int
    """Page number. Use it to list the paginated content"""

    per_page: int
    """Items per page number. Use it to list the paginated content"""

    search: str
    """Aggregated search condition.

    If set, the video list is filtered by one combined SQL criterion:

    - id={s} OR slug={s} OR name like {s}

    i.e. "/videos?search=1000" returns list of videos where id=1000 or slug=1000 or
    name contains "1000".
    """

    status: str
    """Use it to get videos filtered by their status. Possible values:

    - empty
    - pending
    - viewable
    - ready
    - error
    """

    stream_id: int
    """
    Find videos recorded from a specific stream, so for which "`stream_id`" field is
    equal to the search value
    """
