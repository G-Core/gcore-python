import os
from typing import Optional

from httpx import HTTPStatusError

from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import Task


def list_tasks() -> Optional[SyncOffsetPage[Task]]:
    """Demonstrates listing all tasks for a project and region."""
    # The API key is read automatically from the GCORE_API_KEY environment variable if omitted
    # Read base URL from environment variable, if set
    base_url = os.environ.get("GCORE_API_URL")
    gcore = Gcore(
        api_key=os.environ.get("GCORE_API_KEY"),
        base_url=base_url if base_url else None, # Pass base_url only if it's set
    )
    # Get project ID from environment variable GCORE_CLOUD_PROJECT_ID, defaulting to 1 if not set
    project_id = int(os.environ.get("GCORE_CLOUD_PROJECT_ID", "1"))
    # Get region ID from environment variable GCORE_CLOUD_REGION_ID, defaulting to 1 if not set
    region_id = int(os.environ.get("GCORE_CLOUD_REGION_ID", "1"))

    print(f"=== LIST ALL TASKS (Project: {project_id}, Region: {region_id}) ===")
    tasks: Optional[SyncOffsetPage[Task]] = None
    try:
        # Pass project_id and region_id as lists, as expected by the API
        tasks = gcore.cloud.tasks.list(project_id=[project_id], region_id=[region_id])

        count = 0
        print("Results:")
        # Check if tasks_page is not None before iterating
        if tasks:
            for task in tasks:
                print(
                    f"- Task ID: {task.id}, Type: {task.task_type}, State: {task.state},"
                    f" Created: {task.created_on}"
                )
                count += 1

            if count == 0:
                print("No tasks found.")
        else:
            print("Could not retrieve tasks.") # Handle case where tasks_page might remain None

    except Exception as e:
        print(f"Error listing tasks: {e}")  # Basic error logging

    print("=================================================")
    # Note: The SDK handles pagination implicitly for simple iteration.
    # If you need manual control, use the methods on the SyncOffsetPage object.
    return tasks


def get_task_by_id() -> Optional[Task]:
    """Demonstrates retrieving a specific task by its ID."""
    # Initialize client (same as list_tasks)
    base_url = os.environ.get("GCORE_API_URL")
    gcore = Gcore(
        api_key=os.environ.get("GCORE_API_KEY"),
        base_url=base_url if base_url else None,
    )

    # Replace with a valid task ID from your account.
    # You might need to run list_tasks first to find one.
    task_id_to_get = "your-task-id-here" # TODO: Replace with an actual task ID

    print(f"=== GET TASK BY ID ({task_id_to_get}) ===")
    task: Optional[Task] = None
    try:
        task = gcore.cloud.tasks.get(task_id=task_id_to_get)
        print(
            f"- Task ID: {task.id}, Type: {task.task_type}, State: {task.state},"
            f" Created: {task.created_on}"
        )
    except HTTPStatusError as e:
        # Handle cases like 404 Not Found gracefully
        if e.response.status_code == 404:
             print(f"Info: Task '{task_id_to_get}' not found.")
        else:
             print(f"Error retrieving task '{task_id_to_get}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("============================")
    return task


if __name__ == "__main__":
    get_task_by_id()
    list_tasks()