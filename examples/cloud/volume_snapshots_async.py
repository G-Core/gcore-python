import asyncio

from gcore import AsyncGcore


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    # A snapshot is taken of a volume, so create a volume to use as the source.
    volume_id = await create_source_volume(client=gcore)
    snapshot_id = await create_snapshot(client=gcore, volume_id=volume_id)
    await list_snapshots(client=gcore)
    await get_snapshot(client=gcore, snapshot_id=snapshot_id)
    await update_snapshot(client=gcore, snapshot_id=snapshot_id)
    await delete_snapshot(client=gcore, snapshot_id=snapshot_id)
    await delete_source_volume(client=gcore, volume_id=volume_id)


async def create_source_volume(*, client: AsyncGcore) -> str:
    print("\n=== CREATE SOURCE VOLUME ===")
    volume = await client.cloud.volumes.create_and_poll(
        name="gcore-python-example-snapshot-source",
        size=1,
        source="new-volume",
    )
    if not volume.id:
        raise RuntimeError("Failed to create source volume")
    print(f"Created source volume: ID={volume.id}")
    print("============================")
    return volume.id


async def create_snapshot(*, client: AsyncGcore, volume_id: str) -> str:
    print("\n=== CREATE SNAPSHOT ===")
    # create_and_poll creates the snapshot and waits for the underlying task to finish.
    snapshot = await client.cloud.volume_snapshots.create_and_poll(
        name="gcore-python-example-snapshot",
        volume_id=volume_id,
        description="Created by the gcore-python volume snapshot example",
    )
    if not snapshot.id:
        raise RuntimeError("Failed to create snapshot")
    print(f"Created snapshot: ID={snapshot.id}, status={snapshot.status}")
    print("=======================")
    return snapshot.id


async def list_snapshots(*, client: AsyncGcore) -> None:
    print("\n=== LIST SNAPSHOTS ===")
    snapshots = await client.cloud.volume_snapshots.list()
    count = 0
    async for snapshot in snapshots:
        print(f"{count}. Snapshot: ID={snapshot.id}, name={snapshot.name}, size={snapshot.size} GiB, status={snapshot.status}")
        count += 1
    print("======================")


async def get_snapshot(*, client: AsyncGcore, snapshot_id: str) -> None:
    print("\n=== GET SNAPSHOT ===")
    snapshot = await client.cloud.volume_snapshots.get(snapshot_id=snapshot_id)
    print(f"Snapshot: ID={snapshot.id}, name={snapshot.name}, volume_id={snapshot.volume_id}, size={snapshot.size} GiB")
    print("====================")


async def update_snapshot(*, client: AsyncGcore, snapshot_id: str) -> None:
    print("\n=== UPDATE SNAPSHOT ===")
    snapshot = await client.cloud.volume_snapshots.update(
        snapshot_id=snapshot_id,
        name="gcore-python-example-snapshot-updated",
    )
    print(f"Updated snapshot: ID={snapshot.id}, name={snapshot.name}")
    print("=======================")


async def delete_snapshot(*, client: AsyncGcore, snapshot_id: str) -> None:
    print("\n=== DELETE SNAPSHOT ===")
    # delete_and_poll waits for the delete task to complete.
    await client.cloud.volume_snapshots.delete_and_poll(snapshot_id=snapshot_id)
    print(f"Deleted snapshot: ID={snapshot_id}")
    print("=======================")


async def delete_source_volume(*, client: AsyncGcore, volume_id: str) -> None:
    print("\n=== DELETE SOURCE VOLUME ===")
    await client.cloud.volumes.delete_and_poll(volume_id=volume_id)
    print(f"Deleted source volume: ID={volume_id}")
    print("============================")


if __name__ == "__main__":
    asyncio.run(main())
