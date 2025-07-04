from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import Project


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    project = create_project(client=gcore)
    list_all_projects(client=gcore)
    get_project_by_id(client=gcore, project_id=project.id)
    update_project(client=gcore, project_id=project.id)
    delete_project(client=gcore, project_id=project.id)


def create_project(*, client: Gcore) -> Project:
    print("\n=== CREATE PROJECT ===")
    new_project = client.cloud.projects.create(name="gcore-go-example")
    print(f"Project ID: {new_project.id}, name: {new_project.name}")
    print("===========================")
    return new_project


def list_all_projects(*, client: Gcore) -> SyncOffsetPage[Project]:
    print("\n=== LIST ALL PROJECTS ===")
    all_projects = client.cloud.projects.list()
    for count, project in enumerate(all_projects, 1):
        print(f"  {count}. Project ID: {project.id}, name: {project.name}")
    print("==========================")
    return all_projects


def get_project_by_id(*, client: Gcore, project_id: int) -> Project:
    print("\n=== GET PROJECT BY ID ===")
    project = client.cloud.projects.get(project_id=project_id)
    print(f"Project ID: {project.id}, name: {project.name}, created: {project.created_at}")
    print("==========================")
    return project


def update_project(*, client: Gcore, project_id: int) -> Project:
    print("\n=== UPDATE PROJECT ===")
    updated_project = client.cloud.projects.replace(project_id=project_id, name="gcore-go-example-updated")
    print(f"Project ID: {updated_project.id}, name: {updated_project.name}")
    print("=======================")
    return updated_project


def delete_project(*, client: Gcore, project_id: int) -> None:
    print("\n=== DELETE PROJECT ===")
    client.cloud.projects.delete(project_id=project_id)
    print(f"Deleted project: ID={project_id}")
    print("=======================")


if __name__ == "__main__":
    main()
