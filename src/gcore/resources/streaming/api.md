# Streaming

Types:

```python
from gcore.types.streaming import CreateVideo, Video
```

## AITasks

Types:

```python
from gcore.types.streaming import (
    AIContentmoderationHardnudity,
    AIContentmoderationNsfw,
    AIContentmoderationSoftnudity,
    AIContentmoderationSport,
    AITask,
    AITaskCreateResponse,
    AITaskCancelResponse,
    AITaskGetResponse,
    AITaskGetAISettingsResponse,
)
```

Methods:

- <code title="post /streaming/ai/tasks">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">create</a>(\*\*<a href="src/gcore/types/streaming/ai_task_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ai_task_create_response.py">AITaskCreateResponse</a></code>
- <code title="get /streaming/ai/tasks">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">list</a>(\*\*<a href="src/gcore/types/streaming/ai_task_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ai_task.py">SyncPageStreamingAI[AITask]</a></code>
- <code title="post /streaming/ai/tasks/{task_id}/cancel">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">cancel</a>(task_id) -> <a href="./src/gcore/types/streaming/ai_task_cancel_response.py">AITaskCancelResponse</a></code>
- <code title="get /streaming/ai/tasks/{task_id}">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">get</a>(task_id) -> <a href="./src/gcore/types/streaming/ai_task_get_response.py">AITaskGetResponse</a></code>
- <code title="get /streaming/ai/info">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">get_ai_settings</a>(\*\*<a href="src/gcore/types/streaming/ai_task_get_ai_settings_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ai_task_get_ai_settings_response.py">AITaskGetAISettingsResponse</a></code>

## Broadcasts

Types:

```python
from gcore.types.streaming import Broadcast, BroadcastSpectatorsCount
```

Methods:

- <code title="post /streaming/broadcasts">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">create</a>(\*\*<a href="src/gcore/types/streaming/broadcast_create_params.py">params</a>) -> None</code>
- <code title="patch /streaming/broadcasts/{broadcast_id}">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">update</a>(broadcast_id, \*\*<a href="src/gcore/types/streaming/broadcast_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/broadcast.py">Broadcast</a></code>
- <code title="get /streaming/broadcasts">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">list</a>(\*\*<a href="src/gcore/types/streaming/broadcast_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/broadcast.py">SyncPageStreaming[Broadcast]</a></code>
- <code title="delete /streaming/broadcasts/{broadcast_id}">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">delete</a>(broadcast_id) -> None</code>
- <code title="get /streaming/broadcasts/{broadcast_id}">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">get</a>(broadcast_id) -> <a href="./src/gcore/types/streaming/broadcast.py">Broadcast</a></code>
- <code title="get /streaming/broadcasts/{broadcast_id}/spectators">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">get_spectators_count</a>(broadcast_id) -> <a href="./src/gcore/types/streaming/broadcast_spectators_count.py">BroadcastSpectatorsCount</a></code>

## Directories

Types:

```python
from gcore.types.streaming import (
    DirectoriesTree,
    DirectoryBase,
    DirectoryItem,
    DirectoryVideo,
    DirectoryGetResponse,
)
```

Methods:

- <code title="post /streaming/directories">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">create</a>(\*\*<a href="src/gcore/types/streaming/directory_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/directory_base.py">DirectoryBase</a></code>
- <code title="patch /streaming/directories/{directory_id}">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">update</a>(directory_id, \*\*<a href="src/gcore/types/streaming/directory_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/directory_base.py">DirectoryBase</a></code>
- <code title="delete /streaming/directories/{directory_id}">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">delete</a>(directory_id) -> None</code>
- <code title="get /streaming/directories/{directory_id}">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">get</a>(directory_id) -> <a href="./src/gcore/types/streaming/directory_get_response.py">DirectoryGetResponse</a></code>
- <code title="get /streaming/directories/tree">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">get_tree</a>() -> <a href="./src/gcore/types/streaming/directories_tree.py">DirectoriesTree</a></code>

## Players

Types:

```python
from gcore.types.streaming import Player
```

Methods:

- <code title="post /streaming/players">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">create</a>(\*\*<a href="src/gcore/types/streaming/player_create_params.py">params</a>) -> None</code>
- <code title="patch /streaming/players/{player_id}">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">update</a>(player_id, \*\*<a href="src/gcore/types/streaming/player_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/player.py">Player</a></code>
- <code title="get /streaming/players">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">list</a>(\*\*<a href="src/gcore/types/streaming/player_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/player.py">SyncPageStreaming[Player]</a></code>
- <code title="delete /streaming/players/{player_id}">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">delete</a>(player_id) -> None</code>
- <code title="get /streaming/players/{player_id}">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">get</a>(player_id) -> <a href="./src/gcore/types/streaming/player.py">Player</a></code>
- <code title="get /streaming/players/{player_id}/preview">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">preview</a>(player_id) -> None</code>

## QualitySets

Types:

```python
from gcore.types.streaming import QualitySets
```

Methods:

- <code title="get /streaming/quality_sets">client.streaming.quality_sets.<a href="./src/gcore/resources/streaming/quality_sets.py">list</a>() -> <a href="./src/gcore/types/streaming/quality_sets.py">QualitySets</a></code>
- <code title="put /streaming/quality_sets/default">client.streaming.quality_sets.<a href="./src/gcore/resources/streaming/quality_sets.py">set_default</a>(\*\*<a href="src/gcore/types/streaming/quality_set_set_default_params.py">params</a>) -> <a href="./src/gcore/types/streaming/quality_sets.py">QualitySets</a></code>

## Playlists

Types:

```python
from gcore.types.streaming import (
    Playlist,
    PlaylistCreated,
    PlaylistVideo,
    PlaylistListVideosResponse,
)
```

Methods:

- <code title="post /streaming/playlists">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">create</a>(\*\*<a href="src/gcore/types/streaming/playlist_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/playlist_created.py">PlaylistCreated</a></code>
- <code title="patch /streaming/playlists/{playlist_id}">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">update</a>(playlist_id, \*\*<a href="src/gcore/types/streaming/playlist_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/playlist.py">Playlist</a></code>
- <code title="get /streaming/playlists">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">list</a>(\*\*<a href="src/gcore/types/streaming/playlist_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/playlist.py">SyncPageStreaming[Playlist]</a></code>
- <code title="delete /streaming/playlists/{playlist_id}">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">delete</a>(playlist_id) -> None</code>
- <code title="get /streaming/playlists/{playlist_id}">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">get</a>(playlist_id) -> <a href="./src/gcore/types/streaming/playlist.py">Playlist</a></code>
- <code title="get /streaming/playlists/{playlist_id}/videos">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">list_videos</a>(playlist_id) -> <a href="./src/gcore/types/streaming/playlist_list_videos_response.py">PlaylistListVideosResponse</a></code>

## Videos

Types:

```python
from gcore.types.streaming import (
    DirectUploadParameters,
    Subtitle,
    SubtitleBase,
    SubtitleBody,
    SubtitleUpdated,
    VideoCreateResponse,
    VideoCreateMultipleResponse,
)
```

Methods:

- <code title="post /streaming/videos">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">create</a>(\*\*<a href="src/gcore/types/streaming/video_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video_create_response.py">VideoCreateResponse</a></code>
- <code title="patch /streaming/videos/{video_id}">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">update</a>(video_id, \*\*<a href="src/gcore/types/streaming/video_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video.py">Video</a></code>
- <code title="get /streaming/videos">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">list</a>(\*\*<a href="src/gcore/types/streaming/video_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video.py">SyncPageStreaming[Video]</a></code>
- <code title="delete /streaming/videos/{video_id}">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">delete</a>(video_id) -> None</code>
- <code title="post /streaming/videos/batch">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">create_multiple</a>(\*\*<a href="src/gcore/types/streaming/video_create_multiple_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video_create_multiple_response.py">VideoCreateMultipleResponse</a></code>
- <code title="get /streaming/videos/{video_id}">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">get</a>(video_id) -> <a href="./src/gcore/types/streaming/video.py">Video</a></code>
- <code title="get /streaming/videos/{video_id}/upload">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">get_parameters_for_direct_upload</a>(video_id) -> <a href="./src/gcore/types/streaming/direct_upload_parameters.py">DirectUploadParameters</a></code>
- <code title="get /streaming/videos/names">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">list_names</a>(\*\*<a href="src/gcore/types/streaming/video_list_names_params.py">params</a>) -> None</code>

### Subtitles

Types:

```python
from gcore.types.streaming.videos import SubtitleListResponse
```

Methods:

- <code title="post /streaming/videos/{video_id}/subtitles">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">create</a>(video_id, \*\*<a href="src/gcore/types/streaming/videos/subtitle_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/subtitle.py">Subtitle</a></code>
- <code title="patch /streaming/videos/{video_id}/subtitles/{id}">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">update</a>(id, \*, video_id, \*\*<a href="src/gcore/types/streaming/videos/subtitle_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/subtitle_base.py">SubtitleBase</a></code>
- <code title="get /streaming/videos/{video_id}/subtitles">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">list</a>(video_id) -> <a href="./src/gcore/types/streaming/videos/subtitle_list_response.py">SubtitleListResponse</a></code>
- <code title="delete /streaming/videos/{video_id}/subtitles/{id}">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">delete</a>(id, \*, video_id) -> None</code>
- <code title="get /streaming/videos/{video_id}/subtitles/{id}">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">get</a>(id, \*, video_id) -> <a href="./src/gcore/types/streaming/subtitle.py">Subtitle</a></code>

## Streams

Types:

```python
from gcore.types.streaming import (
    Clip,
    Stream,
    StreamListClipsResponse,
    StreamStartRecordingResponse,
)
```

Methods:

- <code title="post /streaming/streams">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">create</a>(\*\*<a href="src/gcore/types/streaming/stream_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream.py">Stream</a></code>
- <code title="patch /streaming/streams/{stream_id}">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">update</a>(stream_id, \*\*<a href="src/gcore/types/streaming/stream_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream.py">Stream</a></code>
- <code title="get /streaming/streams">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">list</a>(\*\*<a href="src/gcore/types/streaming/stream_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream.py">SyncPageStreaming[Stream]</a></code>
- <code title="delete /streaming/streams/{stream_id}">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">delete</a>(stream_id) -> None</code>
- <code title="put /streaming/streams/{stream_id}/dvr_cleanup">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">clear_dvr</a>(stream_id) -> None</code>
- <code title="put /streaming/streams/{stream_id}/clip_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">create_clip</a>(stream_id, \*\*<a href="src/gcore/types/streaming/stream_create_clip_params.py">params</a>) -> <a href="./src/gcore/types/streaming/clip.py">Clip</a></code>
- <code title="get /streaming/streams/{stream_id}">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">get</a>(stream_id) -> <a href="./src/gcore/types/streaming/stream.py">Stream</a></code>
- <code title="get /streaming/streams/{stream_id}/clip_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">list_clips</a>(stream_id) -> <a href="./src/gcore/types/streaming/stream_list_clips_response.py">StreamListClipsResponse</a></code>
- <code title="put /streaming/streams/{stream_id}/start_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">start_recording</a>(stream_id) -> <a href="./src/gcore/types/streaming/stream_start_recording_response.py">StreamStartRecordingResponse</a></code>
- <code title="put /streaming/streams/{stream_id}/stop_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">stop_recording</a>(stream_id) -> <a href="./src/gcore/types/streaming/video.py">Video</a></code>

### Overlays

Types:

```python
from gcore.types.streaming.streams import (
    Overlay,
    OverlayCreateResponse,
    OverlayListResponse,
    OverlayUpdateMultipleResponse,
)
```

Methods:

- <code title="post /streaming/streams/{stream_id}/overlays">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">create</a>(stream_id, \*\*<a href="src/gcore/types/streaming/streams/overlay_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/streams/overlay_create_response.py">OverlayCreateResponse</a></code>
- <code title="patch /streaming/streams/{stream_id}/overlays/{overlay_id}">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">update</a>(overlay_id, \*, stream_id, \*\*<a href="src/gcore/types/streaming/streams/overlay_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/streams/overlay.py">Overlay</a></code>
- <code title="get /streaming/streams/{stream_id}/overlays">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">list</a>(stream_id) -> <a href="./src/gcore/types/streaming/streams/overlay_list_response.py">OverlayListResponse</a></code>
- <code title="delete /streaming/streams/{stream_id}/overlays/{overlay_id}">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">delete</a>(overlay_id, \*, stream_id) -> None</code>
- <code title="get /streaming/streams/{stream_id}/overlays/{overlay_id}">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">get</a>(overlay_id, \*, stream_id) -> <a href="./src/gcore/types/streaming/streams/overlay.py">Overlay</a></code>
- <code title="patch /streaming/streams/{stream_id}/overlays">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">update_multiple</a>(stream_id, \*\*<a href="src/gcore/types/streaming/streams/overlay_update_multiple_params.py">params</a>) -> <a href="./src/gcore/types/streaming/streams/overlay_update_multiple_response.py">OverlayUpdateMultipleResponse</a></code>

## Restreams

Types:

```python
from gcore.types.streaming import Restream
```

Methods:

- <code title="post /streaming/restreams">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">create</a>(\*\*<a href="src/gcore/types/streaming/restream_create_params.py">params</a>) -> None</code>
- <code title="patch /streaming/restreams/{restream_id}">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">update</a>(restream_id, \*\*<a href="src/gcore/types/streaming/restream_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/restream.py">Restream</a></code>
- <code title="get /streaming/restreams">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">list</a>(\*\*<a href="src/gcore/types/streaming/restream_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/restream.py">SyncPageStreaming[Restream]</a></code>
- <code title="delete /streaming/restreams/{restream_id}">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">delete</a>(restream_id) -> None</code>
- <code title="get /streaming/restreams/{restream_id}">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">get</a>(restream_id) -> <a href="./src/gcore/types/streaming/restream.py">Restream</a></code>

## Statistics

Types:

```python
from gcore.types.streaming import (
    Ffprobes,
    MaxStreamSeries,
    PopularVideos,
    StorageSeries,
    StreamSeries,
    UniqueViewers,
    UniqueViewersCDN,
    Views,
    ViewsByBrowser,
    ViewsByCountry,
    ViewsByHostname,
    ViewsByOperatingSystem,
    ViewsByReferer,
    ViewsByRegion,
    ViewsHeatmap,
    VodStatisticsSeries,
    VodTotalStreamDurationSeries,
    StatisticGetLiveUniqueViewersResponse,
    StatisticGetVodWatchTimeTotalCDNResponse,
)
```

Methods:

- <code title="get /streaming/statistics/ffprobe">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_ffprobes</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_ffprobes_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ffprobes.py">Ffprobes</a></code>
- <code title="get /streaming/statistics/stream/viewers">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_live_unique_viewers</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_live_unique_viewers_params.py">params</a>) -> <a href="./src/gcore/types/streaming/statistic_get_live_unique_viewers_response.py">StatisticGetLiveUniqueViewersResponse</a></code>
- <code title="get /streaming/statistics/stream/watching_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_live_watch_time_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_live_watch_time_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream_series.py">StreamSeries</a></code>
- <code title="get /streaming/statistics/stream/watching_duration/total">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_live_watch_time_total_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_live_watch_time_total_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_total_stream_duration_series.py">VodTotalStreamDurationSeries</a></code>
- <code title="get /streaming/statistics/max_stream">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_max_streams_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_max_streams_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/max_stream_series.py">MaxStreamSeries</a></code>
- <code title="get /streaming/statistics/popular">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_popular_videos</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_popular_videos_params.py">params</a>) -> <a href="./src/gcore/types/streaming/popular_videos.py">PopularVideos</a></code>
- <code title="get /streaming/statistics/storage">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_storage_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_storage_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/storage_series.py">StorageSeries</a></code>
- <code title="get /streaming/statistics/stream">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_stream_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_stream_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream_series.py">StreamSeries</a></code>
- <code title="get /streaming/statistics/uniqs">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_unique_viewers</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_unique_viewers_params.py">params</a>) -> <a href="./src/gcore/types/streaming/unique_viewers.py">UniqueViewers</a></code>
- <code title="get /streaming/statistics/cdn/uniqs">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_unique_viewers_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_unique_viewers_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/unique_viewers_cdn.py">UniqueViewersCDN</a></code>
- <code title="get /streaming/statistics/views">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views.py">Views</a></code>
- <code title="get /streaming/statistics/browsers">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_browsers</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_browsers_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_browser.py">ViewsByBrowser</a></code>
- <code title="get /streaming/statistics/countries">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_country</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_country_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_country.py">ViewsByCountry</a></code>
- <code title="get /streaming/statistics/hosts">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_hostname</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_hostname_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_hostname.py">ViewsByHostname</a></code>
- <code title="get /streaming/statistics/systems">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_operating_system</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_operating_system_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_operating_system.py">ViewsByOperatingSystem</a></code>
- <code title="get /streaming/statistics/embeds">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_referer</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_referer_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_referer.py">ViewsByReferer</a></code>
- <code title="get /streaming/statistics/regions">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_region</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_region_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_region.py">ViewsByRegion</a></code>
- <code title="get /streaming/statistics/heatmap">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_heatmap</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_heatmap_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_heatmap.py">ViewsHeatmap</a></code>
- <code title="get /streaming/statistics/vod/storage_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_storage_volume</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_storage_volume_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/transcoding_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_transcoding_duration</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_transcoding_duration_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/viewers">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_unique_viewers_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_unique_viewers_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/watching_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_watch_time_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_watch_time_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/watching_duration/total">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_watch_time_total_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_watch_time_total_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/statistic_get_vod_watch_time_total_cdn_response.py">StatisticGetVodWatchTimeTotalCDNResponse</a></code>
