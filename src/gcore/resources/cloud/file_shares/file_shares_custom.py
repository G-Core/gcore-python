# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....types.cloud import (
    file_share_update_params,
)
from ....types.cloud.file_share import FileShare
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class FileSharesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def update_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        share_settings: file_share_update_params.ShareSettings | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        response = self.update(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            name=name,
            share_settings=share_settings,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if response.tasks:
            self._client.cloud.tasks.poll(
                task_id=response.tasks[0],
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        return cast(
            FileShare,
            self.get(
                file_share_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncFileSharesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def update_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        share_settings: file_share_update_params.ShareSettings | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        response = await self.update(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            name=name,
            share_settings=share_settings,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if response.tasks:
            await self._client.cloud.tasks.poll(
                task_id=response.tasks[0],
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        return cast(
            FileShare,
            await self.get(
                file_share_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
