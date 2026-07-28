# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import required_args
from ....types.cloud import (
    file_share_create_params,
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

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Create file share and poll for the result."""
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        protocol: Literal["NFS"],
        size: int,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["vast"] | Omit = omit,
        volume_type: Literal["vast_share_type"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Create file share and poll for the result."""
        ...

    @required_args(["name", "network", "protocol", "size"], ["name", "protocol", "size"])
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork | Omit = omit,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Literal["vast"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Literal["vast_share_type"] | Omit = omit,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Create file share and poll for the result."""
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            network=network,
            protocol=protocol,
            size=size,
            access=access,
            tags=tags,
            type_name=type_name,
            volume_type=volume_type,
            share_settings=share_settings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.file_shares
            or len(task.created_resources.file_shares) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            FileShare,
            self.get(
                task.created_resources.file_shares[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

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

    def delete_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete file share and poll for the result."""
        response = self.delete(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def resize_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Resize file share and poll for the result."""
        response = self.resize(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            size=size,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
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

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Create file share and poll for the result."""
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        protocol: Literal["NFS"],
        size: int,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["vast"] | Omit = omit,
        volume_type: Literal["vast_share_type"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Create file share and poll for the result."""
        ...

    @required_args(["name", "network", "protocol", "size"], ["name", "protocol", "size"])
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        network: file_share_create_params.CreateStandardFileShareSerializerNetwork | Omit = omit,
        protocol: Literal["NFS"],
        size: int,
        access: Iterable[file_share_create_params.CreateStandardFileShareSerializerAccess] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        type_name: Literal["standard"] | Literal["vast"] | Omit = omit,
        volume_type: Literal["default_share_type"] | Literal["vast_share_type"] | Omit = omit,
        share_settings: file_share_create_params.CreateVastFileShareSerializerShareSettings | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Create file share and poll for the result."""
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            network=network,
            protocol=protocol,
            size=size,
            access=access,
            tags=tags,
            type_name=type_name,
            volume_type=volume_type,
            share_settings=share_settings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.file_shares
            or len(task.created_resources.file_shares) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            FileShare,
            await self.get(
                task.created_resources.file_shares[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

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

    async def delete_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete file share and poll for the result."""
        response = await self.delete(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def resize_and_poll(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileShare:
        """Resize file share and poll for the result."""
        response = await self.resize(
            file_share_id,
            project_id=project_id,
            region_id=region_id,
            size=size,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
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
