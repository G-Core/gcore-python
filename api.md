# Cloud

Types:

```python
from gcore.types.cloud import (
    AllowedAddressPairs,
    BaremetalFlavor,
    BaremetalFlavorList,
    BlackholePort,
    Console,
    DDOSProfile,
    DDOSProfileField,
    DDOSProfileOptionList,
    DDOSProfileStatus,
    DDOSProfileTemplate,
    DDOSProfileTemplateField,
    FixedAddress,
    FixedAddressShort,
    FlavorHardwareDescription,
    FloatingAddress,
    FloatingIP,
    FloatingIPStatus,
    GPUImage,
    GPUImageList,
    HTTPMethod,
    Image,
    ImageList,
    Instance,
    InstanceIsolation,
    InstanceList,
    InstanceMetricsTimeUnit,
    InterfaceIPFamily,
    IPAssignment,
    IPVersion,
    LaasIndexRetentionPolicy,
    LoadBalancer,
    LoadBalancerInstanceRole,
    LoadBalancerMemberConnectivity,
    LoadBalancerOperatingStatus,
    LoadBalancerStatistics,
    Logging,
    Network,
    NetworkAnySubnetFip,
    NetworkDetails,
    NetworkInterface,
    NetworkInterfaceList,
    NetworkSubnetFip,
    ProvisioningStatus,
    Route,
    Subnet,
    Tag,
    TagList,
    TagUpdateMap,
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

- <code title="get /cloud/v1/regions">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">list</a>(\*\*<a href="src/gcore/types/cloud/region_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">SyncOffsetPage[Region]</a></code>
- <code title="get /cloud/v1/regions/{region_id}">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">get</a>(\*, region_id, \*\*<a href="src/gcore/types/cloud/region_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">Region</a></code>

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
from gcore.types.cloud import Secret
```

Methods:

- <code title="get /cloud/v1/secrets/{project_id}/{region_id}">client.cloud.secrets.<a href="./src/gcore/resources/cloud/secrets.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/secret_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/secret.py">SyncOffsetPage[Secret]</a></code>
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

## LoadBalancers

Types:

```python
from gcore.types.cloud import (
    HealthMonitor,
    HealthMonitorStatus,
    LbAlgorithm,
    LbHealthMonitorType,
    LbListenerProtocol,
    LbPoolProtocol,
    LbSessionPersistenceType,
    ListenerStatus,
    LoadBalancerFlavorDetail,
    LoadBalancerFlavorList,
    LoadBalancerL7Policy,
    LoadBalancerL7PolicyList,
    LoadBalancerL7Rule,
    LoadBalancerL7RuleList,
    LoadBalancerListenerDetail,
    LoadBalancerListenerList,
    LoadBalancerMetrics,
    LoadBalancerMetricsList,
    LoadBalancerPool,
    LoadBalancerPoolList,
    LoadBalancerStatus,
    LoadBalancerStatusList,
    Member,
    MemberStatus,
    PoolStatus,
    SessionPersistence,
)
```

Methods:

- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">update</a>(loadbalancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer.py">LoadBalancer</a></code>
- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer.py">SyncOffsetPage[LoadBalancer]</a></code>
- <code title="delete /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">delete</a>(loadbalancer_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">failover</a>(loadbalancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_failover_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">get</a>(loadbalancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer.py">LoadBalancer</a></code>
- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">resize</a>(loadbalancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### L7Policies

Methods:

- <code title="post /cloud/v1/l7policies/{project_id}/{region_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/l7_policy_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/l7policies/{project_id}/{region_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_l7_policy_list.py">LoadBalancerL7PolicyList</a></code>
- <code title="delete /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">delete</a>(l7policy_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">get</a>(l7policy_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_l7_policy.py">LoadBalancerL7Policy</a></code>
- <code title="put /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">replace</a>(l7policy_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/l7_policy_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

#### Rules

Methods:

- <code title="post /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules">client.cloud.load_balancers.l7_policies.rules.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/rules.py">create</a>(l7policy_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/l7_policies/rule_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules">client.cloud.load_balancers.l7_policies.rules.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/rules.py">list</a>(l7policy_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_l7_rule_list.py">LoadBalancerL7RuleList</a></code>
- <code title="delete /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}">client.cloud.load_balancers.l7_policies.rules.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/rules.py">delete</a>(l7rule_id, \*, project_id, region_id, l7policy_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}">client.cloud.load_balancers.l7_policies.rules.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/rules.py">get</a>(l7rule_id, \*, project_id, region_id, l7policy_id) -> <a href="./src/gcore/types/cloud/load_balancer_l7_rule.py">LoadBalancerL7Rule</a></code>
- <code title="put /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}">client.cloud.load_balancers.l7_policies.rules.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/rules.py">replace</a>(l7rule_id, \*, project_id, region_id, l7policy_id, \*\*<a href="src/gcore/types/cloud/load_balancers/l7_policies/rule_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### Flavors

Methods:

- <code title="get /cloud/v1/lbflavors/{project_id}/{region_id}">client.cloud.load_balancers.flavors.<a href="./src/gcore/resources/cloud/load_balancers/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_flavor_list.py">LoadBalancerFlavorList</a></code>

### Listeners

Methods:

- <code title="post /cloud/v1/lblisteners/{project_id}/{region_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/listener_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">update</a>(listener_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/listener_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lblisteners/{project_id}/{region_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/listener_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_listener_list.py">LoadBalancerListenerList</a></code>
- <code title="delete /cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">delete</a>(listener_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">get</a>(listener_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/listener_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_listener_detail.py">LoadBalancerListenerDetail</a></code>

### Pools

Methods:

- <code title="post /cloud/v1/lbpools/{project_id}/{region_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pool_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">update</a>(pool_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lbpools/{project_id}/{region_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pool_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_pool_list.py">LoadBalancerPoolList</a></code>
- <code title="delete /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">delete</a>(pool_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">get</a>(pool_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_pool.py">LoadBalancerPool</a></code>

#### HealthMonitors

Methods:

- <code title="post /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor">client.cloud.load_balancers.pools.health_monitors.<a href="./src/gcore/resources/cloud/load_balancers/pools/health_monitors.py">create</a>(pool_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pools/health_monitor_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="delete /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor">client.cloud.load_balancers.pools.health_monitors.<a href="./src/gcore/resources/cloud/load_balancers/pools/health_monitors.py">delete</a>(pool_id, \*, project_id, region_id) -> None</code>

#### Members

Methods:

- <code title="post /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member">client.cloud.load_balancers.pools.members.<a href="./src/gcore/resources/cloud/load_balancers/pools/members.py">add</a>(pool_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pools/member_add_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="delete /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}">client.cloud.load_balancers.pools.members.<a href="./src/gcore/resources/cloud/load_balancers/pools/members.py">remove</a>(member_id, \*, project_id, region_id, pool_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### Metrics

Methods:

- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/metrics">client.cloud.load_balancers.metrics.<a href="./src/gcore/resources/cloud/load_balancers/metrics.py">list</a>(loadbalancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/metric_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_metrics_list.py">LoadBalancerMetricsList</a></code>

### Statuses

Methods:

- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}/status">client.cloud.load_balancers.statuses.<a href="./src/gcore/resources/cloud/load_balancers/statuses.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_status_list.py">LoadBalancerStatusList</a></code>
- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/status">client.cloud.load_balancers.statuses.<a href="./src/gcore/resources/cloud/load_balancers/statuses.py">get</a>(loadbalancer_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_status.py">LoadBalancerStatus</a></code>

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
    IPWithSubnet,
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
- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/copy">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">copy</a>(group_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_copy_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>
- <code title="get /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">get</a>(group_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>
- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/revert">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">revert_to_default</a>(group_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/security_group.py">SecurityGroup</a></code>

### Rules

Methods:

- <code title="post /cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/rules">client.cloud.security_groups.rules.<a href="./src/gcore/resources/cloud/security_groups/rules.py">create</a>(group_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_groups/rule_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group_rule.py">SecurityGroupRule</a></code>
- <code title="delete /cloud/v1/securitygrouprules/{project_id}/{region_id}/{rule_id}">client.cloud.security_groups.rules.<a href="./src/gcore/resources/cloud/security_groups/rules.py">delete</a>(rule_id, \*, project_id, region_id) -> None</code>
- <code title="put /cloud/v1/securitygrouprules/{project_id}/{region_id}/{rule_id}">client.cloud.security_groups.rules.<a href="./src/gcore/resources/cloud/security_groups/rules.py">replace</a>(rule_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_groups/rule_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/security_group_rule.py">SecurityGroupRule</a></code>

## Users

### RoleAssignments

Types:

```python
from gcore.types.cloud.users import RoleAssignment, RoleAssignmentUpdateDelete
```

Methods:

- <code title="post /cloud/v1/users/assignments">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">create</a>(\*\*<a href="src/gcore/types/cloud/users/role_assignment_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/users/role_assignment.py">RoleAssignment</a></code>
- <code title="patch /cloud/v1/users/assignments/{assignment_id}">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">update</a>(assignment_id, \*\*<a href="src/gcore/types/cloud/users/role_assignment_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/users/role_assignment_update_delete.py">RoleAssignmentUpdateDelete</a></code>
- <code title="get /cloud/v1/users/assignments">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">list</a>(\*\*<a href="src/gcore/types/cloud/users/role_assignment_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/users/role_assignment.py">SyncOffsetPage[RoleAssignment]</a></code>
- <code title="delete /cloud/v1/users/assignments/{assignment_id}">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">delete</a>(assignment_id) -> <a href="./src/gcore/types/cloud/users/role_assignment_update_delete.py">RoleAssignmentUpdateDelete</a></code>

## Inference

Types:

```python
from gcore.types.cloud import InferenceRegionCapacity, InferenceRegionCapacityList
```

Methods:

- <code title="get /cloud/v3/inference/capacity">client.cloud.inference.<a href="./src/gcore/resources/cloud/inference/inference.py">get_capacity_by_region</a>() -> <a href="./src/gcore/types/cloud/inference_region_capacity_list.py">InferenceRegionCapacityList</a></code>

### Flavors

Types:

```python
from gcore.types.cloud.inference import InferenceFlavor
```

Methods:

- <code title="get /cloud/v3/inference/flavors">client.cloud.inference.flavors.<a href="./src/gcore/resources/cloud/inference/flavors.py">list</a>(\*\*<a href="src/gcore/types/cloud/inference/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_flavor.py">SyncOffsetPage[InferenceFlavor]</a></code>
- <code title="get /cloud/v3/inference/flavors/{flavor_name}">client.cloud.inference.flavors.<a href="./src/gcore/resources/cloud/inference/flavors.py">get</a>(flavor_name) -> <a href="./src/gcore/types/cloud/inference/inference_flavor.py">InferenceFlavor</a></code>

### Models

Types:

```python
from gcore.types.cloud.inference import InferenceModel
```

Methods:

- <code title="get /cloud/v3/inference/models">client.cloud.inference.models.<a href="./src/gcore/resources/cloud/inference/models.py">list</a>(\*\*<a href="src/gcore/types/cloud/inference/model_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_model.py">SyncOffsetPage[InferenceModel]</a></code>
- <code title="get /cloud/v3/inference/models/{model_id}">client.cloud.inference.models.<a href="./src/gcore/resources/cloud/inference/models.py">get</a>(model_id) -> <a href="./src/gcore/types/cloud/inference/inference_model.py">InferenceModel</a></code>

### Deployments

Types:

```python
from gcore.types.cloud.inference import (
    InferenceDeployment,
    InferenceDeploymentAPIKey,
    Probe,
    ProbeConfig,
    ProbeExec,
    ProbeHTTPGet,
    ProbeTcpSocket,
)
```

Methods:

- <code title="post /cloud/v3/inference/{project_id}/deployments">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/deployment_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v3/inference/{project_id}/deployments/{deployment_name}">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">update</a>(deployment_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/deployment_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/inference/{project_id}/deployments">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/deployment_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_deployment.py">SyncOffsetPage[InferenceDeployment]</a></code>
- <code title="delete /cloud/v3/inference/{project_id}/deployments/{deployment_name}">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">delete</a>(deployment_name, \*, project_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/inference/{project_id}/deployments/{deployment_name}">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">get</a>(deployment_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_deployment.py">InferenceDeployment</a></code>
- <code title="get /cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">get_api_key</a>(deployment_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_deployment_api_key.py">InferenceDeploymentAPIKey</a></code>
- <code title="post /cloud/v3/inference/{project_id}/deployments/{deployment_name}/start">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">start</a>(deployment_name, \*, project_id) -> None</code>
- <code title="post /cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop">client.cloud.inference.deployments.<a href="./src/gcore/resources/cloud/inference/deployments/deployments.py">stop</a>(deployment_name, \*, project_id) -> None</code>

#### Logs

Types:

```python
from gcore.types.cloud.inference.deployments import InferenceDeploymentLog
```

Methods:

- <code title="get /cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs">client.cloud.inference.deployments.logs.<a href="./src/gcore/resources/cloud/inference/deployments/logs.py">list</a>(deployment_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/deployments/log_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/deployments/inference_deployment_log.py">SyncOffsetPage[InferenceDeploymentLog]</a></code>

### RegistryCredentials

Types:

```python
from gcore.types.cloud.inference import (
    InferenceRegistryCredentials,
    InferenceRegistryCredentialsCreate,
)
```

Methods:

- <code title="post /cloud/v3/inference/{project_id}/registry_credentials">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials_create.py">InferenceRegistryCredentialsCreate</a></code>
- <code title="get /cloud/v3/inference/{project_id}/registry_credentials">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials.py">SyncOffsetPage[InferenceRegistryCredentials]</a></code>
- <code title="delete /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">delete</a>(credential_name, \*, project_id) -> None</code>
- <code title="get /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">get</a>(credential_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials.py">InferenceRegistryCredentials</a></code>
- <code title="put /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">replace</a>(credential_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_replace_params.py">params</a>) -> None</code>

### Secrets

Types:

```python
from gcore.types.cloud.inference import InferenceSecret
```

Methods:

- <code title="post /cloud/v3/inference/{project_id}/secrets">client.cloud.inference.secrets.<a href="./src/gcore/resources/cloud/inference/secrets.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/secret_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_secret.py">InferenceSecret</a></code>
- <code title="get /cloud/v3/inference/{project_id}/secrets">client.cloud.inference.secrets.<a href="./src/gcore/resources/cloud/inference/secrets.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/secret_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_secret.py">SyncOffsetPage[InferenceSecret]</a></code>
- <code title="delete /cloud/v3/inference/{project_id}/secrets/{secret_name}">client.cloud.inference.secrets.<a href="./src/gcore/resources/cloud/inference/secrets.py">delete</a>(secret_name, \*, project_id) -> None</code>
- <code title="get /cloud/v3/inference/{project_id}/secrets/{secret_name}">client.cloud.inference.secrets.<a href="./src/gcore/resources/cloud/inference/secrets.py">get</a>(secret_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_secret.py">InferenceSecret</a></code>
- <code title="put /cloud/v3/inference/{project_id}/secrets/{secret_name}">client.cloud.inference.secrets.<a href="./src/gcore/resources/cloud/inference/secrets.py">replace</a>(secret_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/secret_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_secret.py">InferenceSecret</a></code>

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

### Flavors

Methods:

- <code title="get /cloud/v1/bmflavors/{project_id}/{region_id}">client.cloud.baremetal.flavors.<a href="./src/gcore/resources/cloud/baremetal/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/baremetal/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/baremetal_flavor_list.py">BaremetalFlavorList</a></code>

### Servers

Types:

```python
from gcore.types.cloud.baremetal import (
    BaremetalFixedAddress,
    BaremetalFloatingAddress,
    BaremetalServer,
)
```

Methods:

- <code title="post /cloud/v1/bminstances/{project_id}/{region_id}">client.cloud.baremetal.servers.<a href="./src/gcore/resources/cloud/baremetal/servers.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/baremetal/server_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/bminstances/{project_id}/{region_id}">client.cloud.baremetal.servers.<a href="./src/gcore/resources/cloud/baremetal/servers.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/baremetal/server_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/baremetal/baremetal_server.py">SyncOffsetPage[BaremetalServer]</a></code>
- <code title="post /cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild">client.cloud.baremetal.servers.<a href="./src/gcore/resources/cloud/baremetal/servers.py">rebuild</a>(server_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/baremetal/server_rebuild_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

## Registries

Types:

```python
from gcore.types.cloud import Registry, RegistryList, RegistryTag
```

Methods:

- <code title="post /cloud/v1/registries/{project_id}/{region_id}">client.cloud.registries.<a href="./src/gcore/resources/cloud/registries/registries.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/registry_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/registry.py">Registry</a></code>
- <code title="get /cloud/v1/registries/{project_id}/{region_id}">client.cloud.registries.<a href="./src/gcore/resources/cloud/registries/registries.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/registry_list.py">RegistryList</a></code>
- <code title="delete /cloud/v1/registries/{project_id}/{region_id}/{registry_id}">client.cloud.registries.<a href="./src/gcore/resources/cloud/registries/registries.py">delete</a>(registry_id, \*, project_id, region_id) -> None</code>
- <code title="get /cloud/v1/registries/{project_id}/{region_id}/{registry_id}">client.cloud.registries.<a href="./src/gcore/resources/cloud/registries/registries.py">get</a>(registry_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/registry.py">Registry</a></code>
- <code title="patch /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/resize">client.cloud.registries.<a href="./src/gcore/resources/cloud/registries/registries.py">resize</a>(registry_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/registry_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/registry.py">Registry</a></code>

### Repositories

Types:

```python
from gcore.types.cloud.registries import RegistryRepository, RegistryRepositoryList
```

Methods:

- <code title="get /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/repositories">client.cloud.registries.repositories.<a href="./src/gcore/resources/cloud/registries/repositories.py">list</a>(registry_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/registries/registry_repository_list.py">RegistryRepositoryList</a></code>
- <code title="delete /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/repositories/{repository_name}">client.cloud.registries.repositories.<a href="./src/gcore/resources/cloud/registries/repositories.py">delete</a>(repository_name, \*, project_id, region_id, registry_id) -> None</code>

### Artifacts

Types:

```python
from gcore.types.cloud.registries import RegistryArtifact, RegistryArtifactList
```

Methods:

- <code title="get /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/repositories/{repository_name}/artifacts">client.cloud.registries.artifacts.<a href="./src/gcore/resources/cloud/registries/artifacts.py">list</a>(repository_name, \*, project_id, region_id, registry_id) -> <a href="./src/gcore/types/cloud/registries/registry_artifact_list.py">RegistryArtifactList</a></code>
- <code title="delete /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/repositories/{repository_name}/artifacts/{digest}">client.cloud.registries.artifacts.<a href="./src/gcore/resources/cloud/registries/artifacts.py">delete</a>(digest, \*, project_id, region_id, registry_id, repository_name) -> None</code>

### Tags

Methods:

- <code title="delete /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/repositories/{repository_name}/artifacts/{digest}/tags/{tag_name}">client.cloud.registries.tags.<a href="./src/gcore/resources/cloud/registries/tags.py">delete</a>(tag_name, \*, project_id, region_id, registry_id, repository_name, digest) -> None</code>

### Users

Types:

```python
from gcore.types.cloud.registries import (
    RegistryUser,
    RegistryUserCreated,
    RegistryUserList,
    UserRefreshSecretResponse,
)
```

Methods:

- <code title="post /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users">client.cloud.registries.users.<a href="./src/gcore/resources/cloud/registries/users.py">create</a>(registry_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/registries/user_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/registries/registry_user_created.py">RegistryUserCreated</a></code>
- <code title="patch /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}">client.cloud.registries.users.<a href="./src/gcore/resources/cloud/registries/users.py">update</a>(user_id, \*, project_id, region_id, registry_id, \*\*<a href="src/gcore/types/cloud/registries/user_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/registries/registry_user.py">RegistryUser</a></code>
- <code title="get /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users">client.cloud.registries.users.<a href="./src/gcore/resources/cloud/registries/users.py">list</a>(registry_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/registries/registry_user_list.py">RegistryUserList</a></code>
- <code title="delete /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}">client.cloud.registries.users.<a href="./src/gcore/resources/cloud/registries/users.py">delete</a>(user_id, \*, project_id, region_id, registry_id) -> None</code>
- <code title="post /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/batch">client.cloud.registries.users.<a href="./src/gcore/resources/cloud/registries/users.py">create_multiple</a>(registry_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/registries/user_create_multiple_params.py">params</a>) -> <a href="./src/gcore/types/cloud/registries/registry_user_created.py">RegistryUserCreated</a></code>
- <code title="post /cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users/{user_id}/refresh_secret">client.cloud.registries.users.<a href="./src/gcore/resources/cloud/registries/users.py">refresh_secret</a>(user_id, \*, project_id, region_id, registry_id) -> <a href="./src/gcore/types/cloud/registries/user_refresh_secret_response.py">UserRefreshSecretResponse</a></code>

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

## GPUBaremetalClusters

Types:

```python
from gcore.types.cloud import (
    GPUBaremetalCluster,
    GPUBaremetalClusterServer,
    GPUBaremetalClusterServerList,
    GPUBaremetalFlavor,
    GPUBaremetalFlavorList,
)
```

Methods:

- <code title="post /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_cluster_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v2/ai/clusters/{project_id}/{region_id}">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_cluster_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_baremetal_cluster.py">SyncOffsetPage[GPUBaremetalCluster]</a></code>
- <code title="delete /cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">delete</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_cluster_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">get</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal_cluster.py">GPUBaremetalCluster</a></code>
- <code title="post /cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">powercycle_all_servers</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal_cluster_server_list.py">GPUBaremetalClusterServerList</a></code>
- <code title="post /cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">reboot_all_servers</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal_cluster_server_list.py">GPUBaremetalClusterServerList</a></code>
- <code title="post /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">rebuild</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_cluster_rebuild_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize">client.cloud.gpu_baremetal_clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/gpu_baremetal_clusters.py">resize</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_cluster_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### Interfaces

Methods:

- <code title="get /cloud/v1/ai/clusters/{project_id}/{region_id}/{cluster_id}/interfaces">client.cloud.gpu_baremetal_clusters.interfaces.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/interfaces.py">list</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/network_interface_list.py">NetworkInterfaceList</a></code>

### Servers

Methods:

- <code title="delete /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}">client.cloud.gpu_baremetal_clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/servers.py">delete</a>(instance_id, \*, project_id, region_id, cluster_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_clusters/server_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface">client.cloud.gpu_baremetal_clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/servers.py">attach_interface</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_clusters/server_attach_interface_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface">client.cloud.gpu_baremetal_clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/servers.py">detach_interface</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_clusters/server_detach_interface_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console">client.cloud.gpu_baremetal_clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/servers.py">get_console</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/console.py">Console</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle">client.cloud.gpu_baremetal_clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/servers.py">powercycle</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal_cluster_server.py">GPUBaremetalClusterServer</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot">client.cloud.gpu_baremetal_clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/servers.py">reboot</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal_cluster_server.py">GPUBaremetalClusterServer</a></code>

### Flavors

Methods:

- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/flavors">client.cloud.gpu_baremetal_clusters.flavors.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_clusters/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_baremetal_flavor_list.py">GPUBaremetalFlavorList</a></code>

### Images

Methods:

- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images">client.cloud.gpu_baremetal_clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/images.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_image_list.py">GPUImageList</a></code>
- <code title="delete /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}">client.cloud.gpu_baremetal_clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/images.py">delete</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}">client.cloud.gpu_baremetal_clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/images.py">get</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_image.py">GPUImage</a></code>
- <code title="post /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images">client.cloud.gpu_baremetal_clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal_clusters/images.py">upload</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal_clusters/image_upload_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

## Instances

Types:

```python
from gcore.types.cloud import InstanceInterface
```

Methods:

- <code title="post /cloud/v2/instances/{project_id}/{region_id}">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/instances/{project_id}/{region_id}/{instance_id}">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">update</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/instance.py">Instance</a></code>
- <code title="get /cloud/v1/instances/{project_id}/{region_id}">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/instance.py">SyncOffsetPage[Instance]</a></code>
- <code title="delete /cloud/v1/instances/{project_id}/{region_id}/{instance_id}">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">delete</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">action</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_action_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/put_into_servergroup">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">add_to_placement_group</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_add_to_placement_group_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">assign_security_group</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_assign_security_group_params.py">params</a>) -> None</code>
- <code title="post /cloud/v1/ports/{project_id}/{region_id}/{port_id}/disable_port_security">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">disable_port_security</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/instance_interface.py">InstanceInterface</a></code>
- <code title="post /cloud/v1/ports/{project_id}/{region_id}/{port_id}/enable_port_security">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">enable_port_security</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/instance_interface.py">InstanceInterface</a></code>
- <code title="get /cloud/v1/instances/{project_id}/{region_id}/{instance_id}">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">get</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/instance.py">Instance</a></code>
- <code title="get /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/get_console">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">get_console</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_get_console_params.py">params</a>) -> <a href="./src/gcore/types/cloud/console.py">Console</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/remove_from_servergroup">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">remove_from_placement_group</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">resize</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/delsecuritygroup">client.cloud.instances.<a href="./src/gcore/resources/cloud/instances/instances.py">unassign_security_group</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instance_unassign_security_group_params.py">params</a>) -> None</code>

### Flavors

Types:

```python
from gcore.types.cloud.instances import InstanceFlavor, InstanceFlavorList
```

Methods:

- <code title="get /cloud/v1/flavors/{project_id}/{region_id}">client.cloud.instances.flavors.<a href="./src/gcore/resources/cloud/instances/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/instances/instance_flavor_list.py">InstanceFlavorList</a></code>

### Interfaces

Methods:

- <code title="get /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/interfaces">client.cloud.instances.interfaces.<a href="./src/gcore/resources/cloud/instances/interfaces.py">list</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/network_interface_list.py">NetworkInterfaceList</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface">client.cloud.instances.interfaces.<a href="./src/gcore/resources/cloud/instances/interfaces.py">attach</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/interface_attach_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/detach_interface">client.cloud.instances.interfaces.<a href="./src/gcore/resources/cloud/instances/interfaces.py">detach</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/interface_detach_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### Images

Methods:

- <code title="patch /cloud/v1/images/{project_id}/{region_id}/{image_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">update</a>(image_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image.py">Image</a></code>
- <code title="get /cloud/v1/images/{project_id}/{region_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image_list.py">ImageList</a></code>
- <code title="delete /cloud/v1/images/{project_id}/{region_id}/{image_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">delete</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/images/{project_id}/{region_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">create_from_volume</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_create_from_volume_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/images/{project_id}/{region_id}/{image_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">get</a>(image_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/image.py">Image</a></code>
- <code title="post /cloud/v1/downloadimage/{project_id}/{region_id}">client.cloud.instances.images.<a href="./src/gcore/resources/cloud/instances/images.py">upload</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/image_upload_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### Metrics

Types:

```python
from gcore.types.cloud.instances import Metrics, MetricsList
```

Methods:

- <code title="post /cloud/v1/instances/{project_id}/{region_id}/{instance_id}/metrics">client.cloud.instances.metrics.<a href="./src/gcore/resources/cloud/instances/metrics.py">list</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/instances/metric_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/instances/metrics_list.py">MetricsList</a></code>

# Waap

Types:

```python
from gcore.types.waap import (
    WaapAdvancedRule,
    WaapAdvancedRuleDescriptor,
    WaapAdvancedRuleDescriptorList,
    WaapBlockCsrfPageData,
    WaapBlockPageData,
    WaapBlockedStatistics,
    WaapCaptchaPageData,
    WaapCommonTag,
    WaapCookieDisabledPageData,
    WaapCountStatistics,
    WaapCustomPagePreview,
    WaapCustomPageSet,
    WaapCustomRule,
    WaapCustomerRuleState,
    WaapDDOSAttack,
    WaapDDOSInfo,
    WaapDetailedDomain,
    WaapDomainAPISettings,
    WaapDomainDDOSSettings,
    WaapDomainPolicy,
    WaapDomainSettingsModel,
    WaapDomainStatus,
    WaapEventStatistics,
    WaapFirewallRule,
    WaapHandshakePageData,
    WaapInsight,
    WaapInsightSilence,
    WaapInsightSilenceSortBy,
    WaapInsightSortBy,
    WaapInsightStatus,
    WaapInsightType,
    WaapIPCountryAttack,
    WaapIPDDOSInfoModel,
    WaapIPInfo,
    WaapIPInfoCounts,
    WaapJavascriptDisabledPageData,
    WaapNetworkDetails,
    WaapOrganization,
    WaapPageType,
    WaapPaginatedCustomPageSet,
    WaapPaginatedDDOSAttack,
    WaapPaginatedDDOSInfo,
    WaapPaginatedRequestSummary,
    WaapPatternMatchedTag,
    WaapPolicyAction,
    WaapPolicyMode,
    WaapRequestDetails,
    WaapRequestOrganization,
    WaapRequestSummary,
    WaapResolution,
    WaapRuleActionType,
    WaapRuleBlockedRequests,
    WaapRuleSet,
    WaapStatisticItem,
    WaapStatisticsSeries,
    WaapSummaryDomain,
    WaapTag,
    WaapTimeSeriesAttack,
    WaapTopSession,
    WaapTopURL,
    WaapTopUserAgent,
    WaapTrafficMetrics,
    WaapTrafficType,
    WaapUserAgentDetails,
    WaapGetAccountOverviewResponse,
)
```

Methods:

- <code title="get /waap/v1/clients/me">client.waap.<a href="./src/gcore/resources/waap/waap.py">get_account_overview</a>() -> <a href="./src/gcore/types/waap/waap_get_account_overview_response.py">WaapGetAccountOverviewResponse</a></code>

## Statistics

Methods:

- <code title="get /waap/v1/statistics/series">client.waap.statistics.<a href="./src/gcore/resources/waap/statistics.py">get_usage_series</a>(\*\*<a href="src/gcore/types/waap/statistic_get_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_statistics_series.py">WaapStatisticsSeries</a></code>

## Domains

Types:

```python
from gcore.types.waap import DomainListRuleSetsResponse
```

Methods:

- <code title="patch /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">update</a>(domain_id, \*\*<a href="src/gcore/types/waap/domain_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">list</a>(\*\*<a href="src/gcore/types/waap/domain_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_summary_domain.py">SyncOffsetPage[WaapSummaryDomain]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">delete</a>(domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">get</a>(domain_id) -> <a href="./src/gcore/types/waap/waap_detailed_domain.py">WaapDetailedDomain</a></code>
- <code title="get /waap/v1/domains/{domain_id}/rule-sets">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">list_rule_sets</a>(domain_id) -> <a href="./src/gcore/types/waap/domain_list_rule_sets_response.py">DomainListRuleSetsResponse</a></code>

### Settings

Methods:

- <code title="patch /waap/v1/domains/{domain_id}/settings">client.waap.domains.settings.<a href="./src/gcore/resources/waap/domains/settings.py">update</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/setting_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/settings">client.waap.domains.settings.<a href="./src/gcore/resources/waap/domains/settings.py">get</a>(domain_id) -> <a href="./src/gcore/types/waap/waap_domain_settings_model.py">WaapDomainSettingsModel</a></code>

### APIPaths

Types:

```python
from gcore.types.waap.domains import APIPathCreateResponse, APIPathListResponse, APIPathGetResponse
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/api-paths">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/api_path_create_response.py">APIPathCreateResponse</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">update</a>(path_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/api-paths">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/api_path_list_response.py">SyncOffsetPage[APIPathListResponse]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">delete</a>(path_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">get</a>(path_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/api_path_get_response.py">APIPathGetResponse</a></code>

### APIPathGroups

Types:

```python
from gcore.types.waap.domains import APIPathGroupListResponse
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-path-groups">client.waap.domains.api_path_groups.<a href="./src/gcore/resources/waap/domains/api_path_groups.py">list</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/api_path_group_list_response.py">APIPathGroupListResponse</a></code>

### APIDiscovery

Types:

```python
from gcore.types.waap.domains import (
    APIDiscoveryGetSettingsResponse,
    APIDiscoveryScanOpenAPIResponse,
    APIDiscoveryUpdateSettingsResponse,
    APIDiscoveryUploadOpenAPIResponse,
)
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-discovery/settings">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery/api_discovery.py">get_settings</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/api_discovery_get_settings_response.py">APIDiscoveryGetSettingsResponse</a></code>
- <code title="post /waap/v1/domains/{domain_id}/api-discovery/scan">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery/api_discovery.py">scan_openapi</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/api_discovery_scan_openapi_response.py">APIDiscoveryScanOpenAPIResponse</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/api-discovery/settings">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery/api_discovery.py">update_settings</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_update_settings_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/api_discovery_update_settings_response.py">APIDiscoveryUpdateSettingsResponse</a></code>
- <code title="post /waap/v1/domains/{domain_id}/api-discovery/upload">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery/api_discovery.py">upload_openapi</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_upload_openapi_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/api_discovery_upload_openapi_response.py">APIDiscoveryUploadOpenAPIResponse</a></code>

#### ScanResults

Types:

```python
from gcore.types.waap.domains.api_discovery import ScanResultListResponse, ScanResultGetResponse
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-discovery/scan-results">client.waap.domains.api_discovery.scan_results.<a href="./src/gcore/resources/waap/domains/api_discovery/scan_results.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery/scan_result_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/api_discovery/scan_result_list_response.py">SyncOffsetPage[ScanResultListResponse]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/api-discovery/scan-results/{scan_id}">client.waap.domains.api_discovery.scan_results.<a href="./src/gcore/resources/waap/domains/api_discovery/scan_results.py">get</a>(scan_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/api_discovery/scan_result_get_response.py">ScanResultGetResponse</a></code>

### Insights

Methods:

- <code title="get /waap/v1/domains/{domain_id}/insights">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight.py">SyncOffsetPage[WaapInsight]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/insights/{insight_id}">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">get</a>(insight_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_insight.py">WaapInsight</a></code>
- <code title="put /waap/v1/domains/{domain_id}/insights/{insight_id}">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">replace</a>(insight_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_replace_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight.py">WaapInsight</a></code>

### InsightSilences

Methods:

- <code title="post /waap/v1/domains/{domain_id}/insight-silences">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight_silence.py">WaapInsightSilence</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">update</a>(silence_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_update_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight_silence.py">WaapInsightSilence</a></code>
- <code title="get /waap/v1/domains/{domain_id}/insight-silences">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight_silence.py">SyncOffsetPage[WaapInsightSilence]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">delete</a>(silence_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">get</a>(silence_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_insight_silence.py">WaapInsightSilence</a></code>

### Policies

Methods:

- <code title="patch /waap/v1/domains/{domain_id}/policies/{policy_id}/toggle">client.waap.domains.policies.<a href="./src/gcore/resources/waap/domains/policies.py">toggle</a>(policy_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_policy_mode.py">WaapPolicyMode</a></code>

### Analytics

Types:

```python
from gcore.types.waap.domains import AnalyticsListEventTrafficResponse
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/stats">client.waap.domains.analytics.<a href="./src/gcore/resources/waap/domains/analytics/analytics.py">get_event_statistics</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/analytics_get_event_statistics_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_event_statistics.py">WaapEventStatistics</a></code>
- <code title="get /waap/v1/domains/{domain_id}/ddos-attacks">client.waap.domains.analytics.<a href="./src/gcore/resources/waap/domains/analytics/analytics.py">list_ddos_attacks</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/analytics_list_ddos_attacks_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ddos_attack.py">SyncOffsetPage[WaapDDOSAttack]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/ddos-info">client.waap.domains.analytics.<a href="./src/gcore/resources/waap/domains/analytics/analytics.py">list_ddos_info</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/analytics_list_ddos_info_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ddos_info.py">SyncOffsetPage[WaapDDOSInfo]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/traffic">client.waap.domains.analytics.<a href="./src/gcore/resources/waap/domains/analytics/analytics.py">list_event_traffic</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/analytics_list_event_traffic_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/analytics_list_event_traffic_response.py">AnalyticsListEventTrafficResponse</a></code>

#### Requests

Methods:

- <code title="get /waap/v1/domains/{domain_id}/requests">client.waap.domains.analytics.requests.<a href="./src/gcore/resources/waap/domains/analytics/requests.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/analytics/request_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_request_summary.py">SyncOffsetPage[WaapRequestSummary]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/requests/{request_id}/details">client.waap.domains.analytics.requests.<a href="./src/gcore/resources/waap/domains/analytics/requests.py">get</a>(request_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_request_details.py">WaapRequestDetails</a></code>

### CustomRules

Methods:

- <code title="post /waap/v1/domains/{domain_id}/custom-rules">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_rule.py">WaapCustomRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/custom-rules">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_rule.py">SyncOffsetPage[WaapCustomRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="post /waap/v1/domains/{domain_id}/custom-rules/bulk_delete">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">delete_multiple</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_delete_multiple_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_custom_rule.py">WaapCustomRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/custom-rules/{rule_id}/{action}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

### FirewallRules

Methods:

- <code title="post /waap/v1/domains/{domain_id}/firewall-rules">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_firewall_rule.py">WaapFirewallRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/firewall-rules">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_firewall_rule.py">SyncOffsetPage[WaapFirewallRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="post /waap/v1/domains/{domain_id}/firewall-rules/bulk_delete">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">delete_multiple</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_delete_multiple_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_firewall_rule.py">WaapFirewallRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}/{action}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

### AdvancedRules

Methods:

- <code title="post /waap/v1/domains/{domain_id}/advanced-rules">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_advanced_rule.py">WaapAdvancedRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/advanced-rules">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_advanced_rule.py">SyncOffsetPage[WaapAdvancedRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_advanced_rule.py">WaapAdvancedRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}/{action}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

## CustomPageSets

Methods:

- <code title="post /waap/v1/custom-page-sets">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">create</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">WaapCustomPageSet</a></code>
- <code title="patch /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">update</a>(set_id, \*\*<a href="src/gcore/types/waap/custom_page_set_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/custom-page-sets">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">list</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">SyncOffsetPage[WaapCustomPageSet]</a></code>
- <code title="delete /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">delete</a>(set_id) -> None</code>
- <code title="get /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">get</a>(set_id) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">WaapCustomPageSet</a></code>
- <code title="post /waap/v1/preview-custom-page">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">preview</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_preview_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_preview.py">WaapCustomPagePreview</a></code>

## AdvancedRules

Methods:

- <code title="get /waap/v1/advanced-rules/descriptor">client.waap.advanced_rules.<a href="./src/gcore/resources/waap/advanced_rules.py">list</a>() -> <a href="./src/gcore/types/waap/waap_advanced_rule_descriptor_list.py">WaapAdvancedRuleDescriptorList</a></code>

## Tags

Methods:

- <code title="get /waap/v1/tags">client.waap.tags.<a href="./src/gcore/resources/waap/tags.py">list</a>(\*\*<a href="src/gcore/types/waap/tag_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_tag.py">SyncOffsetPage[WaapTag]</a></code>

## Organizations

Methods:

- <code title="get /waap/v1/organizations">client.waap.organizations.<a href="./src/gcore/resources/waap/organizations.py">list</a>(\*\*<a href="src/gcore/types/waap/organization_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_organization.py">SyncOffsetPage[WaapOrganization]</a></code>

## IPInfo

Types:

```python
from gcore.types.waap import (
    IPInfoGetAttackTimeSeriesResponse,
    IPInfoGetBlockedRequestsResponse,
    IPInfoGetTopSessionsResponse,
    IPInfoGetTopURLsResponse,
    IPInfoGetTopUserAgentsResponse,
    IPInfoListAttackedCountriesResponse,
)
```

Methods:

- <code title="get /waap/v1/ip-info/ip-info">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ip_info.py">WaapIPInfo</a></code>
- <code title="get /waap/v1/ip-info/attack-time-series">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_attack_time_series</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_attack_time_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_attack_time_series_response.py">IPInfoGetAttackTimeSeriesResponse</a></code>
- <code title="get /waap/v1/ip-info/blocked-requests">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_blocked_requests</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_blocked_requests_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_blocked_requests_response.py">IPInfoGetBlockedRequestsResponse</a></code>
- <code title="get /waap/v1/ip-info/counts">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_counts</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_counts_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ip_info_counts.py">WaapIPInfoCounts</a></code>
- <code title="get /waap/v1/ip-info/ddos">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_ddos_attack_series</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_ddos_attack_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ip_ddos_info_model.py">WaapIPDDOSInfoModel</a></code>
- <code title="get /waap/v1/ip-info/top-sessions">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_top_sessions</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_sessions_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_sessions_response.py">IPInfoGetTopSessionsResponse</a></code>
- <code title="get /waap/v1/ip-info/top-urls">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_top_urls</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_urls_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_urls_response.py">IPInfoGetTopURLsResponse</a></code>
- <code title="get /waap/v1/ip-info/top-user-agents">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">get_top_user_agents</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_user_agents_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_user_agents_response.py">IPInfoGetTopUserAgentsResponse</a></code>
- <code title="get /waap/v1/ip-info/attack-map">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info.py">list_attacked_countries</a>(\*\*<a href="src/gcore/types/waap/ip_info_list_attacked_countries_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_list_attacked_countries_response.py">IPInfoListAttackedCountriesResponse</a></code>

# Iam

Types:

```python
from gcore.types.iam import AccountOverview
```

Methods:

- <code title="get /iam/clients/me">client.iam.<a href="./src/gcore/resources/iam/iam.py">get_account_overview</a>() -> <a href="./src/gcore/types/iam/account_overview.py">AccountOverview</a></code>

## APITokens

Types:

```python
from gcore.types.iam import APIToken, APITokenCreate, APITokenList
```

Methods:

- <code title="post /iam/clients/{clientId}/tokens">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">create</a>(client_id, \*\*<a href="src/gcore/types/iam/api_token_create_params.py">params</a>) -> <a href="./src/gcore/types/iam/api_token_create.py">APITokenCreate</a></code>
- <code title="get /iam/clients/{clientId}/tokens">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">list</a>(client_id, \*\*<a href="src/gcore/types/iam/api_token_list_params.py">params</a>) -> <a href="./src/gcore/types/iam/api_token_list.py">APITokenList</a></code>
- <code title="delete /iam/clients/{clientId}/tokens/{tokenId}">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">delete</a>(token_id, \*, client_id) -> None</code>
- <code title="get /iam/clients/{clientId}/tokens/{tokenId}">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">get</a>(token_id, \*, client_id) -> <a href="./src/gcore/types/iam/api_token.py">APIToken</a></code>

## Users

Types:

```python
from gcore.types.iam import User, UserDetailed, UserInvite, UserUpdate
```

Methods:

- <code title="patch /iam/users/{userId}">client.iam.users.<a href="./src/gcore/resources/iam/users.py">update</a>(user_id, \*\*<a href="src/gcore/types/iam/user_update_params.py">params</a>) -> <a href="./src/gcore/types/iam/user_update.py">UserUpdate</a></code>
- <code title="get /iam/users">client.iam.users.<a href="./src/gcore/resources/iam/users.py">list</a>(\*\*<a href="src/gcore/types/iam/user_list_params.py">params</a>) -> <a href="./src/gcore/types/iam/user.py">SyncOffsetPageIam[User]</a></code>
- <code title="delete /iam/clients/{clientId}/client-users/{userId}">client.iam.users.<a href="./src/gcore/resources/iam/users.py">delete</a>(user_id, \*, client_id) -> None</code>
- <code title="get /iam/users/{userId}">client.iam.users.<a href="./src/gcore/resources/iam/users.py">get</a>(user_id) -> <a href="./src/gcore/types/iam/user_detailed.py">UserDetailed</a></code>
- <code title="post /iam/clients/invite_user">client.iam.users.<a href="./src/gcore/resources/iam/users.py">invite</a>(\*\*<a href="src/gcore/types/iam/user_invite_params.py">params</a>) -> <a href="./src/gcore/types/iam/user_invite.py">UserInvite</a></code>

# Fastedge

Types:

```python
from gcore.types.fastedge import Client
```

Methods:

- <code title="get /fastedge/v1/me">client.fastedge.<a href="./src/gcore/resources/fastedge/fastedge.py">get_account_overview</a>() -> <a href="./src/gcore/types/fastedge/client.py">Client</a></code>

## Templates

Types:

```python
from gcore.types.fastedge import Template, TemplateParameter, TemplateShort
```

Methods:

- <code title="post /fastedge/v1/template">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">create</a>(\*\*<a href="src/gcore/types/fastedge/template_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/template_short.py">TemplateShort</a></code>
- <code title="get /fastedge/v1/template">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">list</a>(\*\*<a href="src/gcore/types/fastedge/template_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/template_short.py">SyncOffsetPageFastedgeTemplates[TemplateShort]</a></code>
- <code title="delete /fastedge/v1/template/{id}">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">delete</a>(id, \*\*<a href="src/gcore/types/fastedge/template_delete_params.py">params</a>) -> None</code>
- <code title="get /fastedge/v1/template/{id}">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">get</a>(id) -> <a href="./src/gcore/types/fastedge/template.py">Template</a></code>
- <code title="put /fastedge/v1/template/{id}">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">replace</a>(id, \*\*<a href="src/gcore/types/fastedge/template_replace_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/template_short.py">TemplateShort</a></code>

## Secrets

Types:

```python
from gcore.types.fastedge import Secret, SecretShort, SecretCreateResponse, SecretListResponse
```

Methods:

- <code title="post /fastedge/v1/secrets">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">create</a>(\*\*<a href="src/gcore/types/fastedge/secret_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="patch /fastedge/v1/secrets/{id}">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">update</a>(id, \*\*<a href="src/gcore/types/fastedge/secret_update_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/secret.py">Secret</a></code>
- <code title="get /fastedge/v1/secrets">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">list</a>(\*\*<a href="src/gcore/types/fastedge/secret_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /fastedge/v1/secrets/{id}">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">delete</a>(id, \*\*<a href="src/gcore/types/fastedge/secret_delete_params.py">params</a>) -> None</code>
- <code title="get /fastedge/v1/secrets/{id}">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">get</a>(id) -> <a href="./src/gcore/types/fastedge/secret.py">Secret</a></code>
- <code title="put /fastedge/v1/secrets/{id}">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">replace</a>(id, \*\*<a href="src/gcore/types/fastedge/secret_replace_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/secret.py">Secret</a></code>

## Binaries

Types:

```python
from gcore.types.fastedge import Binary, BinaryShort, BinaryListResponse
```

Methods:

- <code title="get /fastedge/v1/binaries">client.fastedge.binaries.<a href="./src/gcore/resources/fastedge/binaries.py">list</a>() -> <a href="./src/gcore/types/fastedge/binary_list_response.py">BinaryListResponse</a></code>
- <code title="delete /fastedge/v1/binaries/{id}">client.fastedge.binaries.<a href="./src/gcore/resources/fastedge/binaries.py">delete</a>(id) -> None</code>
- <code title="get /fastedge/v1/binaries/{id}">client.fastedge.binaries.<a href="./src/gcore/resources/fastedge/binaries.py">get</a>(id) -> <a href="./src/gcore/types/fastedge/binary.py">Binary</a></code>

## Statistics

Types:

```python
from gcore.types.fastedge import (
    CallStatus,
    DurationStats,
    StatisticGetCallSeriesResponse,
    StatisticGetDurationSeriesResponse,
)
```

Methods:

- <code title="get /fastedge/v1/stats/calls">client.fastedge.statistics.<a href="./src/gcore/resources/fastedge/statistics.py">get_call_series</a>(\*\*<a href="src/gcore/types/fastedge/statistic_get_call_series_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/statistic_get_call_series_response.py">StatisticGetCallSeriesResponse</a></code>
- <code title="get /fastedge/v1/stats/app_duration">client.fastedge.statistics.<a href="./src/gcore/resources/fastedge/statistics.py">get_duration_series</a>(\*\*<a href="src/gcore/types/fastedge/statistic_get_duration_series_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/statistic_get_duration_series_response.py">StatisticGetDurationSeriesResponse</a></code>

## Apps

Types:

```python
from gcore.types.fastedge import App, AppShort
```

Methods:

- <code title="post /fastedge/v1/apps">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps/apps.py">create</a>(\*\*<a href="src/gcore/types/fastedge/app_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/app_short.py">AppShort</a></code>
- <code title="patch /fastedge/v1/apps/{id}">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps/apps.py">update</a>(id, \*\*<a href="src/gcore/types/fastedge/app_update_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/app_short.py">AppShort</a></code>
- <code title="get /fastedge/v1/apps">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps/apps.py">list</a>(\*\*<a href="src/gcore/types/fastedge/app_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/app_short.py">SyncOffsetPageFastedgeApps[AppShort]</a></code>
- <code title="delete /fastedge/v1/apps/{id}">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps/apps.py">delete</a>(id) -> None</code>
- <code title="get /fastedge/v1/apps/{id}">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps/apps.py">get</a>(id) -> <a href="./src/gcore/types/fastedge/app.py">App</a></code>
- <code title="put /fastedge/v1/apps/{id}">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps/apps.py">replace</a>(id, \*\*<a href="src/gcore/types/fastedge/app_replace_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/app_short.py">AppShort</a></code>

### Logs

Types:

```python
from gcore.types.fastedge.apps import Log
```

Methods:

- <code title="get /fastedge/v1/apps/{id}/logs">client.fastedge.apps.logs.<a href="./src/gcore/resources/fastedge/apps/logs.py">list</a>(id, \*\*<a href="src/gcore/types/fastedge/apps/log_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/apps/log.py">SyncOffsetPageFastedgeAppLogs[Log]</a></code>

## KvStores

Types:

```python
from gcore.types.fastedge import (
    KvStore,
    KvStoreShort,
    KvStoreStats,
    KvStoreListResponse,
    KvStoreGetResponse,
)
```

Methods:

- <code title="post /fastedge/v1/kv">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">create</a>(\*\*<a href="src/gcore/types/fastedge/kv_store_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/kv_store.py">KvStore</a></code>
- <code title="get /fastedge/v1/kv">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">list</a>(\*\*<a href="src/gcore/types/fastedge/kv_store_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/kv_store_list_response.py">KvStoreListResponse</a></code>
- <code title="delete /fastedge/v1/kv/{id}">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">delete</a>(id) -> None</code>
- <code title="get /fastedge/v1/kv/{id}">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">get</a>(id) -> <a href="./src/gcore/types/fastedge/kv_store_get_response.py">KvStoreGetResponse</a></code>
- <code title="put /fastedge/v1/kv/{id}">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">replace</a>(id, \*\*<a href="src/gcore/types/fastedge/kv_store_replace_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/kv_store.py">KvStore</a></code>
