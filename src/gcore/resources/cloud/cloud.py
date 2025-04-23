# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from .volumes import (
    VolumesResource,
    AsyncVolumesResource,
    VolumesResourceWithRawResponse,
    AsyncVolumesResourceWithRawResponse,
    VolumesResourceWithStreamingResponse,
    AsyncVolumesResourceWithStreamingResponse,
)
from .projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from .ssh_keys import (
    SSHKeysResource,
    AsyncSSHKeysResource,
    SSHKeysResourceWithRawResponse,
    AsyncSSHKeysResourceWithRawResponse,
    SSHKeysResourceWithStreamingResponse,
    AsyncSSHKeysResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .ip_ranges import (
    IPRangesResource,
    AsyncIPRangesResource,
    IPRangesResourceWithRawResponse,
    AsyncIPRangesResourceWithRawResponse,
    IPRangesResourceWithStreamingResponse,
    AsyncIPRangesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .floating_ips import (
    FloatingIPsResource,
    AsyncFloatingIPsResource,
    FloatingIPsResourceWithRawResponse,
    AsyncFloatingIPsResourceWithRawResponse,
    FloatingIPsResourceWithStreamingResponse,
    AsyncFloatingIPsResourceWithStreamingResponse,
)
from .quotas.quotas import (
    QuotasResource,
    AsyncQuotasResource,
    QuotasResourceWithRawResponse,
    AsyncQuotasResourceWithRawResponse,
    QuotasResourceWithStreamingResponse,
    AsyncQuotasResourceWithStreamingResponse,
)
from .networks.networks import (
    NetworksResource,
    AsyncNetworksResource,
    NetworksResourceWithRawResponse,
    AsyncNetworksResourceWithRawResponse,
    NetworksResourceWithStreamingResponse,
    AsyncNetworksResourceWithStreamingResponse,
)
from .security_groups.security_groups import (
    SecurityGroupsResource,
    AsyncSecurityGroupsResource,
    SecurityGroupsResourceWithRawResponse,
    AsyncSecurityGroupsResourceWithRawResponse,
    SecurityGroupsResourceWithStreamingResponse,
    AsyncSecurityGroupsResourceWithStreamingResponse,
)
from .reserved_fixed_ips.reserved_fixed_ips import (
    ReservedFixedIPsResource,
    AsyncReservedFixedIPsResource,
    ReservedFixedIPsResourceWithRawResponse,
    AsyncReservedFixedIPsResourceWithRawResponse,
    ReservedFixedIPsResourceWithStreamingResponse,
    AsyncReservedFixedIPsResourceWithStreamingResponse,
)

__all__ = ["CloudResource", "AsyncCloudResource"]


class CloudResource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def quotas(self) -> QuotasResource:
        return QuotasResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def ssh_keys(self) -> SSHKeysResource:
        return SSHKeysResource(self._client)

    @cached_property
    def ip_ranges(self) -> IPRangesResource:
        return IPRangesResource(self._client)

    @cached_property
    def reserved_fixed_ips(self) -> ReservedFixedIPsResource:
        return ReservedFixedIPsResource(self._client)

    @cached_property
    def networks(self) -> NetworksResource:
        return NetworksResource(self._client)

    @cached_property
    def volumes(self) -> VolumesResource:
        return VolumesResource(self._client)

    @cached_property
    def floating_ips(self) -> FloatingIPsResource:
        return FloatingIPsResource(self._client)

    @cached_property
    def security_groups(self) -> SecurityGroupsResource:
        return SecurityGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CloudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return CloudResourceWithStreamingResponse(self)


class AsyncCloudResource(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def quotas(self) -> AsyncQuotasResource:
        return AsyncQuotasResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def ssh_keys(self) -> AsyncSSHKeysResource:
        return AsyncSSHKeysResource(self._client)

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResource:
        return AsyncIPRangesResource(self._client)

    @cached_property
    def reserved_fixed_ips(self) -> AsyncReservedFixedIPsResource:
        return AsyncReservedFixedIPsResource(self._client)

    @cached_property
    def networks(self) -> AsyncNetworksResource:
        return AsyncNetworksResource(self._client)

    @cached_property
    def volumes(self) -> AsyncVolumesResource:
        return AsyncVolumesResource(self._client)

    @cached_property
    def floating_ips(self) -> AsyncFloatingIPsResource:
        return AsyncFloatingIPsResource(self._client)

    @cached_property
    def security_groups(self) -> AsyncSecurityGroupsResource:
        return AsyncSecurityGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncCloudResourceWithStreamingResponse(self)


class CloudResourceWithRawResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> QuotasResourceWithRawResponse:
        return QuotasResourceWithRawResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._cloud.secrets)

    @cached_property
    def ssh_keys(self) -> SSHKeysResourceWithRawResponse:
        return SSHKeysResourceWithRawResponse(self._cloud.ssh_keys)

    @cached_property
    def ip_ranges(self) -> IPRangesResourceWithRawResponse:
        return IPRangesResourceWithRawResponse(self._cloud.ip_ranges)

    @cached_property
    def reserved_fixed_ips(self) -> ReservedFixedIPsResourceWithRawResponse:
        return ReservedFixedIPsResourceWithRawResponse(self._cloud.reserved_fixed_ips)

    @cached_property
    def networks(self) -> NetworksResourceWithRawResponse:
        return NetworksResourceWithRawResponse(self._cloud.networks)

    @cached_property
    def volumes(self) -> VolumesResourceWithRawResponse:
        return VolumesResourceWithRawResponse(self._cloud.volumes)

    @cached_property
    def floating_ips(self) -> FloatingIPsResourceWithRawResponse:
        return FloatingIPsResourceWithRawResponse(self._cloud.floating_ips)

    @cached_property
    def security_groups(self) -> SecurityGroupsResourceWithRawResponse:
        return SecurityGroupsResourceWithRawResponse(self._cloud.security_groups)


class AsyncCloudResourceWithRawResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> AsyncQuotasResourceWithRawResponse:
        return AsyncQuotasResourceWithRawResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._cloud.secrets)

    @cached_property
    def ssh_keys(self) -> AsyncSSHKeysResourceWithRawResponse:
        return AsyncSSHKeysResourceWithRawResponse(self._cloud.ssh_keys)

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResourceWithRawResponse:
        return AsyncIPRangesResourceWithRawResponse(self._cloud.ip_ranges)

    @cached_property
    def reserved_fixed_ips(self) -> AsyncReservedFixedIPsResourceWithRawResponse:
        return AsyncReservedFixedIPsResourceWithRawResponse(self._cloud.reserved_fixed_ips)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithRawResponse:
        return AsyncNetworksResourceWithRawResponse(self._cloud.networks)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithRawResponse:
        return AsyncVolumesResourceWithRawResponse(self._cloud.volumes)

    @cached_property
    def floating_ips(self) -> AsyncFloatingIPsResourceWithRawResponse:
        return AsyncFloatingIPsResourceWithRawResponse(self._cloud.floating_ips)

    @cached_property
    def security_groups(self) -> AsyncSecurityGroupsResourceWithRawResponse:
        return AsyncSecurityGroupsResourceWithRawResponse(self._cloud.security_groups)


class CloudResourceWithStreamingResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> QuotasResourceWithStreamingResponse:
        return QuotasResourceWithStreamingResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._cloud.secrets)

    @cached_property
    def ssh_keys(self) -> SSHKeysResourceWithStreamingResponse:
        return SSHKeysResourceWithStreamingResponse(self._cloud.ssh_keys)

    @cached_property
    def ip_ranges(self) -> IPRangesResourceWithStreamingResponse:
        return IPRangesResourceWithStreamingResponse(self._cloud.ip_ranges)

    @cached_property
    def reserved_fixed_ips(self) -> ReservedFixedIPsResourceWithStreamingResponse:
        return ReservedFixedIPsResourceWithStreamingResponse(self._cloud.reserved_fixed_ips)

    @cached_property
    def networks(self) -> NetworksResourceWithStreamingResponse:
        return NetworksResourceWithStreamingResponse(self._cloud.networks)

    @cached_property
    def volumes(self) -> VolumesResourceWithStreamingResponse:
        return VolumesResourceWithStreamingResponse(self._cloud.volumes)

    @cached_property
    def floating_ips(self) -> FloatingIPsResourceWithStreamingResponse:
        return FloatingIPsResourceWithStreamingResponse(self._cloud.floating_ips)

    @cached_property
    def security_groups(self) -> SecurityGroupsResourceWithStreamingResponse:
        return SecurityGroupsResourceWithStreamingResponse(self._cloud.security_groups)


class AsyncCloudResourceWithStreamingResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._cloud.projects)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._cloud.tasks)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._cloud.regions)

    @cached_property
    def quotas(self) -> AsyncQuotasResourceWithStreamingResponse:
        return AsyncQuotasResourceWithStreamingResponse(self._cloud.quotas)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._cloud.secrets)

    @cached_property
    def ssh_keys(self) -> AsyncSSHKeysResourceWithStreamingResponse:
        return AsyncSSHKeysResourceWithStreamingResponse(self._cloud.ssh_keys)

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResourceWithStreamingResponse:
        return AsyncIPRangesResourceWithStreamingResponse(self._cloud.ip_ranges)

    @cached_property
    def reserved_fixed_ips(self) -> AsyncReservedFixedIPsResourceWithStreamingResponse:
        return AsyncReservedFixedIPsResourceWithStreamingResponse(self._cloud.reserved_fixed_ips)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithStreamingResponse:
        return AsyncNetworksResourceWithStreamingResponse(self._cloud.networks)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithStreamingResponse:
        return AsyncVolumesResourceWithStreamingResponse(self._cloud.volumes)

    @cached_property
    def floating_ips(self) -> AsyncFloatingIPsResourceWithStreamingResponse:
        return AsyncFloatingIPsResourceWithStreamingResponse(self._cloud.floating_ips)

    @cached_property
    def security_groups(self) -> AsyncSecurityGroupsResourceWithStreamingResponse:
        return AsyncSecurityGroupsResourceWithStreamingResponse(self._cloud.security_groups)
