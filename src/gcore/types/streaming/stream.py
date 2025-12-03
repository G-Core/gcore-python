# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .streams.overlay import Overlay

__all__ = ["Stream"]


class Stream(BaseModel):
    name: str
    """Stream name.

    Often used as a human-readable name for the stream, but can contain any text you
    wish. The values are not unique and may be repeated.

    Examples:

    - Conference in July
    - Stream #10003
    - Open-Air Camera #31 Backstage
    - 480fd499-2de2-4988-bc1a-a4eebe9818ee
    """

    id: Optional[int] = None
    """Stream ID"""

    active: Optional[bool] = None
    """Stream switch between on and off.

    This is not an indicator of the status "stream is receiving and it is LIVE", but
    rather an on/off switch.

    When stream is switched off, there is no way to process it: PULL is deactivated
    and PUSH will return an error.

    - true – stream can be processed
    - false – stream is off, and cannot be processed
    """

    auto_record: Optional[bool] = None
    """Enables autotomatic recording of the stream when it started.

    So you don't need to call recording manually.

    Result of recording is automatically added to video hosting. For details see the
    /streams/`start_recording` method and in knowledge base

    Values:

    - true – auto recording is enabled
    - false – auto recording is disabled
    """

    backup_live: Optional[bool] = None
    """
    State of receiving and transcoding master stream from source by backup server if
    you pushing stream to "`backup_push_url`" or "`backup_push_url_srt`".

    Displays the backup server status of PUSH method only. For PULL a "live" field
    is always used, even when origin servers are switched using round robin
    scheduling (look "uri" field for details).
    """

    backup_push_url: Optional[str] = None
    """URL to PUSH master stream to our backup server using RTMP/S protocols.

    Servers for the main and backup streams are distributed geographically.

    Mainly sending one stream to main server is enough. But if you need a backup
    stream, then this is the field to PUSH it.

    To use RTMPS just manually change the protocol name from "rtmp://" to
    "rtmps://".

    The backup logs are as follows: In PUSH mode, you initiate sending a stream from
    your machine. If your stream stops or breaks for some reason and it stops coming
    to the main server, then after 3-10 seconds of waiting the stream will turn off
    or the backup one will be automatically turned on, if you are pushing it too.
    """

    backup_push_url_srt: Optional[str] = None
    """
    URL to PUSH master stream to our backup server using SRT protocol with the same
    logic of backup-streams
    """

    broadcast_ids: Optional[List[int]] = None
    """IDs of broadcasts which will include this stream"""

    cdn_id: Optional[int] = None
    """
    ID of custom CDN resource from which the content will be delivered (only if you
    know what you do)
    """

    client_entity_data: Optional[str] = None
    """
    Custom meta field designed to store your own extra information about a video
    entity: video source, video id, parameters, etc. We do not use this field in any
    way when processing the stream. You can store any data in any format (string,
    json, etc), saved as a text string. Example:
    `client_entity_data = '{ "seq_id": "1234567890", "name": "John Doe", "iat": 1516239022 }'`
    """

    client_user_id: Optional[int] = None
    """Custom meta field for storing the Identifier in your system.

    We do not use this field in any way when processing the stream. Example:
    `client_user_id = 1001`
    """

    created_at: Optional[str] = None
    """Datetime of creation in ISO 8601"""

    dash_url: Optional[str] = None
    """MPEG-DASH output.

    URL for transcoded result stream in MPEG-DASH format, with .mpd link.

    Low Latency support: YES.

    This is CMAF-based MPEG-DASH stream. Encoder and packager dynamically assemble
    the video stream with fMP4 fragments. Chunks have ±2-4 seconds duration
    depending on the settings. All chunks for DASH are transferred through CDN using
    chunk transfer technology, which allows to use all the advantages of low latency
    delivery of DASH.

    - by default low latency is ±4 sec, because it's stable for almost all last-mile
      use cases.
    - and its possible to enable ±2 sec for DASH, just ask our Support Team.

    Read more information in the article "How Low Latency streaming works" in the
    Knowledge Base.
    """

    dvr_duration: Optional[int] = None
    """DVR duration in seconds if DVR feature is enabled for the stream.

    So this is duration of how far the user can rewind the live stream.

    `dvr_duration` range is [30...14400].

    Maximum value is 4 hours = 14400 seconds. If you need more, ask the Support Team
    please.
    """

    dvr_enabled: Optional[bool] = None
    """Enables DVR for the stream:

    - true – DVR is enabled
    - false – DVR is disabled
    """

    finished_at_primary: Optional[str] = None
    """Time when the stream ended for the last time. Datetime in ISO 8601.

    After restarting the stream, this value is not reset to "null", and the time of
    the last/previous end is always displayed here. That is, when the start time is
    greater than the end time, it means the current session is still ongoing and the
    stream has not ended yet.

    If you want to see all information about acitivity of the stream, you can get it
    from another method /streaming/statistics/ffprobe. This method shows aggregated
    activity parameters during a time, when stream was alive and transcoded. Also
    you can create graphs to see the activity. For example
    /streaming/statistics/ffprobe?interval=6000&`date_from`=2023-10-01&`date_to`=2023-10-11&`stream_id`=12345
    """

    frame_rate: Optional[float] = None
    """Current FPS of the original stream, if stream is transcoding"""

    hls_cmaf_url: Optional[str] = None
    """HLS output.

    URL for transcoded result of stream in HLS CMAF format, with .m3u8 link.
    Recommended for use for all HLS streams.

    Low Latency support: YES.

    This is CMAF-based HLS stream. Encoder and packager dynamically assemble the
    video stream with fMP4 fragments. Chunks have ±2-4 seconds duration depending on
    the settings. All chunks for LL-HLS are transferred through CDN via dividing
    into parts (small segments `#EXT-X-PART` of 0.5-1.0 sec duration), which allows
    to use all the advantages of low latency delivery of LL-HLS.

    - by default low latency is ±5 sec, because it's stable for almost all last-mile
      use cases.
    - and its possible to enable ±3 sec for LL-HLS, just ask our Support Team.

    It is also possible to use modifier-attributes, which are described in the
    "`hls_mpegts_url`" field above. If you need to get MPEG-TS (.ts) chunks, look at
    the attribute "`hls_mpegts_url`".

    Read more information in the article "How Low Latency streaming works" in the
    Knowledge Base.
    """

    hls_mpegts_endlist_tag: Optional[bool] = None
    """
    Add `#EXT-X-ENDLIST` tag within .m3u8 playlist after the last segment of a live
    stream when broadcast is ended.
    """

    hls_mpegts_url: Optional[str] = None
    """HLS output for legacy devices.

    URL for transcoded result of stream in HLS MPEG-TS (.ts) format, with .m3u8
    link.

    Low Latency support: NO.

    Some legacy devices or software may require MPEG-TS (.ts) segments as a format
    for streaming, so we provide this options keeping backward compatibility with
    any of your existing workflows. For other cases it's better to use
    "`hls_cmaf_url`" instead.

    You can use this legacy HLSv6 format based on MPEG-TS segmenter in parallel with
    main HLS CMAF. Both formats are sharing same segments size, manifest length
    (DVR), etc.

    It is also possible to use additional modifier-attributes:

    - ?`get_duration_sec`=true – Adds the real segment duration in seconds to chunk
      requests. A chunk duration will be automatically added to a chunk request
      string with the "`duration_sec`" attribute. The value is an integer for a
      length multiple of whole seconds, or a fractional number separated by a dot
      for chunks that are not multiples of seconds. This attribute allows you to
      determine duration in seconds at the level of analyzing the logs of CDN
      requests and compare it with file size (so to use it in your analytics).

    Such modifier attributes are applied manually and added to the link obtained
    from this field. I.e. `<hls_url>?get_duration_sec=true`

    Example:
    `https://demo.gvideo.io/mpegts/2675_19146/master_mpegts.m3u8?get_duration_sec=true`

    ```
    #EXTM3U
    #EXT-X-VERSION:6
    #EXT-X-TARGETDURATION:2
    ...
    #EXTINF:2.000000,
    #EXT-X-PROGRAM-DATE-TIME:2025-08-14T08:15:00
    seg1.ts?duration_sec=2
    ...
    ```
    """

    html_overlay: Optional[bool] = None
    """
    Switch on mode to insert and display real-time HTML overlay widgets on top of
    live streams
    """

    html_overlays: Optional[List[Overlay]] = None
    """Array of HTML overlay widgets"""

    iframe_url: Optional[str] = None
    """A URL to a built-in HTML web player with the stream inside.

    It can be inserted into an iframe on your website and the video will
    automatically play in all browsers.

    Please, remember that transcoded streams from "`hls_cmaf_url`" with .m3u8 at the
    end, and from "`dash_url`" with .mpd at the end are to be played inside video
    players only. For example: AVplayer on iOS, Exoplayer on Android, HTML web
    player in browser, etc. General bowsers like Chrome, Firefox, etc cannot play
    transcoded streams with .m3u8 and .mpd at the end. The only exception is Safari,
    which can only play Apple's HLS .m3u8 format with limits.

    That's why you may need to use this HTML web player. Please, look Knowledge Base
    for details.

    Example of usage on a web page:

    <iframe width="560" height="315" src="https://player.gvideo.co/streams/2675_201693" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """

    live: Optional[bool] = None
    """State of receiving and transcoding master stream from source by main server"""

    projection: Optional[Literal["regular", "vr360", "vr180", "vr360tb"]] = None
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

    pull: Optional[bool] = None
    """Indicates if stream is pulled from external server or not.

    Has two possible values:

    - true – stream is received by PULL method. Use this when need to get stream
      from external server.
    - false – stream is received by PUSH method. Use this when need to send stream
      from end-device to our Streaming Platform, i.e. from your encoder, mobile app
      or OBS Studio.
    """

    push_url: Optional[str] = None
    """URL to PUSH master stream to our main server using RTMP and RTMPS protocols.

    To use RTMPS just manually change the protocol name from "rtmp://" to
    "rtmps://".

    Use only 1 protocol of sending a master stream: eitheronly RTMP/S (`push_url`),
    or only SRT (`push_url_srt`).

    If you see an error like "invalid SSL certificate" try the following:

    - Make sure the push URL is correct, and it contains "rtmps://".
    - If the URL looks correct but you still get an SSL error, try specifying the
      port 443 in the URL. Here’s an example:
      rtmps://vp-push.domain.com:443/in/stream?key.
    - If you're still having trouble, then your encoder may not support RTMPS.
      Double-check the documentation for your encoder.

    Please note that 1 connection and 1 protocol can be used at a single moment in
    time per unique stream key input. Trying to send 2+ connection requests into the
    single `push_url`, or 2+ protocols at once will not lead to a result.

    For example, transcoding process will fail if:

    - you are pushing primary and backup RTMP to the same single `push_url`
      simultaneously
    - you are pushing RTMP to `push_url` and SRT to `push_url_srt` simultaneously

    For advanced customers only: For your complexly distributed broadcast systems,
    it is also possible to additionally output an array of multi-regional ingestion
    points for manual selection from them. To activate this mode, contact your
    manager or the Support Team to activate the "`multi_region_push_urls`" attibute.
    But if you clearly don’t understand why you need this, then it’s best to use the
    default single URL in the "`push_url`" attribute.
    """

    push_url_srt: Optional[str] = None
    """URL to PUSH master stream to our main server using SRT protocol.

    Use only 1 protocol of sending a master stream: eitheronly RTMP/S (`push_url`),
    or only SRT (`push_url_srt`).

    **Setup SRT latency on your sender side**

    SRT is designed as a low-latency transport protocol, but real networks are not
    always stable and in some cases the end-to-end path from the venue to the ingest
    point can be long. For this reason, it is important to configure the latency
    parameter carefully to match the actual network conditions.

    Small latency values may lead to packet loss when jitter or retransmissions
    occur, while very large values introduce unnecessary end-to-end delay.

    _Incorrect or low default value is one of the most common reasons for packet
    loss, frames loss, and bad picture._

    We therefore recommend setting latency manually rather than relying on the
    default, to ensure the buffer is correctly sized for your environment. A
    practical range is 400–2000 ms, with the exact value chosen based on RTT,
    jitter, and expected packet loss.

    Be sure to check and test SRT settings on your sender side. The default values
    do not take into account your specific scenarios and do not work well. If
    necessary, ask us and we will help you.

    Please note that 1 connection and 1 protocol can be used at a single moment in
    time per unique stream key input. Trying to send 2+ connection requests into the
    single `push_url_srt`, or 2+ protocols at once will not lead to a result.

    For example, transcoding process will fail if:

    - you are pushing primary and backup SRT to the same single `push_url_srt`
      simultaneously
    - you are pushing RTMP to `push_url` and SRT to `push_url_srt` simultaneously

    See more information and best practices about SRT protocol in the Product
    Documentation.
    """

    push_url_whip: Optional[str] = None
    """URL to PUSH WebRTC stream to our server using WHIP protocol.

    **WebRTC WHIP to LL-HLS and DASH**

    Video Streaming supports WebRTC HTTP Ingest Protocol (WHIP), and WebRTC to
    HLS/DASH converter. As a result you can stream from web broswers natively.

    **WebRTC WHIP server**

    We have dedicated WebRTC WHIP servers in our infrastructure. WebRTC WHIP server
    organizes both signaling and receives video data. Signaling is a term to
    describe communication between WebRTC endpoints, needed to initiate and maintain
    a session. WHIP is an open specification for a simple signaling protocol for
    starting WebRTC sessions in an outgoing direction, (i.e., streaming from your
    device).

    There is the primary link only for WHIP, so no backup link.

    **WebRTC stream encoding parameters**

    At least one video and audio track both must be present in the stream:

    - Video must be encoded with H.264.
    - Audio must be encoded with OPUS.

    Note. Specifically for WebRTC mode a method of constant transcoding with an
    initial given resolution is used. This means that if WebRTC in the end-user's
    browser decides to reduce the quality or resolution of the master stream (to let
    say 360p) due to restrictions on the end-user's device (network conditions, CPU
    consumption, etc.), the transcoder will still continue to transcode the reduced
    stream to the initial resolution (let say 1080p ABR). When the restrictions on
    the end-user's device are removed, quiality will improve again.

    **WebRTC WHIP Client**

    We provide a convenient WebRTC WHIP library for working in browsers. You can use
    our library, or any other you prefer. Simple example of usage is here:
    https://stackblitz.com/edit/stackblitz-starters-j2r9ar?file=index.html

    Also try to use the feature in UI of the Customer Portal. In the Streaming
    section inside the settings of a specific live stream, a new section "Quick
    start in browser" has been added.

    Please note that 1 connection and 1 protocol can be used at a single moment in
    time per unique stream key input. Trying to send 2+ connection requests into the
    single `push_url_whip`, or 2+ protocols at once will not lead to a result.

    For example, transcoding process will fail if:

    - you are pushing primary and backup WHIP to the same single `push_url_whip`
      simultaneously
    - you are pushing WHIP to `push_url_whip` and RTMP to `push_url` simultaneously

    More information in the Product Documentation on the website.
    """

    quality_set_id: Optional[int] = None
    """
    Custom quality set ID for transcoding, if transcoding is required according to
    your conditions. Look at GET /`quality_sets` method
    """

    record_type: Optional[Literal["origin", "transcoded"]] = None
    """Method of recording a stream.

    Specifies the source from which the stream will be recorded: original or
    transcoded.

    Types:

    - "origin" – To record RMTP/SRT/etc original clean media source.
    - "transcoded" – To record the output transcoded version of the stream,
      including overlays, texts, logos, etc. additional media layers.
    """

    recording_duration: Optional[float] = None
    """Duration of current recording in seconds if recording is enabled for the stream"""

    screenshot: Optional[str] = None
    """
    An instant screenshot taken from a live stream, and available as a static JPEG
    image. Resolution 1080 pixels wide, or less if the original stream has a lower
    resolution.

    Screenshot is taken every 10 seconds while the stream is live. This field
    contains a link to the last screenshot created by the system. Screenshot history
    is not stored, so if you need a series of screenshots over time, then download
    them.
    """

    started_at_backup: Optional[str] = None
    """Time of the last session when backup server started receiving the stream.

    Datetime in ISO 8601
    """

    started_at_primary: Optional[str] = None
    """Time of the last session when main server started receiving the stream.

    Datetime in ISO 8601.

    This means that if the stream was started 1 time, then here will be the time it
    was started. If the stream was started several times, or restarted on your side,
    then only the time of the last session is displayed here.
    """

    stream_source_type: Optional[Literal["rtmp", "srt", "webrtc", "https"]] = None
    """
    For the current transcoding, this specifies the source protocol: RTMP, SRT,
    WebRTC, or HTTPS. This does not specify which source is used primary or backup,
    only the source protocol type. If transcoding is inactive, the value will be
    null.
    """

    transcoded_qualities: Optional[List[str]] = None
    """Array of qualities to which live stream is transcoded"""

    transcoding_speed: Optional[float] = None
    """Speed of transcoding the stream.

    Mainly it must be 1.0 for real-time processing. May be less than 1.0 if your
    stream has problems in delivery due to your local internet provider's
    conditions, or the stream does not meet stream inbound requirements. See
    Knowledge Base for details.
    """

    uri: Optional[str] = None
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

    video_height: Optional[float] = None
    """Current height of frame of the original stream, if stream is transcoding"""

    video_width: Optional[float] = None
    """Current width of frame of the original stream, if stream is transcoding"""
