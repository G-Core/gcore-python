import time
import asyncio

from gcore import AsyncGcore


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    storage_id = await create_storage(client=gcore)
    await list_storages(client=gcore)
    await get_storage(client=gcore, storage_id=storage_id)
    await delete_storage(client=gcore, storage_id=storage_id)


async def create_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE STORAGE ===")
    name = f"s3-basic-{int(time.time())}"
    storage = await client.storage.object_storages.create(
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


async def list_storages(*, client: AsyncGcore) -> None:
    print("\n=== LIST STORAGES ===")
    count = 1
    async for storage in client.storage.object_storages.list():
        print(
            f"  {count}. Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}, Status={storage.provisioning_status}"
        )
        count += 1
    print("=====================")


async def get_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== GET STORAGE ===")
    storage = await client.storage.object_storages.get(storage_id=storage_id)
    print(
        f"Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}")
    print("===================")


async def delete_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    await client.storage.object_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    asyncio.run(main())
