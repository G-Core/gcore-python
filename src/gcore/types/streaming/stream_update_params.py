# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
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
    """Enables automatic recording of the stream when it started.

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

    hls_mpegts_cc_tag: bool
    """Show closed captions (CEA-608) in the HLS MPEG-TS output.

    Values:

    - true – the HLS MPEG-TS master playlist (`master_mpegts.m3u8`) advertises the
      captions track
    - false – the playlist is unchanged

    **Input.** Your source must carry CEA-608 captions on channel CC1, embedded in
    the H.264 video (SEI user data), for both RTMP/RTMPS and SRT push. The platform
    does not create captions and cannot detect them in the source. If the stream has
    no captions, players will show a caption track with no text, so enable this only
    for sources with captions. Other caption channels (CC2–CC4) and CEA-708 services
    are not advertised.

    **Output.** HLS MPEG-TS only, in the `hls_mpegts_url` master playlist. DASH and
    HLS CMAF outputs are not changed. The master playlist gets one captions entry,
    and every video variant is linked to it:

    ```text
    #EXT-X-MEDIA:TYPE=CLOSED-CAPTIONS,GROUP-ID="cc",NAME="CC1",LANGUAGE="en",INSTREAM-ID="CC1",AUTOSELECT=YES
    #EXT-X-STREAM-INF:BANDWIDTH=985600,RESOLUTION=688x468,CODECS="avc1.64001e,mp4a.40.2",CLOSED-CAPTIONS="cc"
    ```

    The track name `CC1` and language `en` are fixed and cannot be changed.

    **How to turn on and check:**

    1. Set `hls_mpegts_cc_tag` to `true` when creating the stream, or update an
       existing stream.
    2. Start (or restart) the push. The setting is applied when the stream starts,
       so a stream that is already live will not change until you restart it.
    3. Open the `hls_mpegts_url` in a player with closed captions support, for
       example Safari, or the hls.js demo player. Choose the "CC1" track in the
       captions menu.

    **FFmpeg example.** Pass the captions through when you re-encode the video.
    Option `-a53cc 1` keeps CEA-608 data in the H.264 stream:

    ```text
    ffmpeg -re -i input_with_captions.ts -c:v libx264 -pix_fmt yuv420p -profile:v main -g 60 -a53cc 1 -c:a aac -b:a 128k -f flv "rtmp://<push_url>"
    ```

    You can check that your file or stream has captions with
    `ccextractor input_with_captions.ts`.
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

    - "origin" – To record RTMP/SRT/etc original clean media source.
    - "transcoded" – To record the output transcoded version of the stream,
      including overlays, texts, logos, etc. additional media layers.
    """

    srt_passphrase: Optional[str]
    """Passphrase for encrypted SRT PUSH ingest.

    If set, the sender must use the same passphrase when pushing to primary
    `push_url_srt` or backup `backup_push_url_srt` ingest points.

    The passphrase must be 10–80 characters long and may contain only printable
    ASCII characters: English letters, digits, and punctuation. Whitespace and
    non-ASCII characters are not allowed.

    To clear the passphrase, update the stream with `"srt_passphrase": null`.
    """

    uri: str
    """When using PULL method, this is the URL to pull a stream from.

    You can specify multiple addresses separated by a space (" "), so you can
    organize a backup plan. In this case, the specified addresses will be selected
    one by one using round robin scheduling. If the first address does not respond,
    then the next one in the list will be automatically requested, returning to the
    first and so on in a circle. Also, if the successfully working stream stops
    sending data, then the next one will be selected according to the same scheme.

    After 2 hours of inactivity of your original stream, the system stops PULL
    requests and the stream is deactivated (the "active" field switches to "false").

    Please, note that this field is for PULL only, so is not suitable for PUSH. Look
    at fields "push_url" and "push_url_srt" from GET method.
    """
