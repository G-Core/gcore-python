# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .subtitles import (
    SubtitlesResource,
    AsyncSubtitlesResource,
    SubtitlesResourceWithRawResponse,
    AsyncSubtitlesResourceWithRawResponse,
    SubtitlesResourceWithStreamingResponse,
    AsyncSubtitlesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPageStreaming, AsyncPageStreaming
from ...._base_client import AsyncPaginator, make_request_options
from ....types.streaming import (
    video_list_params,
    video_create_params,
    video_update_params,
    video_list_names_params,
    video_create_multiple_params,
)
from ....types.streaming.video import Video
from ....types.streaming.create_video_param import CreateVideoParam
from ....types.streaming.video_create_response import VideoCreateResponse
from ....types.streaming.direct_upload_parameters import DirectUploadParameters
from ....types.streaming.video_create_multiple_response import VideoCreateMultipleResponse

__all__ = ["VideosResource", "AsyncVideosResource"]


class VideosResource(SyncAPIResource):
    @cached_property
    def subtitles(self) -> SubtitlesResource:
        return SubtitlesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return VideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return VideosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        video: CreateVideoParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoCreateResponse:
        """
        Use this method to create a new video entity.

        **Methods of creating**

        To upload the original video file to the server, there are several possible
        scenarios:

        - **Copy from another server** – If your video is accessable via "http://",
          "https://", or "sftp://" public link, then you can use this method to copy a
          file from an external server. Set `origin_url` parameter with the link to the
          original video file (i.e. "https://domain.com/video.mp4"). After method
          execution file will be uploaded and will be sent to transcoding automatically,
          you don't have to do anything else. Use extra field `origin_http_headers` if
          authorization is required on the external server.

        - **Direct upload from a local device** – If you need to upload video directly
          from your local device or from a mobile app, then use this method. Keep
          `origin_url` empty and use TUS protocol ([tus.io](https://tus.io)) to upload
          file. More details are here
          ["Get TUS' upload"](/docs/api-reference/streaming/videos/get-tus-parameters-for-direct-upload)

        After getting the video, it is processed through the queue. There are 2 priority
        criteria: global and local. Global is determined automatically by the system as
        converters are ready to get next video, so your videos rarely queue longer than
        usual (when you don't have a dedicated region). Local priority works at the
        level of your account and you have full control over it, look at "priority"
        attribute.

        **AI processing**

        When uploading a video, it is possible to automatically create subtitles based
        on AI.

        Read more:

        - What is
          ["AI Speech Recognition"](/docs/api-reference/streaming/ai/create-ai-asr-task).
        - If the option is enabled via
          `auto_transcribe_audio_language: auto|<language_code>`, then immediately after
          successful transcoding, an AI task will be automatically created for
          transcription.
        - If you need to translate subtitles from original language to any other, then
          AI-task of subtitles translation can be applied. Use
          `auto_translate_subtitles_language: default|<language_codes,>` parameter for
          that. Also you can point several languages to translate to, then a separate
          subtitle will be generated for each specified language.
        - How to
          ["add AI-generated subtitles to an exist video"](/docs/api-reference/streaming/subtitles/add-subtitle).

        The created AI-task(s) will be automatically executed, and result will also be
        automatically attached to this video as subtitle(s).

        Please note that transcription is done automatically for all videos uploaded to
        our video hosting. If necessary, you can disable automatic creation of
        subtitles. If AI is disabled in your account, no AI functionality is called.

        **Advanced Features** For details on the requirements for incoming original
        files, and output video parameters after transcoding, refer to the Knowledge
        Base documentation. By default video will be transcoded according to the
        original resolution, and a quality ladder suitable for your original video will
        be applied. There is no automatic upscaling; the maximum quality is taken from
        the original video. If you want to upload specific files not explicitly listed
        in requirements or wish to modify the standard quality ladder (i.e. decrease
        quality or add new non-standard qualities), then such customization is possible.
        Please reach out to us for assistance.

        Additionally, check the Knowledge Base for any supplementary information you may
        need.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/streaming/videos",
            body=maybe_transform({"video": video}, video_create_params.VideoCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoCreateResponse,
        )

    def update(
        self,
        video_id: int,
        *,
        name: str,
        auto_transcribe_audio_language: Literal["disable", "auto", "<language_code>"] | Omit = omit,
        auto_translate_subtitles_language: Literal["disable", "default", "<language_codes,>"] | Omit = omit,
        client_user_id: int | Omit = omit,
        clip_duration_seconds: int | Omit = omit,
        clip_start_seconds: int | Omit = omit,
        custom_iframe_url: str | Omit = omit,
        description: str | Omit = omit,
        directory_id: int | Omit = omit,
        origin_http_headers: str | Omit = omit,
        origin_url: str | Omit = omit,
        poster: str | Omit = omit,
        priority: int | Omit = omit,
        projection: str | Omit = omit,
        quality_set_id: int | Omit = omit,
        remote_poster_url: str | Omit = omit,
        remove_poster: bool | Omit = omit,
        screenshot_id: int | Omit = omit,
        share_url: str | Omit = omit,
        source_bitrate_limit: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Video:
        """
        Changes parameters of the video to new values.

        It's allowed to update only those public parameters that are described in POST
        method to create a new “video” entity. So it's not possible to change calculated
        parameters like "id", "duration", "`hls_url`", etc.

        Examples of changing:

        - Name: `{ "name": "new name of the video" }`
        - Move the video to a new directory: ` { "directory_id": 200 }`

        Please note that some parameters are used on initial step (before transcoding)
        only, so after transcoding there is no use in changing their values. For
        example, "`origin_url`" parameter is used for downloading an original file from
        a source and never used after transcoding; or "priority" parameter is used to
        set priority of processing and never used after transcoding.

        Args:
          name: Video name

          auto_transcribe_audio_language: Automatic creation of subtitles by transcribing the audio track.

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

          auto_translate_subtitles_language: Automatic translation of auto-transcribed subtitles to the specified
              language(s). Can be used both together with `auto_transcribe_audio_language`
              option only.

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

          client_user_id: Custom field where you can specify user ID in your system

          clip_duration_seconds: The length of the trimmed segment to transcode, instead of the entire length of
              the video. Is only used in conjunction with specifying the start of a segment.
              Transcoding duration is a number in seconds.

          clip_start_seconds: If you want to transcode only a trimmed segment of a video instead of entire
              length if the video, then you can provide timecodes of starting point and
              duration of a segment to process. Start encoding from is a number in seconds.

          custom_iframe_url: Deprecated.

              Custom URL of IFrame for video player to be used in share panel in player. Auto
              generated IFrame URL provided by default

          description: Video details; not visible to the end-users

          directory_id: ID of the directory where the video should be uploaded. (beta)

          origin_http_headers: Authorization HTTP request header. Will be used as credentials to authenticate a
              request to download a file (specified in "`origin_url`" parameter) on an
              external server.

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

          origin_url: URL to an original file which you want to copy from external storage. If
              specified, system will download the file and will use it as video source for
              transcoding.

          poster: Poster is your own static image which can be displayed before the video starts.

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

          priority: Priority allows you to adjust the urgency of processing some videos before
              others in your account, if your algorithm requires it. For example, when there
              are very urgent video and some regular ones that can wait in the queue.

              Value range, integer [-10..10]. -10 is the lowest down-priority, 10 is the
              highest up-priority. Default priority is 0.

          projection: Deprecated.

              Regulates the video format:

              - **regular** — plays the video as usual
              - **vr360** — plays the video in 360 degree mode
              - **vr180** — plays the video in 180 degree mode
              - **vr360tb** — plays the video in 3D 360 degree mode Top-Bottom.

              Default is regular

          quality_set_id: Custom quality set ID for transcoding, if transcoding is required according to
              your conditions. Look at GET /`quality_sets` method

          remote_poster_url: Poster URL to download from external resource, instead of uploading via "poster"
              attribute.

              It has the same restrictions as "poster" attribute.

          remove_poster: Set it to true to remove poster

          screenshot_id: Default screenshot index.

              Specify an ID from the "screenshots" array, so that the URL of the required
              screenshot appears in the "screenshot" attribute as the default screenshot. By
              default 5 static screenshots will be taken from different places in the video
              after transcoding. If the video is short, there may be fewer screenshots.

              Counting from 0. A value of -1 sets the default screenshot to the URL of your
              own image from the "poster" attribute.

              Look at "screenshot" attribute in GET /videos/{`video_id`} for details.

          share_url: Deprecated.

              Custom URL or iframe displayed in the link field when a user clicks on a sharing
              button in player. If empty, the link field and social network sharing is
              disabled

          source_bitrate_limit: The option allows you to set the video transcoding rule so that the output
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/videos/{video_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "auto_transcribe_audio_language": auto_transcribe_audio_language,
                    "auto_translate_subtitles_language": auto_translate_subtitles_language,
                    "client_user_id": client_user_id,
                    "clip_duration_seconds": clip_duration_seconds,
                    "clip_start_seconds": clip_start_seconds,
                    "custom_iframe_url": custom_iframe_url,
                    "description": description,
                    "directory_id": directory_id,
                    "origin_http_headers": origin_http_headers,
                    "origin_url": origin_url,
                    "poster": poster,
                    "priority": priority,
                    "projection": projection,
                    "quality_set_id": quality_set_id,
                    "remote_poster_url": remote_poster_url,
                    "remove_poster": remove_poster,
                    "screenshot_id": screenshot_id,
                    "share_url": share_url,
                    "source_bitrate_limit": source_bitrate_limit,
                },
                video_update_params.VideoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Video,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        client_user_id: int | Omit = omit,
        fields: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        status: str | Omit = omit,
        stream_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageStreaming[Video]:
        """
        Returns a set of videos by the given criteria.

        Args:
          id: IDs of the videos to find. You can specify one or more identifiers separated by
              commas. Example, ?id=1,101,1001

          client_user_id: Find videos where "`client_user_id`" meta field is equal to the search value

          fields: Restriction to return only the specified attributes, instead of the entire
              dataset. Specify, if you need to get short response. The following fields are
              available for specifying: id, name, duration, status, `created_at`,
              `updated_at`, `hls_url`, screenshots, `converted_videos`, priority, `stream_id`.
              Example, ?fields=id,name,`hls_url`

          page: Page number. Use it to list the paginated content

          per_page: Items per page number. Use it to list the paginated content

          search: Aggregated search condition. If set, the video list is filtered by one combined
              SQL criterion:

              - id={s} OR slug={s} OR name like {s}

              i.e. "/videos?search=1000" returns list of videos where id=1000 or slug=1000 or
              name contains "1000".

          status:
              Use it to get videos filtered by their status. Possible values:

              - empty
              - pending
              - viewable
              - ready
              - error

          stream_id: Find videos recorded from a specific stream, so for which "`stream_id`" field is
              equal to the search value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/videos",
            page=SyncPageStreaming[Video],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "client_user_id": client_user_id,
                        "fields": fields,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "status": status,
                        "stream_id": stream_id,
                    },
                    video_list_params.VideoListParams,
                ),
            ),
            model=Video,
        )

    def delete(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Operation to delete video entity.

        When you delete a video, all transcoded qualities and all associated files such
        as subtitles and screenshots, as well as other data, are deleted from cloud
        storage.

        The video is deleted permanently and irreversibly. Therefore, it is impossible
        to restore files after this.

        For detailed information and information on calculating your maximum monthly
        storage usage, please refer to the Product Documentation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/videos/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_multiple(
        self,
        *,
        fields: str | Omit = omit,
        videos: Iterable[video_create_multiple_params.Video] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoCreateMultipleResponse:
        """Mass upload of your videos.

        Method is used to set the task of creating videos in
        the form of 1 aggregated request instead of a large number of single requests.

        An additional advantage is the ability to specify subtitles in the same request.
        Whereas for a normal single upload, subtitles are uploaded in separate requests.

        All videos in the request will be processed in queue in order of priority. Use
        "priority" attribute and look at general description in POST /videos method.

        Limits:

        - Batch max size = 500 videos.
        - Max body size (payload) = 64MB.
        - API connection timeout = 30 sec.

        Args:
          fields: Restriction to return only the specified attributes, instead of the entire
              dataset. Specify, if you need to get short response. The following fields are
              available for specifying: id, name, duration, status, `created_at`,
              `updated_at`, `hls_url`, screenshots, `converted_videos`, priority. Example,
              ?fields=id,name,`hls_url`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/streaming/videos/batch",
            body=maybe_transform({"videos": videos}, video_create_multiple_params.VideoCreateMultipleParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"fields": fields}, video_create_multiple_params.VideoCreateMultipleParams),
            ),
            cast_to=VideoCreateMultipleResponse,
        )

    def get(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Video:
        """
        Information about a video entity.

        Contains all the data about the video: meta-data, data for streaming and
        renditions, static media data, data about original video.

        You can use different methods to play video:

        - `iframe_url` – a URL to a built-in HTML video player with automatically
          configured video playback.
        - `hls_url` – a URLs to HLS TS .m3u8 manifest, which can be played in video
          players.
        - `hls_cmaf_url` – a URL to HLS CMAF .m3u8 manifest with chunks in fMP4 format,
          which can be played in most modern video players.
        - `dash_url` – a URL to MPEG-DASH .mpd manifest, which can be played in most
          modern video players. Preferable for Android and Windows devices.
        - `converted_videos`/`mp4_url` – a URL to MP4 file of specific rendition.

        ![Video player](https://demo-files.gvideo.io/apidocs/coffee-run-player.jpg)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/videos/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Video,
        )

    def get_parameters_for_direct_upload(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectUploadParameters:
        """
        Use this method to get TUS' session parameters: hostname of the server to
        upload, secure token.

        The general sequence of actions for a direct upload of a video is as follows:

        - Create video entity via POST method
          ["Create video"](/docs/api-reference/streaming/videos/create-video)
        - Get TUS' session parameters (you are here now)
        - Upload file via TUS client, choose your implementation on
          [tus.io](https://tus.io/implementations)

        Final endpoint for uploading is constructed using the following template:
        "https://{hostname}/upload/". Also you have to provide token, `client_id`,
        `video_id` as metadata too.

        A short javascript example is shown below, based on tus-js-client. Variable
        "data" below is the result of this API request. Please, note that we support 2.x
        version only of tus-js-client.

        ```
            uploads[data.video.id] = new tus.Upload(file, {
              endpoint: `https://${data.servers[0].hostname}/upload/`,
              metadata: {
                filename: data.video.name,
                token: data.token,
                video_id: data.video.id,
                client_id: data.video.client_id
              },
              onSuccess: function() {
                ...
              }
            }
            uploads[data.video.id].start();
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/videos/{video_id}/upload",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectUploadParameters,
        )

    def list_names(
        self,
        *,
        ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns names for specified video IDs

        Args:
          ids: Comma-separated set of video IDs. Example, ?ids=7,17

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/streaming/videos/names",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, video_list_names_params.VideoListNamesParams),
            ),
            cast_to=NoneType,
        )


class AsyncVideosResource(AsyncAPIResource):
    @cached_property
    def subtitles(self) -> AsyncSubtitlesResource:
        return AsyncSubtitlesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncVideosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        video: CreateVideoParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoCreateResponse:
        """
        Use this method to create a new video entity.

        **Methods of creating**

        To upload the original video file to the server, there are several possible
        scenarios:

        - **Copy from another server** – If your video is accessable via "http://",
          "https://", or "sftp://" public link, then you can use this method to copy a
          file from an external server. Set `origin_url` parameter with the link to the
          original video file (i.e. "https://domain.com/video.mp4"). After method
          execution file will be uploaded and will be sent to transcoding automatically,
          you don't have to do anything else. Use extra field `origin_http_headers` if
          authorization is required on the external server.

        - **Direct upload from a local device** – If you need to upload video directly
          from your local device or from a mobile app, then use this method. Keep
          `origin_url` empty and use TUS protocol ([tus.io](https://tus.io)) to upload
          file. More details are here
          ["Get TUS' upload"](/docs/api-reference/streaming/videos/get-tus-parameters-for-direct-upload)

        After getting the video, it is processed through the queue. There are 2 priority
        criteria: global and local. Global is determined automatically by the system as
        converters are ready to get next video, so your videos rarely queue longer than
        usual (when you don't have a dedicated region). Local priority works at the
        level of your account and you have full control over it, look at "priority"
        attribute.

        **AI processing**

        When uploading a video, it is possible to automatically create subtitles based
        on AI.

        Read more:

        - What is
          ["AI Speech Recognition"](/docs/api-reference/streaming/ai/create-ai-asr-task).
        - If the option is enabled via
          `auto_transcribe_audio_language: auto|<language_code>`, then immediately after
          successful transcoding, an AI task will be automatically created for
          transcription.
        - If you need to translate subtitles from original language to any other, then
          AI-task of subtitles translation can be applied. Use
          `auto_translate_subtitles_language: default|<language_codes,>` parameter for
          that. Also you can point several languages to translate to, then a separate
          subtitle will be generated for each specified language.
        - How to
          ["add AI-generated subtitles to an exist video"](/docs/api-reference/streaming/subtitles/add-subtitle).

        The created AI-task(s) will be automatically executed, and result will also be
        automatically attached to this video as subtitle(s).

        Please note that transcription is done automatically for all videos uploaded to
        our video hosting. If necessary, you can disable automatic creation of
        subtitles. If AI is disabled in your account, no AI functionality is called.

        **Advanced Features** For details on the requirements for incoming original
        files, and output video parameters after transcoding, refer to the Knowledge
        Base documentation. By default video will be transcoded according to the
        original resolution, and a quality ladder suitable for your original video will
        be applied. There is no automatic upscaling; the maximum quality is taken from
        the original video. If you want to upload specific files not explicitly listed
        in requirements or wish to modify the standard quality ladder (i.e. decrease
        quality or add new non-standard qualities), then such customization is possible.
        Please reach out to us for assistance.

        Additionally, check the Knowledge Base for any supplementary information you may
        need.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/streaming/videos",
            body=await async_maybe_transform({"video": video}, video_create_params.VideoCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoCreateResponse,
        )

    async def update(
        self,
        video_id: int,
        *,
        name: str,
        auto_transcribe_audio_language: Literal["disable", "auto", "<language_code>"] | Omit = omit,
        auto_translate_subtitles_language: Literal["disable", "default", "<language_codes,>"] | Omit = omit,
        client_user_id: int | Omit = omit,
        clip_duration_seconds: int | Omit = omit,
        clip_start_seconds: int | Omit = omit,
        custom_iframe_url: str | Omit = omit,
        description: str | Omit = omit,
        directory_id: int | Omit = omit,
        origin_http_headers: str | Omit = omit,
        origin_url: str | Omit = omit,
        poster: str | Omit = omit,
        priority: int | Omit = omit,
        projection: str | Omit = omit,
        quality_set_id: int | Omit = omit,
        remote_poster_url: str | Omit = omit,
        remove_poster: bool | Omit = omit,
        screenshot_id: int | Omit = omit,
        share_url: str | Omit = omit,
        source_bitrate_limit: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Video:
        """
        Changes parameters of the video to new values.

        It's allowed to update only those public parameters that are described in POST
        method to create a new “video” entity. So it's not possible to change calculated
        parameters like "id", "duration", "`hls_url`", etc.

        Examples of changing:

        - Name: `{ "name": "new name of the video" }`
        - Move the video to a new directory: ` { "directory_id": 200 }`

        Please note that some parameters are used on initial step (before transcoding)
        only, so after transcoding there is no use in changing their values. For
        example, "`origin_url`" parameter is used for downloading an original file from
        a source and never used after transcoding; or "priority" parameter is used to
        set priority of processing and never used after transcoding.

        Args:
          name: Video name

          auto_transcribe_audio_language: Automatic creation of subtitles by transcribing the audio track.

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

          auto_translate_subtitles_language: Automatic translation of auto-transcribed subtitles to the specified
              language(s). Can be used both together with `auto_transcribe_audio_language`
              option only.

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

          client_user_id: Custom field where you can specify user ID in your system

          clip_duration_seconds: The length of the trimmed segment to transcode, instead of the entire length of
              the video. Is only used in conjunction with specifying the start of a segment.
              Transcoding duration is a number in seconds.

          clip_start_seconds: If you want to transcode only a trimmed segment of a video instead of entire
              length if the video, then you can provide timecodes of starting point and
              duration of a segment to process. Start encoding from is a number in seconds.

          custom_iframe_url: Deprecated.

              Custom URL of IFrame for video player to be used in share panel in player. Auto
              generated IFrame URL provided by default

          description: Video details; not visible to the end-users

          directory_id: ID of the directory where the video should be uploaded. (beta)

          origin_http_headers: Authorization HTTP request header. Will be used as credentials to authenticate a
              request to download a file (specified in "`origin_url`" parameter) on an
              external server.

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

          origin_url: URL to an original file which you want to copy from external storage. If
              specified, system will download the file and will use it as video source for
              transcoding.

          poster: Poster is your own static image which can be displayed before the video starts.

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

          priority: Priority allows you to adjust the urgency of processing some videos before
              others in your account, if your algorithm requires it. For example, when there
              are very urgent video and some regular ones that can wait in the queue.

              Value range, integer [-10..10]. -10 is the lowest down-priority, 10 is the
              highest up-priority. Default priority is 0.

          projection: Deprecated.

              Regulates the video format:

              - **regular** — plays the video as usual
              - **vr360** — plays the video in 360 degree mode
              - **vr180** — plays the video in 180 degree mode
              - **vr360tb** — plays the video in 3D 360 degree mode Top-Bottom.

              Default is regular

          quality_set_id: Custom quality set ID for transcoding, if transcoding is required according to
              your conditions. Look at GET /`quality_sets` method

          remote_poster_url: Poster URL to download from external resource, instead of uploading via "poster"
              attribute.

              It has the same restrictions as "poster" attribute.

          remove_poster: Set it to true to remove poster

          screenshot_id: Default screenshot index.

              Specify an ID from the "screenshots" array, so that the URL of the required
              screenshot appears in the "screenshot" attribute as the default screenshot. By
              default 5 static screenshots will be taken from different places in the video
              after transcoding. If the video is short, there may be fewer screenshots.

              Counting from 0. A value of -1 sets the default screenshot to the URL of your
              own image from the "poster" attribute.

              Look at "screenshot" attribute in GET /videos/{`video_id`} for details.

          share_url: Deprecated.

              Custom URL or iframe displayed in the link field when a user clicks on a sharing
              button in player. If empty, the link field and social network sharing is
              disabled

          source_bitrate_limit: The option allows you to set the video transcoding rule so that the output
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/videos/{video_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "auto_transcribe_audio_language": auto_transcribe_audio_language,
                    "auto_translate_subtitles_language": auto_translate_subtitles_language,
                    "client_user_id": client_user_id,
                    "clip_duration_seconds": clip_duration_seconds,
                    "clip_start_seconds": clip_start_seconds,
                    "custom_iframe_url": custom_iframe_url,
                    "description": description,
                    "directory_id": directory_id,
                    "origin_http_headers": origin_http_headers,
                    "origin_url": origin_url,
                    "poster": poster,
                    "priority": priority,
                    "projection": projection,
                    "quality_set_id": quality_set_id,
                    "remote_poster_url": remote_poster_url,
                    "remove_poster": remove_poster,
                    "screenshot_id": screenshot_id,
                    "share_url": share_url,
                    "source_bitrate_limit": source_bitrate_limit,
                },
                video_update_params.VideoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Video,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        client_user_id: int | Omit = omit,
        fields: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        status: str | Omit = omit,
        stream_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Video, AsyncPageStreaming[Video]]:
        """
        Returns a set of videos by the given criteria.

        Args:
          id: IDs of the videos to find. You can specify one or more identifiers separated by
              commas. Example, ?id=1,101,1001

          client_user_id: Find videos where "`client_user_id`" meta field is equal to the search value

          fields: Restriction to return only the specified attributes, instead of the entire
              dataset. Specify, if you need to get short response. The following fields are
              available for specifying: id, name, duration, status, `created_at`,
              `updated_at`, `hls_url`, screenshots, `converted_videos`, priority, `stream_id`.
              Example, ?fields=id,name,`hls_url`

          page: Page number. Use it to list the paginated content

          per_page: Items per page number. Use it to list the paginated content

          search: Aggregated search condition. If set, the video list is filtered by one combined
              SQL criterion:

              - id={s} OR slug={s} OR name like {s}

              i.e. "/videos?search=1000" returns list of videos where id=1000 or slug=1000 or
              name contains "1000".

          status:
              Use it to get videos filtered by their status. Possible values:

              - empty
              - pending
              - viewable
              - ready
              - error

          stream_id: Find videos recorded from a specific stream, so for which "`stream_id`" field is
              equal to the search value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/videos",
            page=AsyncPageStreaming[Video],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "client_user_id": client_user_id,
                        "fields": fields,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "status": status,
                        "stream_id": stream_id,
                    },
                    video_list_params.VideoListParams,
                ),
            ),
            model=Video,
        )

    async def delete(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Operation to delete video entity.

        When you delete a video, all transcoded qualities and all associated files such
        as subtitles and screenshots, as well as other data, are deleted from cloud
        storage.

        The video is deleted permanently and irreversibly. Therefore, it is impossible
        to restore files after this.

        For detailed information and information on calculating your maximum monthly
        storage usage, please refer to the Product Documentation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/videos/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_multiple(
        self,
        *,
        fields: str | Omit = omit,
        videos: Iterable[video_create_multiple_params.Video] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoCreateMultipleResponse:
        """Mass upload of your videos.

        Method is used to set the task of creating videos in
        the form of 1 aggregated request instead of a large number of single requests.

        An additional advantage is the ability to specify subtitles in the same request.
        Whereas for a normal single upload, subtitles are uploaded in separate requests.

        All videos in the request will be processed in queue in order of priority. Use
        "priority" attribute and look at general description in POST /videos method.

        Limits:

        - Batch max size = 500 videos.
        - Max body size (payload) = 64MB.
        - API connection timeout = 30 sec.

        Args:
          fields: Restriction to return only the specified attributes, instead of the entire
              dataset. Specify, if you need to get short response. The following fields are
              available for specifying: id, name, duration, status, `created_at`,
              `updated_at`, `hls_url`, screenshots, `converted_videos`, priority. Example,
              ?fields=id,name,`hls_url`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/streaming/videos/batch",
            body=await async_maybe_transform(
                {"videos": videos}, video_create_multiple_params.VideoCreateMultipleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"fields": fields}, video_create_multiple_params.VideoCreateMultipleParams
                ),
            ),
            cast_to=VideoCreateMultipleResponse,
        )

    async def get(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Video:
        """
        Information about a video entity.

        Contains all the data about the video: meta-data, data for streaming and
        renditions, static media data, data about original video.

        You can use different methods to play video:

        - `iframe_url` – a URL to a built-in HTML video player with automatically
          configured video playback.
        - `hls_url` – a URLs to HLS TS .m3u8 manifest, which can be played in video
          players.
        - `hls_cmaf_url` – a URL to HLS CMAF .m3u8 manifest with chunks in fMP4 format,
          which can be played in most modern video players.
        - `dash_url` – a URL to MPEG-DASH .mpd manifest, which can be played in most
          modern video players. Preferable for Android and Windows devices.
        - `converted_videos`/`mp4_url` – a URL to MP4 file of specific rendition.

        ![Video player](https://demo-files.gvideo.io/apidocs/coffee-run-player.jpg)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/videos/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Video,
        )

    async def get_parameters_for_direct_upload(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectUploadParameters:
        """
        Use this method to get TUS' session parameters: hostname of the server to
        upload, secure token.

        The general sequence of actions for a direct upload of a video is as follows:

        - Create video entity via POST method
          ["Create video"](/docs/api-reference/streaming/videos/create-video)
        - Get TUS' session parameters (you are here now)
        - Upload file via TUS client, choose your implementation on
          [tus.io](https://tus.io/implementations)

        Final endpoint for uploading is constructed using the following template:
        "https://{hostname}/upload/". Also you have to provide token, `client_id`,
        `video_id` as metadata too.

        A short javascript example is shown below, based on tus-js-client. Variable
        "data" below is the result of this API request. Please, note that we support 2.x
        version only of tus-js-client.

        ```
            uploads[data.video.id] = new tus.Upload(file, {
              endpoint: `https://${data.servers[0].hostname}/upload/`,
              metadata: {
                filename: data.video.name,
                token: data.token,
                video_id: data.video.id,
                client_id: data.video.client_id
              },
              onSuccess: function() {
                ...
              }
            }
            uploads[data.video.id].start();
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/videos/{video_id}/upload",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectUploadParameters,
        )

    async def list_names(
        self,
        *,
        ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns names for specified video IDs

        Args:
          ids: Comma-separated set of video IDs. Example, ?ids=7,17

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/streaming/videos/names",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, video_list_names_params.VideoListNamesParams),
            ),
            cast_to=NoneType,
        )


class VideosResourceWithRawResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.create = to_raw_response_wrapper(
            videos.create,
        )
        self.update = to_raw_response_wrapper(
            videos.update,
        )
        self.list = to_raw_response_wrapper(
            videos.list,
        )
        self.delete = to_raw_response_wrapper(
            videos.delete,
        )
        self.create_multiple = to_raw_response_wrapper(
            videos.create_multiple,
        )
        self.get = to_raw_response_wrapper(
            videos.get,
        )
        self.get_parameters_for_direct_upload = to_raw_response_wrapper(
            videos.get_parameters_for_direct_upload,
        )
        self.list_names = to_raw_response_wrapper(
            videos.list_names,
        )

    @cached_property
    def subtitles(self) -> SubtitlesResourceWithRawResponse:
        return SubtitlesResourceWithRawResponse(self._videos.subtitles)


class AsyncVideosResourceWithRawResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.create = async_to_raw_response_wrapper(
            videos.create,
        )
        self.update = async_to_raw_response_wrapper(
            videos.update,
        )
        self.list = async_to_raw_response_wrapper(
            videos.list,
        )
        self.delete = async_to_raw_response_wrapper(
            videos.delete,
        )
        self.create_multiple = async_to_raw_response_wrapper(
            videos.create_multiple,
        )
        self.get = async_to_raw_response_wrapper(
            videos.get,
        )
        self.get_parameters_for_direct_upload = async_to_raw_response_wrapper(
            videos.get_parameters_for_direct_upload,
        )
        self.list_names = async_to_raw_response_wrapper(
            videos.list_names,
        )

    @cached_property
    def subtitles(self) -> AsyncSubtitlesResourceWithRawResponse:
        return AsyncSubtitlesResourceWithRawResponse(self._videos.subtitles)


class VideosResourceWithStreamingResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.create = to_streamed_response_wrapper(
            videos.create,
        )
        self.update = to_streamed_response_wrapper(
            videos.update,
        )
        self.list = to_streamed_response_wrapper(
            videos.list,
        )
        self.delete = to_streamed_response_wrapper(
            videos.delete,
        )
        self.create_multiple = to_streamed_response_wrapper(
            videos.create_multiple,
        )
        self.get = to_streamed_response_wrapper(
            videos.get,
        )
        self.get_parameters_for_direct_upload = to_streamed_response_wrapper(
            videos.get_parameters_for_direct_upload,
        )
        self.list_names = to_streamed_response_wrapper(
            videos.list_names,
        )

    @cached_property
    def subtitles(self) -> SubtitlesResourceWithStreamingResponse:
        return SubtitlesResourceWithStreamingResponse(self._videos.subtitles)


class AsyncVideosResourceWithStreamingResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.create = async_to_streamed_response_wrapper(
            videos.create,
        )
        self.update = async_to_streamed_response_wrapper(
            videos.update,
        )
        self.list = async_to_streamed_response_wrapper(
            videos.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            videos.delete,
        )
        self.create_multiple = async_to_streamed_response_wrapper(
            videos.create_multiple,
        )
        self.get = async_to_streamed_response_wrapper(
            videos.get,
        )
        self.get_parameters_for_direct_upload = async_to_streamed_response_wrapper(
            videos.get_parameters_for_direct_upload,
        )
        self.list_names = async_to_streamed_response_wrapper(
            videos.list_names,
        )

    @cached_property
    def subtitles(self) -> AsyncSubtitlesResourceWithStreamingResponse:
        return AsyncSubtitlesResourceWithStreamingResponse(self._videos.subtitles)
