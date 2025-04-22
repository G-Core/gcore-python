# Cloud

Types:

```python
from gcore.types.cloud import (
    DDOSProfile,
    DDOSProfileField,
    DDOSProfileOptionList,
    DDOSProfileStatus,
    DDOSProfileTemplate,
    DDOSProfileTemplateField,
    FlavorHardwareDescription,
    FloatingIP,
    FloatingIPStatus,
    InstanceMetricsTimeUnit,
    InterfaceIPFamily,
    IPVersion,
    LoadBalancer,
    LoadBalancerInstanceRole,
    LoadBalancerMemberConnectivity,
    LoadBalancerOperatingStatus,
    LoadBalancerStatistics,
    Network,
    NetworkAnySubnetFip,
    NetworkSubnetFip,
    NeutronRoute,
    ProvisioningStatus,
    Subnet,
    Tag,
    TagList,
    TagUpdateList,
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
from gcore.types.cloud.quotas import RequestGetResponse
```

Methods:

- <code title="post /cloud/v2/limits_request">client.cloud.quotas.requests.<a href="./src/gcore/resources/cloud/quotas/requests.py">create</a>(\*\*<a href="src/gcore/types/cloud/quotas/request_create_params.py">params</a>) -> None</code>
- <code title="get /cloud/v2/limits_request">client.cloud.quotas.requests.<a href="./src/gcore/resources/cloud/quotas/requests.py">list</a>(\*\*<a href="src/gcore/types/cloud/quotas/request_list_params.py">params</a>) -> None</code>
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
