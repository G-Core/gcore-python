# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .....types.cloud.gpu_image import GPUImage

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class ImagesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def delete_and_poll(
        self,
        image_id: str,
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
        """
        Delete a virtual GPU image and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            image_id=image_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def upload_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Optional[Literal["aarch64", "x86_64"]] | Omit = omit,
        cow_format: bool | Omit = omit,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | Omit = omit,
        os_distro: Optional[str] | Omit = omit,
        os_type: Optional[Literal["linux", "windows"]] | Omit = omit,
        os_version: Optional[str] | Omit = omit,
        ssh_key: Literal["allow", "deny", "required"] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUImage:
        """
        Upload a new virtual GPU image and wait for the upload to complete.
        """
        response = self.upload(
            project_id=project_id,
            region_id=region_id,
            name=name,
            url=url,
            architecture=architecture,
            cow_format=cow_format,
            hw_firmware_type=hw_firmware_type,
            os_distro=os_distro,
            os_type=os_type,
            os_version=os_version,
            ssh_key=ssh_key,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.images:
            raise ValueError("No image was created")
        image_id = task.created_resources.images[0]
        return cast(
            GPUImage,
            self.get(
                image_id=image_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncImagesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def delete_and_poll(
        self,
        image_id: str,
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
        """
        Delete a virtual GPU image and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            image_id=image_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def upload_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Optional[Literal["aarch64", "x86_64"]] | Omit = omit,
        cow_format: bool | Omit = omit,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | Omit = omit,
        os_distro: Optional[str] | Omit = omit,
        os_type: Optional[Literal["linux", "windows"]] | Omit = omit,
        os_version: Optional[str] | Omit = omit,
        ssh_key: Literal["allow", "deny", "required"] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUImage:
        """
        Upload a new virtual GPU image and wait for the upload to complete.
        """
        response = await self.upload(
            project_id=project_id,
            region_id=region_id,
            name=name,
            url=url,
            architecture=architecture,
            cow_format=cow_format,
            hw_firmware_type=hw_firmware_type,
            os_distro=os_distro,
            os_type=os_type,
            os_version=os_version,
            ssh_key=ssh_key,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.images:
            raise ValueError("No image was created")
        image_id = task.created_resources.images[0]
        return cast(
            GPUImage,
            await self.get(
                image_id=image_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
