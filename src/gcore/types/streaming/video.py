# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Video", "ConvertedVideo"]


class ConvertedVideo(BaseModel):
    id: Optional[int] = None
    """ID of the converted file of the specific quality"""

    error: Optional[str] = None
    """Video processing error text in this quality"""

    height: Optional[int] = None
    """Height in pixels of the converted video file of the specific quality.

    Can be `null` for audio-only files.
    """

    mp4_url: Optional[str] = None
    """
    A URL to a rendition file of the specified quality in MP4 format for
    downloading.

    **Download methods**

    For each converted video, additional download endpoints are available under
    `converted_videos`/`mp4_urls`. An MP4 download enpoints:

    1. `/videos/{client_id}_{slug}/{filename}.mp4`
    2. `/videos/{client_id}_{slug}/{filename}.mp4/download`
    3. `/videos/{client_id}_{slug}/{filename}.mp4/download={custom_filename}`

    The first option returns the file as is. Response will be:

    ```
    GET .mp4
    ...
    content-type: video/mp4
    ```

    The second option with `/download` will respond with HTTP response header that
    directly tells browsers to download the file instead of playing it in the
    browser:

    ```
    GET .mp4/download
    ...
    content-type: video/mp4
    content-disposition: attachment
    access-control-expose-headers: Content-Disposition
    ```

    The third option allows you to set a custom name for the file being downloaded.
    You can optionally specify a custom filename (just name excluding the .mp4
    extension) using the download= query.

    Filename constraints:

    - Length: 1-255 characters
    - Must NOT include the .mp4 extension (it is added automatically)
    - Allowed characters: a-z, A-Z, 0-9, \\__(underscore), -(dash), .(dot)
    - First character cannot be .(dot)
    - Example valid filenames: `holiday2025`, `_backup.final`, `clip-v1.2`

    ```
    GET .mp4/download={custom_filename}
    ...
    content-type: video/mp4
    content-disposition: attachment; filename="{custom_filename}.mp4"
    access-control-expose-headers: Content-Disposition
    ```

    Examples:

    - MP4:
      `https://demo-public.gvideo.io/videos/2675_1OFgHZ1FWZNNvx1A/qid3567v1_h264_4050_1080.mp4/download`
    - MP4 with custom download filename:
      `https://demo-public.gvideo.io/videos/2675_1OFgHZ1FWZNNvx1A/qid3567v1_h264_4050_1080.mp4/download=highlights_v1.1_2025-05-30`

    **Default MP4 file name structure**

    Link to the file {filename} contains information about the encoding method using
    format: `<quality_version>_<codec>_<bitrate>_<height>.mp4`

    - `<quality_version>` – Internal quality identifier and file version. Please do
      not use it, can be changed at any time without any notice.
    - `<codec>` – Codec name that was used to encode the video, or audio codec if it
      is an audio-only file.
    - `<bitrate>` – Encoding bitrate in Kbps.
    - `<height>` – Video height, or word "audio" if it is an audio-only file.

    Note that this link format has been applied since 14.08.2024. If the video
    entity was uploaded earlier, links may have old simplified format.

    Example: `/videos/{client_id}_{slug}/qid3567v1_h264_4050_1080.mp4`

    **Dynamic speed limiting** This mode sets different limits for different users
    or for different types of content. The speed is adjusted based on requests with
    the “speed” and “buffer” arguments.

    Example: `?speed=50k&buffer=500k`

    Read more in Product Documentation in CDN section "Network limits".

    **Secure token authentication for MP4 (updated)**

    Access to MP4 download links only can be protected using advanced secure tokens
    passed as query parameters.

    Token generation uses the entire MP4 path, which ensures the token only grants
    access to a specific quality/version of the video. This prevents unintended
    access to other bitrate versions of an ABR stream.

    Token Query Parameters:

    - token: The generated hash
    - expires: Expiration timestamp
    - speed: (optional) Speed limit in bytes/sec, or empty string
    - buffer: (optional) Buffer size in bytes, or empty string

    Optional (for IP-bound tokens):

    - ip: The user’s IP address Example:
      `?md5=QX39c77lbQKvYgMMAvpyMQ&expires=1743167062`

    Read more in Product Documentation in Streaming section "Protected temporarily
    link".
    """

    name: Optional[str] = None
    """Specific quality name"""

    progress: Optional[int] = None
    """Status of transcoding into the specific quality, from 0 to 100"""

    size: Optional[int] = None
    """Size in bytes of the converted file of the specific quality.

    Can be `null` until transcoding is fully completed.
    """

    status: Optional[Literal["processing", "complete", "error"]] = None
    """Status of transcoding:

    - processing – video is being transcoded to this quality,
    - complete – quality is fully processed,
    - error – quality processing error, see parameter "error".
    """

    width: Optional[int] = None
    """Width in pixels of the converted video file of the specified quality.

    Can be `null` for audio files.
    """


class Video(BaseModel):
    id: Optional[int] = None
    """Video ID"""

    ad_id: Optional[int] = None
    """ID of ad that should be shown.

    If empty the default ad is show. If there is no default ad, no ad is shownю
    """

    cdn_views: Optional[int] = None
    """Total number of video views.

    It is calculated based on the analysis of all views, no matter in which player.
    """

    client_id: Optional[int] = None
    """Client ID"""

    client_user_id: Optional[int] = None
    """Custom meta field for storing the Identifier in your system.

    We do not use this field in any way when processing the stream. Example:
    `client_user_id = 1001`
    """

    converted_videos: Optional[List[ConvertedVideo]] = None
    """Array of data about each transcoded quality"""

    custom_iframe_url: Optional[str] = None
    """Custom URL of Iframe for video player to be used in share panel in player.

    Auto generated Iframe URL provided by default.
    """

    dash_url: Optional[str] = None
    """
    A URL to a master playlist MPEG-DASH (master.mpd) with CMAF or WebM based
    chunks.

    Chunk type will be selected automatically for each quality:

    - CMAF for H264 and H265 codecs.
    - WebM for AV1 codec.

    This URL is a link to the main manifest. But you can also manually specify
    suffix-options that will allow you to change the manifest to your request:

    ```
    /videos/{client_id}_{slug}/master[-min-N][-max-N][-(h264|hevc|av1)].mpd
    ```

    List of suffix-options:

    - [-min-N] – ABR soft limitation of qualities from below.
    - [-max-N] – ABR soft limitation of qualities from above.
    - [-(h264|hevc|av1) – Video codec soft limitation. Applicable if the video was
      transcoded into multiple codecs H264, H265 and AV1 at once, but you want to
      return just 1 video codec in a manifest. Read the Product Documentation for
      details.

    Read more what is ABR soft-limiting in the "`hls_url`" field above.

    Caution. Solely master.mpd is officially documented and intended for your use.
    Any additional internal manifests, sub-manifests, parameters, chunk names, file
    extensions, and related components are internal infrastructure entities. These
    may undergo modifications without prior notice, in any manner or form. It is
    strongly advised not to store them in your database or cache them on your end.
    """

    description: Optional[str] = None
    """Additional text field for video description"""

    duration: Optional[int] = None
    """Video duration in milliseconds.

    May differ from "`origin_video_duration`" value if the video was uploaded with
    clipping through the parameters "`clip_start_seconds`" and
    "`clip_duration_seconds`"
    """

    error: Optional[str] = None
    """Video processing error text will be saved here if "status: error" """

    hls_cmaf_url: Optional[str] = None
    """A URL to a master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks.

    Chunks are in fMP4 container. It's a code-agnostic container, which allows to
    use any like H264, H265, AV1, etc.

    It is possible to use the same suffix-options as described in the "`hls_url`"
    attribute.

    Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
    and intended for your use. Any additional internal manifests, sub-manifests,
    parameters, chunk names, file extensions, and related components are internal
    infrastructure entities. These may undergo modifications without prior notice,
    in any manner or form. It is strongly advised not to store them in your database
    or cache them on your end.
    """

    hls_url: Optional[str] = None
    """
    A URL to a master playlist HLS (master.m3u8). Chunk type will be selected
    automatically:

    - TS if your video was encoded to H264 only.
    - CMAF if your video was encoded additionally to H265 and/or AV1 codecs (as
      Apple does not support these codecs over MPEG TS, and they are not
      standardized in TS-container).

    You can also manually specify suffix-options that will allow you to change the
    manifest to your request:

    ```
    /videos/{client_id}_{video_slug}/master[-cmaf][-min-N][-max-N][-img][-(h264|hevc|av1)].m3u8
    ```

    List of suffix-options:

    - [-cmaf] – getting HLS CMAF version of the manifest. Look at the `hls_cmaf_url`
      field.
    - [-min-N] – ABR soft limitation of qualities from below.
    - [-max-N] – ABR soft limitation of qualities from above.
    - [-img] – Roku trick play: to add tiles directly into .m3u8 manifest. Read the
      Product Documentation for details.
    - [-(h264|hevc|av1) – Video codec soft limitation. Applicable if the video was
      transcoded into multiple codecs H264, H265 and AV1 at once, but you want to
      return just 1 video codec in a manifest. Read the Product Documentation for
      details.

    ABR soft-limiting: Soft limitation of the list of qualities allows you to return
    not the entire list of transcoded qualities for a video, but only those you
    need. For example, the video is available in 7 qualities from 360p to 4K, but
    you want to return not more than 480p only due to the conditions of distribution
    of content to a specific end-user (i.e. free account): ABR soft-limiting
    examples:

    - To a generic `.../master.m3u8` manifest
    - Add a suffix-option to limit quality `.../master-max-480.m3u8`
    - Add a suffix-option to limit quality and codec
      `.../master-min-320-max-320-h264.m3u8` For more details look at the Product
      Documentation.

    Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
    and intended for your use. Any additional internal manifests, sub-manifests,
    parameters, chunk names, file extensions, and related components are internal
    infrastructure entities. These may undergo modifications without prior notice,
    in any manner or form. It is strongly advised not to store them in your database
    or cache them on your end.
    """

    iframe_url: Optional[str] = None
    """A URL to a built-in HTML video player with the video inside.

    It can be inserted into an iframe on your website and the video will
    automatically play in all browsers.

    The player can be opened or shared via this direct link. Also the video player
    can be integrated into your web pages using the Iframe tag.

    Example of usage on a web page:

    <iframe width="100%" height="100%" src="https://player.gvideo.co/videos/2675_FnlHXwA16ZMxmUr" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


    There are some link modificators you can specify and add manually:

    - ?`no_low_latency` – player is forced to use non-low-latency streams HLS
      MPEG-TS, instead of MPEG-DASH CMAF or HLS/LL-HLS CMAF.
    - ?t=(integer) – time to start playback from specified point in the video.
      Applicable for VOD only.
    - ?`sub_lang`=(language) – force subtitles to specific language (2 letters ISO
      639 code of a language).
    - Read more in the Product Documentation.
    """

    name: Optional[str] = None
    """Title of the video.

    Often used as a human-readable name of the video, but can contain any text you
    wish. The values are not unique and may be repeated. Examples:

    - Educational training 2024-03-29
    - Series X S3E14, The empire strikes back
    - 480fd499-2de2-4988-bc1a-a4eebe9818ee
    """

    origin_size: Optional[int] = None
    """Size of original file"""

    origin_url: Optional[str] = None
    """URL to an original file from which the information for transcoding was taken.

    May contain a link for scenarios:

    - If the video was downloaded from another origin
    - If the video is a recording of a live stream
    - Otherwise it is "null"

    **Copy from another server** URL to an original file that was downloaded. Look
    at method "Copy from another server" in POST /videos. **Recording of an original
    live stream**

    URL to the original non-transcoded stream recording with original quality, saved
    in MP4 format. File is created immediately after the completion of the stream
    recording. The stream from which the recording was made is reflected in
    "`stream_id`" field.

    Can be used for internal operations when a recording needs to be received faster
    than the transcoded versions are ready. But this version is not intended for
    public distribution. Views and downloads occur in the usual way, like viewing an
    MP4 rendition.

    The MP4 file becomes available for downloading when the video entity "status"
    changes from "new" to "pending". The file is stored for 7 days, after which it
    will be automatically deleted.

    Format of URL is `/videos/<cid>_<slug>/origin_<bitrate>_<height>.mp4` Where:

    - `<bitrate>` – Encoding bitrate in Kbps.
    - `<height>` – Video height.

    This is a premium feature, available only upon request through your manager or
    support team.
    """

    origin_video_duration: Optional[int] = None
    """Original video duration in milliseconds"""

    poster: Optional[str] = None
    """
    Poster is your own static image which can be displayed before the video begins
    playing. This is often a frame of the video or a custom title screen.

    Field contains a link to your own uploaded image.

    Also look at "screenshot" attribute.
    """

    poster_thumb: Optional[str] = None
    """Field contains a link to minimized poster image.

    Original "poster" image is proportionally scaled to a size of 200 pixels in
    height.
    """

    projection: Optional[str] = None
    """Regulates the video format:

    - **regular** — plays the video as usual
    - **vr360** — plays the video in 360 degree mode
    - **vr180** — plays the video in 180 degree mode
    - **vr360tb** — plays the video in 3D 360 degree mode Top-Bottom.

    Default is regular
    """

    recording_started_at: Optional[str] = None
    """
    If the video was saved from a stream, then start time of the stream recording is
    saved here. Format is date time in ISO 8601
    """

    screenshot: Optional[str] = None
    """A URL to the default screenshot is here.

    The image is selected from an array of all screenshots based on the
    “`screenshot_id`” attribute. If you use your own "poster", the link to it will
    be here too.

    Our video player uses this field to display the static image before the video
    starts playing. As soon as the user hits "play" the image will go away. If you
    use your own external video player, then you can use the value of this field to
    set the poster/thumbnail in your player.

    Example:

    - `video_js`.poster: `api.screenshot`
    - clappr.poster: `api.screenshot`
    """

    screenshot_id: Optional[int] = None
    """ID of auto generated screenshots to be used for default screenshot.

    Counting from 0. A value of -1 sets the "screenshot" attribute to the URL of
    your own image from the "poster" attribute.
    """

    screenshots: Optional[List[str]] = None
    """Array of auto generated screenshots from the video.

    By default 5 static screenshots are taken from different places in the video. If
    the video is short, there may be fewer screenshots.

    Screenshots are created automatically, so they may contain not very good frames
    from the video. To use your own image look at "poster" attribute.
    """

    share_url: Optional[str] = None
    """
    Custom URL or iframe displayed in the link field when a user clicks on a sharing
    button in player. If empty, the link field and social network sharing is
    disabled
    """

    slug: Optional[str] = None
    """
    A unique alphanumeric identifier used in public URLs to retrieve and view the
    video. It is unique for each video, generated randomly and set automatically by
    the system.

    Format of usage in URL is _.../videos/{`client_id`}\\__{slug}/..._

    Example:

    - Player: /videos/`12345_neAq1bYZ2`
    - Manifest: /videos/`12345_neAq1bYZ2`/master.m3u8
    - Rendition: /videos/`12345_neAq1bYZ2`/`qid90v1_720`.mp4
    """

    sprite: Optional[str] = None
    """Link to picture with video storyboard.

    Image in JPG format. The picture is a set of rectangles with frames from the
    video. Typically storyboard is used to show preview images when hovering the
    video's timeline.
    """

    sprite_vtt: Optional[str] = None
    """Storyboard in VTT format.

    This format implies an explicit indication of the timing and frame area from a
    large sprite image.
    """

    status: Optional[Literal["empty", "pending", "viewable", "ready", "error"]] = None
    """Video processing status:

    - empty – initial status, when video-entity is created, but video-file has not
      yet been fully uploaded (TUS uploading, or downloading from an origin is not
      finished yet)
    - pending – video is in queue to be processed
    - viewable – video has at least 1 quality and can already be viewed via a link,
      but not all qualities are ready yet
    - ready – video is completely ready, available for viewing with all qualities
    - error – error while processing a video, look at "error" field
    """

    stream_id: Optional[int] = None
    """If the video was saved from a stream, then ID of that stream is saved here"""

    views: Optional[int] = None
    """
    Number of video views through the built-in HTML video player of the Streaming
    Platform only. This attribute does not count views from other external players
    and native OS players, so here may be less number of views than in
    "`cdn_views`".
    """
