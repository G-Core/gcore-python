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

    # S3 access key operations
    s3_storage_id = await create_s3_storage(client=gcore)
    await wait_for_storage_provisioning(client=gcore, storage_id=s3_storage_id)
    await get_s3_storage(client=gcore, storage_id=s3_storage_id)
    new_access_key = await create_s3_access_key(client=gcore, storage_id=s3_storage_id)
    await list_s3_access_keys(client=gcore, storage_id=s3_storage_id)
    await delete_s3_access_key(client=gcore, storage_id=s3_storage_id, access_key=new_access_key)
    await list_s3_access_keys(client=gcore, storage_id=s3_storage_id)
    await delete_s3_storage(client=gcore, storage_id=s3_storage_id)

    # SFTP storage operations
    sftp_storage_id = await create_sftp_storage(client=gcore)
    await wait_for_sftp_storage_provisioning(client=gcore, storage_id=sftp_storage_id)
    await get_sftp_storage(client=gcore, storage_id=sftp_storage_id)
    await regenerate_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    await remove_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    await reenable_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    await delete_sftp_storage(client=gcore, storage_id=sftp_storage_id)


async def create_s3_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE S3 STORAGE ===")
    s3_name = f"s3-creds-{int(time.time())}"
    storage = await client.storage.object_storages.create(
        name=s3_name,
        location_name="s-ed1",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}")
    print(f"Storage address: {storage.address}")

    # Display S3 credentials
    if storage.access_keys:
        print(f"S3 Access Key: {storage.access_keys[0].access_key}")
        print(f"S3 Secret Key: {storage.access_keys[0].secret_key}")

    print("=========================")
    return storage.id


async def create_sftp_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE SFTP STORAGE ===")
    sftp_name = f"sftp-creds-{int(time.time())}"
    storage = await client.storage.sftp_storages.create(
        name=sftp_name,
        location_name="ams",
        password_mode="auto",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}")
    print(f"Storage address: {storage.address}")
    if storage.password:
        print(f"SFTP Password: {storage.password}")
    print("==========================")
    return storage.id


async def wait_for_storage_provisioning(
    *, client: AsyncGcore, storage_id: int, max_wait: int = 30, wait_interval: int = 2
) -> None:
    """Wait for an S3 storage to be provisioned"""
    elapsed = 0
    while elapsed < max_wait:
        storage = await client.storage.object_storages.get(storage_id=storage_id)
        if storage.provisioning_status == "active":
            print(f"Storage {storage_id} is ready")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        await asyncio.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready after {max_wait}s")


async def wait_for_sftp_storage_provisioning(
    *, client: AsyncGcore, storage_id: int, max_wait: int = 30, wait_interval: int = 2
) -> None:
    """Wait for an SFTP storage to be provisioned"""
    elapsed = 0
    while elapsed < max_wait:
        storage = await client.storage.sftp_storages.get(storage_id=storage_id)
        if storage.provisioning_status == "active":
            print(f"Storage {storage_id} is ready")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        await asyncio.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready after {max_wait}s")


async def get_s3_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== GET S3 STORAGE DETAILS ===")
    storage = await client.storage.object_storages.get(storage_id=storage_id)
    print(
        f"S3 Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}")
    print("==============================")


async def get_sftp_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== GET SFTP STORAGE DETAILS ===")
    storage = await client.storage.sftp_storages.get(storage_id=storage_id)
    print(
        f"SFTP Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}, HasPassword: {storage.has_password}")
    print("================================")


async def create_s3_access_key(*, client: AsyncGcore, storage_id: int) -> str:
    print("\n=== CREATE S3 ACCESS KEY ===")
    key = await client.storage.object_storages.access_keys.create(storage_id=storage_id)
    print(f"Created new S3 access key for storage {storage_id}:")
    print(f"Access Key: {key.access_key}")
    print(f"Secret Key: {key.secret_key}")
    print("============================")
    return key.access_key


async def list_s3_access_keys(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== LIST S3 ACCESS KEYS ===")
    count = 1
    async for key in client.storage.object_storages.access_keys.list(storage_id=storage_id):
        print(f"  {count}. Access Key: {key.access_key}, Created: {key.created_at}")
        count += 1
    print("===========================")


async def delete_s3_access_key(*, client: AsyncGcore, storage_id: int, access_key: str) -> None:
    print("\n=== DELETE S3 ACCESS KEY ===")
    await client.storage.object_storages.access_keys.delete(access_key, storage_id=storage_id)
    print(f"Deleted access key: {access_key}")
    print("============================")


async def regenerate_sftp_password(*, client: AsyncGcore, sftp_storage_id: int) -> None:
    print("\n=== REGENERATE SFTP PASSWORD ===")
    storage = await client.storage.sftp_storages.update(
        storage_id=sftp_storage_id,
        password_mode="auto",
    )
    if storage.password:
        print(f"Generated new SFTP password for storage {sftp_storage_id}: {storage.password}")
    print("================================")


async def remove_sftp_password(*, client: AsyncGcore, sftp_storage_id: int) -> None:
    print("\n=== REMOVE SFTP PASSWORD ===")
    await client.storage.sftp_storages.update(
        storage_id=sftp_storage_id,
        password_mode="none",
    )
    print(f"Removed SFTP password for storage {sftp_storage_id}")
    print("============================")


async def reenable_sftp_password(*, client: AsyncGcore, sftp_storage_id: int) -> None:
    print("\n=== RE-ENABLE SFTP PASSWORD ===")
    storage = await client.storage.sftp_storages.update(
        storage_id=sftp_storage_id,
        password_mode="auto",
    )
    if storage.password:
        print(f"Re-enabled SFTP password for storage {sftp_storage_id}: {storage.password}")
    print("===============================")


async def delete_s3_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== DELETE S3 STORAGE ===")
    await client.storage.object_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("=========================")


async def delete_sftp_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== DELETE SFTP STORAGE ===")
    await client.storage.sftp_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("===========================")


if __name__ == "__main__":
    asyncio.run(main())
