# Cloud

## Projects

Types:

```python
from gcore.types.cloud import Project, ProjectListResponse, ProjectDeleteResponse
```

Methods:

- <code title="post /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">create</a>(\*\*<a href="src/gcore/types/cloud/project_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="get /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">retrieve</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="put /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">update</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/project_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="get /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">list</a>(\*\*<a href="src/gcore/types/cloud/project_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">delete</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/project_delete_response.py">ProjectDeleteResponse</a></code>

## Quotas

### ClientQuotas

Types:

```python
from gcore.types.cloud.quotas import AllClientQuotas, QuotaNotificationThreshold, QuotaThreshold
```

Methods:

- <code title="get /cloud/v2/client_quotas">client.cloud.quotas.client_quotas.<a href="./src/gcore/resources/cloud/quotas/client_quotas.py">retrieve</a>() -> <a href="./src/gcore/types/cloud/quotas/all_client_quotas.py">AllClientQuotas</a></code>

### Global

Types:

```python
from gcore.types.cloud.quotas import GlobalQuotas
```

Methods:

- <code title="get /cloud/v2/global_quotas/{client_id}">client.cloud.quotas.global*.<a href="./src/gcore/resources/cloud/quotas/global*.py">retrieve</a>(client_id) -> <a href="./src/gcore/types/cloud/quotas/global_quotas.py">GlobalQuotas</a></code>

### Regional

Types:

```python
from gcore.types.cloud.quotas import RegionalQuotas
```

Methods:

- <code title="get /cloud/v2/regional_quotas/{client_id}/{region_id}">client.cloud.quotas.regional.<a href="./src/gcore/resources/cloud/quotas/regional.py">retrieve</a>(\*, client_id, region_id) -> <a href="./src/gcore/types/cloud/quotas/regional_quotas.py">RegionalQuotas</a></code>

### LimitsRequest

Types:

```python
from gcore.types.cloud.quotas import LimitsRequest, LimitsRequestCreate
```

Methods:

- <code title="post /cloud/v2/limits_request">client.cloud.quotas.limits_request.<a href="./src/gcore/resources/cloud/quotas/limits_request.py">create</a>(\*\*<a href="src/gcore/types/cloud/quotas/limits_request_create_params.py">params</a>) -> None</code>
- <code title="get /cloud/v2/limits_request/{request_id}">client.cloud.quotas.limits_request.<a href="./src/gcore/resources/cloud/quotas/limits_request.py">retrieve</a>(request_id) -> <a href="./src/gcore/types/cloud/quotas/limits_request.py">LimitsRequest</a></code>
- <code title="get /cloud/v2/limits_request">client.cloud.quotas.limits_request.<a href="./src/gcore/resources/cloud/quotas/limits_request.py">list</a>(\*\*<a href="src/gcore/types/cloud/quotas/limits_request_list_params.py">params</a>) -> None</code>
- <code title="delete /cloud/v2/limits_request/{request_id}">client.cloud.quotas.limits_request.<a href="./src/gcore/resources/cloud/quotas/limits_request.py">delete</a>(request_id) -> None</code>

## Regions

Types:

```python
from gcore.types.cloud import Region
```

Methods:

- <code title="get /cloud/v1/regions/{region_id}">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">retrieve</a>(\*, region_id, \*\*<a href="src/gcore/types/cloud/region_retrieve_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">Region</a></code>
- <code title="get /cloud/v1/regions">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">list</a>(\*\*<a href="src/gcore/types/cloud/region_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">SyncOffsetPage[Region]</a></code>
