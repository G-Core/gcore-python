# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.streaming.videos import subtitle_create_params, subtitle_update_params
from ....types.streaming.subtitle import Subtitle
from ....types.streaming.subtitle_base import SubtitleBase
from ....types.streaming.videos.subtitle_list_response import SubtitleListResponse

__all__ = ["SubtitlesResource", "AsyncSubtitlesResource"]


class SubtitlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubtitlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SubtitlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubtitlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SubtitlesResourceWithStreamingResponse(self)

    def create(
        self,
        video_id: int,
        *,
        body: subtitle_create_params.Body,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subtitle:
        """
        Add new subtitle/captions to a video entity.

        **Add already exist subtitles**

        Subtitles must be in one of the following formats:

        - SRT – SubRip Text is described on
          [wikipedia.org](https://en.wikipedia.org/wiki/SubRip#SubRip_file_format). Must
          start from integer for sequence number. Use calidators to check the subtitles,
          like
          [srt-validator](https://taoning2014.github.io/srt-validator-website/index.html).
        - WebVTT – Web Video Text Tracks Format is described on
          [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API).
          Must start from "WEBVTT" header. Use validators to check the subtitles, like
          [W3C](https://w3c.github.io/webvtt.js/parser.html).

        Language is 3-letter language code according to ISO-639-2 (bibliographic code).
        Specify language you need, or just look at our list in the attribute
        "`audio_language`" of section
        ["AI Speech Recognition"](/docs/api-reference/streaming/ai/create-ai-asr-task).

        You can add multiple subtitles in the same language, language uniqueness is not
        required.

        Size must be up to 5Mb.

        The update time for added or changed subtitles is up to 30 seconds. Just like
        videos, subtitles are cached, so it takes time to update the data.

        **AI subtitles and transcribing**

        It is also possible to automatically create subtitles based on AI.

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
          subtitle will be generated for each specified language. The created AI-task(s)
          will be automatically executed, and result will also be automatically attached
          to this video as subtitle(s).

        If AI is disabled in your account, you will receive code 422 in response.

        **Where and how subtitles are displayed?**

        Subtitles are became available in the API response and in playback manifests.

        All added subtitles are automatically inserted into the output manifest .m3u8.
        This way, subtitles become available to any player: our player, OS built-in, or
        other specialized ones. You don't need to do anything else. Read more
        information in the Knowledge Base.

        Example:

        ```
        # EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs0",NAME="English",LANGUAGE="en",AUTOSELECT=YES,URI="subs-0.m3u8"
        ```

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/streaming/videos/{video_id}/subtitles",
            body=maybe_transform(body, subtitle_create_params.SubtitleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subtitle,
        )

    def update(
        self,
        id: int,
        *,
        video_id: int,
        language: str | Omit = omit,
        name: str | Omit = omit,
        vtt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubtitleBase:
        """
        Method to update subtitle of a video.

        You can update all or only some of fields you need.

        If you want to replace the text of subtitles (i.e. found a typo in the text, or
        the timing in the video changed), then:

        - download it using GET method,
        - change it in an external editor,
        - and update it using this PATCH method.

        Just like videos, subtitles are cached, so it takes time to update the data. See
        POST method for details.

        Args:
          language: 3-letter language code according to ISO-639-2 (bibliographic code)

          name: Name of subtitle file

          vtt: Full text of subtitles/captions, with escaped "\n" ("\r") symbol of new line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/videos/{video_id}/subtitles/{id}",
            body=maybe_transform(
                {
                    "language": language,
                    "name": name,
                    "vtt": vtt,
                },
                subtitle_update_params.SubtitleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleBase,
        )

    def list(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubtitleListResponse:
        """
        Method returns a list of all subtitles that are already attached to a video.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/videos/{video_id}/subtitles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        video_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete specified video subtitle

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/videos/{video_id}/subtitles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        video_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subtitle:
        """
        Returns information about a specific subtitle for a video.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/videos/{video_id}/subtitles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subtitle,
        )


class AsyncSubtitlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubtitlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubtitlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubtitlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSubtitlesResourceWithStreamingResponse(self)

    async def create(
        self,
        video_id: int,
        *,
        body: subtitle_create_params.Body,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subtitle:
        """
        Add new subtitle/captions to a video entity.

        **Add already exist subtitles**

        Subtitles must be in one of the following formats:

        - SRT – SubRip Text is described on
          [wikipedia.org](https://en.wikipedia.org/wiki/SubRip#SubRip_file_format). Must
          start from integer for sequence number. Use calidators to check the subtitles,
          like
          [srt-validator](https://taoning2014.github.io/srt-validator-website/index.html).
        - WebVTT – Web Video Text Tracks Format is described on
          [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API).
          Must start from "WEBVTT" header. Use validators to check the subtitles, like
          [W3C](https://w3c.github.io/webvtt.js/parser.html).

        Language is 3-letter language code according to ISO-639-2 (bibliographic code).
        Specify language you need, or just look at our list in the attribute
        "`audio_language`" of section
        ["AI Speech Recognition"](/docs/api-reference/streaming/ai/create-ai-asr-task).

        You can add multiple subtitles in the same language, language uniqueness is not
        required.

        Size must be up to 5Mb.

        The update time for added or changed subtitles is up to 30 seconds. Just like
        videos, subtitles are cached, so it takes time to update the data.

        **AI subtitles and transcribing**

        It is also possible to automatically create subtitles based on AI.

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
          subtitle will be generated for each specified language. The created AI-task(s)
          will be automatically executed, and result will also be automatically attached
          to this video as subtitle(s).

        If AI is disabled in your account, you will receive code 422 in response.

        **Where and how subtitles are displayed?**

        Subtitles are became available in the API response and in playback manifests.

        All added subtitles are automatically inserted into the output manifest .m3u8.
        This way, subtitles become available to any player: our player, OS built-in, or
        other specialized ones. You don't need to do anything else. Read more
        information in the Knowledge Base.

        Example:

        ```
        # EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs0",NAME="English",LANGUAGE="en",AUTOSELECT=YES,URI="subs-0.m3u8"
        ```

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/streaming/videos/{video_id}/subtitles",
            body=await async_maybe_transform(body, subtitle_create_params.SubtitleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subtitle,
        )

    async def update(
        self,
        id: int,
        *,
        video_id: int,
        language: str | Omit = omit,
        name: str | Omit = omit,
        vtt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubtitleBase:
        """
        Method to update subtitle of a video.

        You can update all or only some of fields you need.

        If you want to replace the text of subtitles (i.e. found a typo in the text, or
        the timing in the video changed), then:

        - download it using GET method,
        - change it in an external editor,
        - and update it using this PATCH method.

        Just like videos, subtitles are cached, so it takes time to update the data. See
        POST method for details.

        Args:
          language: 3-letter language code according to ISO-639-2 (bibliographic code)

          name: Name of subtitle file

          vtt: Full text of subtitles/captions, with escaped "\n" ("\r") symbol of new line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/videos/{video_id}/subtitles/{id}",
            body=await async_maybe_transform(
                {
                    "language": language,
                    "name": name,
                    "vtt": vtt,
                },
                subtitle_update_params.SubtitleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleBase,
        )

    async def list(
        self,
        video_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubtitleListResponse:
        """
        Method returns a list of all subtitles that are already attached to a video.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/videos/{video_id}/subtitles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        video_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete specified video subtitle

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/videos/{video_id}/subtitles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        video_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subtitle:
        """
        Returns information about a specific subtitle for a video.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/videos/{video_id}/subtitles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subtitle,
        )


class SubtitlesResourceWithRawResponse:
    def __init__(self, subtitles: SubtitlesResource) -> None:
        self._subtitles = subtitles

        self.create = to_raw_response_wrapper(
            subtitles.create,
        )
        self.update = to_raw_response_wrapper(
            subtitles.update,
        )
        self.list = to_raw_response_wrapper(
            subtitles.list,
        )
        self.delete = to_raw_response_wrapper(
            subtitles.delete,
        )
        self.get = to_raw_response_wrapper(
            subtitles.get,
        )


class AsyncSubtitlesResourceWithRawResponse:
    def __init__(self, subtitles: AsyncSubtitlesResource) -> None:
        self._subtitles = subtitles

        self.create = async_to_raw_response_wrapper(
            subtitles.create,
        )
        self.update = async_to_raw_response_wrapper(
            subtitles.update,
        )
        self.list = async_to_raw_response_wrapper(
            subtitles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subtitles.delete,
        )
        self.get = async_to_raw_response_wrapper(
            subtitles.get,
        )


class SubtitlesResourceWithStreamingResponse:
    def __init__(self, subtitles: SubtitlesResource) -> None:
        self._subtitles = subtitles

        self.create = to_streamed_response_wrapper(
            subtitles.create,
        )
        self.update = to_streamed_response_wrapper(
            subtitles.update,
        )
        self.list = to_streamed_response_wrapper(
            subtitles.list,
        )
        self.delete = to_streamed_response_wrapper(
            subtitles.delete,
        )
        self.get = to_streamed_response_wrapper(
            subtitles.get,
        )


class AsyncSubtitlesResourceWithStreamingResponse:
    def __init__(self, subtitles: AsyncSubtitlesResource) -> None:
        self._subtitles = subtitles

        self.create = async_to_streamed_response_wrapper(
            subtitles.create,
        )
        self.update = async_to_streamed_response_wrapper(
            subtitles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subtitles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subtitles.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            subtitles.get,
        )
