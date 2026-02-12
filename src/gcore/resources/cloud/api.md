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
- <code title="patch /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">update</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/project_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="get /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">list</a>(\*\*<a href="src/gcore/types/cloud/project_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">SyncOffsetPage[Project]</a></code>
- <code title="delete /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">delete</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">get</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>

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
- <code title="patch /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">update</a>(load_balancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer.py">LoadBalancer</a></code>
- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer.py">SyncOffsetPage[LoadBalancer]</a></code>
- <code title="delete /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">delete</a>(load_balancer_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}/failover">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">failover</a>(load_balancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_failover_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">get</a>(load_balancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer.py">LoadBalancer</a></code>
- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}/resize">client.cloud.load_balancers.<a href="./src/gcore/resources/cloud/load_balancers/load_balancers.py">resize</a>(load_balancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancer_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### L7Policies

Methods:

- <code title="post /cloud/v1/l7policies/{project_id}/{region_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/l7_policy_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">update</a>(l7policy_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/l7_policy_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/l7policies/{project_id}/{region_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_l7_policy_list.py">LoadBalancerL7PolicyList</a></code>
- <code title="delete /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">delete</a>(l7policy_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}">client.cloud.load_balancers.l7_policies.<a href="./src/gcore/resources/cloud/load_balancers/l7_policies/l7_policies.py">get</a>(l7policy_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_l7_policy.py">LoadBalancerL7Policy</a></code>

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
- <code title="delete /cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">delete</a>(listener_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/listener_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}">client.cloud.load_balancers.listeners.<a href="./src/gcore/resources/cloud/load_balancers/listeners.py">get</a>(listener_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/listener_get_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_listener_detail.py">LoadBalancerListenerDetail</a></code>

### Pools

Methods:

- <code title="post /cloud/v1/lbpools/{project_id}/{region_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pool_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v2/lbpools/{project_id}/{region_id}/{pool_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">update</a>(pool_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lbpools/{project_id}/{region_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pool_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_pool_list.py">LoadBalancerPoolList</a></code>
- <code title="delete /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">delete</a>(pool_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}">client.cloud.load_balancers.pools.<a href="./src/gcore/resources/cloud/load_balancers/pools/pools.py">get</a>(pool_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_pool.py">LoadBalancerPool</a></code>

#### HealthMonitors

Methods:

- <code title="post /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor">client.cloud.load_balancers.pools.health_monitors.<a href="./src/gcore/resources/cloud/load_balancers/pools/health_monitors.py">create</a>(pool_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pools/health_monitor_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="delete /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor">client.cloud.load_balancers.pools.health_monitors.<a href="./src/gcore/resources/cloud/load_balancers/pools/health_monitors.py">delete</a>(pool_id, \*, project_id, region_id) -> None</code>

#### Members

Methods:

- <code title="post /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member">client.cloud.load_balancers.pools.members.<a href="./src/gcore/resources/cloud/load_balancers/pools/members.py">create</a>(pool_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/pools/member_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="delete /cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/member/{member_id}">client.cloud.load_balancers.pools.members.<a href="./src/gcore/resources/cloud/load_balancers/pools/members.py">delete</a>(member_id, \*, project_id, region_id, pool_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

### Metrics

Methods:

- <code title="post /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}/metrics">client.cloud.load_balancers.metrics.<a href="./src/gcore/resources/cloud/load_balancers/metrics.py">list</a>(load_balancer_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/load_balancers/metric_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/load_balancer_metrics_list.py">LoadBalancerMetricsList</a></code>

### Statuses

Methods:

- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}/status">client.cloud.load_balancers.statuses.<a href="./src/gcore/resources/cloud/load_balancers/statuses.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_status_list.py">LoadBalancerStatusList</a></code>
- <code title="get /cloud/v1/loadbalancers/{project_id}/{region_id}/{load_balancer_id}/status">client.cloud.load_balancers.statuses.<a href="./src/gcore/resources/cloud/load_balancers/statuses.py">get</a>(load_balancer_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/load_balancer_status.py">LoadBalancerStatus</a></code>

## ReservedFixedIPs

Types:

```python
from gcore.types.cloud import ReservedFixedIP
```

Methods:

- <code title="post /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ip_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">update</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ip_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">ReservedFixedIP</a></code>
- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ip_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">SyncOffsetPage[ReservedFixedIP]</a></code>
- <code title="delete /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">delete</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/reserved_fixed_ips.py">get</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">ReservedFixedIP</a></code>

### Vip

Types:

```python
from gcore.types.cloud.reserved_fixed_ips import IPWithSubnet
```

Methods:

- <code title="patch /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}">client.cloud.reserved_fixed_ips.vip.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip/vip.py">toggle</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ips/vip_toggle_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ip.py">ReservedFixedIP</a></code>

#### CandidatePorts

Types:

```python
from gcore.types.cloud.reserved_fixed_ips.vip import CandidatePort, CandidatePortList
```

Methods:

- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/available_devices">client.cloud.reserved_fixed_ips.vip.candidate_ports.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip/candidate_ports.py">list</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/vip/candidate_port_list.py">CandidatePortList</a></code>

#### ConnectedPorts

Types:

```python
from gcore.types.cloud.reserved_fixed_ips.vip import ConnectedPort, ConnectedPortList
```

Methods:

- <code title="get /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices">client.cloud.reserved_fixed_ips.vip.connected_ports.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip/connected_ports.py">list</a>(port_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/vip/connected_port_list.py">ConnectedPortList</a></code>
- <code title="patch /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices">client.cloud.reserved_fixed_ips.vip.connected_ports.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip/connected_ports.py">add</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ips/vip/connected_port_add_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/vip/connected_port_list.py">ConnectedPortList</a></code>
- <code title="put /cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices">client.cloud.reserved_fixed_ips.vip.connected_ports.<a href="./src/gcore/resources/cloud/reserved_fixed_ips/vip/connected_ports.py">replace</a>(port_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/reserved_fixed_ips/vip/connected_port_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/reserved_fixed_ips/vip/connected_port_list.py">ConnectedPortList</a></code>

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
- <code title="delete /cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}">client.cloud.networks.subnets.<a href="./src/gcore/resources/cloud/networks/subnets.py">delete</a>(subnet_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
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
- <code title="patch /cloud/v2/floatingips/{project_id}/{region_id}/{floating_ip_id}">client.cloud.floating_ips.<a href="./src/gcore/resources/cloud/floating_ips.py">update</a>(floating_ip_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/floating_ip_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
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

- <code title="post /cloud/v2/security_groups/{project_id}/{region_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v2/security_groups/{project_id}/{region_id}/{group_id}">client.cloud.security_groups.<a href="./src/gcore/resources/cloud/security_groups/security_groups.py">update</a>(group_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/security_group_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
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
from gcore.types.cloud.users import RoleAssignment, RoleAssignmentUpdatedDeleted
```

Methods:

- <code title="post /cloud/v1/users/assignments">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">create</a>(\*\*<a href="src/gcore/types/cloud/users/role_assignment_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/users/role_assignment.py">RoleAssignment</a></code>
- <code title="patch /cloud/v1/users/assignments/{assignment_id}">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">update</a>(assignment_id, \*\*<a href="src/gcore/types/cloud/users/role_assignment_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/users/role_assignment_updated_deleted.py">RoleAssignmentUpdatedDeleted</a></code>
- <code title="get /cloud/v1/users/assignments">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">list</a>(\*\*<a href="src/gcore/types/cloud/users/role_assignment_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/users/role_assignment.py">SyncOffsetPage[RoleAssignment]</a></code>
- <code title="delete /cloud/v1/users/assignments/{assignment_id}">client.cloud.users.role_assignments.<a href="./src/gcore/resources/cloud/users/role_assignments.py">delete</a>(assignment_id) -> <a href="./src/gcore/types/cloud/users/role_assignment_updated_deleted.py">RoleAssignmentUpdatedDeleted</a></code>

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
from gcore.types.cloud.inference import InferenceRegistryCredentials
```

Methods:

- <code title="post /cloud/v3/inference/{project_id}/registry_credentials">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials.py">InferenceRegistryCredentials</a></code>
- <code title="get /cloud/v3/inference/{project_id}/registry_credentials">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials.py">SyncOffsetPage[InferenceRegistryCredentials]</a></code>
- <code title="delete /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">delete</a>(credential_name, \*, project_id) -> None</code>
- <code title="get /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">get</a>(credential_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials.py">InferenceRegistryCredentials</a></code>
- <code title="put /cloud/v3/inference/{project_id}/registry_credentials/{credential_name}">client.cloud.inference.registry_credentials.<a href="./src/gcore/resources/cloud/inference/registry_credentials.py">replace</a>(credential_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/registry_credential_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_registry_credentials.py">InferenceRegistryCredentials</a></code>

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
from gcore.types.cloud.inference import InferenceAPIKey, InferenceAPIKeyCreated
```

Methods:

- <code title="post /cloud/v3/inference/{project_id}/api_keys">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/api_key_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_api_key_created.py">InferenceAPIKeyCreated</a></code>
- <code title="patch /cloud/v3/inference/{project_id}/api_keys/{api_key_name}">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">update</a>(api_key_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/api_key_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_api_key.py">InferenceAPIKey</a></code>
- <code title="get /cloud/v3/inference/{project_id}/api_keys">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">list</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/api_key_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/inference/inference_api_key.py">SyncOffsetPage[InferenceAPIKey]</a></code>
- <code title="delete /cloud/v3/inference/{project_id}/api_keys/{api_key_name}">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">delete</a>(api_key_name, \*, project_id) -> None</code>
- <code title="get /cloud/v3/inference/{project_id}/api_keys/{api_key_name}">client.cloud.inference.api_keys.<a href="./src/gcore/resources/cloud/inference/api_keys.py">get</a>(api_key_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/inference_api_key.py">InferenceAPIKey</a></code>

### Applications

#### Deployments

Types:

```python
from gcore.types.cloud.inference.applications import (
    InferenceApplicationDeployment,
    InferenceApplicationDeploymentList,
)
```

Methods:

- <code title="post /cloud/v3/inference/applications/{project_id}/deployments">client.cloud.inference.applications.deployments.<a href="./src/gcore/resources/cloud/inference/applications/deployments.py">create</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/inference/applications/deployment_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}">client.cloud.inference.applications.deployments.<a href="./src/gcore/resources/cloud/inference/applications/deployments.py">update</a>(deployment_name, \*, project_id, \*\*<a href="src/gcore/types/cloud/inference/applications/deployment_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/inference/applications/{project_id}/deployments">client.cloud.inference.applications.deployments.<a href="./src/gcore/resources/cloud/inference/applications/deployments.py">list</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/inference/applications/inference_application_deployment_list.py">InferenceApplicationDeploymentList</a></code>
- <code title="delete /cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}">client.cloud.inference.applications.deployments.<a href="./src/gcore/resources/cloud/inference/applications/deployments.py">delete</a>(deployment_name, \*, project_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}">client.cloud.inference.applications.deployments.<a href="./src/gcore/resources/cloud/inference/applications/deployments.py">get</a>(deployment_name, \*, project_id) -> <a href="./src/gcore/types/cloud/inference/applications/inference_application_deployment.py">InferenceApplicationDeployment</a></code>

#### Templates

Types:

```python
from gcore.types.cloud.inference.applications import (
    InferenceApplicationTemplate,
    InferenceApplicationTemplateList,
)
```

Methods:

- <code title="get /cloud/v3/inference/applications/catalog">client.cloud.inference.applications.templates.<a href="./src/gcore/resources/cloud/inference/applications/templates.py">list</a>() -> <a href="./src/gcore/types/cloud/inference/applications/inference_application_template_list.py">InferenceApplicationTemplateList</a></code>
- <code title="get /cloud/v3/inference/applications/catalog/{application_name}">client.cloud.inference.applications.templates.<a href="./src/gcore/resources/cloud/inference/applications/templates.py">get</a>(application_name) -> <a href="./src/gcore/types/cloud/inference/applications/inference_application_template.py">InferenceApplicationTemplate</a></code>

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
- <code title="patch /cloud/v3/file_shares/{project_id}/{region_id}/{file_share_id}">client.cloud.file_shares.<a href="./src/gcore/resources/cloud/file_shares/file_shares.py">update</a>(file_share_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/file_share_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
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
from gcore.types.cloud import BillingReservation, BillingReservations
```

Methods:

- <code title="get /cloud/v2/reservations">client.cloud.billing_reservations.<a href="./src/gcore/resources/cloud/billing_reservations.py">list</a>(\*\*<a href="src/gcore/types/cloud/billing_reservation_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/billing_reservations.py">BillingReservations</a></code>

## GPUBaremetal

### Clusters

Types:

```python
from gcore.types.cloud.gpu_baremetal import GPUBaremetalCluster
```

Methods:

- <code title="post /cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/cluster_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/cluster_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_baremetal/gpu_baremetal_cluster.py">SyncOffsetPage[GPUBaremetalCluster]</a></code>
- <code title="delete /cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">delete</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/cluster_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}/action">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">action</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/cluster_action_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">get</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal/gpu_baremetal_cluster.py">GPUBaremetalCluster</a></code>
- <code title="post /cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/powercycle">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">powercycle_all_servers</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal/clusters/gpu_baremetal_cluster_server_v1_list.py">GPUBaremetalClusterServerV1List</a></code>
- <code title="post /cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}/reboot">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">reboot_all_servers</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal/clusters/gpu_baremetal_cluster_server_v1_list.py">GPUBaremetalClusterServerV1List</a></code>
- <code title="post /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">rebuild</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/cluster_rebuild_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize">client.cloud.gpu_baremetal.clusters.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/clusters.py">resize</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/cluster_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

#### Interfaces

Methods:

- <code title="get /cloud/v1/ai/clusters/{project_id}/{region_id}/{cluster_id}/interfaces">client.cloud.gpu_baremetal.clusters.interfaces.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/interfaces.py">list</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/network_interface_list.py">NetworkInterfaceList</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/attach_interface">client.cloud.gpu_baremetal.clusters.interfaces.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/interfaces.py">attach</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/clusters/interface_attach_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/detach_interface">client.cloud.gpu_baremetal.clusters.interfaces.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/interfaces.py">detach</a>(instance_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/clusters/interface_detach_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

#### Servers

Types:

```python
from gcore.types.cloud.gpu_baremetal.clusters import (
    GPUBaremetalClusterServer,
    GPUBaremetalClusterServerV1,
    GPUBaremetalClusterServerV1List,
)
```

Methods:

- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/clusters/{cluster_id}/servers">client.cloud.gpu_baremetal.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/servers.py">list</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/clusters/server_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_baremetal/clusters/gpu_baremetal_cluster_server.py">SyncOffsetPage[GPUBaremetalClusterServer]</a></code>
- <code title="delete /cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}">client.cloud.gpu_baremetal.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/servers.py">delete</a>(instance_id, \*, project_id, region_id, cluster_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/clusters/server_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/get_console">client.cloud.gpu_baremetal.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/servers.py">get_console</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/console.py">Console</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/powercycle">client.cloud.gpu_baremetal.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/servers.py">powercycle</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal/clusters/gpu_baremetal_cluster_server_v1.py">GPUBaremetalClusterServerV1</a></code>
- <code title="post /cloud/v1/ai/clusters/{project_id}/{region_id}/{instance_id}/reboot">client.cloud.gpu_baremetal.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/servers.py">reboot</a>(instance_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_baremetal/clusters/gpu_baremetal_cluster_server_v1.py">GPUBaremetalClusterServerV1</a></code>

#### Flavors

Types:

```python
from gcore.types.cloud.gpu_baremetal.clusters import GPUBaremetalFlavor, GPUBaremetalFlavorList
```

Methods:

- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/flavors">client.cloud.gpu_baremetal.clusters.flavors.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/clusters/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_baremetal/clusters/gpu_baremetal_flavor_list.py">GPUBaremetalFlavorList</a></code>

#### Images

Methods:

- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images">client.cloud.gpu_baremetal.clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/images.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_image_list.py">GPUImageList</a></code>
- <code title="delete /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}">client.cloud.gpu_baremetal.clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/images.py">delete</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}">client.cloud.gpu_baremetal.clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/images.py">get</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_image.py">GPUImage</a></code>
- <code title="post /cloud/v3/gpu/baremetal/{project_id}/{region_id}/images">client.cloud.gpu_baremetal.clusters.images.<a href="./src/gcore/resources/cloud/gpu_baremetal/clusters/images.py">upload</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_baremetal/clusters/image_upload_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

## GPUVirtual

### Clusters

Types:

```python
from gcore.types.cloud.gpu_virtual import GPUVirtualCluster
```

Methods:

- <code title="post /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters">client.cloud.gpu_virtual.clusters.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/clusters.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/cluster_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}">client.cloud.gpu_virtual.clusters.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/clusters.py">update</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/cluster_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_virtual/gpu_virtual_cluster.py">GPUVirtualCluster</a></code>
- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters">client.cloud.gpu_virtual.clusters.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/clusters.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/cluster_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_virtual/gpu_virtual_cluster.py">SyncOffsetPage[GPUVirtualCluster]</a></code>
- <code title="delete /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}">client.cloud.gpu_virtual.clusters.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/clusters.py">delete</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/cluster_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/action">client.cloud.gpu_virtual.clusters.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/clusters.py">action</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/cluster_action_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}">client.cloud.gpu_virtual.clusters.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/clusters.py">get</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_virtual/gpu_virtual_cluster.py">GPUVirtualCluster</a></code>

#### Servers

Types:

```python
from gcore.types.cloud.gpu_virtual.clusters import (
    GPUVirtualClusterServer,
    GPUVirtualClusterServerList,
)
```

Methods:

- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/servers">client.cloud.gpu_virtual.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/servers.py">list</a>(cluster_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/clusters/server_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_virtual/clusters/gpu_virtual_cluster_server_list.py">GPUVirtualClusterServerList</a></code>
- <code title="delete /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/servers/{server_id}">client.cloud.gpu_virtual.clusters.servers.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/servers.py">delete</a>(server_id, \*, project_id, region_id, cluster_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/clusters/server_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

#### Volumes

Types:

```python
from gcore.types.cloud.gpu_virtual.clusters import (
    GPUVirtualClusterVolume,
    GPUVirtualClusterVolumeList,
)
```

Methods:

- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/volumes">client.cloud.gpu_virtual.clusters.volumes.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/volumes.py">list</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_virtual/clusters/gpu_virtual_cluster_volume_list.py">GPUVirtualClusterVolumeList</a></code>

#### Interfaces

Types:

```python
from gcore.types.cloud.gpu_virtual.clusters import GPUVirtualInterface, GPUVirtualInterfaceList
```

Methods:

- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/interfaces">client.cloud.gpu_virtual.clusters.interfaces.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/interfaces.py">list</a>(cluster_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_virtual/clusters/gpu_virtual_interface_list.py">GPUVirtualInterfaceList</a></code>

#### Flavors

Types:

```python
from gcore.types.cloud.gpu_virtual.clusters import GPUVirtualFlavor, GPUVirtualFlavorList
```

Methods:

- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/flavors">client.cloud.gpu_virtual.clusters.flavors.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/clusters/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/gpu_virtual/clusters/gpu_virtual_flavor_list.py">GPUVirtualFlavorList</a></code>

#### Images

Methods:

- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/images">client.cloud.gpu_virtual.clusters.images.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/images.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_image_list.py">GPUImageList</a></code>
- <code title="delete /cloud/v3/gpu/virtual/{project_id}/{region_id}/images/{image_id}">client.cloud.gpu_virtual.clusters.images.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/images.py">delete</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v3/gpu/virtual/{project_id}/{region_id}/images/{image_id}">client.cloud.gpu_virtual.clusters.images.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/images.py">get</a>(image_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/gpu_image.py">GPUImage</a></code>
- <code title="post /cloud/v3/gpu/virtual/{project_id}/{region_id}/images">client.cloud.gpu_virtual.clusters.images.<a href="./src/gcore/resources/cloud/gpu_virtual/clusters/images.py">upload</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/gpu_virtual/clusters/image_upload_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

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
from gcore.types.cloud.instances import InstanceFlavorDetailed, InstanceFlavorList
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

## K8S

Types:

```python
from gcore.types.cloud import K8SClusterVersion, K8SClusterVersionList
```

Methods:

- <code title="get /cloud/v2/k8s/{project_id}/{region_id}/create_versions">client.cloud.k8s.<a href="./src/gcore/resources/cloud/k8s/k8s.py">list_versions</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s_cluster_version_list.py">K8SClusterVersionList</a></code>

### Flavors

Methods:

- <code title="get /cloud/v1/k8s/{project_id}/{region_id}/flavors">client.cloud.k8s.flavors.<a href="./src/gcore/resources/cloud/k8s/flavors.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/flavor_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/baremetal_flavor_list.py">BaremetalFlavorList</a></code>

### Clusters

Types:

```python
from gcore.types.cloud.k8s import (
    K8SCluster,
    K8SClusterCertificate,
    K8SClusterKubeconfig,
    K8SClusterList,
)
```

Methods:

- <code title="post /cloud/v2/k8s/clusters/{project_id}/{region_id}">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/cluster_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">update</a>(cluster_name, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/cluster_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">list</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s/k8s_cluster_list.py">K8SClusterList</a></code>
- <code title="delete /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">delete</a>(cluster_name, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/cluster_delete_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">get</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s/k8s_cluster.py">K8SCluster</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/certificates">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">get_certificate</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s/k8s_cluster_certificate.py">K8SClusterCertificate</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/config">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">get_kubeconfig</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s/k8s_cluster_kubeconfig.py">K8SClusterKubeconfig</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/upgrade_versions">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">list_versions_for_upgrade</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s_cluster_version_list.py">K8SClusterVersionList</a></code>
- <code title="post /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/upgrade">client.cloud.k8s.clusters.<a href="./src/gcore/resources/cloud/k8s/clusters/clusters.py">upgrade</a>(cluster_name, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/cluster_upgrade_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

#### Nodes

Methods:

- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/instances">client.cloud.k8s.clusters.nodes.<a href="./src/gcore/resources/cloud/k8s/clusters/nodes.py">list</a>(cluster_name, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/clusters/node_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/instance_list.py">InstanceList</a></code>
- <code title="delete /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/instances/{instance_id}">client.cloud.k8s.clusters.nodes.<a href="./src/gcore/resources/cloud/k8s/clusters/nodes.py">delete</a>(instance_id, \*, project_id, region_id, cluster_name) -> None</code>

#### Pools

Types:

```python
from gcore.types.cloud.k8s.clusters import K8SClusterPool, K8SClusterPoolList, K8SClusterPoolQuota
```

Methods:

- <code title="post /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">create</a>(cluster_name, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/clusters/pool_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">update</a>(pool_name, \*, project_id, region_id, cluster_name, \*\*<a href="src/gcore/types/cloud/k8s/clusters/pool_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/k8s/clusters/k8s_cluster_pool.py">K8SClusterPool</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">list</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/k8s/clusters/k8s_cluster_pool_list.py">K8SClusterPoolList</a></code>
- <code title="delete /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">delete</a>(pool_name, \*, project_id, region_id, cluster_name) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="post /cloud/v2/k8s/clusters/{project_id}/{region_id}/pools/check_limits">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">check_quota</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/k8s/clusters/pool_check_quota_params.py">params</a>) -> <a href="./src/gcore/types/cloud/k8s/clusters/k8s_cluster_pool_quota.py">K8SClusterPoolQuota</a></code>
- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">get</a>(pool_name, \*, project_id, region_id, cluster_name) -> <a href="./src/gcore/types/cloud/k8s/clusters/k8s_cluster_pool.py">K8SClusterPool</a></code>
- <code title="post /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}/resize">client.cloud.k8s.clusters.pools.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/pools.py">resize</a>(pool_name, \*, project_id, region_id, cluster_name, \*\*<a href="src/gcore/types/cloud/k8s/clusters/pool_resize_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>

##### Nodes

Methods:

- <code title="get /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}/instances">client.cloud.k8s.clusters.pools.nodes.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/nodes.py">list</a>(pool_name, \*, project_id, region_id, cluster_name, \*\*<a href="src/gcore/types/cloud/k8s/clusters/pools/node_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/instance_list.py">InstanceList</a></code>
- <code title="delete /cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/pools/{pool_name}/instances/{instance_id}">client.cloud.k8s.clusters.pools.nodes.<a href="./src/gcore/resources/cloud/k8s/clusters/pools/nodes.py">delete</a>(instance_id, \*, project_id, region_id, cluster_name, pool_name) -> None</code>

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

## Databases

### Postgres

#### Clusters

Types:

```python
from gcore.types.cloud.databases.postgres import PostgresCluster, PostgresClusterShort
```

Methods:

- <code title="post /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}">client.cloud.databases.postgres.clusters.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/clusters.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/databases/postgres/cluster_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}">client.cloud.databases.postgres.clusters.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/clusters.py">update</a>(cluster_name, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/databases/postgres/cluster_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}">client.cloud.databases.postgres.clusters.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/clusters.py">list</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/databases/postgres/cluster_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/databases/postgres/postgres_cluster_short.py">SyncOffsetPage[PostgresClusterShort]</a></code>
- <code title="delete /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}">client.cloud.databases.postgres.clusters.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/clusters.py">delete</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}">client.cloud.databases.postgres.clusters.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/clusters.py">get</a>(cluster_name, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/databases/postgres/postgres_cluster.py">PostgresCluster</a></code>

##### UserCredentials

Types:

```python
from gcore.types.cloud.databases.postgres.clusters import PostgresUserCredentials
```

Methods:

- <code title="get /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}/users/{username}/credentials">client.cloud.databases.postgres.clusters.user_credentials.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/user_credentials.py">get</a>(username, \*, project_id, region_id, cluster_name) -> <a href="./src/gcore/types/cloud/databases/postgres/clusters/postgres_user_credentials.py">PostgresUserCredentials</a></code>
- <code title="post /cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}/users/{username}/credentials">client.cloud.databases.postgres.clusters.user_credentials.<a href="./src/gcore/resources/cloud/databases/postgres/clusters/user_credentials.py">regenerate</a>(username, \*, project_id, region_id, cluster_name) -> <a href="./src/gcore/types/cloud/databases/postgres/clusters/postgres_user_credentials.py">PostgresUserCredentials</a></code>

#### Configurations

Types:

```python
from gcore.types.cloud.databases.postgres import PostgresConfiguration
```

Methods:

- <code title="get /cloud/v1/dbaas/postgres/configuration/{project_id}/{region_id}">client.cloud.databases.postgres.configurations.<a href="./src/gcore/resources/cloud/databases/postgres/configurations.py">get</a>(\*, project_id, region_id) -> <a href="./src/gcore/types/cloud/databases/postgres/postgres_configuration.py">PostgresConfiguration</a></code>

#### CustomConfigurations

Types:

```python
from gcore.types.cloud.databases.postgres import PgConfValidation
```

Methods:

- <code title="post /cloud/v1/dbaas/postgres/validate_pg_conf/{project_id}/{region_id}">client.cloud.databases.postgres.custom_configurations.<a href="./src/gcore/resources/cloud/databases/postgres/custom_configurations.py">validate</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/databases/postgres/custom_configuration_validate_params.py">params</a>) -> <a href="./src/gcore/types/cloud/databases/postgres/pg_conf_validation.py">PgConfValidation</a></code>

## VolumeSnapshots

Types:

```python
from gcore.types.cloud import Snapshot
```

Methods:

- <code title="post /cloud/v1/snapshots/{project_id}/{region_id}">client.cloud.volume_snapshots.<a href="./src/gcore/resources/cloud/volume_snapshots.py">create</a>(\*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_snapshot_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="patch /cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}">client.cloud.volume_snapshots.<a href="./src/gcore/resources/cloud/volume_snapshots.py">update</a>(snapshot_id, \*, project_id, region_id, \*\*<a href="src/gcore/types/cloud/volume_snapshot_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/snapshot.py">Snapshot</a></code>
- <code title="delete /cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}">client.cloud.volume_snapshots.<a href="./src/gcore/resources/cloud/volume_snapshots.py">delete</a>(snapshot_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/task_id_list.py">TaskIDList</a></code>
- <code title="get /cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}">client.cloud.volume_snapshots.<a href="./src/gcore/resources/cloud/volume_snapshots.py">get</a>(snapshot_id, \*, project_id, region_id) -> <a href="./src/gcore/types/cloud/snapshot.py">Snapshot</a></code>
