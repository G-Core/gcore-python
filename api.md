# Cloud

## Projects

Types:

```python
from gcore.types.cloud import Project, ProjectDeleteResponse
```

Methods:

- <code title="post /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">create</a>(\*\*<a href="src/gcore/types/cloud/project_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="get /cloud/v1/projects">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">list</a>(\*\*<a href="src/gcore/types/cloud/project_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">SyncOffsetPage[Project]</a></code>
- <code title="delete /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">delete</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/project_delete_response.py">ProjectDeleteResponse</a></code>
- <code title="get /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">get</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>
- <code title="put /cloud/v1/projects/{project_id}">client.cloud.projects.<a href="./src/gcore/resources/cloud/projects.py">replace</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/project_replace_params.py">params</a>) -> <a href="./src/gcore/types/cloud/project.py">Project</a></code>

## Tasks

Types:

```python
from gcore.types.cloud import Task
```

Methods:

- <code title="get /cloud/v1/tasks/{task_id}">client.cloud.tasks.<a href="./src/gcore/resources/cloud/tasks.py">retrieve</a>(task_id) -> <a href="./src/gcore/types/cloud/task.py">Task</a></code>
- <code title="get /cloud/v1/tasks">client.cloud.tasks.<a href="./src/gcore/resources/cloud/tasks.py">list</a>(\*\*<a href="src/gcore/types/cloud/task_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/task.py">SyncOffsetPage[Task]</a></code>

## Regions

Types:

```python
from gcore.types.cloud import Region
```

Methods:

- <code title="get /cloud/v1/regions/{region_id}">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">retrieve</a>(\*, region_id, \*\*<a href="src/gcore/types/cloud/region_retrieve_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">Region</a></code>
- <code title="get /cloud/v1/regions">client.cloud.regions.<a href="./src/gcore/resources/cloud/regions.py">list</a>(\*\*<a href="src/gcore/types/cloud/region_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/region.py">SyncOffsetPage[Region]</a></code>
