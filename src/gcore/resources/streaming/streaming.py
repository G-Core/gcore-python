# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .players import (
    PlayersResource,
    AsyncPlayersResource,
    PlayersResourceWithRawResponse,
    AsyncPlayersResourceWithRawResponse,
    PlayersResourceWithStreamingResponse,
    AsyncPlayersResourceWithStreamingResponse,
)
from .ai_tasks import (
    AITasksResource,
    AsyncAITasksResource,
    AITasksResourceWithRawResponse,
    AsyncAITasksResourceWithRawResponse,
    AITasksResourceWithStreamingResponse,
    AsyncAITasksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .playlists import (
    PlaylistsResource,
    AsyncPlaylistsResource,
    PlaylistsResourceWithRawResponse,
    AsyncPlaylistsResourceWithRawResponse,
    PlaylistsResourceWithStreamingResponse,
    AsyncPlaylistsResourceWithStreamingResponse,
)
from .restreams import (
    RestreamsResource,
    AsyncRestreamsResource,
    RestreamsResourceWithRawResponse,
    AsyncRestreamsResourceWithRawResponse,
    RestreamsResourceWithStreamingResponse,
    AsyncRestreamsResourceWithStreamingResponse,
)
from .broadcasts import (
    BroadcastsResource,
    AsyncBroadcastsResource,
    BroadcastsResourceWithRawResponse,
    AsyncBroadcastsResourceWithRawResponse,
    BroadcastsResourceWithStreamingResponse,
    AsyncBroadcastsResourceWithStreamingResponse,
)
from .statistics import (
    StatisticsResource,
    AsyncStatisticsResource,
    StatisticsResourceWithRawResponse,
    AsyncStatisticsResourceWithRawResponse,
    StatisticsResourceWithStreamingResponse,
    AsyncStatisticsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .directories import (
    DirectoriesResource,
    AsyncDirectoriesResource,
    DirectoriesResourceWithRawResponse,
    AsyncDirectoriesResourceWithRawResponse,
    DirectoriesResourceWithStreamingResponse,
    AsyncDirectoriesResourceWithStreamingResponse,
)
from .quality_sets import (
    QualitySetsResource,
    AsyncQualitySetsResource,
    QualitySetsResourceWithRawResponse,
    AsyncQualitySetsResourceWithRawResponse,
    QualitySetsResourceWithStreamingResponse,
    AsyncQualitySetsResourceWithStreamingResponse,
)
from .videos.videos import (
    VideosResource,
    AsyncVideosResource,
    VideosResourceWithRawResponse,
    AsyncVideosResourceWithRawResponse,
    VideosResourceWithStreamingResponse,
    AsyncVideosResourceWithStreamingResponse,
)
from .streams.streams import (
    StreamsResource,
    AsyncStreamsResource,
    StreamsResourceWithRawResponse,
    AsyncStreamsResourceWithRawResponse,
    StreamsResourceWithStreamingResponse,
    AsyncStreamsResourceWithStreamingResponse,
)

__all__ = ["StreamingResource", "AsyncStreamingResource"]


class StreamingResource(SyncAPIResource):
    @cached_property
    def ai_tasks(self) -> AITasksResource:
        return AITasksResource(self._client)

    @cached_property
    def broadcasts(self) -> BroadcastsResource:
        return BroadcastsResource(self._client)

    @cached_property
    def directories(self) -> DirectoriesResource:
        return DirectoriesResource(self._client)

    @cached_property
    def players(self) -> PlayersResource:
        return PlayersResource(self._client)

    @cached_property
    def quality_sets(self) -> QualitySetsResource:
        return QualitySetsResource(self._client)

    @cached_property
    def playlists(self) -> PlaylistsResource:
        return PlaylistsResource(self._client)

    @cached_property
    def videos(self) -> VideosResource:
        return VideosResource(self._client)

    @cached_property
    def streams(self) -> StreamsResource:
        return StreamsResource(self._client)

    @cached_property
    def restreams(self) -> RestreamsResource:
        return RestreamsResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        return StatisticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StreamingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return StreamingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return StreamingResourceWithStreamingResponse(self)


class AsyncStreamingResource(AsyncAPIResource):
    @cached_property
    def ai_tasks(self) -> AsyncAITasksResource:
        return AsyncAITasksResource(self._client)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResource:
        return AsyncBroadcastsResource(self._client)

    @cached_property
    def directories(self) -> AsyncDirectoriesResource:
        return AsyncDirectoriesResource(self._client)

    @cached_property
    def players(self) -> AsyncPlayersResource:
        return AsyncPlayersResource(self._client)

    @cached_property
    def quality_sets(self) -> AsyncQualitySetsResource:
        return AsyncQualitySetsResource(self._client)

    @cached_property
    def playlists(self) -> AsyncPlaylistsResource:
        return AsyncPlaylistsResource(self._client)

    @cached_property
    def videos(self) -> AsyncVideosResource:
        return AsyncVideosResource(self._client)

    @cached_property
    def streams(self) -> AsyncStreamsResource:
        return AsyncStreamsResource(self._client)

    @cached_property
    def restreams(self) -> AsyncRestreamsResource:
        return AsyncRestreamsResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        return AsyncStatisticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStreamingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncStreamingResourceWithStreamingResponse(self)


class StreamingResourceWithRawResponse:
    def __init__(self, streaming: StreamingResource) -> None:
        self._streaming = streaming

    @cached_property
    def ai_tasks(self) -> AITasksResourceWithRawResponse:
        return AITasksResourceWithRawResponse(self._streaming.ai_tasks)

    @cached_property
    def broadcasts(self) -> BroadcastsResourceWithRawResponse:
        return BroadcastsResourceWithRawResponse(self._streaming.broadcasts)

    @cached_property
    def directories(self) -> DirectoriesResourceWithRawResponse:
        return DirectoriesResourceWithRawResponse(self._streaming.directories)

    @cached_property
    def players(self) -> PlayersResourceWithRawResponse:
        return PlayersResourceWithRawResponse(self._streaming.players)

    @cached_property
    def quality_sets(self) -> QualitySetsResourceWithRawResponse:
        return QualitySetsResourceWithRawResponse(self._streaming.quality_sets)

    @cached_property
    def playlists(self) -> PlaylistsResourceWithRawResponse:
        return PlaylistsResourceWithRawResponse(self._streaming.playlists)

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._streaming.videos)

    @cached_property
    def streams(self) -> StreamsResourceWithRawResponse:
        return StreamsResourceWithRawResponse(self._streaming.streams)

    @cached_property
    def restreams(self) -> RestreamsResourceWithRawResponse:
        return RestreamsResourceWithRawResponse(self._streaming.restreams)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        return StatisticsResourceWithRawResponse(self._streaming.statistics)


class AsyncStreamingResourceWithRawResponse:
    def __init__(self, streaming: AsyncStreamingResource) -> None:
        self._streaming = streaming

    @cached_property
    def ai_tasks(self) -> AsyncAITasksResourceWithRawResponse:
        return AsyncAITasksResourceWithRawResponse(self._streaming.ai_tasks)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResourceWithRawResponse:
        return AsyncBroadcastsResourceWithRawResponse(self._streaming.broadcasts)

    @cached_property
    def directories(self) -> AsyncDirectoriesResourceWithRawResponse:
        return AsyncDirectoriesResourceWithRawResponse(self._streaming.directories)

    @cached_property
    def players(self) -> AsyncPlayersResourceWithRawResponse:
        return AsyncPlayersResourceWithRawResponse(self._streaming.players)

    @cached_property
    def quality_sets(self) -> AsyncQualitySetsResourceWithRawResponse:
        return AsyncQualitySetsResourceWithRawResponse(self._streaming.quality_sets)

    @cached_property
    def playlists(self) -> AsyncPlaylistsResourceWithRawResponse:
        return AsyncPlaylistsResourceWithRawResponse(self._streaming.playlists)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._streaming.videos)

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithRawResponse:
        return AsyncStreamsResourceWithRawResponse(self._streaming.streams)

    @cached_property
    def restreams(self) -> AsyncRestreamsResourceWithRawResponse:
        return AsyncRestreamsResourceWithRawResponse(self._streaming.restreams)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        return AsyncStatisticsResourceWithRawResponse(self._streaming.statistics)


class StreamingResourceWithStreamingResponse:
    def __init__(self, streaming: StreamingResource) -> None:
        self._streaming = streaming

    @cached_property
    def ai_tasks(self) -> AITasksResourceWithStreamingResponse:
        return AITasksResourceWithStreamingResponse(self._streaming.ai_tasks)

    @cached_property
    def broadcasts(self) -> BroadcastsResourceWithStreamingResponse:
        return BroadcastsResourceWithStreamingResponse(self._streaming.broadcasts)

    @cached_property
    def directories(self) -> DirectoriesResourceWithStreamingResponse:
        return DirectoriesResourceWithStreamingResponse(self._streaming.directories)

    @cached_property
    def players(self) -> PlayersResourceWithStreamingResponse:
        return PlayersResourceWithStreamingResponse(self._streaming.players)

    @cached_property
    def quality_sets(self) -> QualitySetsResourceWithStreamingResponse:
        return QualitySetsResourceWithStreamingResponse(self._streaming.quality_sets)

    @cached_property
    def playlists(self) -> PlaylistsResourceWithStreamingResponse:
        return PlaylistsResourceWithStreamingResponse(self._streaming.playlists)

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._streaming.videos)

    @cached_property
    def streams(self) -> StreamsResourceWithStreamingResponse:
        return StreamsResourceWithStreamingResponse(self._streaming.streams)

    @cached_property
    def restreams(self) -> RestreamsResourceWithStreamingResponse:
        return RestreamsResourceWithStreamingResponse(self._streaming.restreams)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        return StatisticsResourceWithStreamingResponse(self._streaming.statistics)


class AsyncStreamingResourceWithStreamingResponse:
    def __init__(self, streaming: AsyncStreamingResource) -> None:
        self._streaming = streaming

    @cached_property
    def ai_tasks(self) -> AsyncAITasksResourceWithStreamingResponse:
        return AsyncAITasksResourceWithStreamingResponse(self._streaming.ai_tasks)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        return AsyncBroadcastsResourceWithStreamingResponse(self._streaming.broadcasts)

    @cached_property
    def directories(self) -> AsyncDirectoriesResourceWithStreamingResponse:
        return AsyncDirectoriesResourceWithStreamingResponse(self._streaming.directories)

    @cached_property
    def players(self) -> AsyncPlayersResourceWithStreamingResponse:
        return AsyncPlayersResourceWithStreamingResponse(self._streaming.players)

    @cached_property
    def quality_sets(self) -> AsyncQualitySetsResourceWithStreamingResponse:
        return AsyncQualitySetsResourceWithStreamingResponse(self._streaming.quality_sets)

    @cached_property
    def playlists(self) -> AsyncPlaylistsResourceWithStreamingResponse:
        return AsyncPlaylistsResourceWithStreamingResponse(self._streaming.playlists)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._streaming.videos)

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithStreamingResponse:
        return AsyncStreamsResourceWithStreamingResponse(self._streaming.streams)

    @cached_property
    def restreams(self) -> AsyncRestreamsResourceWithStreamingResponse:
        return AsyncRestreamsResourceWithStreamingResponse(self._streaming.restreams)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        return AsyncStatisticsResourceWithStreamingResponse(self._streaming.statistics)
