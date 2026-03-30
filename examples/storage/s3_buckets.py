from __future__ import annotations

import time

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    storage_id = create_s3_storage(client=gcore)
    wait_for_storage_provisioning(client=gcore, storage_id=storage_id)

    bucket_name = create_bucket(client=gcore, storage_id=storage_id)
    list_buckets(client=gcore, storage_id=storage_id)
    get_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    set_bucket_lifecycle(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    set_bucket_cors(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    set_bucket_policy(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    get_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    delete_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)

    delete_storage(client=gcore, storage_id=storage_id)


def create_s3_storage(*, client: Gcore) -> int:
    print("\n=== CREATE S3 STORAGE ===")
    storage_name = f"s3-bucket-example-{int(time.time())}"
    storage = client.storage.object_storages.create(
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


def wait_for_storage_provisioning(*, client: Gcore, storage_id: int) -> None:
    print("\n=== WAIT FOR STORAGE PROVISIONING ===")
    max_wait = 30
    wait_interval = 2
    elapsed = 0
    while elapsed < max_wait:
        storage = client.storage.object_storages.get(storage_id=storage_id)
        if storage.provisioning_status == "active":
            print(f"Storage {storage_id} is ready")
            print("=====================================")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        time.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready, proceeding anyway...")
    print("=====================================")


def create_bucket(*, client: Gcore, storage_id: int) -> str:
    print("\n=== CREATE BUCKET ===")
    timestamp = int(time.time())
    bucket_name = f"example-bucket-{timestamp}"
    bucket = client.storage.object_storages.buckets.create(
        storage_id=storage_id,
        name=bucket_name,
    )
    print(f"Created bucket: {bucket.name}")
    print("=====================")
    return bucket_name


def list_buckets(*, client: Gcore, storage_id: int) -> None:
    print("\n=== LIST BUCKETS ===")
    for count, bucket in enumerate(client.storage.object_storages.buckets.list(storage_id=storage_id), 1):
        lifecycle_info = (
            f", Lifecycle: {bucket.lifecycle.expiration_days} days"
            if bucket.lifecycle.expiration_days > 0
            else ""
        )
        print(f"  {count}. Bucket: Name={bucket.name}{lifecycle_info}")
    print("====================")


def get_bucket(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== GET BUCKET ===")
    bucket = client.storage.object_storages.buckets.get(bucket_name, storage_id=storage_id)
    print(f"Bucket: Name={bucket.name}")
    if bucket.lifecycle:
        print(f"  Lifecycle: {bucket.lifecycle.expiration_days} days")
    if bucket.cors:
        print(f"  CORS origins: {bucket.cors.allowed_origins}")
    if bucket.policy:
        print(f"  Policy public: {bucket.policy.is_public}")
    print("==================")


def set_bucket_lifecycle(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET LIFECYCLE ===")
    client.storage.object_storages.buckets.update(
        bucket_name,
        storage_id=storage_id,
        lifecycle={"expiration_days": 30},
    )
    print(f"Set lifecycle policy for bucket {bucket_name}: objects expire after 30 days")
    print("============================")


def set_bucket_cors(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET CORS ===")
    client.storage.object_storages.buckets.update(
        bucket_name,
        storage_id=storage_id,
        cors={"allowed_origins": ["*"]},
    )
    print(f"Set CORS policy for bucket {bucket_name} with origins: ['*']")
    print("=======================")


def set_bucket_policy(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET POLICY ===")
    client.storage.object_storages.buckets.update(
        bucket_name,
        storage_id=storage_id,
        policy={"is_public": True},
    )
    print(f"Set public read policy for bucket {bucket_name}")
    print("=========================")


def delete_bucket(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== DELETE BUCKET ===")
    client.storage.object_storages.buckets.delete(
        bucket_name,
        storage_id=storage_id,
    )
    print(f"Deleted bucket: {bucket_name}")
    print("=====================")


def delete_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    client.storage.object_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    main()
