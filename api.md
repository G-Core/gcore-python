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
