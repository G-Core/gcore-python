# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.streaming import (
    Views,
    Ffprobes,
    StreamSeries,
    ViewsHeatmap,
    PopularVideos,
    StorageSeries,
    UniqueViewers,
    ViewsByRegion,
    ViewsByBrowser,
    ViewsByCountry,
    ViewsByReferer,
    MaxStreamSeries,
    ViewsByHostname,
    UniqueViewersCdn,
    VodStatisticsSeries,
    ViewsByOperatingSystem,
    VodTotalStreamDurationSeries,
    StatisticGetLiveUniqueViewersResponse,
    StatisticGetVodWatchTimeTotalCdnResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_ffprobes(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
        )
        assert_matches_type(Ffprobes, statistic, path=["response"])

    @parametrize
    def test_method_get_ffprobes_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            interval=0,
            units="second",
        )
        assert_matches_type(Ffprobes, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_ffprobes(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(Ffprobes, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_ffprobes(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(Ffprobes, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_live_unique_viewers(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_live_unique_viewers(
            from_="from",
            to="to",
        )
        assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

    @parametrize
    def test_method_get_live_unique_viewers_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_live_unique_viewers(
            from_="from",
            to="to",
            client_user_id=0,
            granularity="1m",
            stream_id=0,
        )
        assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_live_unique_viewers(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_live_unique_viewers(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_live_unique_viewers(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_live_unique_viewers(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_live_watch_time_cdn(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_live_watch_time_cdn(
            from_="from",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_live_watch_time_cdn_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_live_watch_time_cdn(
            from_="from",
            client_user_id=0,
            granularity="1m",
            stream_id=0,
            to="to",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_live_watch_time_cdn(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_live_watch_time_cdn(
            from_="from",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_live_watch_time_cdn(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_live_watch_time_cdn(
            from_="from",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StreamSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_live_watch_time_total_cdn(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_live_watch_time_total_cdn()
        assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_live_watch_time_total_cdn_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_live_watch_time_total_cdn(
            client_user_id=0,
            from_="from",
            stream_id=0,
            to="to",
        )
        assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_live_watch_time_total_cdn(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_live_watch_time_total_cdn()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_live_watch_time_total_cdn(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_live_watch_time_total_cdn() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_max_streams_series(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_max_streams_series(
            from_="from",
            to="to",
        )
        assert_matches_type(MaxStreamSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_max_streams_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_max_streams_series(
            from_="from",
            to="to",
            granularity="1m",
        )
        assert_matches_type(MaxStreamSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_max_streams_series(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_max_streams_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(MaxStreamSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_max_streams_series(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_max_streams_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(MaxStreamSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_popular_videos(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_popular_videos(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(PopularVideos, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_popular_videos(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_popular_videos(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(PopularVideos, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_popular_videos(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_popular_videos(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(PopularVideos, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_storage_series(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_storage_series(
            from_="from",
            to="to",
        )
        assert_matches_type(StorageSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_storage_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_storage_series(
            from_="from",
            to="to",
            granularity="1m",
        )
        assert_matches_type(StorageSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_storage_series(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_storage_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StorageSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_storage_series(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_storage_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StorageSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_stream_series(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_stream_series(
            from_="from",
            to="to",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_stream_series_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_stream_series(
            from_="from",
            to="to",
            granularity="1m",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_stream_series(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_stream_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_stream_series(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_stream_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StreamSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_unique_viewers(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(UniqueViewers, statistic, path=["response"])

    @parametrize
    def test_method_get_unique_viewers_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
            id="id",
            country="country",
            event="init",
            group=["date"],
            host="host",
            type="live",
        )
        assert_matches_type(UniqueViewers, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_unique_viewers(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(UniqueViewers, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_unique_viewers(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(UniqueViewers, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_unique_viewers_cdn(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

    @parametrize
    def test_method_get_unique_viewers_cdn_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
            id="id",
            type="live",
        )
        assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_unique_viewers_cdn(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_unique_viewers_cdn(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(Views, statistic, path=["response"])

    @parametrize
    def test_method_get_views_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views(
            date_from="date_from",
            date_to="date_to",
            id="id",
            country="country",
            event="init",
            group=["host"],
            host="host",
            type="live",
        )
        assert_matches_type(Views, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(Views, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(Views, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_by_browsers(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_by_browsers(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByBrowser, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_by_browsers(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_by_browsers(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsByBrowser, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_by_browsers(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_by_browsers(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsByBrowser, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_by_country(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_by_country(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByCountry, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_by_country(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_by_country(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsByCountry, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_by_country(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_by_country(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsByCountry, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_by_hostname(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_by_hostname(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByHostname, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_by_hostname(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_by_hostname(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsByHostname, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_by_hostname(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_by_hostname(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsByHostname, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_by_operating_system(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_by_operating_system(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByOperatingSystem, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_by_operating_system(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_by_operating_system(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsByOperatingSystem, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_by_operating_system(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_by_operating_system(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsByOperatingSystem, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_by_referer(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_by_referer(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByReferer, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_by_referer(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_by_referer(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsByReferer, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_by_referer(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_by_referer(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsByReferer, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_by_region(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_by_region(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByRegion, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_by_region(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_by_region(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsByRegion, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_by_region(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_by_region(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsByRegion, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_views_heatmap(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_views_heatmap(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            type="live",
        )
        assert_matches_type(ViewsHeatmap, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_views_heatmap(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_views_heatmap(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            type="live",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(ViewsHeatmap, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_views_heatmap(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_views_heatmap(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            type="live",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(ViewsHeatmap, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_vod_storage_volume(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_storage_volume(
            from_="from",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_vod_storage_volume(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_vod_storage_volume(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_vod_storage_volume(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_vod_storage_volume(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_vod_transcoding_duration(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_transcoding_duration(
            from_="from",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_vod_transcoding_duration(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_vod_transcoding_duration(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_vod_transcoding_duration(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_vod_transcoding_duration(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_vod_unique_viewers_cdn(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_vod_unique_viewers_cdn_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
            client_user_id=0,
            granularity="1m",
            slug="slug",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_vod_unique_viewers_cdn(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_vod_unique_viewers_cdn(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_vod_watch_time_cdn(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_watch_time_cdn(
            from_="from",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_method_get_vod_watch_time_cdn_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_watch_time_cdn(
            from_="from",
            client_user_id=0,
            granularity="1m",
            slug="slug",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_vod_watch_time_cdn(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_vod_watch_time_cdn(
            from_="from",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_vod_watch_time_cdn(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_vod_watch_time_cdn(
            from_="from",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_vod_watch_time_total_cdn(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_watch_time_total_cdn()
        assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

    @parametrize
    def test_method_get_vod_watch_time_total_cdn_with_all_params(self, client: Gcore) -> None:
        statistic = client.streaming.statistics.get_vod_watch_time_total_cdn(
            client_user_id=0,
            from_="from",
            slug="slug",
            to="to",
        )
        assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_get_vod_watch_time_total_cdn(self, client: Gcore) -> None:
        response = client.streaming.statistics.with_raw_response.get_vod_watch_time_total_cdn()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_get_vod_watch_time_total_cdn(self, client: Gcore) -> None:
        with client.streaming.statistics.with_streaming_response.get_vod_watch_time_total_cdn() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_ffprobes(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
        )
        assert_matches_type(Ffprobes, statistic, path=["response"])

    @parametrize
    async def test_method_get_ffprobes_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            interval=0,
            units="second",
        )
        assert_matches_type(Ffprobes, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_ffprobes(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(Ffprobes, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_ffprobes(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_ffprobes(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(Ffprobes, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_live_unique_viewers(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_live_unique_viewers(
            from_="from",
            to="to",
        )
        assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

    @parametrize
    async def test_method_get_live_unique_viewers_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_live_unique_viewers(
            from_="from",
            to="to",
            client_user_id=0,
            granularity="1m",
            stream_id=0,
        )
        assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_live_unique_viewers(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_live_unique_viewers(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_live_unique_viewers(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_live_unique_viewers(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetLiveUniqueViewersResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_live_watch_time_cdn(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_live_watch_time_cdn(
            from_="from",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_live_watch_time_cdn_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_live_watch_time_cdn(
            from_="from",
            client_user_id=0,
            granularity="1m",
            stream_id=0,
            to="to",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_live_watch_time_cdn(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_live_watch_time_cdn(
            from_="from",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_live_watch_time_cdn(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_live_watch_time_cdn(
            from_="from",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StreamSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_live_watch_time_total_cdn(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_live_watch_time_total_cdn()
        assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_live_watch_time_total_cdn_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_live_watch_time_total_cdn(
            client_user_id=0,
            from_="from",
            stream_id=0,
            to="to",
        )
        assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_live_watch_time_total_cdn(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_live_watch_time_total_cdn()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_live_watch_time_total_cdn(self, async_client: AsyncGcore) -> None:
        async with (
            async_client.streaming.statistics.with_streaming_response.get_live_watch_time_total_cdn()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(VodTotalStreamDurationSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_max_streams_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_max_streams_series(
            from_="from",
            to="to",
        )
        assert_matches_type(MaxStreamSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_max_streams_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_max_streams_series(
            from_="from",
            to="to",
            granularity="1m",
        )
        assert_matches_type(MaxStreamSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_max_streams_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_max_streams_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(MaxStreamSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_max_streams_series(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_max_streams_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(MaxStreamSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_popular_videos(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_popular_videos(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(PopularVideos, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_popular_videos(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_popular_videos(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(PopularVideos, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_popular_videos(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_popular_videos(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(PopularVideos, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_storage_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_storage_series(
            from_="from",
            to="to",
        )
        assert_matches_type(StorageSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_storage_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_storage_series(
            from_="from",
            to="to",
            granularity="1m",
        )
        assert_matches_type(StorageSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_storage_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_storage_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StorageSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_storage_series(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_storage_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StorageSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_stream_series(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_stream_series(
            from_="from",
            to="to",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_stream_series_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_stream_series(
            from_="from",
            to="to",
            granularity="1m",
        )
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_stream_series(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_stream_series(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StreamSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_stream_series(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_stream_series(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StreamSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_unique_viewers(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(UniqueViewers, statistic, path=["response"])

    @parametrize
    async def test_method_get_unique_viewers_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
            id="id",
            country="country",
            event="init",
            group=["date"],
            host="host",
            type="live",
        )
        assert_matches_type(UniqueViewers, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_unique_viewers(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(UniqueViewers, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_unique_viewers(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_unique_viewers(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(UniqueViewers, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_unique_viewers_cdn(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

    @parametrize
    async def test_method_get_unique_viewers_cdn_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
            id="id",
            type="live",
        )
        assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_unique_viewers_cdn(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_unique_viewers_cdn(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_unique_viewers_cdn(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(UniqueViewersCdn, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(Views, statistic, path=["response"])

    @parametrize
    async def test_method_get_views_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views(
            date_from="date_from",
            date_to="date_to",
            id="id",
            country="country",
            event="init",
            group=["host"],
            host="host",
            type="live",
        )
        assert_matches_type(Views, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(Views, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(Views, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_by_browsers(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_by_browsers(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByBrowser, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_by_browsers(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_by_browsers(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsByBrowser, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_by_browsers(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_by_browsers(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsByBrowser, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_by_country(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_by_country(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByCountry, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_by_country(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_by_country(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsByCountry, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_by_country(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_by_country(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsByCountry, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_by_hostname(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_by_hostname(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByHostname, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_by_hostname(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_by_hostname(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsByHostname, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_by_hostname(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_by_hostname(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsByHostname, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_by_operating_system(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_by_operating_system(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByOperatingSystem, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_by_operating_system(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_by_operating_system(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsByOperatingSystem, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_by_operating_system(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_by_operating_system(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsByOperatingSystem, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_by_referer(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_by_referer(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByReferer, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_by_referer(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_by_referer(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsByReferer, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_by_referer(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_by_referer(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsByReferer, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_by_region(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_by_region(
            date_from="date_from",
            date_to="date_to",
        )
        assert_matches_type(ViewsByRegion, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_by_region(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_by_region(
            date_from="date_from",
            date_to="date_to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsByRegion, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_by_region(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_by_region(
            date_from="date_from",
            date_to="date_to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsByRegion, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_views_heatmap(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_views_heatmap(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            type="live",
        )
        assert_matches_type(ViewsHeatmap, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_views_heatmap(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_views_heatmap(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            type="live",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(ViewsHeatmap, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_views_heatmap(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_views_heatmap(
            date_from="date_from",
            date_to="date_to",
            stream_id="stream_id",
            type="live",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(ViewsHeatmap, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_vod_storage_volume(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_storage_volume(
            from_="from",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_vod_storage_volume(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_vod_storage_volume(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_vod_storage_volume(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_vod_storage_volume(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_vod_transcoding_duration(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_transcoding_duration(
            from_="from",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_vod_transcoding_duration(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_vod_transcoding_duration(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_vod_transcoding_duration(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_vod_transcoding_duration(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_vod_unique_viewers_cdn(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_vod_unique_viewers_cdn_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
            client_user_id=0,
            granularity="1m",
            slug="slug",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_vod_unique_viewers_cdn(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_vod_unique_viewers_cdn(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_vod_unique_viewers_cdn(
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_vod_watch_time_cdn(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_watch_time_cdn(
            from_="from",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_method_get_vod_watch_time_cdn_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_watch_time_cdn(
            from_="from",
            client_user_id=0,
            granularity="1m",
            slug="slug",
            to="to",
        )
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_vod_watch_time_cdn(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_vod_watch_time_cdn(
            from_="from",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_vod_watch_time_cdn(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_vod_watch_time_cdn(
            from_="from",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(VodStatisticsSeries, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_vod_watch_time_total_cdn(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_watch_time_total_cdn()
        assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

    @parametrize
    async def test_method_get_vod_watch_time_total_cdn_with_all_params(self, async_client: AsyncGcore) -> None:
        statistic = await async_client.streaming.statistics.get_vod_watch_time_total_cdn(
            client_user_id=0,
            from_="from",
            slug="slug",
            to="to",
        )
        assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_get_vod_watch_time_total_cdn(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.statistics.with_raw_response.get_vod_watch_time_total_cdn()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_get_vod_watch_time_total_cdn(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.statistics.with_streaming_response.get_vod_watch_time_total_cdn() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetVodWatchTimeTotalCdnResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True
