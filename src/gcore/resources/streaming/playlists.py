# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPageStreaming, AsyncPageStreaming
from ..._base_client import AsyncPaginator, make_request_options
from ...types.streaming import playlist_list_params, playlist_create_params, playlist_update_params
from ...types.streaming.playlist import Playlist
from ...types.streaming.playlist_create import PlaylistCreate
from ...types.streaming.playlist_list_videos_response import PlaylistListVideosResponse

__all__ = ["PlaylistsResource", "AsyncPlaylistsResource"]


class PlaylistsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlaylistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PlaylistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaylistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PlaylistsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        active: bool | Omit = omit,
        ad_id: int | Omit = omit,
        client_id: int | Omit = omit,
        client_user_id: int | Omit = omit,
        countdown: bool | Omit = omit,
        hls_cmaf_url: str | Omit = omit,
        hls_url: str | Omit = omit,
        iframe_url: str | Omit = omit,
        loop: bool | Omit = omit,
        name: str | Omit = omit,
        player_id: int | Omit = omit,
        playlist_type: Literal["live", "vod"] | Omit = omit,
        start_time: str | Omit = omit,
        video_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaylistCreate:
        """
        Playlist is a curated collection of video content organized in a sequential
        manner.

        This method offers several advantages and features that are typical of live
        streaming but with more control over the content. Here's how it works:

        - Playlist always consists only of static VOD videos you previously uploaded to
          the system.
        - Playlist is always played as a "Live stream" for end-users, so without the
          ability to fast forward the stream to the “future”. Manifest will contain
          chunks as for live stream too.
        - Playlist can be looped endlessly. In this case, all the videos in the list
          will be constantly repeated through the list.
        - Playlist can be programmed to be played at a specific time in the future. In
          that case, before the start time there will be empty manifest.

        You can add new videos to the list, remove unnecessary videos, or change the
        order of videos in the list. But please pay attention to when the video list
        changes, it is updated instantly on the server. This means that after saving the
        changed list, the playlist will be reloaded for all users and it will start
        plays from the very first element.

        Maximum video limit = 128 videos in a row.

        Examples of usage:

        - Looped video playback
        - Scheduled playback

        **Looped video playback**

        It can be used to simulate TV channel pre-programmed behaviour.

        - Selection: Choose a series of videos, such as TV show episodes, movies,
          tutorials, or any other relevant content.
        - Order: Arrange the selected videos in the desired sequence, much like setting
          a broadcast schedule.
        - Looping: Optionally, the playlist can be set to loop, replaying the sequence
          once it finishes to maintain a continuous stream.

        Example:

        ```
          active: true
          loop: true
          name: "Playlist: TV channel 'The world around us' (Programmed broadcast for 24 hours)"
        ```

        **Scheduled playback**

        It can be used to simulate live events such as virtual concerts, webinars, or
        any special broadcasts without the logistical challenges of an actual live
        stream.

        - Timing: Set specific start time, creating the illusion of a live broadcast
          schedule.
        - Selection: Choose a video or series of videos to be played at the specified
          time.
        - No Pauses: Unlike on-demand streaming where users can pause and skip, this
          emulated live stream runs continuously, mirroring the constraints of
          traditional live broadcasts.

        ```
          active: true
          loop: false
          name: "Playlist: Webinar 'Onboarding for new employees on working with the corporate portal'"
          start_time: "2024-07-01T11:00:00Z"
        ```

        Args:
          active:
              Enables/Disables playlist. Has two possible values:

              - true – Playlist can be played.
              - false – Playlist is disabled. No broadcast while it's desabled.

          ad_id: The advertisement ID that will be inserted into the video

          client_id: Current playlist client ID

          client_user_id: Custom field where you can specify user ID in your system

          countdown: Enables countdown before playlist start with `playlist_type: live`

          hls_cmaf_url: A URL to a master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks. Chunks
              are in fMP4 container.

              It is possible to use the same suffix-options as described in the "`hls_url`"
              attribute.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          hls_url: A URL to a master playlist HLS (master.m3u8) with MPEG TS container.

              This URL is a link to the main manifest. But you can also manually specify
              suffix-options that will allow you to change the manifest to your request:
              `/playlists/{client_id}_{playlist_id}/master[-cmaf][-min-N][-max-N][-img][-(h264|hevc|av1)].m3u8`
              Please see the details in `hls_url` attribute of /videos/{id} method.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          iframe_url: A URL to a built-in HTML video player with the video inside. It can be inserted
              into an iframe on your website and the video will automatically play in all
              browsers.

              The player can be opened or shared via this direct link. Also the video player
              can be integrated into your web pages using the Iframe tag.

              Please see the details in `iframe_url` attribute of /videos/{id} method.

          loop: Enables/Disables playlist loop

          name: Playlist name

          player_id: The player ID with which the video will be played

          playlist_type:
              Determines whether the playlist:

              - `live` - playlist for live-streaming
              - `vod` - playlist is for video on demand access

          start_time: Playlist start time. Playlist won't be available before the specified time.
              Datetime in ISO 8601 format.

          video_ids: A list of VOD IDs included in the playlist. Order of videos in a playlist
              reflects the order of IDs in the array.

              Maximum video limit = 128.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/streaming/playlists",
            body=maybe_transform(
                {
                    "active": active,
                    "ad_id": ad_id,
                    "client_id": client_id,
                    "client_user_id": client_user_id,
                    "countdown": countdown,
                    "hls_cmaf_url": hls_cmaf_url,
                    "hls_url": hls_url,
                    "iframe_url": iframe_url,
                    "loop": loop,
                    "name": name,
                    "player_id": player_id,
                    "playlist_type": playlist_type,
                    "start_time": start_time,
                    "video_ids": video_ids,
                },
                playlist_create_params.PlaylistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaylistCreate,
        )

    def update(
        self,
        playlist_id: int,
        *,
        active: bool | Omit = omit,
        ad_id: int | Omit = omit,
        client_id: int | Omit = omit,
        client_user_id: int | Omit = omit,
        countdown: bool | Omit = omit,
        hls_cmaf_url: str | Omit = omit,
        hls_url: str | Omit = omit,
        iframe_url: str | Omit = omit,
        loop: bool | Omit = omit,
        name: str | Omit = omit,
        player_id: int | Omit = omit,
        playlist_type: Literal["live", "vod"] | Omit = omit,
        start_time: str | Omit = omit,
        video_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Playlist:
        """Change playlist

        Args:
          active:
              Enables/Disables playlist.

        Has two possible values:

              - true – Playlist can be played.
              - false – Playlist is disabled. No broadcast while it's desabled.

          ad_id: The advertisement ID that will be inserted into the video

          client_id: Current playlist client ID

          client_user_id: Custom field where you can specify user ID in your system

          countdown: Enables countdown before playlist start with `playlist_type: live`

          hls_cmaf_url: A URL to a master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks. Chunks
              are in fMP4 container.

              It is possible to use the same suffix-options as described in the "`hls_url`"
              attribute.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          hls_url: A URL to a master playlist HLS (master.m3u8) with MPEG TS container.

              This URL is a link to the main manifest. But you can also manually specify
              suffix-options that will allow you to change the manifest to your request:
              `/playlists/{client_id}_{playlist_id}/master[-cmaf][-min-N][-max-N][-img][-(h264|hevc|av1)].m3u8`
              Please see the details in `hls_url` attribute of /videos/{id} method.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          iframe_url: A URL to a built-in HTML video player with the video inside. It can be inserted
              into an iframe on your website and the video will automatically play in all
              browsers.

              The player can be opened or shared via this direct link. Also the video player
              can be integrated into your web pages using the Iframe tag.

              Please see the details in `iframe_url` attribute of /videos/{id} method.

          loop: Enables/Disables playlist loop

          name: Playlist name

          player_id: The player ID with which the video will be played

          playlist_type:
              Determines whether the playlist:

              - `live` - playlist for live-streaming
              - `vod` - playlist is for video on demand access

          start_time: Playlist start time. Playlist won't be available before the specified time.
              Datetime in ISO 8601 format.

          video_ids: A list of VOD IDs included in the playlist. Order of videos in a playlist
              reflects the order of IDs in the array.

              Maximum video limit = 128.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/streaming/playlists/{playlist_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "ad_id": ad_id,
                    "client_id": client_id,
                    "client_user_id": client_user_id,
                    "countdown": countdown,
                    "hls_cmaf_url": hls_cmaf_url,
                    "hls_url": hls_url,
                    "iframe_url": iframe_url,
                    "loop": loop,
                    "name": name,
                    "player_id": player_id,
                    "playlist_type": playlist_type,
                    "start_time": start_time,
                    "video_ids": video_ids,
                },
                playlist_update_params.PlaylistUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Playlist,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageStreaming[Playlist]:
        """Returns a list of created playlists

        Args:
          page: Query parameter.

        Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/playlists",
            page=SyncPageStreaming[Playlist],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, playlist_list_params.PlaylistListParams),
            ),
            model=Playlist,
        )

    def delete(
        self,
        playlist_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete playlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/streaming/playlists/{playlist_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        playlist_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Playlist:
        """
        Returns a playlist details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/playlists/{playlist_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Playlist,
        )

    def list_videos(
        self,
        playlist_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaylistListVideosResponse:
        """
        Shows ordered array of playlist videos

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/streaming/playlists/{playlist_id}/videos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaylistListVideosResponse,
        )


class AsyncPlaylistsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlaylistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaylistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaylistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPlaylistsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        active: bool | Omit = omit,
        ad_id: int | Omit = omit,
        client_id: int | Omit = omit,
        client_user_id: int | Omit = omit,
        countdown: bool | Omit = omit,
        hls_cmaf_url: str | Omit = omit,
        hls_url: str | Omit = omit,
        iframe_url: str | Omit = omit,
        loop: bool | Omit = omit,
        name: str | Omit = omit,
        player_id: int | Omit = omit,
        playlist_type: Literal["live", "vod"] | Omit = omit,
        start_time: str | Omit = omit,
        video_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaylistCreate:
        """
        Playlist is a curated collection of video content organized in a sequential
        manner.

        This method offers several advantages and features that are typical of live
        streaming but with more control over the content. Here's how it works:

        - Playlist always consists only of static VOD videos you previously uploaded to
          the system.
        - Playlist is always played as a "Live stream" for end-users, so without the
          ability to fast forward the stream to the “future”. Manifest will contain
          chunks as for live stream too.
        - Playlist can be looped endlessly. In this case, all the videos in the list
          will be constantly repeated through the list.
        - Playlist can be programmed to be played at a specific time in the future. In
          that case, before the start time there will be empty manifest.

        You can add new videos to the list, remove unnecessary videos, or change the
        order of videos in the list. But please pay attention to when the video list
        changes, it is updated instantly on the server. This means that after saving the
        changed list, the playlist will be reloaded for all users and it will start
        plays from the very first element.

        Maximum video limit = 128 videos in a row.

        Examples of usage:

        - Looped video playback
        - Scheduled playback

        **Looped video playback**

        It can be used to simulate TV channel pre-programmed behaviour.

        - Selection: Choose a series of videos, such as TV show episodes, movies,
          tutorials, or any other relevant content.
        - Order: Arrange the selected videos in the desired sequence, much like setting
          a broadcast schedule.
        - Looping: Optionally, the playlist can be set to loop, replaying the sequence
          once it finishes to maintain a continuous stream.

        Example:

        ```
          active: true
          loop: true
          name: "Playlist: TV channel 'The world around us' (Programmed broadcast for 24 hours)"
        ```

        **Scheduled playback**

        It can be used to simulate live events such as virtual concerts, webinars, or
        any special broadcasts without the logistical challenges of an actual live
        stream.

        - Timing: Set specific start time, creating the illusion of a live broadcast
          schedule.
        - Selection: Choose a video or series of videos to be played at the specified
          time.
        - No Pauses: Unlike on-demand streaming where users can pause and skip, this
          emulated live stream runs continuously, mirroring the constraints of
          traditional live broadcasts.

        ```
          active: true
          loop: false
          name: "Playlist: Webinar 'Onboarding for new employees on working with the corporate portal'"
          start_time: "2024-07-01T11:00:00Z"
        ```

        Args:
          active:
              Enables/Disables playlist. Has two possible values:

              - true – Playlist can be played.
              - false – Playlist is disabled. No broadcast while it's desabled.

          ad_id: The advertisement ID that will be inserted into the video

          client_id: Current playlist client ID

          client_user_id: Custom field where you can specify user ID in your system

          countdown: Enables countdown before playlist start with `playlist_type: live`

          hls_cmaf_url: A URL to a master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks. Chunks
              are in fMP4 container.

              It is possible to use the same suffix-options as described in the "`hls_url`"
              attribute.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          hls_url: A URL to a master playlist HLS (master.m3u8) with MPEG TS container.

              This URL is a link to the main manifest. But you can also manually specify
              suffix-options that will allow you to change the manifest to your request:
              `/playlists/{client_id}_{playlist_id}/master[-cmaf][-min-N][-max-N][-img][-(h264|hevc|av1)].m3u8`
              Please see the details in `hls_url` attribute of /videos/{id} method.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          iframe_url: A URL to a built-in HTML video player with the video inside. It can be inserted
              into an iframe on your website and the video will automatically play in all
              browsers.

              The player can be opened or shared via this direct link. Also the video player
              can be integrated into your web pages using the Iframe tag.

              Please see the details in `iframe_url` attribute of /videos/{id} method.

          loop: Enables/Disables playlist loop

          name: Playlist name

          player_id: The player ID with which the video will be played

          playlist_type:
              Determines whether the playlist:

              - `live` - playlist for live-streaming
              - `vod` - playlist is for video on demand access

          start_time: Playlist start time. Playlist won't be available before the specified time.
              Datetime in ISO 8601 format.

          video_ids: A list of VOD IDs included in the playlist. Order of videos in a playlist
              reflects the order of IDs in the array.

              Maximum video limit = 128.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/streaming/playlists",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "ad_id": ad_id,
                    "client_id": client_id,
                    "client_user_id": client_user_id,
                    "countdown": countdown,
                    "hls_cmaf_url": hls_cmaf_url,
                    "hls_url": hls_url,
                    "iframe_url": iframe_url,
                    "loop": loop,
                    "name": name,
                    "player_id": player_id,
                    "playlist_type": playlist_type,
                    "start_time": start_time,
                    "video_ids": video_ids,
                },
                playlist_create_params.PlaylistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaylistCreate,
        )

    async def update(
        self,
        playlist_id: int,
        *,
        active: bool | Omit = omit,
        ad_id: int | Omit = omit,
        client_id: int | Omit = omit,
        client_user_id: int | Omit = omit,
        countdown: bool | Omit = omit,
        hls_cmaf_url: str | Omit = omit,
        hls_url: str | Omit = omit,
        iframe_url: str | Omit = omit,
        loop: bool | Omit = omit,
        name: str | Omit = omit,
        player_id: int | Omit = omit,
        playlist_type: Literal["live", "vod"] | Omit = omit,
        start_time: str | Omit = omit,
        video_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Playlist:
        """Change playlist

        Args:
          active:
              Enables/Disables playlist.

        Has two possible values:

              - true – Playlist can be played.
              - false – Playlist is disabled. No broadcast while it's desabled.

          ad_id: The advertisement ID that will be inserted into the video

          client_id: Current playlist client ID

          client_user_id: Custom field where you can specify user ID in your system

          countdown: Enables countdown before playlist start with `playlist_type: live`

          hls_cmaf_url: A URL to a master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks. Chunks
              are in fMP4 container.

              It is possible to use the same suffix-options as described in the "`hls_url`"
              attribute.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          hls_url: A URL to a master playlist HLS (master.m3u8) with MPEG TS container.

              This URL is a link to the main manifest. But you can also manually specify
              suffix-options that will allow you to change the manifest to your request:
              `/playlists/{client_id}_{playlist_id}/master[-cmaf][-min-N][-max-N][-img][-(h264|hevc|av1)].m3u8`
              Please see the details in `hls_url` attribute of /videos/{id} method.

              Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
              and intended for your use. Any additional internal manifests, sub-manifests,
              parameters, chunk names, file extensions, and related components are internal
              infrastructure entities. These may undergo modifications without prior notice,
              in any manner or form. It is strongly advised not to store them in your database
              or cache them on your end.

          iframe_url: A URL to a built-in HTML video player with the video inside. It can be inserted
              into an iframe on your website and the video will automatically play in all
              browsers.

              The player can be opened or shared via this direct link. Also the video player
              can be integrated into your web pages using the Iframe tag.

              Please see the details in `iframe_url` attribute of /videos/{id} method.

          loop: Enables/Disables playlist loop

          name: Playlist name

          player_id: The player ID with which the video will be played

          playlist_type:
              Determines whether the playlist:

              - `live` - playlist for live-streaming
              - `vod` - playlist is for video on demand access

          start_time: Playlist start time. Playlist won't be available before the specified time.
              Datetime in ISO 8601 format.

          video_ids: A list of VOD IDs included in the playlist. Order of videos in a playlist
              reflects the order of IDs in the array.

              Maximum video limit = 128.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/streaming/playlists/{playlist_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "ad_id": ad_id,
                    "client_id": client_id,
                    "client_user_id": client_user_id,
                    "countdown": countdown,
                    "hls_cmaf_url": hls_cmaf_url,
                    "hls_url": hls_url,
                    "iframe_url": iframe_url,
                    "loop": loop,
                    "name": name,
                    "player_id": player_id,
                    "playlist_type": playlist_type,
                    "start_time": start_time,
                    "video_ids": video_ids,
                },
                playlist_update_params.PlaylistUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Playlist,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Playlist, AsyncPageStreaming[Playlist]]:
        """Returns a list of created playlists

        Args:
          page: Query parameter.

        Use it to list the paginated content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/playlists",
            page=AsyncPageStreaming[Playlist],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, playlist_list_params.PlaylistListParams),
            ),
            model=Playlist,
        )

    async def delete(
        self,
        playlist_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete playlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/streaming/playlists/{playlist_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        playlist_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Playlist:
        """
        Returns a playlist details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/playlists/{playlist_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Playlist,
        )

    async def list_videos(
        self,
        playlist_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaylistListVideosResponse:
        """
        Shows ordered array of playlist videos

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/streaming/playlists/{playlist_id}/videos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaylistListVideosResponse,
        )


class PlaylistsResourceWithRawResponse:
    def __init__(self, playlists: PlaylistsResource) -> None:
        self._playlists = playlists

        self.create = to_raw_response_wrapper(
            playlists.create,
        )
        self.update = to_raw_response_wrapper(
            playlists.update,
        )
        self.list = to_raw_response_wrapper(
            playlists.list,
        )
        self.delete = to_raw_response_wrapper(
            playlists.delete,
        )
        self.get = to_raw_response_wrapper(
            playlists.get,
        )
        self.list_videos = to_raw_response_wrapper(
            playlists.list_videos,
        )


class AsyncPlaylistsResourceWithRawResponse:
    def __init__(self, playlists: AsyncPlaylistsResource) -> None:
        self._playlists = playlists

        self.create = async_to_raw_response_wrapper(
            playlists.create,
        )
        self.update = async_to_raw_response_wrapper(
            playlists.update,
        )
        self.list = async_to_raw_response_wrapper(
            playlists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            playlists.delete,
        )
        self.get = async_to_raw_response_wrapper(
            playlists.get,
        )
        self.list_videos = async_to_raw_response_wrapper(
            playlists.list_videos,
        )


class PlaylistsResourceWithStreamingResponse:
    def __init__(self, playlists: PlaylistsResource) -> None:
        self._playlists = playlists

        self.create = to_streamed_response_wrapper(
            playlists.create,
        )
        self.update = to_streamed_response_wrapper(
            playlists.update,
        )
        self.list = to_streamed_response_wrapper(
            playlists.list,
        )
        self.delete = to_streamed_response_wrapper(
            playlists.delete,
        )
        self.get = to_streamed_response_wrapper(
            playlists.get,
        )
        self.list_videos = to_streamed_response_wrapper(
            playlists.list_videos,
        )


class AsyncPlaylistsResourceWithStreamingResponse:
    def __init__(self, playlists: AsyncPlaylistsResource) -> None:
        self._playlists = playlists

        self.create = async_to_streamed_response_wrapper(
            playlists.create,
        )
        self.update = async_to_streamed_response_wrapper(
            playlists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            playlists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            playlists.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            playlists.get,
        )
        self.list_videos = async_to_streamed_response_wrapper(
            playlists.list_videos,
        )
