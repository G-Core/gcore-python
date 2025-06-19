# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.image import Image
from ....types.cloud.instances import (
    image_get_params,
    image_list_params,
    image_update_params,
    image_upload_params,
    image_create_from_volume_params,
)
from ....types.cloud.image_list import ImageList
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def update(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        hw_firmware_type: Literal["bios", "uefi"] | NotGiven = NOT_GIVEN,
        hw_machine_type: Literal["pc", "q35"] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Update image properties and tags.

        Args:
          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          hw_machine_type: A virtual chipset type.

          is_baremetal: Set to true if the image will be used by bare metal servers.

          name: Image display name

          os_type: The operating system installed on the image.

          ssh_key: Whether the image supports SSH key or not

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._patch(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            body=maybe_transform(
                {
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "name": name,
                    "os_type": os_type,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Image,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        private: str | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        visibility: Literal["private", "public", "shared"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageList:
        """Retrieve a list of available images in the project and region.

        The list can be
        filtered by visibility, tags, and other parameters. Returned entities are owned
        by the project or are public/shared with the client.

        Args:
          include_prices: Show price

          private: Any value to show private images

          tag_key: Filter by tag keys.

          tag_key_value: Filter by tag key-value pairs. Must be a valid JSON string.

          visibility: Image visibility. Globally visible images are public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/images/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_prices": include_prices,
                        "private": private,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                        "visibility": visibility,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageList,
        )

    def delete(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Delete a specific image.

        The image cannot be deleted if it is used by protected
        snapshots.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._delete(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def delete_and_poll(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
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
        )

    def create_from_volume(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        source: Literal["volume"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new image from a bootable volume.

        The volume must be bootable to create
        an image from it.

        Args:
          name: Image name

          volume_id: Required if source is volume. Volume id

          architecture: Image CPU architecture type: `aarch64`, `x86_64`

          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          hw_machine_type: A virtual chipset type.

          is_baremetal: Set to true if the image will be used by bare metal servers. Defaults to false.

          os_type: The operating system installed on the image.

          source: Image source

          ssh_key: Whether the image supports SSH key or not

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/images/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "volume_id": volume_id,
                    "architecture": architecture,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_type": os_type,
                    "source": source,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_create_from_volume_params.ImageCreateFromVolumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def create_from_volume_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        source: Literal["volume"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
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
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            image_id=task.created_resources.images[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )

    def get(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Retrieve detailed information about a specific image.

        Args:
          include_prices: Show price

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._get(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_prices": include_prices}, image_get_params.ImageGetParams),
            ),
            cast_to=Image,
        )

    def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Upload an image from a URL.

        The image can be configured with various properties
        like OS type, architecture, and tags.

        Args:
          name: Image name

          url: URL

          architecture: Image CPU architecture type: `aarch64`, `x86_64`

          cow_format: When True, image cannot be deleted unless all volumes, created from it, are
              deleted.

          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          hw_machine_type: A virtual chipset type.

          is_baremetal: Set to true if the image will be used by bare metal servers. Defaults to false.

          os_distro: OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc.

          os_type: The operating system installed on the image.

          os_version: OS version, i.e. 22.04 (for Ubuntu) or 9.4 for Debian

          ssh_key: Whether the image supports SSH key or not

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/downloadimage/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_distro": os_distro,
                    "os_type": os_type,
                    "os_version": os_version,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_upload_params.ImageUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def upload_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
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
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            image_id=task.created_resources.images[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def update(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        hw_firmware_type: Literal["bios", "uefi"] | NotGiven = NOT_GIVEN,
        hw_machine_type: Literal["pc", "q35"] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Update image properties and tags.

        Args:
          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          hw_machine_type: A virtual chipset type.

          is_baremetal: Set to true if the image will be used by bare metal servers.

          name: Image display name

          os_type: The operating system installed on the image.

          ssh_key: Whether the image supports SSH key or not

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._patch(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            body=await async_maybe_transform(
                {
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "name": name,
                    "os_type": os_type,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Image,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        private: str | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        visibility: Literal["private", "public", "shared"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageList:
        """Retrieve a list of available images in the project and region.

        The list can be
        filtered by visibility, tags, and other parameters. Returned entities are owned
        by the project or are public/shared with the client.

        Args:
          include_prices: Show price

          private: Any value to show private images

          tag_key: Filter by tag keys.

          tag_key_value: Filter by tag key-value pairs. Must be a valid JSON string.

          visibility: Image visibility. Globally visible images are public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/images/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_prices": include_prices,
                        "private": private,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                        "visibility": visibility,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageList,
        )

    async def delete(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Delete a specific image.

        The image cannot be deleted if it is used by protected
        snapshots.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._delete(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def delete_and_poll(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
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
        )

    async def create_from_volume(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        source: Literal["volume"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new image from a bootable volume.

        The volume must be bootable to create
        an image from it.

        Args:
          name: Image name

          volume_id: Required if source is volume. Volume id

          architecture: Image CPU architecture type: `aarch64`, `x86_64`

          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          hw_machine_type: A virtual chipset type.

          is_baremetal: Set to true if the image will be used by bare metal servers. Defaults to false.

          os_type: The operating system installed on the image.

          source: Image source

          ssh_key: Whether the image supports SSH key or not

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/images/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "volume_id": volume_id,
                    "architecture": architecture,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_type": os_type,
                    "source": source,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_create_from_volume_params.ImageCreateFromVolumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def create_from_volume_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        source: Literal["volume"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
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
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            image_id=task.created_resources.images[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )

    async def get(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Retrieve detailed information about a specific image.

        Args:
          include_prices: Show price

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._get(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include_prices": include_prices}, image_get_params.ImageGetParams),
            ),
            cast_to=Image,
        )

    async def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Upload an image from a URL.

        The image can be configured with various properties
        like OS type, architecture, and tags.

        Args:
          name: Image name

          url: URL

          architecture: Image CPU architecture type: `aarch64`, `x86_64`

          cow_format: When True, image cannot be deleted unless all volumes, created from it, are
              deleted.

          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          hw_machine_type: A virtual chipset type.

          is_baremetal: Set to true if the image will be used by bare metal servers. Defaults to false.

          os_distro: OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc.

          os_type: The operating system installed on the image.

          os_version: OS version, i.e. 22.04 (for Ubuntu) or 9.4 for Debian

          ssh_key: Whether the image supports SSH key or not

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/downloadimage/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_distro": os_distro,
                    "os_type": os_type,
                    "os_version": os_version,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_upload_params.ImageUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def upload_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
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
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.images or len(task.created_resources.images) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            image_id=task.created_resources.images[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.update = to_raw_response_wrapper(
            images.update,
        )
        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
        )
        self.create_from_volume = to_raw_response_wrapper(
            images.create_from_volume,
        )
        self.get = to_raw_response_wrapper(
            images.get,
        )
        self.upload = to_raw_response_wrapper(
            images.upload,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.update = async_to_raw_response_wrapper(
            images.update,
        )
        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
        )
        self.create_from_volume = async_to_raw_response_wrapper(
            images.create_from_volume,
        )
        self.get = async_to_raw_response_wrapper(
            images.get,
        )
        self.upload = async_to_raw_response_wrapper(
            images.upload,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.update = to_streamed_response_wrapper(
            images.update,
        )
        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
        )
        self.create_from_volume = to_streamed_response_wrapper(
            images.create_from_volume,
        )
        self.get = to_streamed_response_wrapper(
            images.get,
        )
        self.upload = to_streamed_response_wrapper(
            images.upload,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.update = async_to_streamed_response_wrapper(
            images.update,
        )
        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )
        self.create_from_volume = async_to_streamed_response_wrapper(
            images.create_from_volume,
        )
        self.get = async_to_streamed_response_wrapper(
            images.get,
        )
        self.upload = async_to_streamed_response_wrapper(
            images.upload,
        )
