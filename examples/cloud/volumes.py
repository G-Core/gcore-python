import os

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set instance ID before running attach/detach operations
    instance_id = os.environ["GCORE_CLOUD_INSTANCE_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    volume_id = create_volume(client=gcore)
    list_volumes(client=gcore)
    get_volume(client=gcore, volume_id=volume_id)
    update_volume(client=gcore, volume_id=volume_id)
    attach_to_instance(client=gcore, volume_id=volume_id, instance_id=instance_id)
    detach_from_instance(client=gcore, volume_id=volume_id, instance_id=instance_id)
    change_type(client=gcore, volume_id=volume_id)
    resize(client=gcore, volume_id=volume_id)
    delete_volume(client=gcore, volume_id=volume_id)


def create_volume(*, client: Gcore) -> str:
    print("\n=== CREATE VOLUME ===")
    response = client.cloud.volumes.create(
        name="gcore-go-example",
        size=1,
        source="new-volume",
    )
    task = client.cloud.tasks.poll(task_id=response.tasks[0])
    if task.created_resources is None or task.created_resources.volumes is None:
        raise RuntimeError("Task completed but created_resources or volumes is missing")
    volume_id: str = task.created_resources.volumes[0]
    print(f"Created volume: ID={volume_id}")
    print("========================")
    return volume_id


def list_volumes(*, client: Gcore) -> None:
    print("\n=== LIST VOLUMES ===")
    volumes = client.cloud.volumes.list()
    for count, volume in enumerate(volumes):
        print(f"{count}. Volume: ID={volume.id}, name={volume.name}, size={volume.size} GiB")
    print("========================")


def get_volume(*, client: Gcore, volume_id: str) -> None:
    print("\n=== GET VOLUME ===")
    volume = client.cloud.volumes.get(volume_id=volume_id)
    print(f"Volume: ID={volume.id}, name={volume.name}, size={volume.size} GiB")
    print("========================")


def update_volume(*, client: Gcore, volume_id: str) -> None:
    print("\n=== UPDATE VOLUME ===")
    volume = client.cloud.volumes.update(
        volume_id=volume_id,
        name="gcore-go-example-updated",
    )
    print(f"Updated volume: ID={volume.id}, name={volume.name}")
    print("========================")


def attach_to_instance(*, client: Gcore, volume_id: str, instance_id: str) -> None:
    print("\n=== ATTACH TO INSTANCE ===")
    response = client.cloud.volumes.attach_to_instance(volume_id=volume_id, instance_id=instance_id)
    task_id = response.tasks[0]
    client.cloud.tasks.poll(task_id=task_id)
    print(f"Attached volume to instance: volume_id={volume_id}, instance_id={instance_id}")
    print("========================")


def detach_from_instance(*, client: Gcore, volume_id: str, instance_id: str) -> None:
    print("\n=== DETACH FROM INSTANCE ===")
    response = client.cloud.volumes.detach_from_instance(volume_id=volume_id, instance_id=instance_id)
    task_id = response.tasks[0]
    client.cloud.tasks.poll(task_id=task_id)
    print(f"Detached volume from instance: volume_id={volume_id}, instance_id={instance_id}")
    print("========================")


def change_type(*, client: Gcore, volume_id: str) -> None:
    print("\n=== CHANGE TYPE ===")
    volume = client.cloud.volumes.change_type(volume_id=volume_id, volume_type="ssd_hiiops")
    print(f"Changed volume type: ID={volume.id}, type=ssd_hiiops")
    print("========================")


def resize(*, client: Gcore, volume_id: str) -> None:
    print("\n=== RESIZE ===")
    response = client.cloud.volumes.resize(volume_id=volume_id, size=2)
    task_id = response.tasks[0]
    client.cloud.tasks.poll(task_id=task_id)
    print(f"Resized volume: ID={volume_id}, size=2 GiB")
    print("========================")


def delete_volume(*, client: Gcore, volume_id: str) -> None:
    print("\n=== DELETE VOLUME ===")
    response = client.cloud.volumes.delete(volume_id=volume_id)
    task_id = response.tasks[0]
    client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted volume: ID={volume_id}")
    print("========================")


if __name__ == "__main__":
    main()
