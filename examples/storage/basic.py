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
    delete_storage(client=gcore, storage_id=storage_id)


def create_storage(*, client: Gcore) -> int:
    print("\n=== CREATE STORAGE ===")
    name = f"s3-basic-{int(time.time())}"
    storage = client.storage.object_storages.create(
        name=name,
        location_name="s-ed1",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}")
    print(f"Storage address: {storage.address}")

    # Display S3 credentials
    if storage.access_keys:
        print(f"S3 Access Key: {storage.access_keys[0].access_key}")
        print(f"S3 Secret Key: {storage.access_keys[0].secret_key}")

    print("======================")
    return storage.id


def list_storages(*, client: Gcore) -> None:
    print("\n=== LIST STORAGES ===")
    for count, storage in enumerate(client.storage.object_storages.list(), 1):
        print(
            f"  {count}. Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}, Status={storage.provisioning_status}"
        )
    print("=====================")


def get_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== GET STORAGE ===")
    storage = client.storage.object_storages.get(storage_id=storage_id)
    print(
        f"Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}")
    print("===================")


def delete_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    client.storage.object_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    main()
