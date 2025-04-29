# Cloud

Types:

```python
from gcore.types.cloud import (
    Console,
    DDOSProfile,
    DDOSProfileField,
    DDOSProfileOptionList,
    DDOSProfileStatus,
    DDOSProfileTemplate,
    DDOSProfileTemplateField,
    FlavorHardwareDescription,
    FloatingIP,
    FloatingIPStatus,
    Image,
    ImageList,
    InstanceMetricsTimeUnit,
    InterfaceIPFamily,
    IPVersion,
    LoadBalancer,
    LoadBalancerInstanceRole,
    LoadBalancerMemberConnectivity,
    LoadBalancerOperatingStatus,
    LoadBalancerStatistics,
    Network,
    ProvisioningStatus,
    Subnet,
    Tag,
    TagList,
    TaskIDList,
)
```

## Projects

Types:

```python
from gcore.types.cloud import Project
```

Methods:

- <code title="post /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">create</a>(\*\*<a href="src/gcore/types/cloud/project_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="get /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">list</a>(\*\*<a href="src/gcore/types/cloud/project_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">SyncOffsetPage[Project]</a></code>
- <code title="delete /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">delete</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">get</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="put /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">replace</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/project_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>

## Tasks

Types:

```python
from gcore.types.cloud import Task
```

Methods:

- <code title="get /cloud/v1/tasks">client.cloud.tasks.<a href="./src/gcore/resources/cloud/tasks.py">list</a>(\*\*<a href="src/gcore/types/cloud/task_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task.py">SyncOffsetPage[Task]</a></code>
- <code title="post /cloud/v1/tasks/acknowledge_all">client.cloud.tasks.<a href="./src/gcore/resources/cloud/tasks.py">acknowledge_all</a>(\*\*<a href="src/gcore/types/cloud/task_acknowledge_all_params.py">params</a>) -> None</code>
- <code title="post /cloud/v1/tasks/{task_id}/acknowledge">client.cloud.tasks.<a href="./src/gcore/resources/cloud/tasks.py">acknowledge_one</a>(task_id) -> <a href="./src/gcore/types/cloud/task.py">Task</a></code>
- <code title="get /cloud/v1/tasks/{task_id}">client.cloud.tasks.<a href="./src/gcore/resources/cloud/tasks.py">get</a>(task_id) -> <a href="./src/gcore/types/cloud/task.py">Task</a></code>

## Regions

Types:

```python
from gcore.types.cloud import Region
```

Methods:

- <code title="get /cloud/v1/regions/{region_id}">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">retrieve</a>(\*, region_id, \*\*<a href="src/gcore/types/cloud/region_retrieve_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">Region</a></code>
- <code title="get /cloud/v1/regions">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">list</a>(\*\*<a href="src/gcore/types/cloud/region_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">SyncOffsetPage[Region]</a></code>

## Quotas

Types:

```python
from gcore.types.cloud import QuotaGetAllResponse, QuotaGetByRegionResponse, QuotaGetGlobalResponse
```

Methods:

- <code title="get /cloud/v2/client_quotas">client.cloud.quotas.<a href="./src/gcore/resources/cloud/quotas/quotas.py">get_all</a>() -> <a href="./src/gcore/types/cloud/quota_get_all_response.py">QuotaGetAllResponse</a></code>
- <code title="get /cloud/v2/regional_quotas/{client_id}/{region_id}">client.cloud.quotas.<a href="./src/gcore/resources/cloud/quotas/quotas.py">get_by_region</a>(\*, client_id, region_id) -> <a href="./src/gcore/types/cloud/quota_get_by_region_response.py">QuotaGetByRegionResponse</a></code>
- <code title="get /cloud/v2/global_quotas/{client_id}">client.cloud.quotas.<a href="./src/gcore/resources/cloud/quotas/quotas.py">get_global</a>(client_id) -> <a href="./src/gcore/types/cloud/quota_get_global_response.py">QuotaGetGlobalResponse</a></code>

### Requests

Types:

```python
from gcore.types.cloud.quotas import RequestListResponse, RequestGetResponse
```

Methods:

- <code title="post /cloud/v2/limits_request">client.cloud.quotas.requests.<a href="./src/gcore/resources/cloud/quotas/requests.py">create</a>(\*\*<a href="src/gcore/types/cloud/quotas/request_create_params.py">params</a>) -> None</code>
- <code title="get /cloud/v2/limits_request">client.cloud.quotas.requests.<a href="./src/gcore/resources/cloud/quotas/requests.py">list</a>(\*\*<a href="src/gcore/types/cloud/quotas/request_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/quotas/request_list_response.py">SyncOffsetPage[RequestListResponse]</a></code>
- <code title="delete /cloud/v2/limits_request/{request_id}">client.cloud.quotas.requests.<a href="./src/gcore/resources/cloud/quotas/requests.py">delete</a>(request_id) -> None</code>
- <code title="get /cloud/v2/limits_request/{request_id}">client.cloud.quotas.requests.<a href="./src/gcore/resources/cloud/quotas/requests.py">get</a>(request_id) -> <a href="./src/gcore/types/cloud/quotas/request_get_response.py">RequestGetResponse</a></code>

## Secrets

Types:

```python
from gcore.types.cloud import Secret, SecretListResponse
```

Methods:

- <code title="post /cloud/v1/secrets/{project_id}/{region_id}">client.cloud.secrets.<a href="./src/gcore/resources/cloud/secrets.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/secret_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/secrets/{project_id}/{region_id}">client.cloud.secrets.<a href="./src/gcore/resources/cloud/secrets.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /cloud/v1/secrets/{project_id}/{region_id}/{secret_id}">client.cloud.secrets.<a href="./src/gcore/resources/cloud/secrets.py">delete</a>(secret_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/secrets/{project_id}/{region_id}/{secret_id}">client.cloud.secrets.<a href="./src/gcore/resources/cloud/secrets.py">get</a>(secret_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/secret.py">Secret</a></code>
- <code title="post /cloud/v2/secrets/{project_id}/{region_id}">client.cloud.secrets.<a href="./src/gcore/resources/cloud/secrets.py">upload_tls_certificate</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/secret_upload_tls_certificate_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

## SSHKeys

Types:

```python
from gcore.types.cloud import SSHKey, SSHKeyCreated
```

Methods:

- <code title="post /cloud/v1/ssh_keys/{project_id}">client.cloud.ssh_keys.<a href="./src/gcore/resources/cloud/ssh_keys.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/ssh_key_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/ssh_key_created.py">SSHKeyCreated</a></code>
- <code title="patch /cloud/v1/ssh_keys/{project_id}/{ssh_key_id}">client.cloud.ssh_keys.<a href="./src/gcore/resources/cloud/ssh_keys.py">update</a>(ssh_key_id, \*, project_id, \*\*<a href="src/gcore/types/cloud/ssh_key_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/ssh_key.py">SSHKey</a></code>
- <code title="get /cloud/v1/ssh_keys/{project_id}">client.cloud.ssh_keys.<a href="./src/gcore/resources/cloud/ssh_keys.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/ssh_key_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/ssh_key.py">SyncOffsetPage[SSHKey]</a></code>
- <code title="delete /cloud/v1/ssh_keys/{project_id}/{ssh_key_id}">client.cloud.ssh_keys.<a href="./src/gcore/resources/cloud/ssh_keys.py">delete</a>(ssh_key_id, \*, project_id) -> None</code>
- <code title="get /cloud/v1/ssh_keys/{project_id}/{ssh_key_id}">client.cloud.ssh_keys.<a href="./src/gcore/resources/cloud/ssh_keys.py">get</a>(ssh_key_id, \*, project_id) -> <a href="./src/gcore/types/cloud/ssh_key.py">SSHKey</a></code>

## IPRanges

Types:

```python
from gcore.types.cloud import IPRanges
```

Methods:

- <code title="get /cloud/public/v1/ipranges/egress">client.cloud.ip_ranges.<a href="./src/gcore/resources/cloud/ip_ranges.py">list</a>() -> <a href="./src/gcore/types/cloud/ip_ranges.py">IPRanges</a></code>

## ReservedFixedIPs

Types:

```python
from gcore.types.cloud import ReservedFixedIP
```

Methods:

- <code title="post /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ip_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ip_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">SyncOffsetPage[ReservedFixedIP]</a></code>
- <code title="delete /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">delete</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">get</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">ReservedFixedIP</a></code>

### Vip

Types:

```python
from gcore.types.cloud.reserved_fixed_ips import (
    CandidatePort,
    CandidatePortList,
    ConnectedPort,
    ConnectedPortList,
    IPAssignment,
)
```

Methods:

- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/available_devices">client.cloud.reserved_fixed_ips.vip.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip.py">list_candidate_ports</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/candidate_port_list.py">CandidatePortList</a></code>
- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices">client.cloud.reserved_fixed_ips.vip.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip.py">list_connected_ports</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/connected_port_list.py">ConnectedPortList</a></code>
- <code title="put /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices">client.cloud.reserved_fixed_ips.vip.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip.py">replace_connected_ports</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ips/vip_replace_connected_ports_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/connected_port_list.py">ConnectedPortList</a></code>
- <code title="patch /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.vip.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip.py">toggle</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ips/vip_toggle_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">ReservedFixedIP</a></code>
- <code title="patch /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices">client.cloud.reserved_fixed_ips.vip.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip.py">update_connected_ports</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ips/vip_update_connected_ports_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/connected_port_list.py">ConnectedPortList</a></code>

## Networks

Methods:

- <code title="post /cloud/v1/networks/{project_id}/{region_id}">client.cloud.networks.<a href="./src/gcore/resources/cloud/networks/networks.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/network_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/networks/{project_id}/{region_id}/{network_id}">client.cloud.networks.<a href="./src/gcore/resources/cloud/networks/networks.py">update</a>(network_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/network_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/network.py">Network</a></code>
- <code title="get /cloud/v1/networks/{project_id}/{region_id}">client.cloud.networks.<a href="./src/gcore/resources/cloud/networks/networks.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/network_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/network.py">SyncOffsetPage[Network]</a></code>
- <code title="delete /cloud/v1/networks/{project_id}/{region_id}/{network_id}">client.cloud.networks.<a href="./src/gcore/resources/cloud/networks/networks.py">delete</a>(network_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/networks/{project_id}/{region_id}/{network_id}">client.cloud.networks.<a href="./src/gcore/resources/cloud/networks/networks.py">get</a>(network_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/network.py">Network</a></code>

### Subnets

Methods:

- <code title="post /cloud/v1/subnets/{project_id}/{region_id}">client.cloud.networks.subnets.<a href="./src/gcore/resources/cloud/networks/subnets.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/subnet_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}">client.cloud.networks.subnets.<a href="./src/gcore/resources/cloud/networks/subnets.py">update</a>(subnet_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/subnet_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/subnet.py">Subnet</a></code>
- <code title="get /cloud/v1/subnets/{project_id}/{region_id}">client.cloud.networks.subnets.<a href="./src/gcore/resources/cloud/networks/subnets.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/subnet_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/subnet.py">SyncOffsetPage[Subnet]</a></code>
- <code title="delete /cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}">client.cloud.networks.subnets.<a href="./src/gcore/resources/cloud/networks/subnets.py">delete</a>(subnet_id, \*, project_id, region_id) -> None</code>
- <code title="get /cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}">client.cloud.networks.subnets.<a href="./src/gcore/resources/cloud/networks/subnets.py">get</a>(subnet_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/subnet.py">Subnet</a></code>

### Routers

Types:

```python
from gcore.types.cloud.networks import Router, RouterList, SubnetID
```

Methods:

- <code title="post /cloud/v1/routers/{project_id}/{region_id}">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/router_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/routers/{project_id}/{region_id}/{router_id}">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">update</a>(router_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/router_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/networks/router.py">Router</a></code>
- <code title="get /cloud/v1/routers/{project_id}/{region_id}">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/router_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/networks/router.py">SyncOffsetPage[Router]</a></code>
- <code title="delete /cloud/v1/routers/{project_id}/{region_id}/{router_id}">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">delete</a>(router_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/routers/{project_id}/{region_id}/{router_id}/attach">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">attach_subnet</a>(router_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/router_attach_subnet_params.py">params</a>) -> <a href="./src/gcore/types/cloud/networks/router.py">Router</a></code>
- <code title="post /cloud/v1/routers/{project_id}/{region_id}/{router_id}/detach">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">detach_subnet</a>(router_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/networks/router_detach_subnet_params.py">params</a>) -> <a href="./src/gcore/types/cloud/networks/router.py">Router</a></code>
- <code title="get /cloud/v1/routers/{project_id}/{region_id}/{router_id}">client.cloud.networks.routers.<a href="./src/gcore/resources/cloud/networks/routers.py">get</a>(router_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/networks/router.py">Router</a></code>

## Volumes

Types:

```python
from gcore.types.cloud import Volume
```

Methods:

- <code title="post /cloud/v1/volumes/{project_id}/{region_id}">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/volumes/{project_id}/{region_id}/{volume_id}">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">update</a>(volume_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/volume.py">Volume</a></code>
- <code title="get /cloud/v1/volumes/{project_id}/{region_id}">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/volume.py">SyncOffsetPage[Volume]</a></code>
- <code title="delete /cloud/v1/volumes/{project_id}/{region_id}/{volume_id}">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">delete</a>(volume_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">attach_to_instance</a>(volume_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_attach_to_instance_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">change_type</a>(volume_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_change_type_params.py">params</a>) -> <a href="./src/gcore/types/cloud/volume.py">Volume</a></code>
- <code title="post /cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">detach_from_instance</a>(volume_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_detach_from_instance_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/volumes/{project_id}/{region_id}/{volume_id}">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">get</a>(volume_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/volume.py">Volume</a></code>
- <code title="post /cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">resize</a>(volume_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert">client.cloud.volumes.<a href="./src/gcore/resources/cloud/volumes.py">revert_to_last_snapshot</a>(volume_id, \*, project_id, region_id) -> None</code>

## FloatingIPs

Types:

```python
from gcore.types.cloud import FloatingIPDetailed
```

Methods:

- <code title="post /cloud/v1/floatingips/{project_id}/{region_id}">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/floating_ip_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/floatingips/{project_id}/{region_id}">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/floating_ip_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/floating_ip_detailed.py">SyncOffsetPage[FloatingIPDetailed]</a></code>
- <code title="delete /cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">delete</a>(floating_ip_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/assign">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">assign</a>(floating_ip_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/floating_ip_assign_params.py">params</a>) -> <a href="./src/gcore/types/cloud/floating_ip.py">FloatingIP</a></code>
- <code title="get /cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">get</a>(floating_ip_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/floating_ip.py">FloatingIP</a></code>
- <code title="post /cloud/v1/floatingips/{project_id}/{region_id}/{floating_ip_id}/unassign">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">unassign</a>(floating_ip_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/floating_ip.py">FloatingIP</a></code>

## SecurityGroups

Types:

```python
from gcore.types.cloud import SecurityGroup, SecurityGroupRule
```

Methods:

- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>
- <code title="patch /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">update</a>(group_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>
- <code title="get /cloud/v1/securitygroups/{project_id}/{region_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group.py">SyncOffsetPage[SecurityGroup]</a></code>
- <code title="delete /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">delete</a>(group_id, \*, project_id, region_id) -> None</code>
- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/copy">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">copy</a>(group_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_copy_params.py">params</a>) -> None</code>
- <code title="get /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">get</a>(group_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>
- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/revert">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">revert_to_default</a>(group_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>

### Rules

Methods:

- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/rules">client.cloud.security_groups.rules.<a href="./src/gcore/resources/cloud/security_groups/rules.py">create</a>(group_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_groups/rule_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group_rule.py">SecurityGroupRule</a></code>
- <code title="delete /cloud/v1/securitygrouprules/{project_id}/{region_id}/{rule_id}">client.cloud.security_groups.rules.<a href="./src/gcore/resources/cloud/security_groups/rules.py">delete</a>(rule_id, \*, project_id, region_id) -> None</code>
- <code title="put /cloud/v1/securitygrouprules/{project_id}/{region_id}/{rule_id}">client.cloud.security_groups.rules.<a href="./src/gcore/resources/cloud/security_groups/rules.py">replace</a>(rule_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_groups/rule_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group_rule.py">SecurityGroupRule</a></code>

## PlacementGroups

Types:

```python
from gcore.types.cloud import PlacementGroup, PlacementGroupList
```

Methods:

- <code title="post /cloud/v1/servergroups/{project_id}/{region_id}">client.cloud.placement_groups.<a href="./src/gcore/resources/cloud/placement_groups.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/placement_group_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/placement_group.py">PlacementGroup</a></code>
- <code title="get /cloud/v1/servergroups/{project_id}/{region_id}">client.cloud.placement_groups.<a href="./src/gcore/resources/cloud/placement_groups.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/placement_group_list.py">PlacementGroupList</a></code>
- <code title="delete /cloud/v1/servergroups/{project_id}/{region_id}/{group_id}">client.cloud.placement_groups.<a href="./src/gcore/resources/cloud/placement_groups.py">delete</a>(group_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/servergroups/{project_id}/{region_id}/{group_id}">client.cloud.placement_groups.<a href="./src/gcore/resources/cloud/placement_groups.py">get</a>(group_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/placement_group.py">PlacementGroup</a></code>

## Baremetal

### Images

Methods:

- <code title="get /cloud/v1/bmimages/{project_id}/{region_id}">client.cloud.baremetal.images.<a href="./src/gcore/resources/cloud/baremetal/images.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/baremetal/image_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image_list.py">ImageList</a></code>

## Instances

### Images

Methods:

- <code title="patch /cloud/v1/images/{project_id}/{region_id}/{image_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">update</a>(image_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image.py">Image</a></code>
- <code title="get /cloud/v1/images/{project_id}/{region_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image_list.py">ImageList</a></code>
- <code title="delete /cloud/v1/images/{project_id}/{region_id}/{image_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">delete</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/images/{project_id}/{region_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">create_from_volume</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_create_from_volume_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/images/{project_id}/{region_id}/{image_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">get</a>(image_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image.py">Image</a></code>
- <code title="post /cloud/v1/downloadimage/{project_id}/{region_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">upload</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_upload_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

## FileShares

Types:

```python
from gcore.types.cloud import FileShare
```

Methods:

- <code title="post /cloud/v1/file_shares/{project_id}/{region_id}">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/file_share_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">update</a>(file_share_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/file_share_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/file_share.py">FileShare</a></code>
- <code title="get /cloud/v1/file_shares/{project_id}/{region_id}">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/file_share_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/file_share.py">SyncOffsetPage[FileShare]</a></code>
- <code title="delete /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">delete</a>(file_share_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">get</a>(file_share_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/file_share.py">FileShare</a></code>
- <code title="post /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/extend">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">resize</a>(file_share_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/file_share_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### AccessRules

Types:

```python
from gcore.types.cloud.file_shares import AccessRule, AccessRuleList
```

Methods:

- <code title="post /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule">client.cloud.file_shares.access_rules.<a href="./src/gcore/resources/cloud/file_shares/access_rules.py">create</a>(file_share_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/file_shares/access_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/file_shares/access_rule.py">AccessRule</a></code>
- <code title="get /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule">client.cloud.file_shares.access_rules.<a href="./src/gcore/resources/cloud/file_shares/access_rules.py">list</a>(file_share_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/file_shares/access_rule_list.py">AccessRuleList</a></code>
- <code title="delete /cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule/{access_rule_id}">client.cloud.file_shares.access_rules.<a href="./src/gcore/resources/cloud/file_shares/access_rules.py">delete</a>(access_rule_id, \*, project_id, region_id, file_share_id) -> None</code>

## BillingReservations

Types:

```python
from gcore.types.cloud import BillingReservation
```

Methods:

- <code title="get /cloud/v1/reservations">client.cloud.billing_reservations.<a href="./src/gcore/resources/cloud/billing_reservations.py">list</a>(\*\*<a href="src/gcore/types/cloud/billing_reservation_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/billing_reservation.py">SyncOffsetPage[BillingReservation]</a></code>
- <code title="get /cloud/v1/reservations/{reservation_id}">client.cloud.billing_reservations.<a href="./src/gcore/resources/cloud/billing_reservations.py">get</a>(reservation_id) -> <a href="./src/gcore/types/cloud/billing_reservation.py">BillingReservation</a></code>
