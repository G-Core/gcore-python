# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.streaming.streams import clip_create_params
from ....types.streaming.streams.clip import Clip
from ....types.streaming.streams.clip_list_response import ClipListResponse

__all__ = ["ClipsResource", "AsyncClipsResource"]


class ClipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ClipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ClipsResourceWithStreamingResponse(self)

    def create(
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
        "dvr_enabled: true". The DVR serves as a source for creating clips:

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
              Therefore, to change the maximum, use "dvr_duration" parameter of this stream.

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
            path_template("/streaming/streams/{stream_id}/clip_recording", stream_id=stream_id),
            body=maybe_transform(
                {
                    "duration": duration,
                    "expiration": expiration,
                    "start": start,
                    "vod_required": vod_required,
                },
                clip_create_params.ClipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Clip,
        )

    def list(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClipListResponse:
        """
        Get list of non expired instant clips for a stream.

        You can now use both MP4 just-in-time packager and HLS for all clips. Get URLs
        from "hls_master" and "mp4_master".

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
            path_template("/streaming/streams/{stream_id}/clip_recording", stream_id=stream_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClipListResponse,
        )


class AsyncClipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncClipsResourceWithStreamingResponse(self)

    async def create(
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
        "dvr_enabled: true". The DVR serves as a source for creating clips:

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
              Therefore, to change the maximum, use "dvr_duration" parameter of this stream.

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
            path_template("/streaming/streams/{stream_id}/clip_recording", stream_id=stream_id),
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "expiration": expiration,
                    "start": start,
                    "vod_required": vod_required,
                },
                clip_create_params.ClipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Clip,
        )

    async def list(
        self,
        stream_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClipListResponse:
        """
        Get list of non expired instant clips for a stream.

        You can now use both MP4 just-in-time packager and HLS for all clips. Get URLs
        from "hls_master" and "mp4_master".

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
            path_template("/streaming/streams/{stream_id}/clip_recording", stream_id=stream_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClipListResponse,
        )


class ClipsResourceWithRawResponse:
    def __init__(self, clips: ClipsResource) -> None:
        self._clips = clips

        self.create = to_raw_response_wrapper(
            clips.create,
        )
        self.list = to_raw_response_wrapper(
            clips.list,
        )


class AsyncClipsResourceWithRawResponse:
    def __init__(self, clips: AsyncClipsResource) -> None:
        self._clips = clips

        self.create = async_to_raw_response_wrapper(
            clips.create,
        )
        self.list = async_to_raw_response_wrapper(
            clips.list,
        )


class ClipsResourceWithStreamingResponse:
    def __init__(self, clips: ClipsResource) -> None:
        self._clips = clips

        self.create = to_streamed_response_wrapper(
            clips.create,
        )
        self.list = to_streamed_response_wrapper(
            clips.list,
        )


class AsyncClipsResourceWithStreamingResponse:
    def __init__(self, clips: AsyncClipsResource) -> None:
        self._clips = clips

        self.create = async_to_streamed_response_wrapper(
            clips.create,
        )
        self.list = async_to_streamed_response_wrapper(
            clips.list,
        )
