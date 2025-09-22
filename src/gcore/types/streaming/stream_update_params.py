# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StreamUpdateParams", "Stream"]


class StreamUpdateParams(TypedDict, total=False):
    stream: Stream


class Stream(TypedDict, total=False):
    name: Required[str]
    """Stream name.

    Often used as a human-readable name for the stream, but can contain any text you
    wish. The values are not unique and may be repeated.

    Examples:

    - Conference in July
    - Stream #10003
    - Open-Air Camera #31 Backstage
    - 480fd499-2de2-4988-bc1a-a4eebe9818ee
    """

    active: bool
    """Stream switch between on and off.

    This is not an indicator of the status "stream is receiving and it is LIVE", but
    rather an on/off switch.

    When stream is switched off, there is no way to process it: PULL is deactivated
    and PUSH will return an error.

    - true – stream can be processed
    - false – stream is off, and cannot be processed
    """

    auto_record: bool
    """Enables autotomatic recording of the stream when it started.

    So you don't need to call recording manually.

    Result of recording is automatically added to video hosting. For details see the
    /streams/`start_recording` method and in knowledge base

    Values:

    - true – auto recording is enabled
    - false – auto recording is disabled
    """

    broadcast_ids: Iterable[int]
    """IDs of broadcasts which will include this stream"""

    cdn_id: int
    """
    ID of custom CDN resource from which the content will be delivered (only if you
    know what you do)
    """

    client_entity_data: str
    """
    Custom meta field designed to store your own extra information about a video
    entity: video source, video id, parameters, etc. We do not use this field in any
    way when processing the stream. You can store any data in any format (string,
    json, etc), saved as a text string. Example:
    `client_entity_data = '{ "seq_id": "1234567890", "name": "John Doe", "iat": 1516239022 }'`
    """

    client_user_id: int
    """Custom meta field for storing the Identifier in your system.

    We do not use this field in any way when processing the stream. Example:
    `client_user_id = 1001`
    """

    dvr_duration: int
    """DVR duration in seconds if DVR feature is enabled for the stream.

    So this is duration of how far the user can rewind the live stream.

    `dvr_duration` range is [30...14400].

    Maximum value is 4 hours = 14400 seconds. If you need more, ask the Support Team
    please.
    """

    dvr_enabled: bool
    """Enables DVR for the stream:

    - true – DVR is enabled
    - false – DVR is disabled
    """

    hls_mpegts_endlist_tag: bool
    """
    Add `#EXT-X-ENDLIST` tag within .m3u8 playlist after the last segment of a live
    stream when broadcast is ended.
    """

    html_overlay: bool
    """
    Switch on mode to insert and display real-time HTML overlay widgets on top of
    live streams
    """

    projection: Literal["regular", "vr360", "vr180", "vr360tb"]
    """
    Visualization mode for 360° streams, how the stream is rendered in our web
    player ONLY. If you would like to show video 360° in an external video player,
    then use parameters of that video player.

    Modes:

    - regular – regular “flat” stream
    - vr360 – display stream in 360° mode
    - vr180 – display stream in 180° mode
    - vr360tb – display stream in 3D 360° mode Top-Bottom
    """

    pull: bool
    """Indicates if stream is pulled from external server or not.

    Has two possible values:

    - true – stream is received by PULL method. Use this when need to get stream
      from external server.
    - false – stream is received by PUSH method. Use this when need to send stream
      from end-device to our Streaming Platform, i.e. from your encoder, mobile app
      or OBS Studio.
    """

    quality_set_id: int
    """
    Custom quality set ID for transcoding, if transcoding is required according to
    your conditions. Look at GET /`quality_sets` method
    """

    record_type: Literal["origin", "transcoded"]
    """Method of recording a stream.

    Specifies the source from which the stream will be recorded: original or
    transcoded.

    Types:

    - "origin" – To record RMTP/SRT/etc original clean media source.
    - "transcoded" – To record the output transcoded version of the stream,
      including overlays, texts, logos, etc. additional media layers.
    """

    uri: str
    """When using PULL method, this is the URL to pull a stream from.

    You can specify multiple addresses separated by a space (" "), so you can
    organize a backup plan. In this case, the specified addresses will be selected
    one by one using round robin scheduling. If the first address does not respond,
    then the next one in the list will be automatically requested, returning to the
    first and so on in a circle. Also, if the sucessfully working stream stops
    sending data, then the next one will be selected according to the same scheme.

    After 2 hours of inactivity of your original stream, the system stops PULL
    requests and the stream is deactivated (the "active" field switches to "false").

    Please, note that this field is for PULL only, so is not suitable for PUSH. Look
    at fields "`push_url`" and "`push_url_srt`" from GET method.
    """
