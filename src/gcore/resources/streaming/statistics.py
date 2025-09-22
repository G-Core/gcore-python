# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ...types.streaming import (
    statistic_get_views_params,
    statistic_get_ffprobes_params,
    statistic_get_stream_series_params,
    statistic_get_views_heatmap_params,
    statistic_get_popular_videos_params,
    statistic_get_storage_series_params,
    statistic_get_unique_viewers_params,
    statistic_get_views_by_region_params,
    statistic_get_views_by_country_params,
    statistic_get_views_by_referer_params,
    statistic_get_views_by_browsers_params,
    statistic_get_views_by_hostname_params,
    statistic_get_max_streams_series_params,
    statistic_get_unique_viewers_cdn_params,
    statistic_get_vod_storage_volume_params,
    statistic_get_vod_watch_time_cdn_params,
    statistic_get_live_unique_viewers_params,
    statistic_get_live_watch_time_cdn_params,
    statistic_get_vod_unique_viewers_cdn_params,
    statistic_get_vod_transcoding_duration_params,
    statistic_get_vod_watch_time_total_cdn_params,
    statistic_get_live_watch_time_total_cdn_params,
    statistic_get_views_by_operating_system_params,
)
from ...types.streaming.views import Views
from ...types.streaming.ffprobes import Ffprobes
from ...types.streaming.stream_series import StreamSeries
from ...types.streaming.views_heatmap import ViewsHeatmap
from ...types.streaming.popular_videos import PopularVideos
from ...types.streaming.storage_series import StorageSeries
from ...types.streaming.unique_viewers import UniqueViewers
from ...types.streaming.views_by_region import ViewsByRegion
from ...types.streaming.views_by_browser import ViewsByBrowser
from ...types.streaming.views_by_country import ViewsByCountry
from ...types.streaming.views_by_referer import ViewsByReferer
from ...types.streaming.max_stream_series import MaxStreamSeries
from ...types.streaming.views_by_hostname import ViewsByHostname
from ...types.streaming.unique_viewers_cdn import UniqueViewersCdn
from ...types.streaming.vod_statistics_series import VodStatisticsSeries
from ...types.streaming.views_by_operating_system import ViewsByOperatingSystem
from ...types.streaming.vod_total_stream_duration_series import VodTotalStreamDurationSeries
from ...types.streaming.statistic_get_live_unique_viewers_response import StatisticGetLiveUniqueViewersResponse
from ...types.streaming.statistic_get_vod_watch_time_total_cdn_response import StatisticGetVodWatchTimeTotalCdnResponse

__all__ = ["StatisticsResource", "AsyncStatisticsResource"]


class StatisticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return StatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return StatisticsResourceWithStreamingResponse(self)

    def get_ffprobes(
        self,
        *,
        date_from: str,
        date_to: str,
        stream_id: str,
        interval: int | Omit = omit,
        units: Literal["second", "minute", "hour", "day", "week", "month"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ffprobes:
        """
        Aggregates data for the specified video stream in the specified time interval.
        "interval" and "units" params working together to point aggregation interval.

        You can use this method to watch when stream was alive in time, and when it was
        off.

        Args:
          date_from: Start of time frame. Format is ISO 8601.

          date_to: End of time frame. Datetime in ISO 8601 format.

          stream_id: Stream ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/ffprobe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "stream_id": stream_id,
                        "interval": interval,
                        "units": units,
                    },
                    statistic_get_ffprobes_params.StatisticGetFfprobesParams,
                ),
            ),
            cast_to=Ffprobes,
        )

    def get_live_unique_viewers(
        self,
        *,
        from_: str,
        to: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        stream_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetLiveUniqueViewersResponse:
        """
        Calculates time series of unique viewers of Live streams via CDN.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Works similar to the method `/statistics/cdn/uniqs`. But this allows you to
        break down data with the specified granularity: minutes, hours, days.

        Based on this method, a graph of unique views in the Customer Portal is built.

        ![Unique viewers via CDN in Customer Portal](https://demo-files.gvideo.io/apidocs/cdn_unique_viewers.png)

        Args:
          from_: Start of time frame. Format is date time in ISO 8601

          to: End of time frame. Format is date time in ISO 8601

          client_user_id: Filter by "`client_user_id`"

          granularity: Specifies the time interval for grouping data

          stream_id: Filter by "`stream_id`"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/stream/viewers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "stream_id": stream_id,
                    },
                    statistic_get_live_unique_viewers_params.StatisticGetLiveUniqueViewersParams,
                ),
            ),
            cast_to=StatisticGetLiveUniqueViewersResponse,
        )

    def get_live_watch_time_cdn(
        self,
        *,
        from_: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d", "1mo"] | Omit = omit,
        stream_id: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamSeries:
        """Calculates a time series of live streams watching duration in minutes.

        Views of
        only those streams that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Please note that the result for each time interval is in minutes, it is rounded
        to the nearest upper integer. You cannot use the sum of all intervals as the
        total watch time value; instead, use the /total method.

        Args:
          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601.

          client_user_id: Filter by field "`client_user_id`"

          granularity: Data is grouped by the specified time interval

          stream_id: Filter by `stream_id`

          to: End of time frame. Datetime in ISO 8601 format. If omitted, then the current
              time is taken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/stream/watching_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "stream_id": stream_id,
                        "to": to,
                    },
                    statistic_get_live_watch_time_cdn_params.StatisticGetLiveWatchTimeCdnParams,
                ),
            ),
            cast_to=StreamSeries,
        )

    def get_live_watch_time_total_cdn(
        self,
        *,
        client_user_id: int | Omit = omit,
        from_: str | Omit = omit,
        stream_id: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodTotalStreamDurationSeries:
        """Calculates the total duration of live streams watching in minutes.

        Views of only
        those streams that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Args:
          client_user_id: Filter by field "`client_user_id`"

          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601. If omitted, the earliest start time for viewing is taken

          stream_id: Filter by `stream_id`

          to: End of time frame. Datetime in ISO 8601 format. If missed, then the current time
              is taken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/stream/watching_duration/total",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_user_id": client_user_id,
                        "from_": from_,
                        "stream_id": stream_id,
                        "to": to,
                    },
                    statistic_get_live_watch_time_total_cdn_params.StatisticGetLiveWatchTimeTotalCdnParams,
                ),
            ),
            cast_to=VodTotalStreamDurationSeries,
        )

    def get_max_streams_series(
        self,
        *,
        from_: str,
        to: str,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MaxStreamSeries:
        """Calculates time series of the amount of simultaneous streams.

        The data is
        updated near realtime.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          granularity: specifies the time interval for grouping data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/max_stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "granularity": granularity,
                    },
                    statistic_get_max_streams_series_params.StatisticGetMaxStreamsSeriesParams,
                ),
            ),
            cast_to=MaxStreamSeries,
        )

    def get_popular_videos(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PopularVideos:
        """
        Aggregates the number of views for all client videos, grouping them by id and
        sort from most popular to less in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/popular",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_popular_videos_params.StatisticGetPopularVideosParams,
                ),
            ),
            cast_to=PopularVideos,
        )

    def get_storage_series(
        self,
        *,
        from_: str,
        to: str,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StorageSeries:
        """
        Calculates time series of the size of disk space in bytes for all processed and
        undeleted client videos. The data is updated every 8 hours, it does not make
        sense to set the granulation less than 1 day.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          granularity: specifies the time interval for grouping data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "granularity": granularity,
                    },
                    statistic_get_storage_series_params.StatisticGetStorageSeriesParams,
                ),
            ),
            cast_to=StorageSeries,
        )

    def get_stream_series(
        self,
        *,
        from_: str,
        to: str,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamSeries:
        """Calculates time series of the transcoding minutes of all streams.

        The data is
        updated near realtime.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          granularity: specifies the time interval for grouping data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "granularity": granularity,
                    },
                    statistic_get_stream_series_params.StatisticGetStreamSeriesParams,
                ),
            ),
            cast_to=StreamSeries,
        )

    def get_unique_viewers(
        self,
        *,
        date_from: str,
        date_to: str,
        id: str | Omit = omit,
        country: str | Omit = omit,
        event: Literal["init", "start", "watch"] | Omit = omit,
        group: List[Literal["date", "host", "os", "browser", "platform", "ip", "country", "event", "id"]] | Omit = omit,
        host: str | Omit = omit,
        type: Literal["live", "vod", "playlist"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UniqueViewers:
        """
        Get the number of unique viewers in the built-in player.

        Counts the number of unique IPs.

        Allows flexible grouping and filtering. The fields in the response depend on the
        selected grouping.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          id: filter by entity's id

          country: filter by country

          event: filter by event's name

          group: group=1,2,4 OR group=1&group=2&group=3

          host: filter by host

          type: filter by entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/uniqs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "id": id,
                        "country": country,
                        "event": event,
                        "group": group,
                        "host": host,
                        "type": type,
                    },
                    statistic_get_unique_viewers_params.StatisticGetUniqueViewersParams,
                ),
            ),
            cast_to=UniqueViewers,
        )

    def get_unique_viewers_cdn(
        self,
        *,
        date_from: str,
        date_to: str,
        id: str | Omit = omit,
        type: Literal["live", "vod", "playlist"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UniqueViewersCdn:
        """Сounts the number of unique viewers of a video entity over CDN.

        It doesn't
        matter what player you used.

        All unique viewers for the specified period of time are counted.

        **How does it work?**

        Calculating the number of unique viewers for a Live stream or VOD over CDN
        involves aggregating and analyzing various metrics to ensure each individual
        viewer is counted only once, regardless of how many times they connect or
        disconnect during the stream.

        This method provides statistics for any video viewing by unique users,
        regardless of viewing method and a player you used. Thus, this is the most
        important difference from viewing through the built-in player:

        - In method /statistics/uniqs viewers of the built-in player are tracked only.
        - But this method tracks all viewers from everywhere.

        This method is a combination of two other Live and VOD detailed methods. If you
        need detailed information, then see the methods: `/statistics/stream/viewers`
        and `/statistics/vod/viewers`.

        **Data Processing and Deduplication**

        We us IP Address & User-Agent combination. Each unique combination of IP address
        and User-Agent string might be considered a unique viewer.

        This approach allows to accurately estimate the number of unique viewers.
        However, this is not foolproof due to NAT (Network Address Translation) and
        shared networks. Thus if your users fall under such restrictions, then the
        number of unique viewers may be higher than calculated.

        **Why is there no "Unique Views" method?**

        Based on CDN data, we can calculate the number of unique viewers only. Thus only
        your player will be able to count the number of unique views (clicks on the Play
        button) within the player session (i.e. how many times 1 unique viewer clicked
        the Play button within a unique player's session).

        Args:
          date_from: Start of time frame. Format is date time in ISO 8601.

          date_to: End of time frame. Format is date time in ISO 8601.

          id: Filter by entity's id. Put ID of a Live stream, VOD or a playlist to be
              calculated.

              If the value is omitted, then the calculation is done for all videos/streams of
              the specified type.

              When using this "id" parameter, be sure to specify the "type" parameter too. If
              you do not specify a type, the "id" will be ignored.

          type: Filter by entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/cdn/uniqs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "id": id,
                        "type": type,
                    },
                    statistic_get_unique_viewers_cdn_params.StatisticGetUniqueViewersCdnParams,
                ),
            ),
            cast_to=UniqueViewersCdn,
        )

    def get_views(
        self,
        *,
        date_from: str,
        date_to: str,
        id: str | Omit = omit,
        country: str | Omit = omit,
        event: Literal["init", "start", "watch"] | Omit = omit,
        group: List[Literal["host", "os", "browser", "platform", "ip", "country", "event", "id"]] | Omit = omit,
        host: str | Omit = omit,
        type: Literal["live", "vod", "playlist"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Views:
        """
        Get the number of views in the built-in player.

        Allows flexible grouping and filtering. The fields in the response depend on the
        selected grouping.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          id: filter by entity's id

          country: filter by country

          event: filter by event's name

          group: group=1,2,4 OR group=1&group=2&group=3

          host: filter by host

          type: filter by entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "id": id,
                        "country": country,
                        "event": event,
                        "group": group,
                        "host": host,
                        "type": type,
                    },
                    statistic_get_views_params.StatisticGetViewsParams,
                ),
            ),
            cast_to=Views,
        )

    def get_views_by_browsers(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByBrowser:
        """
        Aggregates the number of views for all client videos, grouping them by browsers
        in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/browsers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_browsers_params.StatisticGetViewsByBrowsersParams,
                ),
            ),
            cast_to=ViewsByBrowser,
        )

    def get_views_by_country(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByCountry:
        """
        Aggregates the number of views grouping them by country in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_country_params.StatisticGetViewsByCountryParams,
                ),
            ),
            cast_to=ViewsByCountry,
        )

    def get_views_by_hostname(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByHostname:
        """
        Aggregates the number of views, grouping them by "host" domain name the built-in
        player was embeded to.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/hosts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_hostname_params.StatisticGetViewsByHostnameParams,
                ),
            ),
            cast_to=ViewsByHostname,
        )

    def get_views_by_operating_system(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByOperatingSystem:
        """
        Aggregates the number of views for all client videos, grouping them by device
        OSs in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/systems",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_operating_system_params.StatisticGetViewsByOperatingSystemParams,
                ),
            ),
            cast_to=ViewsByOperatingSystem,
        )

    def get_views_by_referer(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByReferer:
        """
        Aggregates the number of views, grouping them by "referer" URL of pages the
        built-in player was embeded to.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/embeds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_referer_params.StatisticGetViewsByRefererParams,
                ),
            ),
            cast_to=ViewsByReferer,
        )

    def get_views_by_region(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByRegion:
        """
        Aggregates the number of views grouping them by regions of countries in the
        built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_region_params.StatisticGetViewsByRegionParams,
                ),
            ),
            cast_to=ViewsByRegion,
        )

    def get_views_heatmap(
        self,
        *,
        date_from: str,
        date_to: str,
        stream_id: str,
        type: Literal["live", "vod", "playlist"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsHeatmap:
        """
        Shows information about what part of the video your viewers watched in the
        built-in player.

        This way you can find out how many viewers started watching the video, and where
        they stopped watching instead of watching the entire video to the end.

        Has different format of response depends on query param "type".

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          stream_id: video streaming ID

          type: entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/heatmap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "stream_id": stream_id,
                        "type": type,
                    },
                    statistic_get_views_heatmap_params.StatisticGetViewsHeatmapParams,
                ),
            ),
            cast_to=ViewsHeatmap,
        )

    def get_vod_storage_volume(
        self,
        *,
        from_: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """
        Calculates time series of the duration in minutes for all processed and
        undeleted client videos.

        The data is updated every 8 hours, it does not make sense to set the granulation
        less than 1 day.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/vod/storage_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    statistic_get_vod_storage_volume_params.StatisticGetVodStorageVolumeParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    def get_vod_transcoding_duration(
        self,
        *,
        from_: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """
        Calculates time series of the transcoding time in minutes for all processed
        client videos.

        The data is updated every 8 hours, it does not make sense to set the granulation
        less than 1 day.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/vod/transcoding_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    statistic_get_vod_transcoding_duration_params.StatisticGetVodTranscodingDurationParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    def get_vod_unique_viewers_cdn(
        self,
        *,
        from_: str,
        to: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """
        Calculates time series of unique viewers of VOD via CDN.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Works similar to the method `/statistics/cdn/uniqs`. But this allows you to
        break down data with the specified granularity: minutes, hours, days.

        Based on this method, a graph of unique views in the Customer Portal is built.

        ![Unique viewers via CDN in Customer Portal](https://demo-files.gvideo.io/apidocs/cdn_unique_viewers.png)

        Args:
          from_: Start of time frame. Format is date time in ISO 8601

          to: End of time frame. Format is date time in ISO 8601

          client_user_id: Filter by user "id"

          granularity: Specifies the time interval for grouping data

          slug: Filter by video "slug"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/vod/viewers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "slug": slug,
                    },
                    statistic_get_vod_unique_viewers_cdn_params.StatisticGetVodUniqueViewersCdnParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    def get_vod_watch_time_cdn(
        self,
        *,
        from_: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d", "1mo"] | Omit = omit,
        slug: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """Calculates a time series of video watching duration in minutes.

        Views of only
        those videos that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Please note that the result for each time interval is in minutes, it is rounded
        to the nearest upper integer. You cannot use the sum of all intervals as the
        total watch time value; instead, use the /total method.

        Args:
          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601.

          client_user_id: Filter by field "`client_user_id`"

          granularity: Data is grouped by the specified time interval

          slug: Filter by video's slug

          to: End of time frame. Datetime in ISO 8601 format. If omitted, then the current
              time is taken.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/vod/watching_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "slug": slug,
                        "to": to,
                    },
                    statistic_get_vod_watch_time_cdn_params.StatisticGetVodWatchTimeCdnParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    def get_vod_watch_time_total_cdn(
        self,
        *,
        client_user_id: int | Omit = omit,
        from_: str | Omit = omit,
        slug: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetVodWatchTimeTotalCdnResponse:
        """Calculates the total duration of video watching in minutes.

        Views of only those
        videos that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Args:
          client_user_id: Filter by field "`client_user_id`"

          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601. If omitted, the earliest start time for viewing is taken

          slug: Filter by video's slug

          to: End of time frame. Datetime in ISO 8601 format. If omitted, then the current
              time is taken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/statistics/vod/watching_duration/total",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_user_id": client_user_id,
                        "from_": from_,
                        "slug": slug,
                        "to": to,
                    },
                    statistic_get_vod_watch_time_total_cdn_params.StatisticGetVodWatchTimeTotalCdnParams,
                ),
            ),
            cast_to=StatisticGetVodWatchTimeTotalCdnResponse,
        )


class AsyncStatisticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncStatisticsResourceWithStreamingResponse(self)

    async def get_ffprobes(
        self,
        *,
        date_from: str,
        date_to: str,
        stream_id: str,
        interval: int | Omit = omit,
        units: Literal["second", "minute", "hour", "day", "week", "month"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ffprobes:
        """
        Aggregates data for the specified video stream in the specified time interval.
        "interval" and "units" params working together to point aggregation interval.

        You can use this method to watch when stream was alive in time, and when it was
        off.

        Args:
          date_from: Start of time frame. Format is ISO 8601.

          date_to: End of time frame. Datetime in ISO 8601 format.

          stream_id: Stream ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/ffprobe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "stream_id": stream_id,
                        "interval": interval,
                        "units": units,
                    },
                    statistic_get_ffprobes_params.StatisticGetFfprobesParams,
                ),
            ),
            cast_to=Ffprobes,
        )

    async def get_live_unique_viewers(
        self,
        *,
        from_: str,
        to: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        stream_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetLiveUniqueViewersResponse:
        """
        Calculates time series of unique viewers of Live streams via CDN.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Works similar to the method `/statistics/cdn/uniqs`. But this allows you to
        break down data with the specified granularity: minutes, hours, days.

        Based on this method, a graph of unique views in the Customer Portal is built.

        ![Unique viewers via CDN in Customer Portal](https://demo-files.gvideo.io/apidocs/cdn_unique_viewers.png)

        Args:
          from_: Start of time frame. Format is date time in ISO 8601

          to: End of time frame. Format is date time in ISO 8601

          client_user_id: Filter by "`client_user_id`"

          granularity: Specifies the time interval for grouping data

          stream_id: Filter by "`stream_id`"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/stream/viewers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "stream_id": stream_id,
                    },
                    statistic_get_live_unique_viewers_params.StatisticGetLiveUniqueViewersParams,
                ),
            ),
            cast_to=StatisticGetLiveUniqueViewersResponse,
        )

    async def get_live_watch_time_cdn(
        self,
        *,
        from_: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d", "1mo"] | Omit = omit,
        stream_id: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamSeries:
        """Calculates a time series of live streams watching duration in minutes.

        Views of
        only those streams that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Please note that the result for each time interval is in minutes, it is rounded
        to the nearest upper integer. You cannot use the sum of all intervals as the
        total watch time value; instead, use the /total method.

        Args:
          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601.

          client_user_id: Filter by field "`client_user_id`"

          granularity: Data is grouped by the specified time interval

          stream_id: Filter by `stream_id`

          to: End of time frame. Datetime in ISO 8601 format. If omitted, then the current
              time is taken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/stream/watching_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "stream_id": stream_id,
                        "to": to,
                    },
                    statistic_get_live_watch_time_cdn_params.StatisticGetLiveWatchTimeCdnParams,
                ),
            ),
            cast_to=StreamSeries,
        )

    async def get_live_watch_time_total_cdn(
        self,
        *,
        client_user_id: int | Omit = omit,
        from_: str | Omit = omit,
        stream_id: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodTotalStreamDurationSeries:
        """Calculates the total duration of live streams watching in minutes.

        Views of only
        those streams that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Args:
          client_user_id: Filter by field "`client_user_id`"

          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601. If omitted, the earliest start time for viewing is taken

          stream_id: Filter by `stream_id`

          to: End of time frame. Datetime in ISO 8601 format. If missed, then the current time
              is taken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/stream/watching_duration/total",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_user_id": client_user_id,
                        "from_": from_,
                        "stream_id": stream_id,
                        "to": to,
                    },
                    statistic_get_live_watch_time_total_cdn_params.StatisticGetLiveWatchTimeTotalCdnParams,
                ),
            ),
            cast_to=VodTotalStreamDurationSeries,
        )

    async def get_max_streams_series(
        self,
        *,
        from_: str,
        to: str,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MaxStreamSeries:
        """Calculates time series of the amount of simultaneous streams.

        The data is
        updated near realtime.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          granularity: specifies the time interval for grouping data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/max_stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "granularity": granularity,
                    },
                    statistic_get_max_streams_series_params.StatisticGetMaxStreamsSeriesParams,
                ),
            ),
            cast_to=MaxStreamSeries,
        )

    async def get_popular_videos(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PopularVideos:
        """
        Aggregates the number of views for all client videos, grouping them by id and
        sort from most popular to less in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/popular",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_popular_videos_params.StatisticGetPopularVideosParams,
                ),
            ),
            cast_to=PopularVideos,
        )

    async def get_storage_series(
        self,
        *,
        from_: str,
        to: str,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StorageSeries:
        """
        Calculates time series of the size of disk space in bytes for all processed and
        undeleted client videos. The data is updated every 8 hours, it does not make
        sense to set the granulation less than 1 day.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          granularity: specifies the time interval for grouping data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "granularity": granularity,
                    },
                    statistic_get_storage_series_params.StatisticGetStorageSeriesParams,
                ),
            ),
            cast_to=StorageSeries,
        )

    async def get_stream_series(
        self,
        *,
        from_: str,
        to: str,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamSeries:
        """Calculates time series of the transcoding minutes of all streams.

        The data is
        updated near realtime.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          granularity: specifies the time interval for grouping data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "granularity": granularity,
                    },
                    statistic_get_stream_series_params.StatisticGetStreamSeriesParams,
                ),
            ),
            cast_to=StreamSeries,
        )

    async def get_unique_viewers(
        self,
        *,
        date_from: str,
        date_to: str,
        id: str | Omit = omit,
        country: str | Omit = omit,
        event: Literal["init", "start", "watch"] | Omit = omit,
        group: List[Literal["date", "host", "os", "browser", "platform", "ip", "country", "event", "id"]] | Omit = omit,
        host: str | Omit = omit,
        type: Literal["live", "vod", "playlist"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UniqueViewers:
        """
        Get the number of unique viewers in the built-in player.

        Counts the number of unique IPs.

        Allows flexible grouping and filtering. The fields in the response depend on the
        selected grouping.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          id: filter by entity's id

          country: filter by country

          event: filter by event's name

          group: group=1,2,4 OR group=1&group=2&group=3

          host: filter by host

          type: filter by entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/uniqs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "id": id,
                        "country": country,
                        "event": event,
                        "group": group,
                        "host": host,
                        "type": type,
                    },
                    statistic_get_unique_viewers_params.StatisticGetUniqueViewersParams,
                ),
            ),
            cast_to=UniqueViewers,
        )

    async def get_unique_viewers_cdn(
        self,
        *,
        date_from: str,
        date_to: str,
        id: str | Omit = omit,
        type: Literal["live", "vod", "playlist"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UniqueViewersCdn:
        """Сounts the number of unique viewers of a video entity over CDN.

        It doesn't
        matter what player you used.

        All unique viewers for the specified period of time are counted.

        **How does it work?**

        Calculating the number of unique viewers for a Live stream or VOD over CDN
        involves aggregating and analyzing various metrics to ensure each individual
        viewer is counted only once, regardless of how many times they connect or
        disconnect during the stream.

        This method provides statistics for any video viewing by unique users,
        regardless of viewing method and a player you used. Thus, this is the most
        important difference from viewing through the built-in player:

        - In method /statistics/uniqs viewers of the built-in player are tracked only.
        - But this method tracks all viewers from everywhere.

        This method is a combination of two other Live and VOD detailed methods. If you
        need detailed information, then see the methods: `/statistics/stream/viewers`
        and `/statistics/vod/viewers`.

        **Data Processing and Deduplication**

        We us IP Address & User-Agent combination. Each unique combination of IP address
        and User-Agent string might be considered a unique viewer.

        This approach allows to accurately estimate the number of unique viewers.
        However, this is not foolproof due to NAT (Network Address Translation) and
        shared networks. Thus if your users fall under such restrictions, then the
        number of unique viewers may be higher than calculated.

        **Why is there no "Unique Views" method?**

        Based on CDN data, we can calculate the number of unique viewers only. Thus only
        your player will be able to count the number of unique views (clicks on the Play
        button) within the player session (i.e. how many times 1 unique viewer clicked
        the Play button within a unique player's session).

        Args:
          date_from: Start of time frame. Format is date time in ISO 8601.

          date_to: End of time frame. Format is date time in ISO 8601.

          id: Filter by entity's id. Put ID of a Live stream, VOD or a playlist to be
              calculated.

              If the value is omitted, then the calculation is done for all videos/streams of
              the specified type.

              When using this "id" parameter, be sure to specify the "type" parameter too. If
              you do not specify a type, the "id" will be ignored.

          type: Filter by entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/cdn/uniqs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "id": id,
                        "type": type,
                    },
                    statistic_get_unique_viewers_cdn_params.StatisticGetUniqueViewersCdnParams,
                ),
            ),
            cast_to=UniqueViewersCdn,
        )

    async def get_views(
        self,
        *,
        date_from: str,
        date_to: str,
        id: str | Omit = omit,
        country: str | Omit = omit,
        event: Literal["init", "start", "watch"] | Omit = omit,
        group: List[Literal["host", "os", "browser", "platform", "ip", "country", "event", "id"]] | Omit = omit,
        host: str | Omit = omit,
        type: Literal["live", "vod", "playlist"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Views:
        """
        Get the number of views in the built-in player.

        Allows flexible grouping and filtering. The fields in the response depend on the
        selected grouping.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          id: filter by entity's id

          country: filter by country

          event: filter by event's name

          group: group=1,2,4 OR group=1&group=2&group=3

          host: filter by host

          type: filter by entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "id": id,
                        "country": country,
                        "event": event,
                        "group": group,
                        "host": host,
                        "type": type,
                    },
                    statistic_get_views_params.StatisticGetViewsParams,
                ),
            ),
            cast_to=Views,
        )

    async def get_views_by_browsers(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByBrowser:
        """
        Aggregates the number of views for all client videos, grouping them by browsers
        in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/browsers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_browsers_params.StatisticGetViewsByBrowsersParams,
                ),
            ),
            cast_to=ViewsByBrowser,
        )

    async def get_views_by_country(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByCountry:
        """
        Aggregates the number of views grouping them by country in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_country_params.StatisticGetViewsByCountryParams,
                ),
            ),
            cast_to=ViewsByCountry,
        )

    async def get_views_by_hostname(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByHostname:
        """
        Aggregates the number of views, grouping them by "host" domain name the built-in
        player was embeded to.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/hosts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_hostname_params.StatisticGetViewsByHostnameParams,
                ),
            ),
            cast_to=ViewsByHostname,
        )

    async def get_views_by_operating_system(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByOperatingSystem:
        """
        Aggregates the number of views for all client videos, grouping them by device
        OSs in the built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/systems",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_operating_system_params.StatisticGetViewsByOperatingSystemParams,
                ),
            ),
            cast_to=ViewsByOperatingSystem,
        )

    async def get_views_by_referer(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByReferer:
        """
        Aggregates the number of views, grouping them by "referer" URL of pages the
        built-in player was embeded to.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/embeds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_referer_params.StatisticGetViewsByRefererParams,
                ),
            ),
            cast_to=ViewsByReferer,
        )

    async def get_views_by_region(
        self,
        *,
        date_from: str,
        date_to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsByRegion:
        """
        Aggregates the number of views grouping them by regions of countries in the
        built-in player.

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                    },
                    statistic_get_views_by_region_params.StatisticGetViewsByRegionParams,
                ),
            ),
            cast_to=ViewsByRegion,
        )

    async def get_views_heatmap(
        self,
        *,
        date_from: str,
        date_to: str,
        stream_id: str,
        type: Literal["live", "vod", "playlist"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewsHeatmap:
        """
        Shows information about what part of the video your viewers watched in the
        built-in player.

        This way you can find out how many viewers started watching the video, and where
        they stopped watching instead of watching the entire video to the end.

        Has different format of response depends on query param "type".

        Note. This method operates only on data collected by the built-in HTML player.
        It will not show statistics if you are using another player or viewing in native
        OS players through direct .m3u8/.mpd/.mp4 links. For such cases, use
        calculations through CDN (look at method /statistics/cdn/uniqs) or statistics of
        the players you have chosen.

        Args:
          date_from: Start of time frame. Datetime in ISO 8601 format.

          date_to: End of time frame. Datetime in ISO 8601 format.

          stream_id: video streaming ID

          type: entity's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/heatmap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "stream_id": stream_id,
                        "type": type,
                    },
                    statistic_get_views_heatmap_params.StatisticGetViewsHeatmapParams,
                ),
            ),
            cast_to=ViewsHeatmap,
        )

    async def get_vod_storage_volume(
        self,
        *,
        from_: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """
        Calculates time series of the duration in minutes for all processed and
        undeleted client videos.

        The data is updated every 8 hours, it does not make sense to set the granulation
        less than 1 day.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/vod/storage_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    statistic_get_vod_storage_volume_params.StatisticGetVodStorageVolumeParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    async def get_vod_transcoding_duration(
        self,
        *,
        from_: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """
        Calculates time series of the transcoding time in minutes for all processed
        client videos.

        The data is updated every 8 hours, it does not make sense to set the granulation
        less than 1 day.

        Args:
          from_: Start of time frame. Datetime in ISO 8601 format.

          to: End of time frame. Datetime in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/vod/transcoding_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    statistic_get_vod_transcoding_duration_params.StatisticGetVodTranscodingDurationParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    async def get_vod_unique_viewers_cdn(
        self,
        *,
        from_: str,
        to: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d"] | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """
        Calculates time series of unique viewers of VOD via CDN.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Works similar to the method `/statistics/cdn/uniqs`. But this allows you to
        break down data with the specified granularity: minutes, hours, days.

        Based on this method, a graph of unique views in the Customer Portal is built.

        ![Unique viewers via CDN in Customer Portal](https://demo-files.gvideo.io/apidocs/cdn_unique_viewers.png)

        Args:
          from_: Start of time frame. Format is date time in ISO 8601

          to: End of time frame. Format is date time in ISO 8601

          client_user_id: Filter by user "id"

          granularity: Specifies the time interval for grouping data

          slug: Filter by video "slug"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/vod/viewers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "slug": slug,
                    },
                    statistic_get_vod_unique_viewers_cdn_params.StatisticGetVodUniqueViewersCdnParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    async def get_vod_watch_time_cdn(
        self,
        *,
        from_: str,
        client_user_id: int | Omit = omit,
        granularity: Literal["1m", "5m", "15m", "1h", "1d", "1mo"] | Omit = omit,
        slug: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VodStatisticsSeries:
        """Calculates a time series of video watching duration in minutes.

        Views of only
        those videos that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Please note that the result for each time interval is in minutes, it is rounded
        to the nearest upper integer. You cannot use the sum of all intervals as the
        total watch time value; instead, use the /total method.

        Args:
          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601.

          client_user_id: Filter by field "`client_user_id`"

          granularity: Data is grouped by the specified time interval

          slug: Filter by video's slug

          to: End of time frame. Datetime in ISO 8601 format. If omitted, then the current
              time is taken.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/vod/watching_duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "client_user_id": client_user_id,
                        "granularity": granularity,
                        "slug": slug,
                        "to": to,
                    },
                    statistic_get_vod_watch_time_cdn_params.StatisticGetVodWatchTimeCdnParams,
                ),
            ),
            cast_to=VodStatisticsSeries,
        )

    async def get_vod_watch_time_total_cdn(
        self,
        *,
        client_user_id: int | Omit = omit,
        from_: str | Omit = omit,
        slug: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetVodWatchTimeTotalCdnResponse:
        """Calculates the total duration of video watching in minutes.

        Views of only those
        videos that meet the specified filters are summed up.

        The statistics are taken from the data of CDN and work regardless of which
        player the views were made with.

        Args:
          client_user_id: Filter by field "`client_user_id`"

          from_: Start of the time period for counting minutes of watching. Format is date time
              in ISO 8601. If omitted, the earliest start time for viewing is taken

          slug: Filter by video's slug

          to: End of time frame. Datetime in ISO 8601 format. If omitted, then the current
              time is taken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/statistics/vod/watching_duration/total",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_user_id": client_user_id,
                        "from_": from_,
                        "slug": slug,
                        "to": to,
                    },
                    statistic_get_vod_watch_time_total_cdn_params.StatisticGetVodWatchTimeTotalCdnParams,
                ),
            ),
            cast_to=StatisticGetVodWatchTimeTotalCdnResponse,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_ffprobes = to_raw_response_wrapper(
            statistics.get_ffprobes,
        )
        self.get_live_unique_viewers = to_raw_response_wrapper(
            statistics.get_live_unique_viewers,
        )
        self.get_live_watch_time_cdn = to_raw_response_wrapper(
            statistics.get_live_watch_time_cdn,
        )
        self.get_live_watch_time_total_cdn = to_raw_response_wrapper(
            statistics.get_live_watch_time_total_cdn,
        )
        self.get_max_streams_series = to_raw_response_wrapper(
            statistics.get_max_streams_series,
        )
        self.get_popular_videos = to_raw_response_wrapper(
            statistics.get_popular_videos,
        )
        self.get_storage_series = to_raw_response_wrapper(
            statistics.get_storage_series,
        )
        self.get_stream_series = to_raw_response_wrapper(
            statistics.get_stream_series,
        )
        self.get_unique_viewers = to_raw_response_wrapper(
            statistics.get_unique_viewers,
        )
        self.get_unique_viewers_cdn = to_raw_response_wrapper(
            statistics.get_unique_viewers_cdn,
        )
        self.get_views = to_raw_response_wrapper(
            statistics.get_views,
        )
        self.get_views_by_browsers = to_raw_response_wrapper(
            statistics.get_views_by_browsers,
        )
        self.get_views_by_country = to_raw_response_wrapper(
            statistics.get_views_by_country,
        )
        self.get_views_by_hostname = to_raw_response_wrapper(
            statistics.get_views_by_hostname,
        )
        self.get_views_by_operating_system = to_raw_response_wrapper(
            statistics.get_views_by_operating_system,
        )
        self.get_views_by_referer = to_raw_response_wrapper(
            statistics.get_views_by_referer,
        )
        self.get_views_by_region = to_raw_response_wrapper(
            statistics.get_views_by_region,
        )
        self.get_views_heatmap = to_raw_response_wrapper(
            statistics.get_views_heatmap,
        )
        self.get_vod_storage_volume = to_raw_response_wrapper(
            statistics.get_vod_storage_volume,
        )
        self.get_vod_transcoding_duration = to_raw_response_wrapper(
            statistics.get_vod_transcoding_duration,
        )
        self.get_vod_unique_viewers_cdn = to_raw_response_wrapper(
            statistics.get_vod_unique_viewers_cdn,
        )
        self.get_vod_watch_time_cdn = to_raw_response_wrapper(
            statistics.get_vod_watch_time_cdn,
        )
        self.get_vod_watch_time_total_cdn = to_raw_response_wrapper(
            statistics.get_vod_watch_time_total_cdn,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_ffprobes = async_to_raw_response_wrapper(
            statistics.get_ffprobes,
        )
        self.get_live_unique_viewers = async_to_raw_response_wrapper(
            statistics.get_live_unique_viewers,
        )
        self.get_live_watch_time_cdn = async_to_raw_response_wrapper(
            statistics.get_live_watch_time_cdn,
        )
        self.get_live_watch_time_total_cdn = async_to_raw_response_wrapper(
            statistics.get_live_watch_time_total_cdn,
        )
        self.get_max_streams_series = async_to_raw_response_wrapper(
            statistics.get_max_streams_series,
        )
        self.get_popular_videos = async_to_raw_response_wrapper(
            statistics.get_popular_videos,
        )
        self.get_storage_series = async_to_raw_response_wrapper(
            statistics.get_storage_series,
        )
        self.get_stream_series = async_to_raw_response_wrapper(
            statistics.get_stream_series,
        )
        self.get_unique_viewers = async_to_raw_response_wrapper(
            statistics.get_unique_viewers,
        )
        self.get_unique_viewers_cdn = async_to_raw_response_wrapper(
            statistics.get_unique_viewers_cdn,
        )
        self.get_views = async_to_raw_response_wrapper(
            statistics.get_views,
        )
        self.get_views_by_browsers = async_to_raw_response_wrapper(
            statistics.get_views_by_browsers,
        )
        self.get_views_by_country = async_to_raw_response_wrapper(
            statistics.get_views_by_country,
        )
        self.get_views_by_hostname = async_to_raw_response_wrapper(
            statistics.get_views_by_hostname,
        )
        self.get_views_by_operating_system = async_to_raw_response_wrapper(
            statistics.get_views_by_operating_system,
        )
        self.get_views_by_referer = async_to_raw_response_wrapper(
            statistics.get_views_by_referer,
        )
        self.get_views_by_region = async_to_raw_response_wrapper(
            statistics.get_views_by_region,
        )
        self.get_views_heatmap = async_to_raw_response_wrapper(
            statistics.get_views_heatmap,
        )
        self.get_vod_storage_volume = async_to_raw_response_wrapper(
            statistics.get_vod_storage_volume,
        )
        self.get_vod_transcoding_duration = async_to_raw_response_wrapper(
            statistics.get_vod_transcoding_duration,
        )
        self.get_vod_unique_viewers_cdn = async_to_raw_response_wrapper(
            statistics.get_vod_unique_viewers_cdn,
        )
        self.get_vod_watch_time_cdn = async_to_raw_response_wrapper(
            statistics.get_vod_watch_time_cdn,
        )
        self.get_vod_watch_time_total_cdn = async_to_raw_response_wrapper(
            statistics.get_vod_watch_time_total_cdn,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_ffprobes = to_streamed_response_wrapper(
            statistics.get_ffprobes,
        )
        self.get_live_unique_viewers = to_streamed_response_wrapper(
            statistics.get_live_unique_viewers,
        )
        self.get_live_watch_time_cdn = to_streamed_response_wrapper(
            statistics.get_live_watch_time_cdn,
        )
        self.get_live_watch_time_total_cdn = to_streamed_response_wrapper(
            statistics.get_live_watch_time_total_cdn,
        )
        self.get_max_streams_series = to_streamed_response_wrapper(
            statistics.get_max_streams_series,
        )
        self.get_popular_videos = to_streamed_response_wrapper(
            statistics.get_popular_videos,
        )
        self.get_storage_series = to_streamed_response_wrapper(
            statistics.get_storage_series,
        )
        self.get_stream_series = to_streamed_response_wrapper(
            statistics.get_stream_series,
        )
        self.get_unique_viewers = to_streamed_response_wrapper(
            statistics.get_unique_viewers,
        )
        self.get_unique_viewers_cdn = to_streamed_response_wrapper(
            statistics.get_unique_viewers_cdn,
        )
        self.get_views = to_streamed_response_wrapper(
            statistics.get_views,
        )
        self.get_views_by_browsers = to_streamed_response_wrapper(
            statistics.get_views_by_browsers,
        )
        self.get_views_by_country = to_streamed_response_wrapper(
            statistics.get_views_by_country,
        )
        self.get_views_by_hostname = to_streamed_response_wrapper(
            statistics.get_views_by_hostname,
        )
        self.get_views_by_operating_system = to_streamed_response_wrapper(
            statistics.get_views_by_operating_system,
        )
        self.get_views_by_referer = to_streamed_response_wrapper(
            statistics.get_views_by_referer,
        )
        self.get_views_by_region = to_streamed_response_wrapper(
            statistics.get_views_by_region,
        )
        self.get_views_heatmap = to_streamed_response_wrapper(
            statistics.get_views_heatmap,
        )
        self.get_vod_storage_volume = to_streamed_response_wrapper(
            statistics.get_vod_storage_volume,
        )
        self.get_vod_transcoding_duration = to_streamed_response_wrapper(
            statistics.get_vod_transcoding_duration,
        )
        self.get_vod_unique_viewers_cdn = to_streamed_response_wrapper(
            statistics.get_vod_unique_viewers_cdn,
        )
        self.get_vod_watch_time_cdn = to_streamed_response_wrapper(
            statistics.get_vod_watch_time_cdn,
        )
        self.get_vod_watch_time_total_cdn = to_streamed_response_wrapper(
            statistics.get_vod_watch_time_total_cdn,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_ffprobes = async_to_streamed_response_wrapper(
            statistics.get_ffprobes,
        )
        self.get_live_unique_viewers = async_to_streamed_response_wrapper(
            statistics.get_live_unique_viewers,
        )
        self.get_live_watch_time_cdn = async_to_streamed_response_wrapper(
            statistics.get_live_watch_time_cdn,
        )
        self.get_live_watch_time_total_cdn = async_to_streamed_response_wrapper(
            statistics.get_live_watch_time_total_cdn,
        )
        self.get_max_streams_series = async_to_streamed_response_wrapper(
            statistics.get_max_streams_series,
        )
        self.get_popular_videos = async_to_streamed_response_wrapper(
            statistics.get_popular_videos,
        )
        self.get_storage_series = async_to_streamed_response_wrapper(
            statistics.get_storage_series,
        )
        self.get_stream_series = async_to_streamed_response_wrapper(
            statistics.get_stream_series,
        )
        self.get_unique_viewers = async_to_streamed_response_wrapper(
            statistics.get_unique_viewers,
        )
        self.get_unique_viewers_cdn = async_to_streamed_response_wrapper(
            statistics.get_unique_viewers_cdn,
        )
        self.get_views = async_to_streamed_response_wrapper(
            statistics.get_views,
        )
        self.get_views_by_browsers = async_to_streamed_response_wrapper(
            statistics.get_views_by_browsers,
        )
        self.get_views_by_country = async_to_streamed_response_wrapper(
            statistics.get_views_by_country,
        )
        self.get_views_by_hostname = async_to_streamed_response_wrapper(
            statistics.get_views_by_hostname,
        )
        self.get_views_by_operating_system = async_to_streamed_response_wrapper(
            statistics.get_views_by_operating_system,
        )
        self.get_views_by_referer = async_to_streamed_response_wrapper(
            statistics.get_views_by_referer,
        )
        self.get_views_by_region = async_to_streamed_response_wrapper(
            statistics.get_views_by_region,
        )
        self.get_views_heatmap = async_to_streamed_response_wrapper(
            statistics.get_views_heatmap,
        )
        self.get_vod_storage_volume = async_to_streamed_response_wrapper(
            statistics.get_vod_storage_volume,
        )
        self.get_vod_transcoding_duration = async_to_streamed_response_wrapper(
            statistics.get_vod_transcoding_duration,
        )
        self.get_vod_unique_viewers_cdn = async_to_streamed_response_wrapper(
            statistics.get_vod_unique_viewers_cdn,
        )
        self.get_vod_watch_time_cdn = async_to_streamed_response_wrapper(
            statistics.get_vod_watch_time_cdn,
        )
        self.get_vod_watch_time_total_cdn = async_to_streamed_response_wrapper(
            statistics.get_vod_watch_time_total_cdn,
        )
