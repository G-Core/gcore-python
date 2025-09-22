# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VideoUpdateParams"]


class VideoUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Video name"""

    auto_transcribe_audio_language: Literal["disable", "auto", "<language_code>"]
    """Automatic creation of subtitles by transcribing the audio track.

    Values:

    - disable – Do not transcribe.
    - auto – Automatically detects the activation of the option based on the
      settings in your account. If generation is activated, then automatic language
      detection while transcribing.
    - \\  – Transcribe from specific language. Can be used to specify the exact
      language spoken in the audio track, or when auto language detection fails.
      Language is set by 3-letter language code according to ISO-639-2
      (bibliographic code). List of languages is available in `audio_language`
      attribute of API POST /streaming/ai/transcribe .

    Example:

    ```
    auto_transcribe_audio_language: "auto"
    auto_transcribe_audio_language: "ger"
    ```

    More details:

    - List of AI tasks – API
      [GET /streaming/ai/tasks](/docs/api-reference/streaming/ai/get-list-of-ai-tasks)
    - Add subtitles to an exist video – API
      [POST /streaming/videos/{`video_id`}/subtitles](/docs/api-reference/streaming/subtitles/add-subtitle).
    """

    auto_translate_subtitles_language: Literal["disable", "default", "<language_codes,>"]
    """Automatic translation of auto-transcribed subtitles to the specified
    language(s).

    Can be used both together with `auto_transcribe_audio_language` option only.

    Use it when you want to make automatic subtitles in languages other than the
    original language in audio.

    Values:

    - disable – Do not translate.
    - default – There are 3 default languages: eng,fre,ger
    - \\  – Explicit language to translate to, or list of languages separated by a
      comma. Look at list of available languages in description of AI ASR task
      creation.

    If several languages are specified for translation, a separate subtitle will be
    generated for each language.

    Example:

    ```
    auto_translate_subtitles_language: default
    auto_translate_subtitles_language: eng,fre,ger
    ```

    Please note that subtitle translation is done separately and after
    transcription. Thus separate AI-tasks are created for translation.
    """

    client_user_id: int
    """Custom field where you can specify user ID in your system"""

    clip_duration_seconds: int
    """
    The length of the trimmed segment to transcode, instead of the entire length of
    the video. Is only used in conjunction with specifying the start of a segment.
    Transcoding duration is a number in seconds.
    """

    clip_start_seconds: int
    """
    If you want to transcode only a trimmed segment of a video instead of entire
    length if the video, then you can provide timecodes of starting point and
    duration of a segment to process. Start encoding from is a number in seconds.
    """

    custom_iframe_url: str
    """Deprecated.

    Custom URL of IFrame for video player to be used in share panel in player. Auto
    generated IFrame URL provided by default
    """

    description: str
    """Video details; not visible to the end-users"""

    directory_id: int
    """ID of the directory where the video should be uploaded. (beta)"""

    origin_http_headers: str
    """Authorization HTTP request header.

    Will be used as credentials to authenticate a request to download a file
    (specified in "`origin_url`" parameter) on an external server.

    Syntax: `Authorization: <auth-scheme> <authorization-parameters>`

    Examples:

    - "`origin_http_headers`": "Authorization: Basic ..."
    - "`origin_http_headers`": "Authorization: Bearer ..."
    - "`origin_http_headers`": "Authorization: APIKey ..." Example of usage when
      downloading a file from Google Drive:

    ```
    POST https://api.gcore.com/streaming/videos

    "video": {
      "name": "IBC 2024 intro.mp4",
      "origin_url": "https://www.googleapis.com/drive/v3/files/...?alt=media",
      "origin_http_headers": "Authorization: Bearer ABC"
    }
    ```
    """

    origin_url: str
    """
    URL to an original file which you want to copy from external storage. If
    specified, system will download the file and will use it as video source for
    transcoding.
    """

    poster: str
    """Poster is your own static image which can be displayed before the video starts.

    After uploading the video, the system will automatically create several
    screenshots (they will be stored in "screenshots" attribute) from which you can
    select an default screenshot. This "poster" field is for uploading your own
    image. Also use attribute "`screenshot_id`" to select poster as a default
    screnshot.

    Attribute accepts single image as base64-encoded string
    [(RFC 2397 – The "data" URL scheme)](https://www.rfc-editor.org/rfc/rfc2397). In
    format: `data:[<mediatype>];base64,<data>`

    MIME-types are image/jpeg, image/webp, and image/png and file sizes up to 1Mb.

    Examples:

    - `data:image/jpeg;base64,/9j/4AA...qf/2Q==`
    - `data:image/png;base64,iVBORw0KGg...ggg==`
    - `data:image/webp;base64,UklGRt.../DgAAAAA`
    """

    priority: int
    """
    Priority allows you to adjust the urgency of processing some videos before
    others in your account, if your algorithm requires it. For example, when there
    are very urgent video and some regular ones that can wait in the queue.

    Value range, integer [-10..10]. -10 is the lowest down-priority, 10 is the
    highest up-priority. Default priority is 0.
    """

    projection: str
    """Deprecated.

    Regulates the video format:

    - **regular** — plays the video as usual
    - **vr360** — plays the video in 360 degree mode
    - **vr180** — plays the video in 180 degree mode
    - **vr360tb** — plays the video in 3D 360 degree mode Top-Bottom.

    Default is regular
    """

    quality_set_id: int
    """
    Custom quality set ID for transcoding, if transcoding is required according to
    your conditions. Look at GET /`quality_sets` method
    """

    remote_poster_url: str
    """
    Poster URL to download from external resource, instead of uploading via "poster"
    attribute.

    It has the same restrictions as "poster" attribute.
    """

    remove_poster: bool
    """Set it to true to remove poster"""

    screenshot_id: int
    """Default screenshot index.

    Specify an ID from the "screenshots" array, so that the URL of the required
    screenshot appears in the "screenshot" attribute as the default screenshot. By
    default 5 static screenshots will be taken from different places in the video
    after transcoding. If the video is short, there may be fewer screenshots.

    Counting from 0. A value of -1 sets the default screenshot to the URL of your
    own image from the "poster" attribute.

    Look at "screenshot" attribute in GET /videos/{`video_id`} for details.
    """

    share_url: str
    """Deprecated.

    Custom URL or iframe displayed in the link field when a user clicks on a sharing
    button in player. If empty, the link field and social network sharing is
    disabled
    """

    source_bitrate_limit: bool
    """
    The option allows you to set the video transcoding rule so that the output
    bitrate in ABR ladder is not exceeding the bitrate of the original video.

    This option is for advanced users only.

    By default `source_bitrate_limit: true` this option allows you to have the
    output bitrate not more than in the original video, thus to transcode video
    faster and to deliver it to end-viewers faster as well. At the same time, the
    quality will be similar to the original.

    If for some reason you need more byte-space in the output quality when encoding,
    you can set this option to `source_bitrate_limit: false`. Then, when
    transcoding, the quality ceiling will be raised from the bitrate of the original
    video to the maximum possible limit specified in our the Product Documentation.
    For example, this may be needed when:

    - to improve the visual quality parameters using PSNR, SSIM, VMAF metrics,
    - to improve the picture quality on dynamic scenes,
    - etc.

    The option is applied only at the video creation stage and cannot be changed
    later. If you want to re-transcode the video using new value, then you need to
    create and upload a new video only.
    """
