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
    set_bucket_lifecycle(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    set_bucket_cors(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    set_bucket_policy(client=gcore, storage_id=storage_id, bucket_name=bucket_name)
    list_buckets(client=gcore, storage_id=storage_id)
    delete_bucket(client=gcore, storage_id=storage_id, bucket_name=bucket_name)

    delete_storage(client=gcore, storage_id=storage_id)


def create_s3_storage(*, client: Gcore) -> int:
    print("\n=== CREATE S3 STORAGE ===")
    storage_name = f"s3-bucket-example-{int(time.time())}"
    storage = client.storage.create(
        name=storage_name,
        type="s3",
        location="s-ed1",
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}")
    print(f"Storage address: {storage.address}")
    print(f"S3 Access Key: {storage.credentials.s3.access_key}")  # type: ignore[union-attr]
    print(f"S3 Secret Key: {storage.credentials.s3.secret_key}")  # type: ignore[union-attr]
    print("=========================")
    return storage.id


def wait_for_storage_provisioning(*, client: Gcore, storage_id: int) -> None:
    print("\n=== WAIT FOR STORAGE PROVISIONING ===")
    max_wait = 30
    wait_interval = 2
    elapsed = 0
    while elapsed < max_wait:
        storage = client.storage.get(storage_id=storage_id)
        if storage.provisioning_status == "ok":
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
    client.storage.buckets.create(
        bucket_name=bucket_name,
        storage_id=storage_id,
    )
    print(f"Created bucket: {bucket_name}")
    print("=====================")
    return bucket_name


def list_buckets(*, client: Gcore, storage_id: int) -> None:
    print("\n=== LIST BUCKETS ===")
    buckets = client.storage.buckets.list(storage_id=storage_id)
    for count, bucket in enumerate(buckets, 1):
        lifecycle_info = f", Lifecycle: {bucket.lifecycle} days" if bucket.lifecycle and bucket.lifecycle > 0 else ""
        print(f"  {count}. Bucket: Name={bucket.name}{lifecycle_info}")
    print("====================")


def set_bucket_lifecycle(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET LIFECYCLE ===")
    client.storage.buckets.lifecycle.create(
        bucket_name=bucket_name,
        storage_id=storage_id,
        expiration_days=30,
    )
    print(f"Set lifecycle policy for bucket {bucket_name}: objects expire after 30 days")
    print("============================")


def set_bucket_cors(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET CORS ===")
    client.storage.buckets.cors.create(
        bucket_name=bucket_name,
        storage_id=storage_id,
        allowed_origins=["*"],
    )
    print(f"Set CORS policy for bucket {bucket_name} with origins: ['*']")
    print("=======================")


def set_bucket_policy(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== SET BUCKET POLICY ===")
    client.storage.buckets.policy.create(
        bucket_name=bucket_name,
        storage_id=storage_id,
    )
    print(f"Set public read policy for bucket {bucket_name}")
    print("=========================")


def delete_bucket(*, client: Gcore, storage_id: int, bucket_name: str) -> None:
    print("\n=== DELETE BUCKET ===")
    client.storage.buckets.delete(
        bucket_name=bucket_name,
        storage_id=storage_id,
    )
    print(f"Deleted bucket: {bucket_name}")
    print("=====================")


def delete_storage(*, client: Gcore, storage_id: int) -> None:
    print("\n=== DELETE STORAGE ===")
    client.storage.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    main()
