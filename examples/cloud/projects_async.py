import os
import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import Project


async def get_project_by_id() -> Project:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Project ID can be specified via environment variable or default to 100
    project_id = int(os.environ.get("GCORE_CLOUD_PROJECT_ID", "100"))
    project = await gcore.cloud.projects.get(project_id=project_id)

    print("\n=== GET PROJECT BY ID ===")
    print(f"Project ID: {project.id}, Name: {project.name}, Created: {project.created_at}")
    print("==========================")
    return project


async def list_all_projects() -> AsyncOffsetPage[Project]:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_projects = await gcore.cloud.projects.list()

    print("\n=== LIST ALL PROJECTS ===")
    count = 1
    async for project in all_projects:
        print(f"  {count}. Project ID: {project.id}, Name: {project.name}")
        count += 1
    print("==========================")
    return all_projects


async def create_new_project() -> Project:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Project name can be specified via environment variable or default
    project_name = "Example Project"
    new_project = await gcore.cloud.projects.create(name=project_name)

    print("\n=== CREATE NEW PROJECT ===")
    print(f"Project ID: {new_project.id}, Name: {new_project.name}")
    print("===========================")
    return new_project


async def update_project(project_id: int) -> Project:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Updated project name can be specified via environment variable or default
    updated_name = "Updated Example Project"
    updated_project = await gcore.cloud.projects.replace(project_id=project_id, name=updated_name)

    print("\n=== UPDATE PROJECT ===")
    print(f"Project ID: {updated_project.id}, Updated Name: {updated_project.name}")
    print("=======================")
    return updated_project


async def delete_project(project_id: int) -> None:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    await gcore.cloud.projects.delete(project_id=project_id)

    print("\n=== DELETE PROJECT ===")
    print(f"Project ID: {project_id} has been deleted")
    print("=======================")


async def main() -> None:
    # Follow the order: create, list, get, update, delete
    new_project = await create_new_project()
    await list_all_projects()
    await get_project_by_id()
    await update_project(project_id=new_project.id)
    await delete_project(project_id=new_project.id)


if __name__ == "__main__":
    asyncio.run(main())
