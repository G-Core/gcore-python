import os

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    # TODO set cloud network ID before running
    cloud_task_id = os.environ["GCORE_CLOUD_TASK_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    list_tasks(client=gcore)
    get_task(client=gcore, task_id=cloud_task_id)
    poll_task(client=gcore, task_id=cloud_task_id)
    acknowledge_task(client=gcore, task_id=cloud_task_id)
    acknowledge_all_tasks(client=gcore)


def list_tasks(*, client: Gcore) -> None:
    print("\n=== LIST TASKS ===")
    tasks = client.cloud.tasks.list(state=["RUNNING"])
    for count, task in enumerate(tasks, 1):
        print(f"{count}. Task: ID={task.id}, type={task.task_type}, state={task.state}")
    print("========================")


def get_task(*, client: Gcore, task_id: str) -> None:
    print("\n=== GET TASK ===")
    task = client.cloud.tasks.get(task_id=task_id)
    print(f"Task: ID={task.id}, type={task.task_type}, state={task.state}")
    print("========================")


def poll_task(*, client: Gcore, task_id: str) -> None:
    print("\n=== POLL TASK ===")
    task = client.cloud.tasks.poll(task_id=task_id)
    print(f"Polled task: ID={task.id}, type={task.task_type}, state={task.state}")
    print("========================")


def acknowledge_task(*, client: Gcore, task_id: str) -> None:
    print("\n=== ACKNOWLEDGE TASK ===")
    client.cloud.tasks.acknowledge_one(task_id=task_id)
    print(f"Acknowledged task: ID={task_id}")
    print("========================")


def acknowledge_all_tasks(*, client: Gcore) -> None:
    print("\n=== ACKNOWLEDGE ALL TASKS ===")
    client.cloud.tasks.acknowledge_all()
    print("Acknowledged all tasks")
    print("========================")


if __name__ == "__main__":
    main()
