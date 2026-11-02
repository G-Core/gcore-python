import os

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set instance ID before running attach/detach operations
    instance_id = os.environ["GCORE_CLOUD_INSTANCE_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    list_volume_types(client=gcore, region_id=int(cloud_region_id))
    volume_id = create_volume(client=gcore)
    list_volumes(client=gcore)
    get_volume(client=gcore, volume_id=volume_id)
    update_volume(client=gcore, volume_id=volume_id)
    attach_to_instance(client=gcore, volume_id=volume_id, instance_id=instance_id)
    detach_from_instance(client=gcore, volume_id=volume_id, instance_id=instance_id)
    change_type(client=gcore, volume_id=volume_id)
    resize(client=gcore, volume_id=volume_id)
    delete_volume(client=gcore, volume_id=volume_id)


def list_volume_types(*, client: Gcore, region_id: int) -> None:
    print("\n=== LIST VOLUME TYPES ===")
    # With region_id, the list shows only the types that the region supports
    volume_types = client.cloud.volumes.types.list(region_id=region_id)
    for count, volume_type in enumerate(volume_types.results, 1):
        capabilities = volume_type.capabilities
        print(
            f"{count}. Volume type: name={volume_type.name}, resizable={capabilities.resizable}, "
            f"retypable={capabilities.retypable}, snapshottable={capabilities.snapshottable}, "
            f"attachable_to_boot={capabilities.attachable_to_boot}"
        )
        # qos is None if the type has no QoS limits
        if volume_type.qos:
            print(f"   QoS: iops_per_gib={volume_type.qos.iops_per_gib}, iops_max={volume_type.qos.iops_max}")
    print("========================")


def create_volume(*, client: Gcore) -> str:
    print("\n=== CREATE VOLUME ===")
    volume = client.cloud.volumes.create_and_poll(
        name="gcore-go-example",
        size=1,
        source="new-volume",
    )
    if not volume.id:
        raise RuntimeError("Failed to create volume")
    print(f"Created volume: ID={volume.id}")
    print("========================")
    return volume.id


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
    client.cloud.volumes.attach_to_instance_and_poll(volume_id=volume_id, instance_id=instance_id)
    print(f"Attached volume to instance: volume_id={volume_id}, instance_id={instance_id}")
    print("========================")


def detach_from_instance(*, client: Gcore, volume_id: str, instance_id: str) -> None:
    print("\n=== DETACH FROM INSTANCE ===")
    client.cloud.volumes.detach_from_instance_and_poll(volume_id=volume_id, instance_id=instance_id)
    print(f"Detached volume from instance: volume_id={volume_id}, instance_id={instance_id}")
    print("========================")


def change_type(*, client: Gcore, volume_id: str) -> None:
    print("\n=== CHANGE TYPE ===")
    volume = client.cloud.volumes.change_type(volume_id=volume_id, volume_type="ssd_hiiops")
    print(f"Changed volume type: ID={volume.id}, type=ssd_hiiops")
    print("========================")


def resize(*, client: Gcore, volume_id: str) -> None:
    print("\n=== RESIZE ===")
    volume = client.cloud.volumes.resize_and_poll(volume_id=volume_id, size=2)
    print(f"Resized volume: ID={volume.id}, size={volume.size} GiB")
    print("========================")


def delete_volume(*, client: Gcore, volume_id: str) -> None:
    print("\n=== DELETE VOLUME ===")
    client.cloud.volumes.delete_and_poll(volume_id=volume_id)
    print(f"Deleted volume: ID={volume_id}")
    print("========================")


if __name__ == "__main__":
    main()
