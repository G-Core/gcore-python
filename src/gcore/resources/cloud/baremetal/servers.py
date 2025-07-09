# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
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
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.baremetal import server_list_params, server_create_params, server_rebuild_params
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.baremetal.baremetal_server import BaremetalServer

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ServersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[object] | NotGiven = NOT_GIVEN,
        apptemplate_id: str | NotGiven = NOT_GIVEN,
        ddos_profile: server_create_params.DDOSProfile | NotGiven = NOT_GIVEN,
        image_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new bare metal server with the specified configuration.

        How to get
        access: For Linux,

        - Use the `user_data` field to provide a
          [cloud-init script](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)
          in base64 to apply configurations to the instance.
        - Specify the `username` and `password` to create a new user.
        - When only `password` is provided, it is set as the password for the default
          user of the image.
        - The `user_data` is ignored when the `password` is specified. For Windows,
        - Use the `user_data` field to provide a
          [cloudbase-init script](https://cloudbase-init.readthedocs.io/en/latest/userdata.html#cloud-config)
          in base64 to create new users on Windows.
        - Use the `password` field to set the password for the 'Admin' user on Windows.
        - The password of the Admin user cannot be updated via `user_data`.
        - The `username` cannot be specified in the request.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: The flavor of the instance.

          interfaces: A list of network interfaces for the server. You can create one or more
              interfaces - private, public, or both.

          app_config: Parameters for the application template if creating the instance from an
              `apptemplate`.

          apptemplate_id: Apptemplate ID. Either `image_id` or `apptemplate_id` is required.

          ddos_profile: Enable advanced DDoS protection for the server

          image_id: Image ID. Either `image_id` or `apptemplate_id` is required.

          name: Server name.

          name_template: If you want server names to be automatically generated based on IP addresses,
              you can provide a name template instead of specifying the name manually. The
              template should include a placeholder that will be replaced during provisioning.
              Supported placeholders are: `{`ip_octets`}` (last 3 octets of the IP),
              `{`two_ip_octets`}`, and `{`one_ip_octet`}`.

          password: For Linux instances, 'username' and 'password' are used to create a new user.
              When only 'password' is provided, it is set as the password for the default user
              of the image. For Windows instances, 'username' cannot be specified. Use the
              'password' field to set the password for the 'Admin' user on Windows. Use the
              '`user_data`' field to provide a script to create new users on Windows. The
              password of the Admin user cannot be updated via '`user_data`'.

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          user_data: String in base64 format. For Linux instances, '`user_data`' is ignored when
              'password' field is provided. For Windows instances, Admin user password is set
              by 'password' field and cannot be updated via '`user_data`'. Examples of the
              `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          username: For Linux instances, 'username' and 'password' are used to create a new user.
              For Windows instances, 'username' cannot be specified. Use 'password' field to
              set the password for the 'Admin' user on Windows.

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
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "flavor": flavor,
                    "interfaces": interfaces,
                    "app_config": app_config,
                    "apptemplate_id": apptemplate_id,
                    "ddos_profile": ddos_profile,
                    "image_id": image_id,
                    "name": name,
                    "name_template": name_template,
                    "password": password,
                    "ssh_key_name": ssh_key_name,
                    "tags": tags,
                    "user_data": user_data,
                    "username": username,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        changes_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        changes_since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flavor_id: str | NotGiven = NOT_GIVEN,
        flavor_prefix: str | NotGiven = NOT_GIVEN,
        include_k8s: bool | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        only_isolated: bool | NotGiven = NOT_GIVEN,
        only_with_fixed_external_ip: bool | NotGiven = NOT_GIVEN,
        order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc", "status.asc", "status.desc"]
        | NotGiven = NOT_GIVEN,
        profile_name: str | NotGiven = NOT_GIVEN,
        protection_status: Literal["Active", "Queued", "Error"] | NotGiven = NOT_GIVEN,
        status: Literal[
            "ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "REBOOT", "REBUILD", "RESCUE", "SHUTOFF", "SUSPENDED"
        ]
        | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        tag_value: List[str] | NotGiven = NOT_GIVEN,
        type_ddos_profile: Literal["basic", "advanced"] | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        with_interfaces_name: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[BaremetalServer]:
        """List all bare metal servers in the specified project and region.

        Results can be
        filtered by various parameters like name, status, and IP address.

        Args:
          project_id: Project ID

          region_id: Region ID

          changes_before: Filters the instances by a date and time stamp when the instances last changed.

          changes_since: Filters the instances by a date and time stamp when the instances last changed
              status.

          flavor_id: Filter out instances by `flavor_id`. Flavor id must match exactly.

          flavor_prefix: Filter out instances by `flavor_prefix`.

          include_k8s: Include managed k8s worker nodes

          ip: An IPv4 address to filter results by. Note: partial matches are allowed. For
              example, searching for 192.168.0.1 will return 192.168.0.1, 192.168.0.10,
              192.168.0.110, and so on.

          limit: Optional. Limit the number of returned items

          name: Filter instances by name. You can provide a full or partial name, instances with
              matching names will be returned. For example, entering 'test' will return all
              instances that contain 'test' in their name.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          only_isolated: Include only isolated instances

          only_with_fixed_external_ip: Return bare metals only with external fixed IP addresses.

          order_by: Order by field and direction.

          profile_name: Filter result by ddos protection profile name. Effective only with `with_ddos`
              set to true.

          protection_status: Filter result by DDoS `protection_status`. Effective only with `with_ddos` set
              to true. (Active, Queued or Error)

          status: Filters instances by a server status, as a string.

          tag_key_value: Optional. Filter by tag key-value pairs.

          tag_value: Optional. Filter by tag values. ?`tag_value`=value1&`tag_value`=value2

          type_ddos_profile: Return bare metals either only with advanced or only basic DDoS protection.
              Effective only with `with_ddos` set to true. (advanced or basic)

          uuid: Filter the server list result by the UUID of the server. Allowed UUID part

          with_ddos: Include DDoS profile information for bare-metal servers in the response when set
              to `true`. Otherwise, the `ddos_profile` field in the response is `null` by
              default.

          with_interfaces_name: Include `interface_name` in the addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            page=SyncOffsetPage[BaremetalServer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changes_before": changes_before,
                        "changes_since": changes_since,
                        "flavor_id": flavor_id,
                        "flavor_prefix": flavor_prefix,
                        "include_k8s": include_k8s,
                        "ip": ip,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "only_isolated": only_isolated,
                        "only_with_fixed_external_ip": only_with_fixed_external_ip,
                        "order_by": order_by,
                        "profile_name": profile_name,
                        "protection_status": protection_status,
                        "status": status,
                        "tag_key_value": tag_key_value,
                        "tag_value": tag_value,
                        "type_ddos_profile": type_ddos_profile,
                        "uuid": uuid,
                        "with_ddos": with_ddos,
                        "with_interfaces_name": with_interfaces_name,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=BaremetalServer,
        )

    def rebuild(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Rebuild a bare metal server with a new image while preserving its configuration.

        Args:
          image_id: Image ID

          user_data: String in base64 format. Must not be passed together with 'username' or
              'password'. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._post(
            f"/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild",
            body=maybe_transform(
                {
                    "image_id": image_id,
                    "user_data": user_data,
                },
                server_rebuild_params.ServerRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[object] | NotGiven = NOT_GIVEN,
        apptemplate_id: str | NotGiven = NOT_GIVEN,
        ddos_profile: server_create_params.DDOSProfile | NotGiven = NOT_GIVEN,
        image_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Create a bare metal server and wait for it to be ready.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            app_config=app_config,
            apptemplate_id=apptemplate_id,
            ddos_profile=ddos_profile,
            image_id=image_id,
            name=name,
            name_template=name_template,
            password=password,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.instances:
            raise ValueError("No server was created")
        server_id = task.created_resources.instances[0]
        servers = self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return servers.results[0]

    def rebuild_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Rebuild a bare metal server and wait for it to be ready. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.rebuild(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        servers = self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return servers.results[0]


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncServersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[object] | NotGiven = NOT_GIVEN,
        apptemplate_id: str | NotGiven = NOT_GIVEN,
        ddos_profile: server_create_params.DDOSProfile | NotGiven = NOT_GIVEN,
        image_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new bare metal server with the specified configuration.

        How to get
        access: For Linux,

        - Use the `user_data` field to provide a
          [cloud-init script](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)
          in base64 to apply configurations to the instance.
        - Specify the `username` and `password` to create a new user.
        - When only `password` is provided, it is set as the password for the default
          user of the image.
        - The `user_data` is ignored when the `password` is specified. For Windows,
        - Use the `user_data` field to provide a
          [cloudbase-init script](https://cloudbase-init.readthedocs.io/en/latest/userdata.html#cloud-config)
          in base64 to create new users on Windows.
        - Use the `password` field to set the password for the 'Admin' user on Windows.
        - The password of the Admin user cannot be updated via `user_data`.
        - The `username` cannot be specified in the request.

        Args:
          project_id: Project ID

          region_id: Region ID

          flavor: The flavor of the instance.

          interfaces: A list of network interfaces for the server. You can create one or more
              interfaces - private, public, or both.

          app_config: Parameters for the application template if creating the instance from an
              `apptemplate`.

          apptemplate_id: Apptemplate ID. Either `image_id` or `apptemplate_id` is required.

          ddos_profile: Enable advanced DDoS protection for the server

          image_id: Image ID. Either `image_id` or `apptemplate_id` is required.

          name: Server name.

          name_template: If you want server names to be automatically generated based on IP addresses,
              you can provide a name template instead of specifying the name manually. The
              template should include a placeholder that will be replaced during provisioning.
              Supported placeholders are: `{`ip_octets`}` (last 3 octets of the IP),
              `{`two_ip_octets`}`, and `{`one_ip_octet`}`.

          password: For Linux instances, 'username' and 'password' are used to create a new user.
              When only 'password' is provided, it is set as the password for the default user
              of the image. For Windows instances, 'username' cannot be specified. Use the
              'password' field to set the password for the 'Admin' user on Windows. Use the
              '`user_data`' field to provide a script to create new users on Windows. The
              password of the Admin user cannot be updated via '`user_data`'.

          ssh_key_name: Specifies the name of the SSH keypair, created via the
              [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          user_data: String in base64 format. For Linux instances, '`user_data`' is ignored when
              'password' field is provided. For Windows instances, Admin user password is set
              by 'password' field and cannot be updated via '`user_data`'. Examples of the
              `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          username: For Linux instances, 'username' and 'password' are used to create a new user.
              For Windows instances, 'username' cannot be specified. Use 'password' field to
              set the password for the 'Admin' user on Windows.

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
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "flavor": flavor,
                    "interfaces": interfaces,
                    "app_config": app_config,
                    "apptemplate_id": apptemplate_id,
                    "ddos_profile": ddos_profile,
                    "image_id": image_id,
                    "name": name,
                    "name_template": name_template,
                    "password": password,
                    "ssh_key_name": ssh_key_name,
                    "tags": tags,
                    "user_data": user_data,
                    "username": username,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        changes_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        changes_since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flavor_id: str | NotGiven = NOT_GIVEN,
        flavor_prefix: str | NotGiven = NOT_GIVEN,
        include_k8s: bool | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        only_isolated: bool | NotGiven = NOT_GIVEN,
        only_with_fixed_external_ip: bool | NotGiven = NOT_GIVEN,
        order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc", "status.asc", "status.desc"]
        | NotGiven = NOT_GIVEN,
        profile_name: str | NotGiven = NOT_GIVEN,
        protection_status: Literal["Active", "Queued", "Error"] | NotGiven = NOT_GIVEN,
        status: Literal[
            "ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "REBOOT", "REBUILD", "RESCUE", "SHUTOFF", "SUSPENDED"
        ]
        | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        tag_value: List[str] | NotGiven = NOT_GIVEN,
        type_ddos_profile: Literal["basic", "advanced"] | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        with_ddos: bool | NotGiven = NOT_GIVEN,
        with_interfaces_name: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BaremetalServer, AsyncOffsetPage[BaremetalServer]]:
        """List all bare metal servers in the specified project and region.

        Results can be
        filtered by various parameters like name, status, and IP address.

        Args:
          project_id: Project ID

          region_id: Region ID

          changes_before: Filters the instances by a date and time stamp when the instances last changed.

          changes_since: Filters the instances by a date and time stamp when the instances last changed
              status.

          flavor_id: Filter out instances by `flavor_id`. Flavor id must match exactly.

          flavor_prefix: Filter out instances by `flavor_prefix`.

          include_k8s: Include managed k8s worker nodes

          ip: An IPv4 address to filter results by. Note: partial matches are allowed. For
              example, searching for 192.168.0.1 will return 192.168.0.1, 192.168.0.10,
              192.168.0.110, and so on.

          limit: Optional. Limit the number of returned items

          name: Filter instances by name. You can provide a full or partial name, instances with
              matching names will be returned. For example, entering 'test' will return all
              instances that contain 'test' in their name.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          only_isolated: Include only isolated instances

          only_with_fixed_external_ip: Return bare metals only with external fixed IP addresses.

          order_by: Order by field and direction.

          profile_name: Filter result by ddos protection profile name. Effective only with `with_ddos`
              set to true.

          protection_status: Filter result by DDoS `protection_status`. Effective only with `with_ddos` set
              to true. (Active, Queued or Error)

          status: Filters instances by a server status, as a string.

          tag_key_value: Optional. Filter by tag key-value pairs.

          tag_value: Optional. Filter by tag values. ?`tag_value`=value1&`tag_value`=value2

          type_ddos_profile: Return bare metals either only with advanced or only basic DDoS protection.
              Effective only with `with_ddos` set to true. (advanced or basic)

          uuid: Filter the server list result by the UUID of the server. Allowed UUID part

          with_ddos: Include DDoS profile information for bare-metal servers in the response when set
              to `true`. Otherwise, the `ddos_profile` field in the response is `null` by
              default.

          with_interfaces_name: Include `interface_name` in the addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/bminstances/{project_id}/{region_id}",
            page=AsyncOffsetPage[BaremetalServer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changes_before": changes_before,
                        "changes_since": changes_since,
                        "flavor_id": flavor_id,
                        "flavor_prefix": flavor_prefix,
                        "include_k8s": include_k8s,
                        "ip": ip,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "only_isolated": only_isolated,
                        "only_with_fixed_external_ip": only_with_fixed_external_ip,
                        "order_by": order_by,
                        "profile_name": profile_name,
                        "protection_status": protection_status,
                        "status": status,
                        "tag_key_value": tag_key_value,
                        "tag_value": tag_value,
                        "type_ddos_profile": type_ddos_profile,
                        "uuid": uuid,
                        "with_ddos": with_ddos,
                        "with_interfaces_name": with_interfaces_name,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=BaremetalServer,
        )

    async def rebuild(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Rebuild a bare metal server with a new image while preserving its configuration.

        Args:
          image_id: Image ID

          user_data: String in base64 format. Must not be passed together with 'username' or
              'password'. Examples of the `user_data`:
              https://cloudinit.readthedocs.io/en/latest/topics/examples.html

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._post(
            f"/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild",
            body=await async_maybe_transform(
                {
                    "image_id": image_id,
                    "user_data": user_data,
                },
                server_rebuild_params.ServerRebuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[object] | NotGiven = NOT_GIVEN,
        apptemplate_id: str | NotGiven = NOT_GIVEN,
        ddos_profile: server_create_params.DDOSProfile | NotGiven = NOT_GIVEN,
        image_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        name_template: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        ssh_key_name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Create a bare metal server and wait for it to be ready.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            app_config=app_config,
            apptemplate_id=apptemplate_id,
            ddos_profile=ddos_profile,
            image_id=image_id,
            name=name,
            name_template=name_template,
            password=password,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.instances:
            raise ValueError("No server was created")
        server_id = task.created_resources.instances[0]
        servers = await self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return servers.results[0]

    async def rebuild_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Rebuild a bare metal server and wait for it to be ready. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.rebuild(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        servers = await self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return servers.results[0]


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_raw_response_wrapper(
            servers.create,
        )
        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.rebuild = to_raw_response_wrapper(
            servers.rebuild,
        )


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_raw_response_wrapper(
            servers.create,
        )
        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.rebuild = async_to_raw_response_wrapper(
            servers.rebuild,
        )


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_streamed_response_wrapper(
            servers.create,
        )
        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.rebuild = to_streamed_response_wrapper(
            servers.rebuild,
        )


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_streamed_response_wrapper(
            servers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.rebuild = async_to_streamed_response_wrapper(
            servers.rebuild,
        )
