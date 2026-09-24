# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RestreamUpdateParams", "Restream"]


class RestreamUpdateParams(TypedDict, total=False):
    restream: Restream


class Restream(TypedDict, total=False):
    active: bool
    """Enables/Disables restream. Has two possible values:

    - **true** — restream is enabled and can be started
    - **false** — restream is disabled.

    Default is true
    """

    client_user_id: int
    """Custom field where you can specify user ID in your system"""

    live: bool
    """Indicates that the stream is being published. Has two possible values:

    - **true** — stream is being published
    - **false** — stream isn't published
    """

    name: str
    """Restream name"""

    no_audio: bool
    """Removes the source audio track from the restream. Has two possible values:

    - false – the source audio track is forwarded to the target as is (default)
    - true – the audio track is removed or replaced, depending on `no_audio_mode`

    Useful to avoid copyright claims on platforms like YouTube when the source
    stream contains licensed music or other copyrighted audio.

    Only strict boolean values (`true`/`false`) are accepted; any other value
    returns a 422 error.
    """

    no_audio_mode: Literal["drop", "silence"]
    """Defines how the audio track is handled when `no_audio` is `true`.

    Ignored when `no_audio` is `false`.

    Types:

    - "drop" – removes the audio track entirely.
    - "silence" – replaces the audio track with a silent track instead of removing
      it.

    > **Note:** YouTube rejects incoming streams with no audio track at all. Use
    > `no_audio_mode=silence` when restreaming to YouTube.
    """

    source: Literal["original", "transcoded"]
    """Selects which version of the stream is used as the source for the restream.

    Types:

    - "original" – uses the original ingested stream without any modifications
      (default).
    - "transcoded" – uses the transcoded output, including overlays. Use it when you
      want to restream the stream with enabled overlays.

    > **Note:** For `transcoded`, the highest quality available in the stream's
    > quality ladder is used. For example, if the ladder is 480p/720p/1080p, 1080p
    > is used; if the ladder goes up to 4K, 4K is used.
    """

    stream_id: int
    """ID of the stream to restream"""

    uri: str
    """A URL to push the stream to.

    Supported protocols: rtmp, rtmps, srt. For SRT target URLs, only `mode=caller`
    is supported.
    """
