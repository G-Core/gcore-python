import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import Project


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    project = await create_project(client=gcore)
    await list_all_projects(client=gcore)
    await get_project_by_id(client=gcore, project_id=project.id)
    await update_project(client=gcore, project_id=project.id)
    await delete_project(client=gcore, project_id=project.id)


async def create_project(*, client: AsyncGcore) -> Project:
    print("\n=== CREATE PROJECT ===")
    new_project = await client.cloud.projects.create(name="gcore-go-example")
    print(f"Project ID: {new_project.id}, name: {new_project.name}")
    print("===========================")
    return new_project


async def list_all_projects(*, client: AsyncGcore) -> AsyncOffsetPage[Project]:
    print("\n=== LIST ALL PROJECTS ===")
    all_projects = await client.cloud.projects.list()
    count = 1
    async for project in all_projects:
        print(f"  {count}. Project ID: {project.id}, name: {project.name}")
        count += 1
    print("==========================")
    return all_projects


async def get_project_by_id(*, client: AsyncGcore, project_id: int) -> Project:
    print("\n=== GET PROJECT BY ID ===")
    project = await client.cloud.projects.get(project_id=project_id)
    print(f"Project ID: {project.id}, name: {project.name}, created: {project.created_at}")
    print("==========================")
    return project


async def update_project(*, client: AsyncGcore, project_id: int) -> Project:
    print("\n=== UPDATE PROJECT ===")
    updated_project = await client.cloud.projects.replace(project_id=project_id, name="gcore-go-example-updated")
    print(f"Project ID: {updated_project.id}, name: {updated_project.name}")
    print("=======================")
    return updated_project


async def delete_project(*, client: AsyncGcore, project_id: int) -> None:
    print("\n=== DELETE PROJECT ===")
    await client.cloud.projects.delete(project_id=project_id)
    print(f"Deleted project: ID={project_id}")
    print("=======================")


if __name__ == "__main__":
    asyncio.run(main())
