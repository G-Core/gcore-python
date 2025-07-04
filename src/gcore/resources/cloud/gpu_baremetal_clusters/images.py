# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
from ....types.cloud.gpu_image import GPUImage
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.gpu_image_list import GPUImageList
from ....types.cloud.gpu_baremetal_clusters import image_upload_params

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

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUImageList:
        """
        List bare metal GPU images

        Args:
          project_id: Project ID

          region_id: Region ID

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImageList,
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
        """
        Delete bare metal GPU image

        Args:
          project_id: Project ID

          region_id: Region ID

          image_id: Image ID

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
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
        Delete a bare metal GPU image and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
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
        )

    def get(
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
    ) -> GPUImage:
        """
        Get bare metal GPU image

        Args:
          project_id: Project ID

          region_id: Region ID

          image_id: Image ID

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImage,
        )

    def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Optional[Literal["aarch64", "x86_64"]] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Optional[Literal["linux", "windows"]] | NotGiven = NOT_GIVEN,
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
        """
        Upload new bare metal GPU image

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Image name

          url: Image URL

          architecture: Image architecture type: aarch64, `x86_64`

          cow_format: When True, image cannot be deleted unless all volumes, created from it, are
              deleted.

          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          os_distro: OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc.

          os_type: The operating system installed on the image. Linux by default

          os_version: OS version, i.e. 19.04 (for Ubuntu) or 9.4 for Debian

          ssh_key: Permission to use a ssh key in instances

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
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
        architecture: Optional[Literal["aarch64", "x86_64"]] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Optional[Literal["linux", "windows"]] | NotGiven = NOT_GIVEN,
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
    ) -> GPUImage:
        """
        Upload a new bare metal GPU image and wait for the upload to complete.
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
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.images:
            raise ValueError("No image was created")
        image_id = task.created_resources.images[0]
        return self.get(
            image_id=image_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUImageList:
        """
        List bare metal GPU images

        Args:
          project_id: Project ID

          region_id: Region ID

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImageList,
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
        """
        Delete bare metal GPU image

        Args:
          project_id: Project ID

          region_id: Region ID

          image_id: Image ID

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
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
        Delete a bare metal GPU image and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
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
        )

    async def get(
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
    ) -> GPUImage:
        """
        Get bare metal GPU image

        Args:
          project_id: Project ID

          region_id: Region ID

          image_id: Image ID

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImage,
        )

    async def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Optional[Literal["aarch64", "x86_64"]] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Optional[Literal["linux", "windows"]] | NotGiven = NOT_GIVEN,
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
        """
        Upload new bare metal GPU image

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Image name

          url: Image URL

          architecture: Image architecture type: aarch64, `x86_64`

          cow_format: When True, image cannot be deleted unless all volumes, created from it, are
              deleted.

          hw_firmware_type: Specifies the type of firmware with which to boot the guest.

          os_distro: OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc.

          os_type: The operating system installed on the image. Linux by default

          os_version: OS version, i.e. 19.04 (for Ubuntu) or 9.4 for Debian

          ssh_key: Permission to use a ssh key in instances

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
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
        architecture: Optional[Literal["aarch64", "x86_64"]] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Optional[Literal["linux", "windows"]] | NotGiven = NOT_GIVEN,
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
    ) -> GPUImage:
        """
        Upload a new bare metal GPU image and wait for the upload to complete.
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
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.images:
            raise ValueError("No image was created")
        image_id = task.created_resources.images[0]
        return await self.get(
            image_id=image_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
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

        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
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

        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
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

        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            images.get,
        )
        self.upload = async_to_streamed_response_wrapper(
            images.upload,
        )
