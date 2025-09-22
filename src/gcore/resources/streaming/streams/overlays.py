# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ...._base_client import make_request_options
from ....types.streaming.streams import overlay_create_params, overlay_update_params, overlay_update_multiple_params
from ....types.streaming.streams.overlay import Overlay
from ....types.streaming.streams.overlay_list_response import OverlayListResponse
from ....types.streaming.streams.overlay_create_response import OverlayCreateResponse
from ....types.streaming.streams.overlay_update_multiple_response import OverlayUpdateMultipleResponse

__all__ = ["OverlaysResource", "AsyncOverlaysResource"]


class OverlaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverlaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return OverlaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverlaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return OverlaysResourceWithStreamingResponse(self)

    def create(
        self,
        stream_id: int,
        *,
        body: Iterable[overlay_create_params.Body] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverlayCreateResponse:
        """
        "Overlay" is a live HTML widget, which rendered and inserted over the live
        stream.

        There are can be more that 1 overlay over a stream, which are small or stretched
        over full frame. Overlays can have transparent areas. Frequency of update is 1
        FPS. Automatic size scaling for Adaptative Bitrate qualities is applied.

        ![HTML Overlays](https://demo-files.gvideo.io/apidocs/coffee_run_overlays.gif)

        How to activate and use in simple steps:

        - Activate feature on your account, ask the Support Team
        - Set “`html_overlay`” attribute to "true" for a stream
        - Set array of overlays
        - Start or restart your stream again
        - Enjoy :-)

        For the first time an overlay should be enabled **before** start pushing of a
        live stream. If you are pushing the stream already (stream is alive and you are
        activating overlay for the first time), then overlay will become active after
        restart pushing.

        Once you activate the overlay for the stream for the first time, you can add,
        change, move, delete widgets on the fly even during a live stream with no
        affection on a result stream.

        Tech limits:

        - Max original stream resolution = FullHD.
        - It is necessary that all widgets must fit into the original frame of the
          source stream (width x height). If one of the widgets does not fit into the
          original frame, for example, goes 1 pixel beyond the frame, then all widgets
          will be hidden.
        - Attributes of overlays:
        - url – should be valid http/https url
        - 0 < width <= 1920
        - 0 < height <= 1080
        - 0 <= x < 1920
        - 0 <= y < 1080
        - stretch – stretch to full frame. Cannot be used with positioning attributes.
        - HTML widget can be access by HTTP 80 or HTTPS 443 ports.
        - HTML page code at the "url" link is read once when starting the stream only.
          For dynamically updating widgets, you must use either dynamic code via
          JavaScript or cause a page refresh via HTML meta tag
          <meta http-equiv="refresh" content="N">.
        - Widgets can contain scripts, but they must be lightweight and using small
          amount memory, CPU, and bandwidth. It is prohibited to run heavy scripts,
          create a heavy load on the network, or run other heavy modules. Such widgets
          can be stopped automatically, and the ability to insert widgets itself is
          banned.
        - If feature is disabled, you will receive HTTP code: 422. Error text: Feature
          disabled. Contact support to enable.

        Please, pay attention to the content of HTML widges you use. If you don't trust
        them, then you shouldn't use them, as their result will be displayed in live
        stream to all users.

        **Will there be a widget in the recording?** Right now overlay widgets are sent
        to the end viewer in the HLS/DASH streams, but are not recorded due to technical
        limitations. We are working to ensure that widgets remain in the recordings as
        well. Follow the news.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/streaming/streams/{stream_id}/overlays",
            body=maybe_transform(body, Iterable[overlay_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverlayCreateResponse,
        )

    def update(
        self,
        overlay_id: int,
        *,
        stream_id: int,
        height: int | Omit = omit,
        stretch: bool | Omit = omit,
        url: str | Omit = omit,
        width: int | Omit = omit,
        x: int | Omit = omit,
        y: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Overlay:
        """
        Updates overlay settings

        Args:
          height: Height of the widget

          stretch: Switch of auto scaling the widget. Must not be used as "true" simultaneously
              with the coordinate installation method (w, h, x, y).

          url: Valid http/https URL to an HTML page/widget

          width: Width of the widget

          x: Coordinate of left upper corner

          y: Coordinate of left upper corner

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/streams/{stream_id}/overlays/{overlay_id}",
            body=maybe_transform(
                {
                    "height": height,
                    "stretch": stretch,
                    "url": url,
                    "width": width,
                    "x": x,
                    "y": y,
                },
                overlay_update_params.OverlayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Overlay,
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
    ) -> OverlayListResponse:
        """
        Returns a list of HTML overlay widgets which are attached to a stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/streams/{stream_id}/overlays",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverlayListResponse,
        )

    def delete(
        self,
        overlay_id: int,
        *,
        stream_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an overlay

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/streams/{stream_id}/overlays/{overlay_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        overlay_id: int,
        *,
        stream_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Overlay:
        """
        Get overlay details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/streams/{stream_id}/overlays/{overlay_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Overlay,
        )

    def update_multiple(
        self,
        stream_id: int,
        *,
        body: Iterable[overlay_update_multiple_params.Body] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverlayUpdateMultipleResponse:
        """
        Updates settings for set of overlays

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/streams/{stream_id}/overlays",
            body=maybe_transform(body, Iterable[overlay_update_multiple_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverlayUpdateMultipleResponse,
        )


class AsyncOverlaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverlaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOverlaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverlaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncOverlaysResourceWithStreamingResponse(self)

    async def create(
        self,
        stream_id: int,
        *,
        body: Iterable[overlay_create_params.Body] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverlayCreateResponse:
        """
        "Overlay" is a live HTML widget, which rendered and inserted over the live
        stream.

        There are can be more that 1 overlay over a stream, which are small or stretched
        over full frame. Overlays can have transparent areas. Frequency of update is 1
        FPS. Automatic size scaling for Adaptative Bitrate qualities is applied.

        ![HTML Overlays](https://demo-files.gvideo.io/apidocs/coffee_run_overlays.gif)

        How to activate and use in simple steps:

        - Activate feature on your account, ask the Support Team
        - Set “`html_overlay`” attribute to "true" for a stream
        - Set array of overlays
        - Start or restart your stream again
        - Enjoy :-)

        For the first time an overlay should be enabled **before** start pushing of a
        live stream. If you are pushing the stream already (stream is alive and you are
        activating overlay for the first time), then overlay will become active after
        restart pushing.

        Once you activate the overlay for the stream for the first time, you can add,
        change, move, delete widgets on the fly even during a live stream with no
        affection on a result stream.

        Tech limits:

        - Max original stream resolution = FullHD.
        - It is necessary that all widgets must fit into the original frame of the
          source stream (width x height). If one of the widgets does not fit into the
          original frame, for example, goes 1 pixel beyond the frame, then all widgets
          will be hidden.
        - Attributes of overlays:
        - url – should be valid http/https url
        - 0 < width <= 1920
        - 0 < height <= 1080
        - 0 <= x < 1920
        - 0 <= y < 1080
        - stretch – stretch to full frame. Cannot be used with positioning attributes.
        - HTML widget can be access by HTTP 80 or HTTPS 443 ports.
        - HTML page code at the "url" link is read once when starting the stream only.
          For dynamically updating widgets, you must use either dynamic code via
          JavaScript or cause a page refresh via HTML meta tag
          <meta http-equiv="refresh" content="N">.
        - Widgets can contain scripts, but they must be lightweight and using small
          amount memory, CPU, and bandwidth. It is prohibited to run heavy scripts,
          create a heavy load on the network, or run other heavy modules. Such widgets
          can be stopped automatically, and the ability to insert widgets itself is
          banned.
        - If feature is disabled, you will receive HTTP code: 422. Error text: Feature
          disabled. Contact support to enable.

        Please, pay attention to the content of HTML widges you use. If you don't trust
        them, then you shouldn't use them, as their result will be displayed in live
        stream to all users.

        **Will there be a widget in the recording?** Right now overlay widgets are sent
        to the end viewer in the HLS/DASH streams, but are not recorded due to technical
        limitations. We are working to ensure that widgets remain in the recordings as
        well. Follow the news.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/streaming/streams/{stream_id}/overlays",
            body=await async_maybe_transform(body, Iterable[overlay_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverlayCreateResponse,
        )

    async def update(
        self,
        overlay_id: int,
        *,
        stream_id: int,
        height: int | Omit = omit,
        stretch: bool | Omit = omit,
        url: str | Omit = omit,
        width: int | Omit = omit,
        x: int | Omit = omit,
        y: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Overlay:
        """
        Updates overlay settings

        Args:
          height: Height of the widget

          stretch: Switch of auto scaling the widget. Must not be used as "true" simultaneously
              with the coordinate installation method (w, h, x, y).

          url: Valid http/https URL to an HTML page/widget

          width: Width of the widget

          x: Coordinate of left upper corner

          y: Coordinate of left upper corner

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/streams/{stream_id}/overlays/{overlay_id}",
            body=await async_maybe_transform(
                {
                    "height": height,
                    "stretch": stretch,
                    "url": url,
                    "width": width,
                    "x": x,
                    "y": y,
                },
                overlay_update_params.OverlayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Overlay,
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
    ) -> OverlayListResponse:
        """
        Returns a list of HTML overlay widgets which are attached to a stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/streams/{stream_id}/overlays",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverlayListResponse,
        )

    async def delete(
        self,
        overlay_id: int,
        *,
        stream_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an overlay

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/streams/{stream_id}/overlays/{overlay_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        overlay_id: int,
        *,
        stream_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Overlay:
        """
        Get overlay details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/streams/{stream_id}/overlays/{overlay_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Overlay,
        )

    async def update_multiple(
        self,
        stream_id: int,
        *,
        body: Iterable[overlay_update_multiple_params.Body] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverlayUpdateMultipleResponse:
        """
        Updates settings for set of overlays

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/streams/{stream_id}/overlays",
            body=await async_maybe_transform(body, Iterable[overlay_update_multiple_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverlayUpdateMultipleResponse,
        )


class OverlaysResourceWithRawResponse:
    def __init__(self, overlays: OverlaysResource) -> None:
        self._overlays = overlays

        self.create = to_raw_response_wrapper(
            overlays.create,
        )
        self.update = to_raw_response_wrapper(
            overlays.update,
        )
        self.list = to_raw_response_wrapper(
            overlays.list,
        )
        self.delete = to_raw_response_wrapper(
            overlays.delete,
        )
        self.get = to_raw_response_wrapper(
            overlays.get,
        )
        self.update_multiple = to_raw_response_wrapper(
            overlays.update_multiple,
        )


class AsyncOverlaysResourceWithRawResponse:
    def __init__(self, overlays: AsyncOverlaysResource) -> None:
        self._overlays = overlays

        self.create = async_to_raw_response_wrapper(
            overlays.create,
        )
        self.update = async_to_raw_response_wrapper(
            overlays.update,
        )
        self.list = async_to_raw_response_wrapper(
            overlays.list,
        )
        self.delete = async_to_raw_response_wrapper(
            overlays.delete,
        )
        self.get = async_to_raw_response_wrapper(
            overlays.get,
        )
        self.update_multiple = async_to_raw_response_wrapper(
            overlays.update_multiple,
        )


class OverlaysResourceWithStreamingResponse:
    def __init__(self, overlays: OverlaysResource) -> None:
        self._overlays = overlays

        self.create = to_streamed_response_wrapper(
            overlays.create,
        )
        self.update = to_streamed_response_wrapper(
            overlays.update,
        )
        self.list = to_streamed_response_wrapper(
            overlays.list,
        )
        self.delete = to_streamed_response_wrapper(
            overlays.delete,
        )
        self.get = to_streamed_response_wrapper(
            overlays.get,
        )
        self.update_multiple = to_streamed_response_wrapper(
            overlays.update_multiple,
        )


class AsyncOverlaysResourceWithStreamingResponse:
    def __init__(self, overlays: AsyncOverlaysResource) -> None:
        self._overlays = overlays

        self.create = async_to_streamed_response_wrapper(
            overlays.create,
        )
        self.update = async_to_streamed_response_wrapper(
            overlays.update,
        )
        self.list = async_to_streamed_response_wrapper(
            overlays.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            overlays.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            overlays.get,
        )
        self.update_multiple = async_to_streamed_response_wrapper(
            overlays.update_multiple,
        )
