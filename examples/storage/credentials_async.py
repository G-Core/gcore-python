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

    # S3
    s3_storage_id = await create_s3_storage(client=gcore)
    await get_storage(client=gcore, storage_id=s3_storage_id)
    await generate_s3_keys(client=gcore, s3_storage_id=s3_storage_id)
    await delete_storage(client=gcore, storage_id=s3_storage_id)

    # SFTP storage operations
    sftp_storage_id = await create_sftp_storage(client=gcore)
    await get_storage(client=gcore, storage_id=sftp_storage_id)
    await generate_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    await delete_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    await set_custom_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    await delete_storage(client=gcore, storage_id=sftp_storage_id)


async def create_s3_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE S3 STORAGE ===")
    s3_name = f"s3-creds-example-{int(time.time())}"
    storage = await client.storage.create(
        name=s3_name,
        type="s3",
        location="s-ed1",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}")
    print(f"Storage address: {storage.address}")
    if storage.credentials and storage.credentials.s3:
        print(f"S3 Access Key: {storage.credentials.s3.access_key}")
        print(f"S3 Secret Key: {storage.credentials.s3.secret_key}")
    print("=========================")
    return storage.id


async def create_sftp_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE SFTP STORAGE ===")
    sftp_name = f"sftp-ex-{int(time.time()) % 1000000}"
    storage = await client.storage.create(
        name=sftp_name,
        type="sftp",
        location="ams",
        generate_sftp_password=True,
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}")
    print(f"Storage address: {storage.address}")
    if storage.credentials and storage.credentials.sftp_password:
        print(f"SFTP Password: {storage.credentials.sftp_password}")
    print("==========================")
    return storage.id


async def wait_for_storage_provisioning(
    *, client: AsyncGcore, storage_id: int, max_wait: int = 30, wait_interval: int = 2
) -> None:
    """Wait for a single storage to be provisioned"""
    elapsed = 0
    while elapsed < max_wait:
        storage = await client.storage.get(storage_id=storage_id)
        if storage.provisioning_status == "ok":
            print(f"Storage {storage_id} is ready")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        await asyncio.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready after {max_wait}s")


async def get_storage(*, client: AsyncGcore, storage_id: int) -> None:
    """Get and display details for a single storage"""
    print("\n=== GET STORAGE DETAILS ===")
    storage = await client.storage.get(storage_id=storage_id)
    print(
        f"Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}, Can Restore: {storage.can_restore}")
    print("===========================")


async def generate_s3_keys(*, client: AsyncGcore, s3_storage_id: int) -> None:
    print("\n=== GENERATE S3 KEYS ===")
    storage = await client.storage.credentials.recreate(
        storage_id=s3_storage_id,
        generate_s3_keys=True,
    )
    if storage.credentials and storage.credentials.s3:
        print(f"Generated new S3 keys for storage {s3_storage_id}")
        print(f"Access Key: {storage.credentials.s3.access_key}")
        print(f"Secret Key: {storage.credentials.s3.secret_key}")
    print("========================")


async def generate_sftp_password(*, client: AsyncGcore, sftp_storage_id: int) -> None:
    print("\n=== GENERATE SFTP PASSWORD ===")
    storage = await client.storage.credentials.recreate(
        storage_id=sftp_storage_id,
        generate_sftp_password=True,
    )
    if storage.credentials and storage.credentials.sftp_password:
        print(f"Generated SFTP password for storage {sftp_storage_id}: {storage.credentials.sftp_password}")
    print("==============================")


async def set_custom_sftp_password(*, client: AsyncGcore, sftp_storage_id: int) -> None:
    print("\n=== SET CUSTOM SFTP PASSWORD ===")
    custom_password = "MyNewSecurePassword456!"
    await client.storage.credentials.recreate(
        storage_id=sftp_storage_id,
        sftp_password=custom_password,
    )
    print(f"Set custom SFTP password for storage {sftp_storage_id}: {custom_password}")
    print("================================")


async def delete_sftp_password(*, client: AsyncGcore, sftp_storage_id: int) -> None:
    print("\n=== DELETE SFTP PASSWORD ===")
    await client.storage.credentials.recreate(
        storage_id=sftp_storage_id,
        delete_sftp_password=True,
    )
    print(f"Deleted SFTP password for storage {sftp_storage_id}")
    print("============================")


async def delete_storage(*, client: AsyncGcore, storage_id: int) -> None:
    """Delete a single storage"""
    print("\n=== DELETE STORAGE ===")
    await client.storage.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    asyncio.run(main())
