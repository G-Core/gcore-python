import time

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    storage_id = create_storage(client=gcore)
    list_storages(client=gcore)
    get_storage(client=gcore, storage_id=storage_id)
    update_storage(client=gcore, storage_id=storage_id)
    delete_storage(client=gcore, storage_id=storage_id)


def create_storage(*, client: Gcore) -> int:
    print("\n=== CREATE STORAGE ===")
    name = f"example-s3-storage-{int(time.time())}"
    storage = client.storage.create(
        name=name,
        type="s3",
        location="s-ed1",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}")
    print(f"Storage address: {storage.address}")
    print(f"S3 Access Key: {storage.credentials.s3.access_key}")  # type: ignore[union-attr]
    print(f"S3 Secret Key: {storage.credentials.s3.secret_key}")  # type: ignore[union-attr]
    print("======================")
    return storage.id


def list_storages(*, client: Gcore) -> None:
    print("\n=== LIST STORAGES ===")
    storages = client.storage.list()
    for count, storage in enumerate(storages, 1):
        print(
            f"  {count}. Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}, Status={storage.provisioning_status}"
        )
    print("=====================")


def get_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== GET STORAGE ===")
    storage = client.storage.get(storage_id=storage_id)
    print(
        f"Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}, Can Restore: {storage.can_restore}")
    print("===================")


def update_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== UPDATE STORAGE ===")
    storage = client.storage.update(
        storage_id=storage_id,
        expires="30 days",
    )
    print(f"Updated Storage: ID={storage.id}, Expires: {storage.expires}")
    print("======================")


def delete_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    client.storage.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    main()
