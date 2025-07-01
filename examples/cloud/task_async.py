import os
import asyncio

from gcore import AsyncGcore


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    # TODO set cloud network ID before running
    cloud_task_id = os.environ["GCORE_CLOUD_TASK_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    await list_tasks(client=gcore)
    await get_task(client=gcore, task_id=cloud_task_id)
    await poll_task(client=gcore, task_id=cloud_task_id)
    await acknowledge_task(client=gcore, task_id=cloud_task_id)
    await acknowledge_all_tasks(client=gcore)


async def list_tasks(*, client: AsyncGcore) -> None:
    print("\n=== LIST ALL TASKS ===")
    all_tasks = await client.cloud.tasks.list(state=["RUNNING"])
    count = 1
    async for task in all_tasks:
        print(f"  {count}. Task {task.id} ({task.task_type}): {task.state}")
        count += 1
    print("========================")


async def get_task(*, client: AsyncGcore, task_id: str) -> None:
    print("\n=== GET TASK BY ID ===")
    task = await client.cloud.tasks.get(task_id=task_id)
    print(f"Task {task.id} ({task.task_type}): {task.state}")
    print("======================")


async def poll_task(*, client: AsyncGcore, task_id: str) -> None:
    print("\n=== POLL TASK ===")
    task = await client.cloud.tasks.poll(task_id=task_id)
    print(f"Task {task.id} ({task.task_type}): {task.state}")
    print("==================")


async def acknowledge_task(*, client: AsyncGcore, task_id: str) -> None:
    print("\n=== ACKNOWLEDGE TASK ===")
    await client.cloud.tasks.acknowledge_one(task_id=task_id)
    print(f"Acknowledged task: ID={task_id}")
    print("========================")


async def acknowledge_all_tasks(*, client: AsyncGcore) -> None:
    print("\n=== ACKNOWLEDGE ALL TASKS ===")
    await client.cloud.tasks.acknowledge_all()
    print("Acknowledged all tasks")
    print("=============================")


if __name__ == "__main__":
    asyncio.run(main())
