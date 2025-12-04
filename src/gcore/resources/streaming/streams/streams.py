# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .overlays import (
    OverlaysResource,
    AsyncOverlaysResource,
    OverlaysResourceWithRawResponse,
    AsyncOverlaysResourceWithRawResponse,
    OverlaysResourceWithStreamingResponse,
    AsyncOverlaysResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
    stream_list_params,
    stream_create_params,
    stream_update_params,
    stream_create_clip_params,
)
from ....types.streaming.clip import Clip
from ....types.streaming.video import Video
from ....types.streaming.stream import Stream
from ....types.streaming.stream_list_clips_response import StreamListClipsResponse
from ....types.streaming.stream_start_recording_response import StreamStartRecordingResponse

__all__ = ["StreamsResource", "AsyncStreamsResource"]


class StreamsResource(SyncAPIResource):
    @cached_property
    def overlays(self) -> OverlaysResource:
        return OverlaysResource(self._client)

    @cached_property
    def with_raw_response(self) -> StreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return StreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return StreamsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        active: bool | Omit = omit,
        auto_record: bool | Omit = omit,
        broadcast_ids: Iterable[int] | Omit = omit,
        cdn_id: int | Omit = omit,
        client_entity_data: str | Omit = omit,
        client_user_id: int | Omit = omit,
        dvr_duration: int | Omit = omit,
        dvr_enabled: bool | Omit = omit,
        hls_mpegts_endlist_tag: bool | Omit = omit,
        html_overlay: bool | Omit = omit,
        projection: Literal["regular", "vr360", "vr180", "vr360tb"] | Omit = omit,
        pull: bool | Omit = omit,
        quality_set_id: int | Omit = omit,
        record_type: Literal["origin", "transcoded"] | Omit = omit,
        uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream:
        """
        Use this method to create a new live stream entity for broadcasting.

        The input in API may contain streams of different formats, including the most
        common ones RTMP, RTMPS, SRT, HLS. Note that multicast MPEG-TS over UDP and
        others are supported too, ask the Support Team please.

        For ingestion, you can use both PUSH and PULL methods.

        Also you can use the main and backup servers, which are geographically located
        in different locations. By default, any free ingest points in the world are
        used. Settings have been applied that deliver low-latency streams in the optimal
        way. If for some reason you need to set a fixed ingest point, or if you need to
        set the main and backup ingest points in the same region (for example, do not
        send streams outside the EU or US), then contact our Support Team.

        The output is HLS and MPEG-DASH with ABR. We transcode video for you by our
        cloud-based infrastructure. ABR ladder supports all qualities from SD to 8K HDR
        60fps.

        All our streams are Low Latency enabled. We support a delay of ±4 seconds for
        video streams by utilizing Common Media Application Format (CMAF) technology. So
        you obtain latency from the traditional 30-50 seconds to ±4 seconds only by
        default. If you need legacy non-low-latency HLS, then look at HLS MPEG-TS
        delivery below.

        You have access to additional functions such as:

        - DVR
        - Recording
        - Live clipping
        - Restreaming
        - (soon) AI Automatic Speech Recognition for subtitles/captions generating

        For more information see specific API methods, and the Knowledge Base.

        ![HTML Overlays](https://demo-files.gvideo.io/apidocs/low-latency-football.gif)

        Args:
          name: Stream name.

              Often used as a human-readable name for the stream, but can contain any text you
              wish. The values are not unique and may be repeated.

              Examples:

              - Conference in July
              - Stream #10003
              - Open-Air Camera #31 Backstage
              - 480fd499-2de2-4988-bc1a-a4eebe9818ee

          active: Stream switch between on and off. This is not an indicator of the status "stream
              is receiving and it is LIVE", but rather an on/off switch.

              When stream is switched off, there is no way to process it: PULL is deactivated
              and PUSH will return an error.

              - true – stream can be processed
              - false – stream is off, and cannot be processed

          auto_record: Enables autotomatic recording of the stream when it started. So you don't need
              to call recording manually.

              Result of recording is automatically added to video hosting. For details see the
              /streams/`start_recording` method and in knowledge base

              Values:

              - true – auto recording is enabled
              - false – auto recording is disabled

          broadcast_ids: IDs of broadcasts which will include this stream

          cdn_id: ID of custom CDN resource from which the content will be delivered (only if you
              know what you do)

          client_entity_data: Custom meta field designed to store your own extra information about a video
              entity: video source, video id, parameters, etc. We do not use this field in any
              way when processing the stream. You can store any data in any format (string,
              json, etc), saved as a text string. Example:
              `client_entity_data = '{ "seq_id": "1234567890", "name": "John Doe", "iat": 1516239022 }'`

          client_user_id: Custom meta field for storing the Identifier in your system. We do not use this
              field in any way when processing the stream. Example: `client_user_id = 1001`

          dvr_duration: DVR duration in seconds if DVR feature is enabled for the stream. So this is
              duration of how far the user can rewind the live stream.

              `dvr_duration` range is [30...14400].

              Maximum value is 4 hours = 14400 seconds. If you need more, ask the Support Team
              please.

          dvr_enabled:
              Enables DVR for the stream:

              - true – DVR is enabled
              - false – DVR is disabled

          hls_mpegts_endlist_tag: Add `#EXT-X-ENDLIST` tag within .m3u8 playlist after the last segment of a live
              stream when broadcast is ended.

          html_overlay: Switch on mode to insert and display real-time HTML overlay widgets on top of
              live streams

          projection: Visualization mode for 360° streams, how the stream is rendered in our web
              player ONLY. If you would like to show video 360° in an external video player,
              then use parameters of that video player.

              Modes:

              - regular – regular “flat” stream
              - vr360 – display stream in 360° mode
              - vr180 – display stream in 180° mode
              - vr360tb – display stream in 3D 360° mode Top-Bottom

          pull: Indicates if stream is pulled from external server or not. Has two possible
              values:

              - true – stream is received by PULL method. Use this when need to get stream
                from external server.
              - false – stream is received by PUSH method. Use this when need to send stream
                from end-device to our Streaming Platform, i.e. from your encoder, mobile app
                or OBS Studio.

          quality_set_id: Custom quality set ID for transcoding, if transcoding is required according to
              your conditions. Look at GET /`quality_sets` method

          record_type: Method of recording a stream. Specifies the source from which the stream will be
              recorded: original or transcoded.

              Types:

              - "origin" – To record RMTP/SRT/etc original clean media source.
              - "transcoded" – To record the output transcoded version of the stream,
                including overlays, texts, logos, etc. additional media layers.

          uri: When using PULL method, this is the URL to pull a stream from.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/streaming/streams",
            body=maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "auto_record": auto_record,
                    "broadcast_ids": broadcast_ids,
                    "cdn_id": cdn_id,
                    "client_entity_data": client_entity_data,
                    "client_user_id": client_user_id,
                    "dvr_duration": dvr_duration,
                    "dvr_enabled": dvr_enabled,
                    "hls_mpegts_endlist_tag": hls_mpegts_endlist_tag,
                    "html_overlay": html_overlay,
                    "projection": projection,
                    "pull": pull,
                    "quality_set_id": quality_set_id,
                    "record_type": record_type,
                    "uri": uri,
                },
                stream_create_params.StreamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Stream,
        )

    def update(
        self,
        stream_id: int,
        *,
        stream: stream_update_params.Stream | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream:
        """
        Updates stream settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/streams/{stream_id}",
            body=maybe_transform({"stream": stream}, stream_update_params.StreamUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Stream,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        with_broadcasts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageStreaming[Stream]:
        """Returns a list of streams

        Args:
          page: Query parameter.

        Use it to list the paginated content

          with_broadcasts: Query parameter. Set to 1 to get details of the broadcasts associated with the
              stream

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/streams",
            page=SyncPageStreaming[Stream],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "with_broadcasts": with_broadcasts,
                    },
                    stream_list_params.StreamListParams,
                ),
            ),
            model=Stream,
        )

    def delete(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a live stream.

        After deleting the live stream, all associated data is deleted: settings, PUSH
        and PULL links, video playback links, etc.

        Live stream information is deleted permanently and irreversibly. Therefore, it
        is impossible to restore data and files after this.

        But if the live had recordings, they continue to remain independent Video
        entities. The "`stream_id`" parameter will simply point to a stream that no
        longer exists.

        Perhaps, instead of deleting, you may use the stream deactivation:

        ```
        PATCH / videos / {stream_id}
        {"active": false}
        ```

        For details, see the Product Documentation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clear_dvr(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Clear live stream DVR

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/streaming/streams/{stream_id}/dvr_cleanup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_clip(
        self,
        stream_id: int,
        *,
        duration: int,
        expiration: int | Omit = omit,
        start: int | Omit = omit,
        vod_required: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Clip:
        """
        Create an instant clip from on-going live stream.

        Instant clips are applicable in cases where there is no time to wait for the
        broadcast to be completed and recorded. For example, for quickly cutting
        highlights in sport events, or cutting an important moment in the news or live
        performance.

        DVR function must be enabled for clip recording. If the DVR is disabled, the
        response will be error 422.

        Instant clip becomes available for viewing in the following formats:

        - HLS .m3u8,
        - MP4,
        - VOD in video hosting with a permanent link to watch video.

        ![HTML Overlays](https://demo-files.gvideo.io/apidocs/clip_recording_mp4_hls.gif)

        **Clip lifetime:**

        Instant clips are a copy of the stream, created from a live stream. They are
        stored in memory for a limited time, after which the clip ceases to exist and
        you will receive a 404 on the link.

        Limits that you should keep in mind:

        - The clip's lifespan is controlled by `expiration` parameter.
        - The default expiration value is 1 hour. The value can be set from 1 minute to
          4 hours.
        - If you want a video for longer or permanent viewing, then create a regular VOD
          based on the clip. This way you can use the clip's link for the first time,
          and immediately after the transcoded version is ready, you can change by
          yourself it to a permanent link of VOD.
        - The clip becomes available only after it is completely copied from the live
          stream. So the clip will be available after `start + duration` exact time. If
          you try to request it before this time, the response will be error code 425
          "Too Early".

        **Cutting a clip from a source:**

        In order to use clips recording feature, DVR must be enabled for a stream:
        "`dvr_enabled`: true". The DVR serves as a source for creating clips:

        - By default live stream DVR is set to 1 hour (3600 seconds). You can create an
          instant clip using any segment of this time period by specifying the desired
          start time and duration.
        - If you create a clip, but the DVR expires, the clip will still exist for the
          specified time as a copy of the stream.

        **Getting permanent VOD:**

        To get permanent VOD version of a live clip use this parameter when making a
        request to create a clip: `vod_required: true`.

        Later, when the clip is ready, grab `video_id` value from the response and query
        the video by regular GET /video/{id} method.

        Args:
          duration: Requested segment duration in seconds to be cut.

              Please, note that cutting is based on the idea of instantly creating a clip,
              instead of precise timing. So final segment may be:

              - Less than the specified value if there is less data in the DVR than the
                requested segment.
              - Greater than the specified value, because segment is aligned to the first and
                last key frames of already stored fragment in DVR, this way -1 and +1 chunks
                can be added to left and right.

              Duration of cutted segment cannot be greater than DVR duration for this stream.
              Therefore, to change the maximum, use "`dvr_duration`" parameter of this stream.

          expiration: Expire time of the clip via a public link.

              Unix timestamp in seconds, absolute value.

              This is the time how long the instant clip will be stored in the server memory
              and can be accessed via public HLS/MP4 links. Download and/or use the instant
              clip before this time expires.

              After the time has expired, the clip is deleted from memory and is no longer
              available via the link. You need to create a new segment, or use
              `vod_required: true` attribute.

              If value is omitted, then expiration is counted as +3600 seconds (1 hour) to the
              end of the clip (i.e. `unix timestamp = <start> + <duration> + 3600`).

              Allowed range: 1m <= expiration <= 4h.

              Example:
              `24.05.2024 14:00:00 (GMT) + 60 seconds of duration + 3600 seconds of expiration = 24.05.2024 15:01:00 (GMT) is Unix timestamp = 1716562860`

          start: Starting point of the segment to cut.

              Unix timestamp in seconds, absolute value. Example:
              `24.05.2024 14:00:00 (GMT) is Unix timestamp = 1716559200`

              If a value from the past is specified, it is used as the starting point for the
              segment to cut. If the value is omitted, then clip will start from now.

          vod_required: Indicates if video needs to be stored also as permanent VOD

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/streaming/streams/{stream_id}/clip_recording",
            body=maybe_transform(
                {
                    "duration": duration,
                    "expiration": expiration,
                    "start": start,
                    "vod_required": vod_required,
                },
                stream_create_clip_params.StreamCreateClipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Clip,
        )

    def get(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream:
        """
        Returns stream details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Stream,
        )

    def list_clips(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamListClipsResponse:
        """
        Get list of non expired instant clips for a stream.

        You can now use both MP4 just-in-time packager and HLS for all clips. Get URLs
        from "`hls_master`" and "`mp4_master`".

        **How to download renditions of clips:**

        URLs contain "master" alias by default, which means maximum available quality
        from ABR set (based on height metadata). There is also possibility to access
        individual bitrates from ABR ladder. That works for both HLS and MP4. You can
        replace manually "master" to a value from renditions list in order to get exact
        bitrate/quality from the set. Example:

        - HLS 720p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_master.m3u8`
        - HLS 720p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_media_1_360.m3u8`
        - MP4 360p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_master.mp4`
        - MP4 360p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_media_1_360.mp4`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/streams/{stream_id}/clip_recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamListClipsResponse,
        )

    def start_recording(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamStartRecordingResponse:
        """
        Start recording a stream.

        Stream will be recorded and automatically saved in our video hosting as a
        separate video VOD:

        - ID of the stream from which the recording was organized is added to
          "`stream_id`" field. You can find the video by that value later.
        - Title of the video is based on pattern "Stream Record: {`stream_title`},
          {`recording_end_time_utc`}".
        - Recording start time is stored in "`recording_started_at`" field.
        - You can record the original stream or the transcoded one. Only the transcoded
          version will contain overlays. Set the appropriate recording method when
          creating the stream or before calling this recording method. Details in the
          "`record_type`" parameter of the stream.
        - If you have access to the premium feature of saving the original stream (so
          not just transcoded renditions), then the link to the original file will be in
          the "`origin_url`" field. Look at the description of the field how to use it.

        Stream must be live for the recording to start, please check fields "live"
        and/or "`backup_live`". After the recording starts, field "recording" will
        switch to "true", and the recording duration in seconds will appear in the
        "`recording_duration`" field.

        Please, keep in mind that recording doesn't start instantly, it takes ±3-7
        seconds to initialize the process after executing this method.

        Stream recording stops when:

        - Explicit execution of the method /`stop_recording`. In this case, the file
          will be completely saved and closed. When you execute the stream recording
          method again, the recording will be made to a new video file.
        - When sending the stream stops on the client side, or stops accidentally. In
          this case, recording process is waiting for 10 seconds to resume recording:

        - If the stream resumes within that period, recording will continue to the same
          file.
        - After that period, the file will be completely saved and closed.
        - If the stream suddenly resumes after this period, the recording will go to a
          new file, because old file is closed already. Please, also note that if you
          have long broadcasts, the recording will be cut into 4-hour videos. This value
          is fixed, but can be changed upon request to the Support Team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/streaming/streams/{stream_id}/start_recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamStartRecordingResponse,
        )

    def stop_recording(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Video:
        """
        Stop recording a stream.

        Stream must be in "recording: true" state for recording to be stopped.

        If there was a recording, the created video entity will be returned. Otherwise
        the response will be empty. Please see conditions and restrictions for recording
        a stream in the description of method /`start_recording`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/streaming/streams/{stream_id}/stop_recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Video,
        )


class AsyncStreamsResource(AsyncAPIResource):
    @cached_property
    def overlays(self) -> AsyncOverlaysResource:
        return AsyncOverlaysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncStreamsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        active: bool | Omit = omit,
        auto_record: bool | Omit = omit,
        broadcast_ids: Iterable[int] | Omit = omit,
        cdn_id: int | Omit = omit,
        client_entity_data: str | Omit = omit,
        client_user_id: int | Omit = omit,
        dvr_duration: int | Omit = omit,
        dvr_enabled: bool | Omit = omit,
        hls_mpegts_endlist_tag: bool | Omit = omit,
        html_overlay: bool | Omit = omit,
        projection: Literal["regular", "vr360", "vr180", "vr360tb"] | Omit = omit,
        pull: bool | Omit = omit,
        quality_set_id: int | Omit = omit,
        record_type: Literal["origin", "transcoded"] | Omit = omit,
        uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream:
        """
        Use this method to create a new live stream entity for broadcasting.

        The input in API may contain streams of different formats, including the most
        common ones RTMP, RTMPS, SRT, HLS. Note that multicast MPEG-TS over UDP and
        others are supported too, ask the Support Team please.

        For ingestion, you can use both PUSH and PULL methods.

        Also you can use the main and backup servers, which are geographically located
        in different locations. By default, any free ingest points in the world are
        used. Settings have been applied that deliver low-latency streams in the optimal
        way. If for some reason you need to set a fixed ingest point, or if you need to
        set the main and backup ingest points in the same region (for example, do not
        send streams outside the EU or US), then contact our Support Team.

        The output is HLS and MPEG-DASH with ABR. We transcode video for you by our
        cloud-based infrastructure. ABR ladder supports all qualities from SD to 8K HDR
        60fps.

        All our streams are Low Latency enabled. We support a delay of ±4 seconds for
        video streams by utilizing Common Media Application Format (CMAF) technology. So
        you obtain latency from the traditional 30-50 seconds to ±4 seconds only by
        default. If you need legacy non-low-latency HLS, then look at HLS MPEG-TS
        delivery below.

        You have access to additional functions such as:

        - DVR
        - Recording
        - Live clipping
        - Restreaming
        - (soon) AI Automatic Speech Recognition for subtitles/captions generating

        For more information see specific API methods, and the Knowledge Base.

        ![HTML Overlays](https://demo-files.gvideo.io/apidocs/low-latency-football.gif)

        Args:
          name: Stream name.

              Often used as a human-readable name for the stream, but can contain any text you
              wish. The values are not unique and may be repeated.

              Examples:

              - Conference in July
              - Stream #10003
              - Open-Air Camera #31 Backstage
              - 480fd499-2de2-4988-bc1a-a4eebe9818ee

          active: Stream switch between on and off. This is not an indicator of the status "stream
              is receiving and it is LIVE", but rather an on/off switch.

              When stream is switched off, there is no way to process it: PULL is deactivated
              and PUSH will return an error.

              - true – stream can be processed
              - false – stream is off, and cannot be processed

          auto_record: Enables autotomatic recording of the stream when it started. So you don't need
              to call recording manually.

              Result of recording is automatically added to video hosting. For details see the
              /streams/`start_recording` method and in knowledge base

              Values:

              - true – auto recording is enabled
              - false – auto recording is disabled

          broadcast_ids: IDs of broadcasts which will include this stream

          cdn_id: ID of custom CDN resource from which the content will be delivered (only if you
              know what you do)

          client_entity_data: Custom meta field designed to store your own extra information about a video
              entity: video source, video id, parameters, etc. We do not use this field in any
              way when processing the stream. You can store any data in any format (string,
              json, etc), saved as a text string. Example:
              `client_entity_data = '{ "seq_id": "1234567890", "name": "John Doe", "iat": 1516239022 }'`

          client_user_id: Custom meta field for storing the Identifier in your system. We do not use this
              field in any way when processing the stream. Example: `client_user_id = 1001`

          dvr_duration: DVR duration in seconds if DVR feature is enabled for the stream. So this is
              duration of how far the user can rewind the live stream.

              `dvr_duration` range is [30...14400].

              Maximum value is 4 hours = 14400 seconds. If you need more, ask the Support Team
              please.

          dvr_enabled:
              Enables DVR for the stream:

              - true – DVR is enabled
              - false – DVR is disabled

          hls_mpegts_endlist_tag: Add `#EXT-X-ENDLIST` tag within .m3u8 playlist after the last segment of a live
              stream when broadcast is ended.

          html_overlay: Switch on mode to insert and display real-time HTML overlay widgets on top of
              live streams

          projection: Visualization mode for 360° streams, how the stream is rendered in our web
              player ONLY. If you would like to show video 360° in an external video player,
              then use parameters of that video player.

              Modes:

              - regular – regular “flat” stream
              - vr360 – display stream in 360° mode
              - vr180 – display stream in 180° mode
              - vr360tb – display stream in 3D 360° mode Top-Bottom

          pull: Indicates if stream is pulled from external server or not. Has two possible
              values:

              - true – stream is received by PULL method. Use this when need to get stream
                from external server.
              - false – stream is received by PUSH method. Use this when need to send stream
                from end-device to our Streaming Platform, i.e. from your encoder, mobile app
                or OBS Studio.

          quality_set_id: Custom quality set ID for transcoding, if transcoding is required according to
              your conditions. Look at GET /`quality_sets` method

          record_type: Method of recording a stream. Specifies the source from which the stream will be
              recorded: original or transcoded.

              Types:

              - "origin" – To record RMTP/SRT/etc original clean media source.
              - "transcoded" – To record the output transcoded version of the stream,
                including overlays, texts, logos, etc. additional media layers.

          uri: When using PULL method, this is the URL to pull a stream from.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/streaming/streams",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "auto_record": auto_record,
                    "broadcast_ids": broadcast_ids,
                    "cdn_id": cdn_id,
                    "client_entity_data": client_entity_data,
                    "client_user_id": client_user_id,
                    "dvr_duration": dvr_duration,
                    "dvr_enabled": dvr_enabled,
                    "hls_mpegts_endlist_tag": hls_mpegts_endlist_tag,
                    "html_overlay": html_overlay,
                    "projection": projection,
                    "pull": pull,
                    "quality_set_id": quality_set_id,
                    "record_type": record_type,
                    "uri": uri,
                },
                stream_create_params.StreamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Stream,
        )

    async def update(
        self,
        stream_id: int,
        *,
        stream: stream_update_params.Stream | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream:
        """
        Updates stream settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/streams/{stream_id}",
            body=await async_maybe_transform({"stream": stream}, stream_update_params.StreamUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Stream,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        with_broadcasts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Stream, AsyncPageStreaming[Stream]]:
        """Returns a list of streams

        Args:
          page: Query parameter.

        Use it to list the paginated content

          with_broadcasts: Query parameter. Set to 1 to get details of the broadcasts associated with the
              stream

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/streams",
            page=AsyncPageStreaming[Stream],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "with_broadcasts": with_broadcasts,
                    },
                    stream_list_params.StreamListParams,
                ),
            ),
            model=Stream,
        )

    async def delete(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a live stream.

        After deleting the live stream, all associated data is deleted: settings, PUSH
        and PULL links, video playback links, etc.

        Live stream information is deleted permanently and irreversibly. Therefore, it
        is impossible to restore data and files after this.

        But if the live had recordings, they continue to remain independent Video
        entities. The "`stream_id`" parameter will simply point to a stream that no
        longer exists.

        Perhaps, instead of deleting, you may use the stream deactivation:

        ```
        PATCH / videos / {stream_id}
        {"active": false}
        ```

        For details, see the Product Documentation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clear_dvr(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Clear live stream DVR

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/streaming/streams/{stream_id}/dvr_cleanup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_clip(
        self,
        stream_id: int,
        *,
        duration: int,
        expiration: int | Omit = omit,
        start: int | Omit = omit,
        vod_required: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Clip:
        """
        Create an instant clip from on-going live stream.

        Instant clips are applicable in cases where there is no time to wait for the
        broadcast to be completed and recorded. For example, for quickly cutting
        highlights in sport events, or cutting an important moment in the news or live
        performance.

        DVR function must be enabled for clip recording. If the DVR is disabled, the
        response will be error 422.

        Instant clip becomes available for viewing in the following formats:

        - HLS .m3u8,
        - MP4,
        - VOD in video hosting with a permanent link to watch video.

        ![HTML Overlays](https://demo-files.gvideo.io/apidocs/clip_recording_mp4_hls.gif)

        **Clip lifetime:**

        Instant clips are a copy of the stream, created from a live stream. They are
        stored in memory for a limited time, after which the clip ceases to exist and
        you will receive a 404 on the link.

        Limits that you should keep in mind:

        - The clip's lifespan is controlled by `expiration` parameter.
        - The default expiration value is 1 hour. The value can be set from 1 minute to
          4 hours.
        - If you want a video for longer or permanent viewing, then create a regular VOD
          based on the clip. This way you can use the clip's link for the first time,
          and immediately after the transcoded version is ready, you can change by
          yourself it to a permanent link of VOD.
        - The clip becomes available only after it is completely copied from the live
          stream. So the clip will be available after `start + duration` exact time. If
          you try to request it before this time, the response will be error code 425
          "Too Early".

        **Cutting a clip from a source:**

        In order to use clips recording feature, DVR must be enabled for a stream:
        "`dvr_enabled`: true". The DVR serves as a source for creating clips:

        - By default live stream DVR is set to 1 hour (3600 seconds). You can create an
          instant clip using any segment of this time period by specifying the desired
          start time and duration.
        - If you create a clip, but the DVR expires, the clip will still exist for the
          specified time as a copy of the stream.

        **Getting permanent VOD:**

        To get permanent VOD version of a live clip use this parameter when making a
        request to create a clip: `vod_required: true`.

        Later, when the clip is ready, grab `video_id` value from the response and query
        the video by regular GET /video/{id} method.

        Args:
          duration: Requested segment duration in seconds to be cut.

              Please, note that cutting is based on the idea of instantly creating a clip,
              instead of precise timing. So final segment may be:

              - Less than the specified value if there is less data in the DVR than the
                requested segment.
              - Greater than the specified value, because segment is aligned to the first and
                last key frames of already stored fragment in DVR, this way -1 and +1 chunks
                can be added to left and right.

              Duration of cutted segment cannot be greater than DVR duration for this stream.
              Therefore, to change the maximum, use "`dvr_duration`" parameter of this stream.

          expiration: Expire time of the clip via a public link.

              Unix timestamp in seconds, absolute value.

              This is the time how long the instant clip will be stored in the server memory
              and can be accessed via public HLS/MP4 links. Download and/or use the instant
              clip before this time expires.

              After the time has expired, the clip is deleted from memory and is no longer
              available via the link. You need to create a new segment, or use
              `vod_required: true` attribute.

              If value is omitted, then expiration is counted as +3600 seconds (1 hour) to the
              end of the clip (i.e. `unix timestamp = <start> + <duration> + 3600`).

              Allowed range: 1m <= expiration <= 4h.

              Example:
              `24.05.2024 14:00:00 (GMT) + 60 seconds of duration + 3600 seconds of expiration = 24.05.2024 15:01:00 (GMT) is Unix timestamp = 1716562860`

          start: Starting point of the segment to cut.

              Unix timestamp in seconds, absolute value. Example:
              `24.05.2024 14:00:00 (GMT) is Unix timestamp = 1716559200`

              If a value from the past is specified, it is used as the starting point for the
              segment to cut. If the value is omitted, then clip will start from now.

          vod_required: Indicates if video needs to be stored also as permanent VOD

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/streaming/streams/{stream_id}/clip_recording",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "expiration": expiration,
                    "start": start,
                    "vod_required": vod_required,
                },
                stream_create_clip_params.StreamCreateClipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Clip,
        )

    async def get(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream:
        """
        Returns stream details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Stream,
        )

    async def list_clips(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamListClipsResponse:
        """
        Get list of non expired instant clips for a stream.

        You can now use both MP4 just-in-time packager and HLS for all clips. Get URLs
        from "`hls_master`" and "`mp4_master`".

        **How to download renditions of clips:**

        URLs contain "master" alias by default, which means maximum available quality
        from ABR set (based on height metadata). There is also possibility to access
        individual bitrates from ABR ladder. That works for both HLS and MP4. You can
        replace manually "master" to a value from renditions list in order to get exact
        bitrate/quality from the set. Example:

        - HLS 720p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_master.m3u8`
        - HLS 720p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_media_1_360.m3u8`
        - MP4 360p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_master.mp4`
        - MP4 360p:
          `https://CID.domain.com/rec/111_1000/rec_d7bsli54p8n4_qsid42_media_1_360.mp4`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/streams/{stream_id}/clip_recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamListClipsResponse,
        )

    async def start_recording(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamStartRecordingResponse:
        """
        Start recording a stream.

        Stream will be recorded and automatically saved in our video hosting as a
        separate video VOD:

        - ID of the stream from which the recording was organized is added to
          "`stream_id`" field. You can find the video by that value later.
        - Title of the video is based on pattern "Stream Record: {`stream_title`},
          {`recording_end_time_utc`}".
        - Recording start time is stored in "`recording_started_at`" field.
        - You can record the original stream or the transcoded one. Only the transcoded
          version will contain overlays. Set the appropriate recording method when
          creating the stream or before calling this recording method. Details in the
          "`record_type`" parameter of the stream.
        - If you have access to the premium feature of saving the original stream (so
          not just transcoded renditions), then the link to the original file will be in
          the "`origin_url`" field. Look at the description of the field how to use it.

        Stream must be live for the recording to start, please check fields "live"
        and/or "`backup_live`". After the recording starts, field "recording" will
        switch to "true", and the recording duration in seconds will appear in the
        "`recording_duration`" field.

        Please, keep in mind that recording doesn't start instantly, it takes ±3-7
        seconds to initialize the process after executing this method.

        Stream recording stops when:

        - Explicit execution of the method /`stop_recording`. In this case, the file
          will be completely saved and closed. When you execute the stream recording
          method again, the recording will be made to a new video file.
        - When sending the stream stops on the client side, or stops accidentally. In
          this case, recording process is waiting for 10 seconds to resume recording:

        - If the stream resumes within that period, recording will continue to the same
          file.
        - After that period, the file will be completely saved and closed.
        - If the stream suddenly resumes after this period, the recording will go to a
          new file, because old file is closed already. Please, also note that if you
          have long broadcasts, the recording will be cut into 4-hour videos. This value
          is fixed, but can be changed upon request to the Support Team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/streaming/streams/{stream_id}/start_recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamStartRecordingResponse,
        )

    async def stop_recording(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Video:
        """
        Stop recording a stream.

        Stream must be in "recording: true" state for recording to be stopped.

        If there was a recording, the created video entity will be returned. Otherwise
        the response will be empty. Please see conditions and restrictions for recording
        a stream in the description of method /`start_recording`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/streaming/streams/{stream_id}/stop_recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Video,
        )


class StreamsResourceWithRawResponse:
    def __init__(self, streams: StreamsResource) -> None:
        self._streams = streams

        self.create = to_raw_response_wrapper(
            streams.create,
        )
        self.update = to_raw_response_wrapper(
            streams.update,
        )
        self.list = to_raw_response_wrapper(
            streams.list,
        )
        self.delete = to_raw_response_wrapper(
            streams.delete,
        )
        self.clear_dvr = to_raw_response_wrapper(
            streams.clear_dvr,
        )
        self.create_clip = to_raw_response_wrapper(
            streams.create_clip,
        )
        self.get = to_raw_response_wrapper(
            streams.get,
        )
        self.list_clips = to_raw_response_wrapper(
            streams.list_clips,
        )
        self.start_recording = to_raw_response_wrapper(
            streams.start_recording,
        )
        self.stop_recording = to_raw_response_wrapper(
            streams.stop_recording,
        )

    @cached_property
    def overlays(self) -> OverlaysResourceWithRawResponse:
        return OverlaysResourceWithRawResponse(self._streams.overlays)


class AsyncStreamsResourceWithRawResponse:
    def __init__(self, streams: AsyncStreamsResource) -> None:
        self._streams = streams

        self.create = async_to_raw_response_wrapper(
            streams.create,
        )
        self.update = async_to_raw_response_wrapper(
            streams.update,
        )
        self.list = async_to_raw_response_wrapper(
            streams.list,
        )
        self.delete = async_to_raw_response_wrapper(
            streams.delete,
        )
        self.clear_dvr = async_to_raw_response_wrapper(
            streams.clear_dvr,
        )
        self.create_clip = async_to_raw_response_wrapper(
            streams.create_clip,
        )
        self.get = async_to_raw_response_wrapper(
            streams.get,
        )
        self.list_clips = async_to_raw_response_wrapper(
            streams.list_clips,
        )
        self.start_recording = async_to_raw_response_wrapper(
            streams.start_recording,
        )
        self.stop_recording = async_to_raw_response_wrapper(
            streams.stop_recording,
        )

    @cached_property
    def overlays(self) -> AsyncOverlaysResourceWithRawResponse:
        return AsyncOverlaysResourceWithRawResponse(self._streams.overlays)


class StreamsResourceWithStreamingResponse:
    def __init__(self, streams: StreamsResource) -> None:
        self._streams = streams

        self.create = to_streamed_response_wrapper(
            streams.create,
        )
        self.update = to_streamed_response_wrapper(
            streams.update,
        )
        self.list = to_streamed_response_wrapper(
            streams.list,
        )
        self.delete = to_streamed_response_wrapper(
            streams.delete,
        )
        self.clear_dvr = to_streamed_response_wrapper(
            streams.clear_dvr,
        )
        self.create_clip = to_streamed_response_wrapper(
            streams.create_clip,
        )
        self.get = to_streamed_response_wrapper(
            streams.get,
        )
        self.list_clips = to_streamed_response_wrapper(
            streams.list_clips,
        )
        self.start_recording = to_streamed_response_wrapper(
            streams.start_recording,
        )
        self.stop_recording = to_streamed_response_wrapper(
            streams.stop_recording,
        )

    @cached_property
    def overlays(self) -> OverlaysResourceWithStreamingResponse:
        return OverlaysResourceWithStreamingResponse(self._streams.overlays)


class AsyncStreamsResourceWithStreamingResponse:
    def __init__(self, streams: AsyncStreamsResource) -> None:
        self._streams = streams

        self.create = async_to_streamed_response_wrapper(
            streams.create,
        )
        self.update = async_to_streamed_response_wrapper(
            streams.update,
        )
        self.list = async_to_streamed_response_wrapper(
            streams.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            streams.delete,
        )
        self.clear_dvr = async_to_streamed_response_wrapper(
            streams.clear_dvr,
        )
        self.create_clip = async_to_streamed_response_wrapper(
            streams.create_clip,
        )
        self.get = async_to_streamed_response_wrapper(
            streams.get,
        )
        self.list_clips = async_to_streamed_response_wrapper(
            streams.list_clips,
        )
        self.start_recording = async_to_streamed_response_wrapper(
            streams.start_recording,
        )
        self.stop_recording = async_to_streamed_response_wrapper(
            streams.stop_recording,
        )

    @cached_property
    def overlays(self) -> AsyncOverlaysResourceWithStreamingResponse:
        return AsyncOverlaysResourceWithStreamingResponse(self._streams.overlays)
