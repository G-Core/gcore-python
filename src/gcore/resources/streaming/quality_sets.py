# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.streaming import quality_set_set_default_params
from ...types.streaming.quality_sets import QualitySets

__all__ = ["QualitySetsResource", "AsyncQualitySetsResource"]


class QualitySetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QualitySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return QualitySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualitySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return QualitySetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualitySets:
        """
        Method returns a list of all custom quality sets.

        Transcoding is designed to minimize video file size while maintaining maximum
        visual quality. This is done so that the video can be delivered and viewed on
        any device, on any Internet connection, anywhere in the world. It's always a
        compromise between video/audio quality and delivery+viewing quality (QoE).

        Our experts have selected the optimal parameters for transcoding, to ensure
        maximum video/audio quality with the best compression. Default quality sets are
        described in the
        [documentation](/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-and-codecs#custom-quality-sets).
        These values are the default for everyone. There is no need to configure
        anything additional.

        Read more about qiality in our blog
        [How we lowered the bitrate for live and VOD streaming by 32.5% without sacrificing quality](https://gcore.com/blog/how-we-lowered-the-bitrate-for-live-and-vod-streaming-by-32-5-without-sacrificing-quality).

        ![Quality ladder](https://demo-files.gvideo.io/apidocs/encoding_ladder.png)

        Only for those cases when, in addition to the main parameters, it is necessary
        to use your own, then it is necessary to use custom quality sets.

        How to use:

        1. By default custom quality set is empty – `{ "live":[],"vod":[] }`
        2. Request the use of custom quality sets from your manager or the Support Team.
        3. Please forward your requirements to us, since the parameters are set not by
           you, but by our engineers. (We are working to ensure that later you can
           create qualities by yourself.)
        4. Use the created quality sets through the these specified API methods.

        Here are some common parameters of quality settings:

        - Resolution: Determines the size of the video frame. I.e. 720p, 1080p, 4K, etc.
        - Bitrate: Refers to the amount of data processed per unit of time.
        - Codec: Codec used for transcoding can significantly affect quality. Popular
          codecs include H.264 (AVC), H.265 (HEVC), and AV1.
        - Frame Rate: Determines how many frames per second are displayed. Common frame
          rates include 24fps, 30fps, and 60fps.
        - Color Depth and Chroma Subsampling: These settings determine the accuracy of
          color representation in the video.
        - Audio Bitrate and Codec: Don't forget about the audio :) Bitrate and codec
          used for audio can also affect the overall quality. Note: Custom quality set
          is a paid feature.
        """
        return self._get(
            "/streaming/quality_sets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualitySets,
        )

    def set_default(
        self,
        *,
        live: quality_set_set_default_params.Live | Omit = omit,
        vod: quality_set_set_default_params.Vod | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualitySets:
        """
        Method to set default quality set for VOD and Live transcoding.

        For changing default quality set, specify the ID of the custom quality set from
        the method GET /`quality_sets`.

        Default value can be reverted to the system defaults (cleared) by setting
        `"id": null`.

        Live transcoding management:

        - You can specify quality set explicitly in POST /streams method, look at
          attribute "`quality_set_id`".
        - Otherwise these default values will be used by the system by default.

        VOD transcoding management:

        - You can specify quality set explicitly in POST /videos method, look at
          attribute "`quality_set_id`".
        - Otherwise these default values will be used by the system by default.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/streaming/quality_sets/default",
            body=maybe_transform(
                {
                    "live": live,
                    "vod": vod,
                },
                quality_set_set_default_params.QualitySetSetDefaultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualitySets,
        )


class AsyncQualitySetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQualitySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualitySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualitySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncQualitySetsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualitySets:
        """
        Method returns a list of all custom quality sets.

        Transcoding is designed to minimize video file size while maintaining maximum
        visual quality. This is done so that the video can be delivered and viewed on
        any device, on any Internet connection, anywhere in the world. It's always a
        compromise between video/audio quality and delivery+viewing quality (QoE).

        Our experts have selected the optimal parameters for transcoding, to ensure
        maximum video/audio quality with the best compression. Default quality sets are
        described in the
        [documentation](/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-and-codecs#custom-quality-sets).
        These values are the default for everyone. There is no need to configure
        anything additional.

        Read more about qiality in our blog
        [How we lowered the bitrate for live and VOD streaming by 32.5% without sacrificing quality](https://gcore.com/blog/how-we-lowered-the-bitrate-for-live-and-vod-streaming-by-32-5-without-sacrificing-quality).

        ![Quality ladder](https://demo-files.gvideo.io/apidocs/encoding_ladder.png)

        Only for those cases when, in addition to the main parameters, it is necessary
        to use your own, then it is necessary to use custom quality sets.

        How to use:

        1. By default custom quality set is empty – `{ "live":[],"vod":[] }`
        2. Request the use of custom quality sets from your manager or the Support Team.
        3. Please forward your requirements to us, since the parameters are set not by
           you, but by our engineers. (We are working to ensure that later you can
           create qualities by yourself.)
        4. Use the created quality sets through the these specified API methods.

        Here are some common parameters of quality settings:

        - Resolution: Determines the size of the video frame. I.e. 720p, 1080p, 4K, etc.
        - Bitrate: Refers to the amount of data processed per unit of time.
        - Codec: Codec used for transcoding can significantly affect quality. Popular
          codecs include H.264 (AVC), H.265 (HEVC), and AV1.
        - Frame Rate: Determines how many frames per second are displayed. Common frame
          rates include 24fps, 30fps, and 60fps.
        - Color Depth and Chroma Subsampling: These settings determine the accuracy of
          color representation in the video.
        - Audio Bitrate and Codec: Don't forget about the audio :) Bitrate and codec
          used for audio can also affect the overall quality. Note: Custom quality set
          is a paid feature.
        """
        return await self._get(
            "/streaming/quality_sets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualitySets,
        )

    async def set_default(
        self,
        *,
        live: quality_set_set_default_params.Live | Omit = omit,
        vod: quality_set_set_default_params.Vod | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualitySets:
        """
        Method to set default quality set for VOD and Live transcoding.

        For changing default quality set, specify the ID of the custom quality set from
        the method GET /`quality_sets`.

        Default value can be reverted to the system defaults (cleared) by setting
        `"id": null`.

        Live transcoding management:

        - You can specify quality set explicitly in POST /streams method, look at
          attribute "`quality_set_id`".
        - Otherwise these default values will be used by the system by default.

        VOD transcoding management:

        - You can specify quality set explicitly in POST /videos method, look at
          attribute "`quality_set_id`".
        - Otherwise these default values will be used by the system by default.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/streaming/quality_sets/default",
            body=await async_maybe_transform(
                {
                    "live": live,
                    "vod": vod,
                },
                quality_set_set_default_params.QualitySetSetDefaultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualitySets,
        )


class QualitySetsResourceWithRawResponse:
    def __init__(self, quality_sets: QualitySetsResource) -> None:
        self._quality_sets = quality_sets

        self.list = to_raw_response_wrapper(
            quality_sets.list,
        )
        self.set_default = to_raw_response_wrapper(
            quality_sets.set_default,
        )


class AsyncQualitySetsResourceWithRawResponse:
    def __init__(self, quality_sets: AsyncQualitySetsResource) -> None:
        self._quality_sets = quality_sets

        self.list = async_to_raw_response_wrapper(
            quality_sets.list,
        )
        self.set_default = async_to_raw_response_wrapper(
            quality_sets.set_default,
        )


class QualitySetsResourceWithStreamingResponse:
    def __init__(self, quality_sets: QualitySetsResource) -> None:
        self._quality_sets = quality_sets

        self.list = to_streamed_response_wrapper(
            quality_sets.list,
        )
        self.set_default = to_streamed_response_wrapper(
            quality_sets.set_default,
        )


class AsyncQualitySetsResourceWithStreamingResponse:
    def __init__(self, quality_sets: AsyncQualitySetsResource) -> None:
        self._quality_sets = quality_sets

        self.list = async_to_streamed_response_wrapper(
            quality_sets.list,
        )
        self.set_default = async_to_streamed_response_wrapper(
            quality_sets.set_default,
        )
