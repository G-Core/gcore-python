from __future__ import annotations

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

    storage_id = await create_s3_storage(client=gcore)
    await wait_for_storage_provisioning(client=gcore, storage_id=storage_id)

    bucket_name = await create_bucket(client=gcore, storage_id=storage_id)
    await list_buckets(client=gcore, storage_id=storage_id)
    await get_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    await set_bucket_lifecycle(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    await set_bucket_cors(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    await set_bucket_policy(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    await get_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    await delete_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    await delete_storage(client=gcore, storage_id=storage_id)


async def create_s3_storage(*, client: AsyncGcore) -> int:
    print("\n=== CREATE S3 STORAGE ===")
    storage_name = f"s3-bucket-example-{int(time.time())}"
    storage = await client.storage.object_storages.create(
        name=storage_name,
        location_name="s-ed1",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}")
    print(f"Storage address: {storage.address}")
    if storage.access_keys:
        print(f"S3 Access Key: {storage.access_keys[0].access_key}")
        print(f"S3 Secret Key: {storage.access_keys[0].secret_key}")
    print("=========================")
    return storage.id


async def wait_for_storage_provisioning(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== WAIT FOR STORAGE PROVISIONING ===")
    max_wait = 30
    wait_interval = 2
    elapsed = 0
    while elapsed < max_wait:
        storage = await client.storage.object_storages.get(storage_id=storage_id)
        if storage.provisioning_status == "active":
            print(f"Storage {storage_id} is ready")
            print("=====================================")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        await asyncio.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready, proceeding anyway...")
    print("=====================================")


async def create_bucket(*, client: AsyncGcore, storage_id: int) -> str:
    print("\n=== CREATE BUCKET ===")
    timestamp = int(time.time())
    bucket_name = f"example-bucket-{timestamp}"
    bucket = await client.storage.object_storages.buckets.create(
        storage_id=storage_id,
        name=bucket_name,
    )
    print(f"Created bucket: {bucket.name}")
    print("=====================")
    return bucket_name


async def list_buckets(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== LIST BUCKETS ===")
    count = 1
    async for bucket in client.storage.object_storages.buckets.list(storage_id=storage_id):
        lifecycle_info = (
            f", Lifecycle: {bucket.lifecycle.expiration_days} days"
            if bucket.lifecycle.expiration_days > 0
            else ""
        )
        print(f"  {count}. Bucket: Name={bucket.name}{lifecycle_info}")
        count += 1
    print("====================")


async def get_bucket(*, client: AsyncGcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== GET BUCKET ===")
    bucket = await client.storage.object_storages.buckets.get(bucket_name, storage_id=storage_id)
    print(f"Bucket: Name={bucket.name}")
    if bucket.lifecycle:
        print(f"  Lifecycle: {bucket.lifecycle.expiration_days} days")
    if bucket.cors:
        print(f"  CORS origins: {bucket.cors.allowed_origins}")
    if bucket.policy:
        print(f"  Policy public: {bucket.policy.is_public}")
    print("==================")


async def set_bucket_lifecycle(*, client: AsyncGcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET LIFECYCLE ===")
    await client.storage.object_storages.buckets.update(
        bucket_name,
        storage_id=storage_id,
        lifecycle={"expiration_days": 30},
    )
    print(f"Set lifecycle policy for bucket {bucket_name}: objects expire after 30 days")
    print("============================")


async def set_bucket_cors(*, client: AsyncGcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET CORS ===")
    await client.storage.object_storages.buckets.update(
        bucket_name,
        storage_id=storage_id,
        cors={"allowed_origins": ["*"]},
    )
    print(f"Set CORS policy for bucket {bucket_name} with origins: ['*']")
    print("=======================")


async def set_bucket_policy(*, client: AsyncGcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET POLICY ===")
    await client.storage.object_storages.buckets.update(
        bucket_name,
        storage_id=storage_id,
        policy={"is_public": True},
    )
    print(f"Set public read policy for bucket {bucket_name}")
    print("=========================")


async def delete_bucket(*, client: AsyncGcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== DELETE BUCKET ===")
    await client.storage.object_storages.buckets.delete(
        bucket_name,
        storage_id=storage_id,
    )
    print(f"Deleted bucket: {bucket_name}")
    print("=====================")


async def delete_storage(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    await client.storage.object_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    asyncio.run(main())
