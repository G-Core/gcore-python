# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, Dict, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ...._utils import is_given
from ....types.cloud.instances.image import Image

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete image and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
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
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def create_from_volume_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | Omit = omit,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | Omit = omit,
        hw_machine_type: Optional[Literal["i440", "q35"]] | Omit = omit,
        is_baremetal: bool | Omit = omit,
        os_type: Literal["linux", "windows"] | Omit = omit,
        source: Literal["volume"] | Omit = omit,
        ssh_key: Literal["allow", "deny", "required"] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Create image from volume and poll for completion
        """
        response = self.create_from_volume(
            project_id=project_id,
            region_id=region_id,
            name=name,
            volume_id=volume_id,
            architecture=architecture,
            hw_firmware_type=hw_firmware_type,
            hw_machine_type=hw_machine_type,
            is_baremetal=is_baremetal,
            os_type=os_type,
            source=source,
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
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Image,
            self.get(
                image_id=task.created_resources.images[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    def upload_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | Omit = omit,
        cow_format: bool | Omit = omit,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | Omit = omit,
        hw_machine_type: Optional[Literal["i440", "q35"]] | Omit = omit,
        is_baremetal: bool | Omit = omit,
        os_distro: Optional[str] | Omit = omit,
        os_type: Literal["linux", "windows"] | Omit = omit,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Upload image and poll for completion
        """
        response = self.upload(
            project_id=project_id,
            region_id=region_id,
            name=name,
            url=url,
            architecture=architecture,
            cow_format=cow_format,
            hw_firmware_type=hw_firmware_type,
            hw_machine_type=hw_machine_type,
            is_baremetal=is_baremetal,
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
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        image_id = task.created_resources.images[0]

        # The upload task is marked complete as soon as the image bytes are handed
        # off to the image store; the image itself then transitions
        # queued -> saving -> active asynchronously and only reports its final
        # `size` once active. Poll the image until it settles so callers observe
        # fully-resolved fields instead of a transient `status="saving", size=0`.
        if not is_given(polling_interval_seconds):
            polling_interval_seconds = cast(int, self._client.polling_interval_seconds)
        polling_interval_seconds = max(1, polling_interval_seconds)
        if not is_given(polling_timeout_seconds):
            polling_timeout_seconds = cast(int, self._client.polling_timeout_seconds)
        end_time = time.time() + polling_timeout_seconds
        while True:
            image = cast(
                Image,
                self.get(
                    image_id=image_id,
                    project_id=project_id,
                    region_id=region_id,
                    extra_headers=extra_headers,
                ),
            )
            if image.status == "active" and image.size:
                return image
            if image.status not in ("queued", "saving", "active"):
                raise ValueError(
                    f"Image {image_id} entered unexpected status {image.status!r} while waiting for it to become active"
                )
            if time.time() >= end_time:
                raise RuntimeError(
                    f"Timed out waiting for image {image_id} to become active (last status {image.status!r})"
                )
            self._sleep(polling_interval_seconds)


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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete image and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
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
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def create_from_volume_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | Omit = omit,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | Omit = omit,
        hw_machine_type: Optional[Literal["i440", "q35"]] | Omit = omit,
        is_baremetal: bool | Omit = omit,
        os_type: Literal["linux", "windows"] | Omit = omit,
        source: Literal["volume"] | Omit = omit,
        ssh_key: Literal["allow", "deny", "required"] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Create image from volume and poll for completion
        """
        response = await self.create_from_volume(
            project_id=project_id,
            region_id=region_id,
            name=name,
            volume_id=volume_id,
            architecture=architecture,
            hw_firmware_type=hw_firmware_type,
            hw_machine_type=hw_machine_type,
            is_baremetal=is_baremetal,
            os_type=os_type,
            source=source,
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
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Image,
            await self.get(
                image_id=task.created_resources.images[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    async def upload_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | Omit = omit,
        cow_format: bool | Omit = omit,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | Omit = omit,
        hw_machine_type: Optional[Literal["i440", "q35"]] | Omit = omit,
        is_baremetal: bool | Omit = omit,
        os_distro: Optional[str] | Omit = omit,
        os_type: Literal["linux", "windows"] | Omit = omit,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Upload image and poll for completion
        """
        response = await self.upload(
            project_id=project_id,
            region_id=region_id,
            name=name,
            url=url,
            architecture=architecture,
            cow_format=cow_format,
            hw_firmware_type=hw_firmware_type,
            hw_machine_type=hw_machine_type,
            is_baremetal=is_baremetal,
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
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        image_id = task.created_resources.images[0]

        # The upload task is marked complete as soon as the image bytes are handed
        # off to the image store; the image itself then transitions
        # queued -> saving -> active asynchronously and only reports its final
        # `size` once active. Poll the image until it settles so callers observe
        # fully-resolved fields instead of a transient `status="saving", size=0`.
        if not is_given(polling_interval_seconds):
            polling_interval_seconds = cast(int, self._client.polling_interval_seconds)
        polling_interval_seconds = max(1, polling_interval_seconds)
        if not is_given(polling_timeout_seconds):
            polling_timeout_seconds = cast(int, self._client.polling_timeout_seconds)
        end_time = time.time() + polling_timeout_seconds
        while True:
            image = cast(
                Image,
                await self.get(
                    image_id=image_id,
                    project_id=project_id,
                    region_id=region_id,
                    extra_headers=extra_headers,
                ),
            )
            if image.status == "active" and image.size:
                return image
            if image.status not in ("queued", "saving", "active"):
                raise ValueError(
                    f"Image {image_id} entered unexpected status {image.status!r} while waiting for it to become active"
                )
            if time.time() >= end_time:
                raise RuntimeError(
                    f"Timed out waiting for image {image_id} to become active (last status {image.status!r})"
                )
            await self._sleep(polling_interval_seconds)
