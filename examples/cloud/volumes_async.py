import os
import asyncio

from gcore import AsyncGcore


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set instance ID before running
    instance_id = os.environ["GCORE_CLOUD_INSTANCE_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    await list_volume_types(client=gcore, region_id=int(cloud_region_id))
    volume_id = await create_volume(client=gcore)
    await list_volumes(client=gcore)
    await get_volume(client=gcore, volume_id=volume_id)
    await update_volume(client=gcore, volume_id=volume_id)
    await attach_to_instance(client=gcore, volume_id=volume_id, instance_id=instance_id)
    await detach_from_instance(client=gcore, volume_id=volume_id, instance_id=instance_id)
    await change_type(client=gcore, volume_id=volume_id)
    await resize(client=gcore, volume_id=volume_id)
    await delete_volume(client=gcore, volume_id=volume_id)


async def list_volume_types(*, client: AsyncGcore, region_id: int) -> None:
    print("\n=== LIST VOLUME TYPES ===")
    # With region_id, the list shows only the types that the region supports
    volume_types = await client.cloud.volumes.types.list(region_id=region_id)
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


async def create_volume(*, client: AsyncGcore) -> str:
    print("\n=== CREATE VOLUME ===")
    volume = await client.cloud.volumes.create_and_poll(
        name="gcore-go-example",
        size=1,
        source="new-volume",
    )
    if not volume.id:
        raise RuntimeError("Failed to create volume")
    print(f"Created volume: ID={volume.id}")
    print("========================")
    return volume.id


async def list_volumes(*, client: AsyncGcore) -> None:
    print("\n=== LIST VOLUMES ===")
    count = 0
    async for volume in client.cloud.volumes.list():
        print(f"{count}. Volume: ID={volume.id}, name={volume.name}, size={volume.size} GiB")
        count += 1
    print("========================")


async def get_volume(*, client: AsyncGcore, volume_id: str) -> None:
    print("\n=== GET VOLUME ===")
    volume = await client.cloud.volumes.get(volume_id=volume_id)
    print(f"Volume: ID={volume.id}, name={volume.name}, size={volume.size} GiB")
    print("========================")


async def update_volume(*, client: AsyncGcore, volume_id: str) -> None:
    print("\n=== UPDATE VOLUME ===")
    volume = await client.cloud.volumes.update(
        volume_id=volume_id,
        name="gcore-go-example-updated",
    )
    print(f"Updated volume: ID={volume.id}, name={volume.name}")
    print("========================")


async def attach_to_instance(*, client: AsyncGcore, volume_id: str, instance_id: str) -> None:
    print("\n=== ATTACH TO INSTANCE ===")
    await client.cloud.volumes.attach_to_instance_and_poll(volume_id=volume_id, instance_id=instance_id)
    print(f"Attached volume to instance: volume_id={volume_id}, instance_id={instance_id}")
    print("========================")


async def detach_from_instance(*, client: AsyncGcore, volume_id: str, instance_id: str) -> None:
    print("\n=== DETACH FROM INSTANCE ===")
    await client.cloud.volumes.detach_from_instance_and_poll(volume_id=volume_id, instance_id=instance_id)
    print(f"Detached volume from instance: volume_id={volume_id}, instance_id={instance_id}")
    print("========================")


async def change_type(*, client: AsyncGcore, volume_id: str) -> None:
    print("\n=== CHANGE TYPE ===")
    volume = await client.cloud.volumes.change_type(volume_id=volume_id, volume_type="ssd_hiiops")
    print(f"Changed volume type: ID={volume.id}, type=ssd_hiiops")
    print("========================")


async def resize(*, client: AsyncGcore, volume_id: str) -> None:
    print("\n=== RESIZE ===")
    volume = await client.cloud.volumes.resize_and_poll(volume_id=volume_id, size=2)
    print(f"Resized volume: ID={volume.id}, size={volume.size} GiB")
    print("========================")


async def delete_volume(*, client: AsyncGcore, volume_id: str) -> None:
    print("\n=== DELETE VOLUME ===")
    await client.cloud.volumes.delete_and_poll(volume_id=volume_id)
    print(f"Deleted volume: ID={volume_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
