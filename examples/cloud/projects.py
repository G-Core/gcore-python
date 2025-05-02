import os

from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import Project


def get_project_by_id() -> Project:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Project ID can be specified via environment variable or default to 100
    project_id = int(os.environ.get("GCORE_CLOUD_PROJECT_ID", "100"))
    project = gcore.cloud.projects.get(project_id=project_id)

    print("\n=== GET PROJECT BY ID ===")
    print(f"Project ID: {project.id}, Name: {project.name}, Created: {project.created_at}")
    print("==========================")
    return project


def list_all_projects() -> SyncOffsetPage[Project]:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_projects = gcore.cloud.projects.list()

    print("\n=== LIST ALL PROJECTS ===")
    for count, project in enumerate(all_projects, 1):
        print(f"  {count}. Project ID: {project.id}, Name: {project.name}")
    print("==========================")
    return all_projects


def create_new_project() -> Project:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Project name can be specified via environment variable or default
    project_name = "Example Project"
    new_project = gcore.cloud.projects.create(name=project_name)

    print("\n=== CREATE NEW PROJECT ===")
    print(f"Project ID: {new_project.id}, Name: {new_project.name}")
    print("===========================")
    return new_project


def update_project(project_id: int) -> Project:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Updated project name can be specified via environment variable or default
    updated_name = "Updated Example Project"
    updated_project = gcore.cloud.projects.replace(project_id=project_id, name=updated_name)

    print("\n=== UPDATE PROJECT ===")
    print(f"Project ID: {updated_project.id}, Updated Name: {updated_project.name}")
    print("=======================")
    return updated_project


def delete_project(project_id: int) -> None:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    gcore.cloud.projects.delete(project_id=project_id)

    print("\n=== DELETE PROJECT ===")
    print(f"Project ID: {project_id} has been deleted")
    print("=======================")


if __name__ == "__main__":
    # Follow the order: create, list, get, delete
    new_project = create_new_project()
    list_all_projects()
    get_project_by_id()
    update_project(project_id=new_project.id)
    delete_project(project_id=new_project.id)
