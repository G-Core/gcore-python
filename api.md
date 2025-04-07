# Cloud

## Projects

### V1

Types:

```python
from gcore.types.cloud.projects import Project, V1ListResponse, V1DeleteResponse
```

Methods:

- <code title="post /cloud/v1/projects">client.cloud.projects.v1.<a href="./src/gcore/resources/cloud/projects/v1.py">create</a>(\*\*<a href="src/gcore/types/cloud/projects/v1_create_params.py">params</a>) -> <a href="./src/gcore/types/cloud/projects/project.py">Project</a></code>
- <code title="get /cloud/v1/projects/{project_id}">client.cloud.projects.v1.<a href="./src/gcore/resources/cloud/projects/v1.py">retrieve</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/projects/project.py">Project</a></code>
- <code title="put /cloud/v1/projects/{project_id}">client.cloud.projects.v1.<a href="./src/gcore/resources/cloud/projects/v1.py">update</a>(\*, project_id, \*\*<a href="src/gcore/types/cloud/projects/v1_update_params.py">params</a>) -> <a href="./src/gcore/types/cloud/projects/project.py">Project</a></code>
- <code title="get /cloud/v1/projects">client.cloud.projects.v1.<a href="./src/gcore/resources/cloud/projects/v1.py">list</a>(\*\*<a href="src/gcore/types/cloud/projects/v1_list_params.py">params</a>) -> <a href="./src/gcore/types/cloud/projects/v1_list_response.py">V1ListResponse</a></code>
- <code title="delete /cloud/v1/projects/{project_id}">client.cloud.projects.v1.<a href="./src/gcore/resources/cloud/projects/v1.py">delete</a>(\*, project_id) -> <a href="./src/gcore/types/cloud/projects/v1_delete_response.py">V1DeleteResponse</a></code>
