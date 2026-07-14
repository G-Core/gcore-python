from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    # A snapshot is taken of a volume, so create a volume to use as the source.
    volume_id = create_source_volume(client=gcore)
    snapshot_id = create_snapshot(client=gcore, volume_id=volume_id)
    list_snapshots(client=gcore)
    get_snapshot(client=gcore, snapshot_id=snapshot_id)
    update_snapshot(client=gcore, snapshot_id=snapshot_id)
    delete_snapshot(client=gcore, snapshot_id=snapshot_id)
    delete_source_volume(client=gcore, volume_id=volume_id)


def create_source_volume(*, client: Gcore) -> str:
    print("\n=== CREATE SOURCE VOLUME ===")
    volume = client.cloud.volumes.create_and_poll(
        name="gcore-python-example-snapshot-source",
        size=1,
        source="new-volume",
    )
    if not volume.id:
        raise RuntimeError("Failed to create source volume")
    print(f"Created source volume: ID={volume.id}")
    print("============================")
    return volume.id


def create_snapshot(*, client: Gcore, volume_id: str) -> str:
    print("\n=== CREATE SNAPSHOT ===")
    # create_and_poll creates the snapshot and waits for the underlying task to finish.
    snapshot = client.cloud.volume_snapshots.create_and_poll(
        name="gcore-python-example-snapshot",
        volume_id=volume_id,
        description="Created by the gcore-python volume snapshot example",
    )
    if not snapshot.id:
        raise RuntimeError("Failed to create snapshot")
    print(f"Created snapshot: ID={snapshot.id}, status={snapshot.status}")
    print("=======================")
    return snapshot.id


def list_snapshots(*, client: Gcore) -> None:
    print("\n=== LIST SNAPSHOTS ===")
    snapshots = client.cloud.volume_snapshots.list()
    for count, snapshot in enumerate(snapshots):
        print(f"{count}. Snapshot: ID={snapshot.id}, name={snapshot.name}, size={snapshot.size} GiB, status={snapshot.status}")
    print("======================")


def get_snapshot(*, client: Gcore, snapshot_id: str) -> None:
    print("\n=== GET SNAPSHOT ===")
    snapshot = client.cloud.volume_snapshots.get(snapshot_id=snapshot_id)
    print(f"Snapshot: ID={snapshot.id}, name={snapshot.name}, volume_id={snapshot.volume_id}, size={snapshot.size} GiB")
    print("====================")


def update_snapshot(*, client: Gcore, snapshot_id: str) -> None:
    print("\n=== UPDATE SNAPSHOT ===")
    snapshot = client.cloud.volume_snapshots.update(
        snapshot_id=snapshot_id,
        name="gcore-python-example-snapshot-updated",
    )
    print(f"Updated snapshot: ID={snapshot.id}, name={snapshot.name}")
    print("=======================")


def delete_snapshot(*, client: Gcore, snapshot_id: str) -> None:
    print("\n=== DELETE SNAPSHOT ===")
    # delete_and_poll waits for the delete task to complete.
    client.cloud.volume_snapshots.delete_and_poll(snapshot_id=snapshot_id)
    print(f"Deleted snapshot: ID={snapshot_id}")
    print("=======================")


def delete_source_volume(*, client: Gcore, volume_id: str) -> None:
    print("\n=== DELETE SOURCE VOLUME ===")
    client.cloud.volumes.delete_and_poll(volume_id=volume_id)
    print(f"Deleted source volume: ID={volume_id}")
    print("============================")


if __name__ == "__main__":
    main()
