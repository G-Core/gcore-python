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
- <code title="put /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">replace</a>(credential_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials_create.py">InferenceRegistryCredentialsCreate</a></code>

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

### APIKeys

Types:

```python
from gcore.types.cloud.inference import InferenceAPIKey, InferenceAPIKeyCreate
```

Methods:

- <code title="post /cloud/v3/inference/{project_id}/api_keys">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/api_key_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_api_key_create.py">InferenceAPIKeyCreate</a></code>
- <code title="patch /cloud/v3/inference/{project_id}/api_keys/{api_key_name}">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">update</a>(api_key_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/api_key_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_api_key.py">InferenceAPIKey</a></code>
- <code title="get /cloud/v3/inference/{project_id}/api_keys">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/api_key_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_api_key.py">SyncOffsetPage[InferenceAPIKey]</a></code>
- <code title="delete /cloud/v3/inference/{project_id}/api_keys/{api_key_name}">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">delete</a>(api_key_name, \*, project_id) -> None</code>
- <code title="get /cloud/v3/inference/{project_id}/api_keys/{api_key_name}">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">get</a>(api_key_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_api_key.py">InferenceAPIKey</a></code>

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

## AuditLogs

Types:

```python
from gcore.types.cloud import AuditLogEntry
```

Methods:

- <code title="get /cloud/v1/user_actions">client.cloud.audit_logs.<a href="./src/gcore/resources/cloud/audit_logs.py">list</a>(\*\*<a href="src/gcore/types/cloud/audit_log_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/audit_log_entry.py">SyncOffsetPage[AuditLogEntry]</a></code>

## CostReports

Types:

```python
from gcore.types.cloud import CostReportAggregated, CostReportAggregatedMonthly, CostReportDetailed
```

Methods:

- <code title="post /cloud/v1/cost_report/totals">client.cloud.cost_reports.<a href="./src/gcore/resources/cloud/cost_reports.py">get_aggregated</a>(\*\*<a href="src/gcore/types/cloud/cost_report_get_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/cloud/cost_report_aggregated.py">CostReportAggregated</a></code>
- <code title="post /cloud/v1/reservation_cost_report/totals">client.cloud.cost_reports.<a href="./src/gcore/resources/cloud/cost_reports.py">get_aggregated_monthly</a>(\*\*<a href="src/gcore/types/cloud/cost_report_get_aggregated_monthly_params.py">params</a>) -> <a href="./src/gcore/types/cloud/cost_report_aggregated_monthly.py">CostReportAggregatedMonthly</a></code>
- <code title="post /cloud/v1/cost_report/resources">client.cloud.cost_reports.<a href="./src/gcore/resources/cloud/cost_reports.py">get_detailed</a>(\*\*<a href="src/gcore/types/cloud/cost_report_get_detailed_params.py">params</a>) -> <a href="./src/gcore/types/cloud/cost_report_detailed.py">CostReportDetailed</a></code>

## UsageReports

Types:

```python
from gcore.types.cloud import UsageReport
```

Methods:

- <code title="post /cloud/v1/usage_report">client.cloud.usage_reports.<a href="./src/gcore/resources/cloud/usage_reports.py">get</a>(\*\*<a href="src/gcore/types/cloud/usage_report_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/usage_report.py">UsageReport</a></code>

# Waap

Types:

```python
from gcore.types.waap import WaapGetAccountOverviewResponse
```

Methods:

- <code title="get /waap/v1/clients/me">client.waap.<a href="./src/gcore/resources/waap/waap.py">get_account_overview</a>() -> <a href="./src/gcore/types/waap/waap_get_account_overview_response.py">WaapGetAccountOverviewResponse</a></code>

## Statistics

Types:

```python
from gcore.types.waap import WaapStatisticItem, WaapStatisticsSeries
```

Methods:

- <code title="get /waap/v1/statistics/series">client.waap.statistics.<a href="./src/gcore/resources/waap/statistics.py">get_usage_series</a>(\*\*<a href="src/gcore/types/waap/statistic_get_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_statistics_series.py">WaapStatisticsSeries</a></code>

## Domains

Types:

```python
from gcore.types.waap import (
    WaapDetailedDomain,
    WaapDomainAPISettings,
    WaapDomainDDOSSettings,
    WaapDomainSettingsModel,
    WaapPolicyMode,
    WaapRuleSet,
    WaapSummaryDomain,
    DomainListRuleSetsResponse,
)
```

Methods:

- <code title="patch /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">update</a>(domain_id, \*\*<a href="src/gcore/types/waap/domain_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">list</a>(\*\*<a href="src/gcore/types/waap/domain_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_summary_domain.py">SyncOffsetPage[WaapSummaryDomain]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">delete</a>(domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">get</a>(domain_id) -> <a href="./src/gcore/types/waap/waap_detailed_domain.py">WaapDetailedDomain</a></code>
- <code title="get /waap/v1/domains/{domain_id}/rule-sets">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">list_rule_sets</a>(domain_id) -> <a href="./src/gcore/types/waap/domain_list_rule_sets_response.py">DomainListRuleSetsResponse</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/policies/{policy_id}/toggle">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">toggle_policy</a>(policy_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_policy_mode.py">WaapPolicyMode</a></code>

### Settings

Methods:

- <code title="patch /waap/v1/domains/{domain_id}/settings">client.waap.domains.settings.<a href="./src/gcore/resources/waap/domains/settings.py">update</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/setting_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/settings">client.waap.domains.settings.<a href="./src/gcore/resources/waap/domains/settings.py">get</a>(domain_id) -> <a href="./src/gcore/types/waap/waap_domain_settings_model.py">WaapDomainSettingsModel</a></code>

### APIPaths

Types:

```python
from gcore.types.waap.domains import WaapAPIPath
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/api-paths">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_path.py">WaapAPIPath</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">update</a>(path_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/api-paths">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_path.py">SyncOffsetPage[WaapAPIPath]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">delete</a>(path_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">get</a>(path_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_api_path.py">WaapAPIPath</a></code>

### APIPathGroups

Types:

```python
from gcore.types.waap.domains import APIPathGroupList
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-path-groups">client.waap.domains.api_path_groups.<a href="./src/gcore/resources/waap/domains/api_path_groups.py">list</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/api_path_group_list.py">APIPathGroupList</a></code>

### APIDiscovery

Types:

```python
from gcore.types.waap.domains import WaapAPIDiscoverySettings, WaapAPIScanResult, WaapTaskID
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-discovery/scan-results/{scan_id}">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">get_scan_result</a>(scan_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_api_scan_result.py">WaapAPIScanResult</a></code>
- <code title="get /waap/v1/domains/{domain_id}/api-discovery/settings">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">get_settings</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/waap_api_discovery_settings.py">WaapAPIDiscoverySettings</a></code>
- <code title="get /waap/v1/domains/{domain_id}/api-discovery/scan-results">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">list_scan_results</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_list_scan_results_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_scan_result.py">SyncOffsetPage[WaapAPIScanResult]</a></code>
- <code title="post /waap/v1/domains/{domain_id}/api-discovery/scan">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">scan_openapi</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/waap_task_id.py">WaapTaskID</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/api-discovery/settings">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">update_settings</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_update_settings_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_discovery_settings.py">WaapAPIDiscoverySettings</a></code>
- <code title="post /waap/v1/domains/{domain_id}/api-discovery/upload">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">upload_openapi</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_upload_openapi_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_task_id.py">WaapTaskID</a></code>

### Insights

Types:

```python
from gcore.types.waap.domains import WaapInsight
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/insights">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight.py">SyncOffsetPage[WaapInsight]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/insights/{insight_id}">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">get</a>(insight_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_insight.py">WaapInsight</a></code>
- <code title="put /waap/v1/domains/{domain_id}/insights/{insight_id}">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">replace</a>(insight_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_replace_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight.py">WaapInsight</a></code>

### InsightSilences

Types:

```python
from gcore.types.waap.domains import WaapInsightSilence
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/insight-silences">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">WaapInsightSilence</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">update</a>(silence_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_update_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">WaapInsightSilence</a></code>
- <code title="get /waap/v1/domains/{domain_id}/insight-silences">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">SyncOffsetPage[WaapInsightSilence]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">delete</a>(silence_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">get</a>(silence_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">WaapInsightSilence</a></code>

### Statistics

Types:

```python
from gcore.types.waap.domains import (
    WaapBlockedStatistics,
    WaapCountStatistics,
    WaapDDOSAttack,
    WaapDDOSInfo,
    WaapEventStatistics,
    WaapRequestDetails,
    WaapRequestSummary,
    WaapTrafficMetrics,
    StatisticGetTrafficSeriesResponse,
)
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/ddos-attacks">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_ddos_attacks</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_ddos_attacks_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_ddos_attack.py">SyncOffsetPage[WaapDDOSAttack]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/ddos-info">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_ddos_info</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_ddos_info_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_ddos_info.py">SyncOffsetPage[WaapDDOSInfo]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/stats">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_events_aggregated</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_events_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_event_statistics.py">WaapEventStatistics</a></code>
- <code title="get /waap/v1/domains/{domain_id}/requests/{request_id}/details">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_request_details</a>(request_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_request_details.py">WaapRequestDetails</a></code>
- <code title="get /waap/v1/domains/{domain_id}/requests">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_requests_series</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_requests_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_request_summary.py">SyncOffsetPage[WaapRequestSummary]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/traffic">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_traffic_series</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_traffic_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/statistic_get_traffic_series_response.py">StatisticGetTrafficSeriesResponse</a></code>

### CustomRules

Types:

```python
from gcore.types.waap.domains import WaapCustomRule
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/custom-rules">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_custom_rule.py">WaapCustomRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/custom-rules">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_custom_rule.py">SyncOffsetPage[WaapCustomRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="post /waap/v1/domains/{domain_id}/custom-rules/bulk_delete">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">delete_multiple</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_delete_multiple_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_custom_rule.py">WaapCustomRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/custom-rules/{rule_id}/{action}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

### FirewallRules

Types:

```python
from gcore.types.waap.domains import WaapFirewallRule
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/firewall-rules">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_firewall_rule.py">WaapFirewallRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/firewall-rules">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_firewall_rule.py">SyncOffsetPage[WaapFirewallRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="post /waap/v1/domains/{domain_id}/firewall-rules/bulk_delete">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">delete_multiple</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_delete_multiple_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_firewall_rule.py">WaapFirewallRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}/{action}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

### AdvancedRules

Types:

```python
from gcore.types.waap.domains import WaapAdvancedRule
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/advanced-rules">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_advanced_rule.py">WaapAdvancedRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/advanced-rules">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_advanced_rule.py">SyncOffsetPage[WaapAdvancedRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_advanced_rule.py">WaapAdvancedRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}/{action}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

## CustomPageSets

Types:

```python
from gcore.types.waap import WaapCustomPagePreview, WaapCustomPageSet
```

Methods:

- <code title="post /waap/v1/custom-page-sets">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">create</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">WaapCustomPageSet</a></code>
- <code title="patch /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">update</a>(set_id, \*\*<a href="src/gcore/types/waap/custom_page_set_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/custom-page-sets">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">list</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">SyncOffsetPage[WaapCustomPageSet]</a></code>
- <code title="delete /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">delete</a>(set_id) -> None</code>
- <code title="get /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">get</a>(set_id) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">WaapCustomPageSet</a></code>
- <code title="post /waap/v1/preview-custom-page">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">preview</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_preview_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_preview.py">WaapCustomPagePreview</a></code>

## AdvancedRules

Types:

```python
from gcore.types.waap import WaapAdvancedRuleDescriptor, WaapAdvancedRuleDescriptorList
```

Methods:

- <code title="get /waap/v1/advanced-rules/descriptor">client.waap.advanced_rules.<a href="./src/gcore/resources/waap/advanced_rules.py">list</a>() -> <a href="./src/gcore/types/waap/waap_advanced_rule_descriptor_list.py">WaapAdvancedRuleDescriptorList</a></code>

## Tags

Types:

```python
from gcore.types.waap import WaapTag
```

Methods:

- <code title="get /waap/v1/tags">client.waap.tags.<a href="./src/gcore/resources/waap/tags.py">list</a>(\*\*<a href="src/gcore/types/waap/tag_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_tag.py">SyncOffsetPage[WaapTag]</a></code>

## Organizations

Types:

```python
from gcore.types.waap import WaapOrganization
```

Methods:

- <code title="get /waap/v1/organizations">client.waap.organizations.<a href="./src/gcore/resources/waap/organizations.py">list</a>(\*\*<a href="src/gcore/types/waap/organization_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_organization.py">SyncOffsetPage[WaapOrganization]</a></code>

## Insights

Types:

```python
from gcore.types.waap import WaapInsightType
```

Methods:

- <code title="get /waap/v1/security-insights/types">client.waap.insights.<a href="./src/gcore/resources/waap/insights.py">list_types</a>(\*\*<a href="src/gcore/types/waap/insight_list_types_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight_type.py">SyncOffsetPage[WaapInsightType]</a></code>

## IPInfo

Types:

```python
from gcore.types.waap import (
    WaapIPCountryAttack,
    WaapIPDDOSInfoModel,
    WaapRuleBlockedRequests,
    WaapTimeSeriesAttack,
    WaapTopSession,
    WaapTopUserAgent,
    IPInfoGetAttackTimeSeriesResponse,
    IPInfoGetBlockedRequestsResponse,
    IPInfoGetIPInfoResponse,
    IPInfoGetTopURLsResponse,
    IPInfoGetTopUserAgentsResponse,
    IPInfoGetTopUserSessionsResponse,
    IPInfoListAttackedCountriesResponse,
)
```

Methods:

- <code title="get /waap/v1/ip-info/attack-time-series">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_attack_time_series</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_attack_time_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_attack_time_series_response.py">IPInfoGetAttackTimeSeriesResponse</a></code>
- <code title="get /waap/v1/ip-info/blocked-requests">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_blocked_requests</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_blocked_requests_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_blocked_requests_response.py">IPInfoGetBlockedRequestsResponse</a></code>
- <code title="get /waap/v1/ip-info/ddos">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_ddos_attack_series</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_ddos_attack_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ip_ddos_info_model.py">WaapIPDDOSInfoModel</a></code>
- <code title="get /waap/v1/ip-info/ip-info">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_ip_info</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_ip_info_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_ip_info_response.py">IPInfoGetIPInfoResponse</a></code>
- <code title="get /waap/v1/ip-info/top-urls">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_top_urls</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_urls_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_urls_response.py">IPInfoGetTopURLsResponse</a></code>
- <code title="get /waap/v1/ip-info/top-user-agents">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_top_user_agents</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_user_agents_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_user_agents_response.py">IPInfoGetTopUserAgentsResponse</a></code>
- <code title="get /waap/v1/ip-info/top-sessions">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_top_user_sessions</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_user_sessions_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_user_sessions_response.py">IPInfoGetTopUserSessionsResponse</a></code>
- <code title="get /waap/v1/ip-info/attack-map">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">list_attacked_countries</a>(\*\*<a href="src/gcore/types/waap/ip_info_list_attacked_countries_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_list_attacked_countries_response.py">IPInfoListAttackedCountriesResponse</a></code>

### Metrics

Types:

```python
from gcore.types.waap.ip_info import WaapIPInfoCounts
```

Methods:

- <code title="get /waap/v1/ip-info/counts">client.waap.ip_info.metrics.<a href="./src/gcore/resources/waap/ip_info/metrics.py">list</a>(\*\*<a href="src/gcore/types/waap/ip_info/metric_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info/waap_ip_info_counts.py">WaapIPInfoCounts</a></code>

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
- <code title="get /iam/users">client.iam.users.<a href="./src/gcore/resources/iam/users.py">list</a>(\*\*<a href="src/gcore/types/iam/user_list_params.py">params</a>) -> <a href="./src/gcore/types/iam/user.py">SyncOffsetPage[User]</a></code>
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

- <code title="post /fastedge/v1/binaries/raw">client.fastedge.binaries.<a href="./src/gcore/resources/fastedge/binaries.py">create</a>(body, \*\*<a href="src/gcore/types/fastedge/binary_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/binary_short.py">BinaryShort</a></code>
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

# Streaming

Types:

```python
from gcore.types.streaming import CreateVideo, Video
```

## AITasks

Types:

```python
from gcore.types.streaming import (
    AIContentmoderationCasm,
    AIContentmoderationHardnudity,
    AIContentmoderationNsfw,
    AIContentmoderationSoftnudity,
    AIContentmoderationSport,
    AIContentmoderationWeapon,
    AITask,
    AITaskCreateResponse,
    AITaskCancelResponse,
    AITaskGetResponse,
    AITaskGetAISettingsResponse,
)
```

Methods:

- <code title="post /streaming/ai/tasks">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">create</a>(\*\*<a href="src/gcore/types/streaming/ai_task_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ai_task_create_response.py">AITaskCreateResponse</a></code>
- <code title="get /streaming/ai/tasks">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">list</a>(\*\*<a href="src/gcore/types/streaming/ai_task_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ai_task.py">SyncPageStreamingAI[AITask]</a></code>
- <code title="post /streaming/ai/tasks/{task_id}/cancel">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">cancel</a>(task_id) -> <a href="./src/gcore/types/streaming/ai_task_cancel_response.py">AITaskCancelResponse</a></code>
- <code title="get /streaming/ai/tasks/{task_id}">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">get</a>(task_id) -> <a href="./src/gcore/types/streaming/ai_task_get_response.py">AITaskGetResponse</a></code>
- <code title="get /streaming/ai/info">client.streaming.ai_tasks.<a href="./src/gcore/resources/streaming/ai_tasks.py">get_ai_settings</a>(\*\*<a href="src/gcore/types/streaming/ai_task_get_ai_settings_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ai_task_get_ai_settings_response.py">AITaskGetAISettingsResponse</a></code>

## Broadcasts

Types:

```python
from gcore.types.streaming import Broadcast, BroadcastSpectatorsCount
```

Methods:

- <code title="post /streaming/broadcasts">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">create</a>(\*\*<a href="src/gcore/types/streaming/broadcast_create_params.py">params</a>) -> None</code>
- <code title="patch /streaming/broadcasts/{broadcast_id}">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">update</a>(broadcast_id, \*\*<a href="src/gcore/types/streaming/broadcast_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/broadcast.py">Broadcast</a></code>
- <code title="get /streaming/broadcasts">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">list</a>(\*\*<a href="src/gcore/types/streaming/broadcast_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/broadcast.py">SyncPageStreaming[Broadcast]</a></code>
- <code title="delete /streaming/broadcasts/{broadcast_id}">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">delete</a>(broadcast_id) -> None</code>
- <code title="get /streaming/broadcasts/{broadcast_id}">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">get</a>(broadcast_id) -> <a href="./src/gcore/types/streaming/broadcast.py">Broadcast</a></code>
- <code title="get /streaming/broadcasts/{broadcast_id}/spectators">client.streaming.broadcasts.<a href="./src/gcore/resources/streaming/broadcasts.py">get_spectators_count</a>(broadcast_id) -> <a href="./src/gcore/types/streaming/broadcast_spectators_count.py">BroadcastSpectatorsCount</a></code>

## Directories

Types:

```python
from gcore.types.streaming import (
    DirectoriesTree,
    DirectoryBase,
    DirectoryItem,
    DirectoryVideo,
    DirectoryGetResponse,
)
```

Methods:

- <code title="post /streaming/directories">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">create</a>(\*\*<a href="src/gcore/types/streaming/directory_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/directory_base.py">DirectoryBase</a></code>
- <code title="patch /streaming/directories/{directory_id}">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">update</a>(directory_id, \*\*<a href="src/gcore/types/streaming/directory_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/directory_base.py">DirectoryBase</a></code>
- <code title="delete /streaming/directories/{directory_id}">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">delete</a>(directory_id) -> None</code>
- <code title="get /streaming/directories/{directory_id}">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">get</a>(directory_id) -> <a href="./src/gcore/types/streaming/directory_get_response.py">DirectoryGetResponse</a></code>
- <code title="get /streaming/directories/tree">client.streaming.directories.<a href="./src/gcore/resources/streaming/directories.py">get_tree</a>() -> <a href="./src/gcore/types/streaming/directories_tree.py">DirectoriesTree</a></code>

## Players

Types:

```python
from gcore.types.streaming import Player
```

Methods:

- <code title="post /streaming/players">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">create</a>(\*\*<a href="src/gcore/types/streaming/player_create_params.py">params</a>) -> None</code>
- <code title="patch /streaming/players/{player_id}">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">update</a>(player_id, \*\*<a href="src/gcore/types/streaming/player_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/player.py">Player</a></code>
- <code title="get /streaming/players">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">list</a>(\*\*<a href="src/gcore/types/streaming/player_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/player.py">SyncPageStreaming[Player]</a></code>
- <code title="delete /streaming/players/{player_id}">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">delete</a>(player_id) -> None</code>
- <code title="get /streaming/players/{player_id}">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">get</a>(player_id) -> <a href="./src/gcore/types/streaming/player.py">Player</a></code>
- <code title="get /streaming/players/{player_id}/preview">client.streaming.players.<a href="./src/gcore/resources/streaming/players.py">preview</a>(player_id) -> None</code>

## QualitySets

Types:

```python
from gcore.types.streaming import QualitySets
```

Methods:

- <code title="get /streaming/quality_sets">client.streaming.quality_sets.<a href="./src/gcore/resources/streaming/quality_sets.py">list</a>() -> <a href="./src/gcore/types/streaming/quality_sets.py">QualitySets</a></code>
- <code title="put /streaming/quality_sets/default">client.streaming.quality_sets.<a href="./src/gcore/resources/streaming/quality_sets.py">set_default</a>(\*\*<a href="src/gcore/types/streaming/quality_set_set_default_params.py">params</a>) -> <a href="./src/gcore/types/streaming/quality_sets.py">QualitySets</a></code>

## Playlists

Types:

```python
from gcore.types.streaming import (
    Playlist,
    PlaylistCreate,
    PlaylistVideo,
    PlaylistListVideosResponse,
)
```

Methods:

- <code title="post /streaming/playlists">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">create</a>(\*\*<a href="src/gcore/types/streaming/playlist_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/playlist_create.py">PlaylistCreate</a></code>
- <code title="patch /streaming/playlists/{playlist_id}">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">update</a>(playlist_id, \*\*<a href="src/gcore/types/streaming/playlist_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/playlist.py">Playlist</a></code>
- <code title="get /streaming/playlists">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">list</a>(\*\*<a href="src/gcore/types/streaming/playlist_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/playlist.py">SyncPageStreaming[Playlist]</a></code>
- <code title="delete /streaming/playlists/{playlist_id}">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">delete</a>(playlist_id) -> None</code>
- <code title="get /streaming/playlists/{playlist_id}">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">get</a>(playlist_id) -> <a href="./src/gcore/types/streaming/playlist.py">Playlist</a></code>
- <code title="get /streaming/playlists/{playlist_id}/videos">client.streaming.playlists.<a href="./src/gcore/resources/streaming/playlists.py">list_videos</a>(playlist_id) -> <a href="./src/gcore/types/streaming/playlist_list_videos_response.py">PlaylistListVideosResponse</a></code>

## Videos

Types:

```python
from gcore.types.streaming import (
    DirectUploadParameters,
    Subtitle,
    SubtitleBase,
    SubtitleBody,
    SubtitleUpdate,
    VideoCreateResponse,
    VideoCreateMultipleResponse,
)
```

Methods:

- <code title="post /streaming/videos">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">create</a>(\*\*<a href="src/gcore/types/streaming/video_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video_create_response.py">VideoCreateResponse</a></code>
- <code title="patch /streaming/videos/{video_id}">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">update</a>(video_id, \*\*<a href="src/gcore/types/streaming/video_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video.py">Video</a></code>
- <code title="get /streaming/videos">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">list</a>(\*\*<a href="src/gcore/types/streaming/video_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video.py">SyncPageStreaming[Video]</a></code>
- <code title="delete /streaming/videos/{video_id}">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">delete</a>(video_id) -> None</code>
- <code title="post /streaming/videos/batch">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">create_multiple</a>(\*\*<a href="src/gcore/types/streaming/video_create_multiple_params.py">params</a>) -> <a href="./src/gcore/types/streaming/video_create_multiple_response.py">VideoCreateMultipleResponse</a></code>
- <code title="get /streaming/videos/{video_id}">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">get</a>(video_id) -> <a href="./src/gcore/types/streaming/video.py">Video</a></code>
- <code title="get /streaming/videos/{video_id}/upload">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">get_parameters_for_direct_upload</a>(video_id) -> <a href="./src/gcore/types/streaming/direct_upload_parameters.py">DirectUploadParameters</a></code>
- <code title="get /streaming/videos/names">client.streaming.videos.<a href="./src/gcore/resources/streaming/videos/videos.py">list_names</a>(\*\*<a href="src/gcore/types/streaming/video_list_names_params.py">params</a>) -> None</code>

### Subtitles

Types:

```python
from gcore.types.streaming.videos import SubtitleListResponse
```

Methods:

- <code title="post /streaming/videos/{video_id}/subtitles">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">create</a>(video_id, \*\*<a href="src/gcore/types/streaming/videos/subtitle_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/subtitle.py">Subtitle</a></code>
- <code title="patch /streaming/videos/{video_id}/subtitles/{id}">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">update</a>(id, \*, video_id, \*\*<a href="src/gcore/types/streaming/videos/subtitle_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/subtitle_base.py">SubtitleBase</a></code>
- <code title="get /streaming/videos/{video_id}/subtitles">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">list</a>(video_id) -> <a href="./src/gcore/types/streaming/videos/subtitle_list_response.py">SubtitleListResponse</a></code>
- <code title="delete /streaming/videos/{video_id}/subtitles/{id}">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">delete</a>(id, \*, video_id) -> None</code>
- <code title="get /streaming/videos/{video_id}/subtitles/{id}">client.streaming.videos.subtitles.<a href="./src/gcore/resources/streaming/videos/subtitles.py">get</a>(id, \*, video_id) -> <a href="./src/gcore/types/streaming/subtitle.py">Subtitle</a></code>

## Streams

Types:

```python
from gcore.types.streaming import (
    Clip,
    Stream,
    StreamListClipsResponse,
    StreamStartRecordingResponse,
)
```

Methods:

- <code title="post /streaming/streams">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">create</a>(\*\*<a href="src/gcore/types/streaming/stream_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream.py">Stream</a></code>
- <code title="patch /streaming/streams/{stream_id}">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">update</a>(stream_id, \*\*<a href="src/gcore/types/streaming/stream_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream.py">Stream</a></code>
- <code title="get /streaming/streams">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">list</a>(\*\*<a href="src/gcore/types/streaming/stream_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream.py">SyncPageStreaming[Stream]</a></code>
- <code title="delete /streaming/streams/{stream_id}">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">delete</a>(stream_id) -> None</code>
- <code title="put /streaming/streams/{stream_id}/dvr_cleanup">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">clear_dvr</a>(stream_id) -> None</code>
- <code title="put /streaming/streams/{stream_id}/clip_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">create_clip</a>(stream_id, \*\*<a href="src/gcore/types/streaming/stream_create_clip_params.py">params</a>) -> <a href="./src/gcore/types/streaming/clip.py">Clip</a></code>
- <code title="get /streaming/streams/{stream_id}">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">get</a>(stream_id) -> <a href="./src/gcore/types/streaming/stream.py">Stream</a></code>
- <code title="get /streaming/streams/{stream_id}/clip_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">list_clips</a>(stream_id) -> <a href="./src/gcore/types/streaming/stream_list_clips_response.py">StreamListClipsResponse</a></code>
- <code title="put /streaming/streams/{stream_id}/start_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">start_recording</a>(stream_id) -> <a href="./src/gcore/types/streaming/stream_start_recording_response.py">StreamStartRecordingResponse</a></code>
- <code title="put /streaming/streams/{stream_id}/stop_recording">client.streaming.streams.<a href="./src/gcore/resources/streaming/streams/streams.py">stop_recording</a>(stream_id) -> <a href="./src/gcore/types/streaming/video.py">Video</a></code>

### Overlays

Types:

```python
from gcore.types.streaming.streams import (
    Overlay,
    OverlayCreateResponse,
    OverlayListResponse,
    OverlayUpdateMultipleResponse,
)
```

Methods:

- <code title="post /streaming/streams/{stream_id}/overlays">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">create</a>(stream_id, \*\*<a href="src/gcore/types/streaming/streams/overlay_create_params.py">params</a>) -> <a href="./src/gcore/types/streaming/streams/overlay_create_response.py">OverlayCreateResponse</a></code>
- <code title="patch /streaming/streams/{stream_id}/overlays/{overlay_id}">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">update</a>(overlay_id, \*, stream_id, \*\*<a href="src/gcore/types/streaming/streams/overlay_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/streams/overlay.py">Overlay</a></code>
- <code title="get /streaming/streams/{stream_id}/overlays">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">list</a>(stream_id) -> <a href="./src/gcore/types/streaming/streams/overlay_list_response.py">OverlayListResponse</a></code>
- <code title="delete /streaming/streams/{stream_id}/overlays/{overlay_id}">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">delete</a>(overlay_id, \*, stream_id) -> None</code>
- <code title="get /streaming/streams/{stream_id}/overlays/{overlay_id}">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">get</a>(overlay_id, \*, stream_id) -> <a href="./src/gcore/types/streaming/streams/overlay.py">Overlay</a></code>
- <code title="patch /streaming/streams/{stream_id}/overlays">client.streaming.streams.overlays.<a href="./src/gcore/resources/streaming/streams/overlays.py">update_multiple</a>(stream_id, \*\*<a href="src/gcore/types/streaming/streams/overlay_update_multiple_params.py">params</a>) -> <a href="./src/gcore/types/streaming/streams/overlay_update_multiple_response.py">OverlayUpdateMultipleResponse</a></code>

## Restreams

Types:

```python
from gcore.types.streaming import Restream
```

Methods:

- <code title="post /streaming/restreams">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">create</a>(\*\*<a href="src/gcore/types/streaming/restream_create_params.py">params</a>) -> None</code>
- <code title="patch /streaming/restreams/{restream_id}">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">update</a>(restream_id, \*\*<a href="src/gcore/types/streaming/restream_update_params.py">params</a>) -> <a href="./src/gcore/types/streaming/restream.py">Restream</a></code>
- <code title="get /streaming/restreams">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">list</a>(\*\*<a href="src/gcore/types/streaming/restream_list_params.py">params</a>) -> <a href="./src/gcore/types/streaming/restream.py">SyncPageStreaming[Restream]</a></code>
- <code title="delete /streaming/restreams/{restream_id}">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">delete</a>(restream_id) -> None</code>
- <code title="get /streaming/restreams/{restream_id}">client.streaming.restreams.<a href="./src/gcore/resources/streaming/restreams.py">get</a>(restream_id) -> <a href="./src/gcore/types/streaming/restream.py">Restream</a></code>

## Statistics

Types:

```python
from gcore.types.streaming import (
    Ffprobes,
    MaxStreamSeries,
    MeetSeries,
    PopularVideos,
    StorageSeries,
    StreamSeries,
    UniqueViewers,
    UniqueViewersCdn,
    Views,
    ViewsByBrowser,
    ViewsByCountry,
    ViewsByHostname,
    ViewsByOperatingSystem,
    ViewsByReferer,
    ViewsByRegion,
    ViewsHeatmap,
    VodStatisticsSeries,
    VodTotalStreamDurationSeries,
    StatisticGetLiveUniqueViewersResponse,
    StatisticGetVodWatchTimeTotalCdnResponse,
)
```

Methods:

- <code title="get /streaming/statistics/ffprobe">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_ffprobes</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_ffprobes_params.py">params</a>) -> <a href="./src/gcore/types/streaming/ffprobes.py">Ffprobes</a></code>
- <code title="get /streaming/statistics/stream/viewers">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_live_unique_viewers</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_live_unique_viewers_params.py">params</a>) -> <a href="./src/gcore/types/streaming/statistic_get_live_unique_viewers_response.py">StatisticGetLiveUniqueViewersResponse</a></code>
- <code title="get /streaming/statistics/stream/watching_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_live_watch_time_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_live_watch_time_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream_series.py">StreamSeries</a></code>
- <code title="get /streaming/statistics/stream/watching_duration/total">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_live_watch_time_total_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_live_watch_time_total_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_total_stream_duration_series.py">VodTotalStreamDurationSeries</a></code>
- <code title="get /streaming/statistics/max_stream">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_max_streams_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_max_streams_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/max_stream_series.py">MaxStreamSeries</a></code>
- <code title="get /streaming/statistics/meet">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_meet_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_meet_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/meet_series.py">MeetSeries</a></code>
- <code title="get /streaming/statistics/popular">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_popular_videos</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_popular_videos_params.py">params</a>) -> <a href="./src/gcore/types/streaming/popular_videos.py">PopularVideos</a></code>
- <code title="get /streaming/statistics/storage">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_storage_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_storage_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/storage_series.py">StorageSeries</a></code>
- <code title="get /streaming/statistics/stream">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_stream_series</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_stream_series_params.py">params</a>) -> <a href="./src/gcore/types/streaming/stream_series.py">StreamSeries</a></code>
- <code title="get /streaming/statistics/uniqs">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_unique_viewers</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_unique_viewers_params.py">params</a>) -> <a href="./src/gcore/types/streaming/unique_viewers.py">UniqueViewers</a></code>
- <code title="get /streaming/statistics/cdn/uniqs">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_unique_viewers_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_unique_viewers_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/unique_viewers_cdn.py">UniqueViewersCdn</a></code>
- <code title="get /streaming/statistics/views">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views.py">Views</a></code>
- <code title="get /streaming/statistics/browsers">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_browsers</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_browsers_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_browser.py">ViewsByBrowser</a></code>
- <code title="get /streaming/statistics/countries">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_country</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_country_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_country.py">ViewsByCountry</a></code>
- <code title="get /streaming/statistics/hosts">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_hostname</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_hostname_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_hostname.py">ViewsByHostname</a></code>
- <code title="get /streaming/statistics/systems">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_operating_system</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_operating_system_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_operating_system.py">ViewsByOperatingSystem</a></code>
- <code title="get /streaming/statistics/embeds">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_referer</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_referer_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_referer.py">ViewsByReferer</a></code>
- <code title="get /streaming/statistics/regions">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_by_region</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_by_region_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_by_region.py">ViewsByRegion</a></code>
- <code title="get /streaming/statistics/heatmap">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_views_heatmap</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_views_heatmap_params.py">params</a>) -> <a href="./src/gcore/types/streaming/views_heatmap.py">ViewsHeatmap</a></code>
- <code title="get /streaming/statistics/vod/storage_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_storage_volume</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_storage_volume_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/transcoding_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_transcoding_duration</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_transcoding_duration_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/viewers">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_unique_viewers_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_unique_viewers_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/watching_duration">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_watch_time_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_watch_time_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/vod_statistics_series.py">VodStatisticsSeries</a></code>
- <code title="get /streaming/statistics/vod/watching_duration/total">client.streaming.statistics.<a href="./src/gcore/resources/streaming/statistics.py">get_vod_watch_time_total_cdn</a>(\*\*<a href="src/gcore/types/streaming/statistic_get_vod_watch_time_total_cdn_params.py">params</a>) -> <a href="./src/gcore/types/streaming/statistic_get_vod_watch_time_total_cdn_response.py">StatisticGetVodWatchTimeTotalCdnResponse</a></code>

# Security

## Events

Types:

```python
from gcore.types.security import ClientView
```

Methods:

- <code title="get /security/notifier/v1/event_logs">client.security.events.<a href="./src/gcore/resources/security/events.py">list</a>(\*\*<a href="src/gcore/types/security/event_list_params.py">params</a>) -> <a href="./src/gcore/types/security/client_view.py">SyncOffsetPage[ClientView]</a></code>

## BgpAnnounces

Types:

```python
from gcore.types.security import ClientAnnounce, BgpAnnounceListResponse
```

Methods:

- <code title="get /security/sifter/v2/protected_addresses/announces">client.security.bgp_announces.<a href="./src/gcore/resources/security/bgp_announces.py">list</a>(\*\*<a href="src/gcore/types/security/bgp_announce_list_params.py">params</a>) -> <a href="./src/gcore/types/security/bgp_announce_list_response.py">BgpAnnounceListResponse</a></code>
- <code title="post /security/sifter/v2/protected_addresses/announces">client.security.bgp_announces.<a href="./src/gcore/resources/security/bgp_announces.py">toggle</a>(\*\*<a href="src/gcore/types/security/bgp_announce_toggle_params.py">params</a>) -> object</code>

## ProfileTemplates

Types:

```python
from gcore.types.security import ClientProfileTemplate, ProfileTemplateListResponse
```

Methods:

- <code title="get /security/iaas/profile-templates">client.security.profile_templates.<a href="./src/gcore/resources/security/profile_templates.py">list</a>() -> <a href="./src/gcore/types/security/profile_template_list_response.py">ProfileTemplateListResponse</a></code>

## Profiles

Types:

```python
from gcore.types.security import ClientProfile, ProfileListResponse
```

Methods:

- <code title="post /security/iaas/v2/profiles">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">create</a>(\*\*<a href="src/gcore/types/security/profile_create_params.py">params</a>) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
- <code title="get /security/iaas/v2/profiles">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">list</a>(\*\*<a href="src/gcore/types/security/profile_list_params.py">params</a>) -> <a href="./src/gcore/types/security/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /security/iaas/v2/profiles/{id}">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">delete</a>(id) -> None</code>
- <code title="get /security/iaas/v2/profiles/{id}">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">get</a>(id) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
- <code title="put /security/iaas/v2/profiles/{id}/recreate">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">recreate</a>(id, \*\*<a href="src/gcore/types/security/profile_recreate_params.py">params</a>) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
- <code title="put /security/iaas/v2/profiles/{id}">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">replace</a>(id, \*\*<a href="src/gcore/types/security/profile_replace_params.py">params</a>) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
