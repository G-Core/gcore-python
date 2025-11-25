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
    await update_storage(client=gcore, storage_id=storage_id)
    await delete_storage(client=gcore, storage_id=storage_id)


async def create_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE STORAGE ===")
    name = f"example-s3-storage-{int(time.time())}"
    storage = await client.storage.create(
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


async def list_storages(*, client: AsyncGcore) -> None:
    print("\n=== LIST STORAGES ===")
    storages = client.storage.list()
    count = 1
    async for storage in storages:
        print(
            f"  {count}. Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}, Status={storage.provisioning_status}"
        )
        count += 1
    print("=====================")


async def get_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== GET STORAGE ===")
    storage = await client.storage.get(storage_id=storage_id)
    print(
        f"Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}, Can Restore: {storage.can_restore}")
    print("===================")


async def update_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== UPDATE STORAGE ===")
    storage = await client.storage.update(
        storage_id=storage_id,
        expires="30 days",
    )
    print(f"Updated Storage: ID={storage.id}, Expires: {storage.expires}")
    print("======================")


async def delete_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    await client.storage.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    asyncio.run(main())
