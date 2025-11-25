import time

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    # S3
    s3_storage_id = create_s3_storage(client=gcore)
    get_storage(client=gcore, storage_id=s3_storage_id)
    generate_s3_keys(client=gcore, s3_storage_id=s3_storage_id)
    delete_storage(client=gcore, storage_id=s3_storage_id)

    # SFTP storage operations
    sftp_storage_id = create_sftp_storage(client=gcore)
    get_storage(client=gcore, storage_id=sftp_storage_id)
    generate_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    delete_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    set_custom_sftp_password(client=gcore, sftp_storage_id=sftp_storage_id)
    delete_storage(client=gcore, storage_id=sftp_storage_id)


def create_s3_storage(*, client: Gcore) -> int:
    print("\n=== CREATE S3 STORAGE ===")
    s3_name = f"s3-creds-example-{int(time.time())}"
    storage = client.storage.create(
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


def create_sftp_storage(*, client: Gcore) -> int:
    print("\n=== CREATE SFTP STORAGE ===")
    sftp_name = f"sftp-ex-{int(time.time()) % 1000000}"
    storage = client.storage.create(
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


def wait_for_storage_provisioning(
    *, client: Gcore, storage_id: int, max_wait: int = 30, wait_interval: int = 2
) -> None:
    """Wait for a single storage to be provisioned"""
    elapsed = 0
    while elapsed < max_wait:
        storage = client.storage.get(storage_id=storage_id)
        if storage.provisioning_status == "ok":
            print(f"Storage {storage_id} is ready")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        time.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready after {max_wait}s")


def get_storage(*, client: Gcore, storage_id: int) -> None:
    """Get and display details for a single storage"""
    print("\n=== GET STORAGE DETAILS ===")
    storage = client.storage.get(storage_id=storage_id)
    print(
        f"Storage: ID={storage.id}, Name={storage.name}, Type={storage.type}, Location={storage.location}, Status={storage.provisioning_status}"
    )
    print(f"Address: {storage.address}, Created: {storage.created_at}, Can Restore: {storage.can_restore}")
    print("===========================")


def generate_s3_keys(*, client: Gcore, s3_storage_id: int) -> None:
    print("\n=== GENERATE S3 KEYS ===")
    storage = client.storage.credentials.recreate(
        storage_id=s3_storage_id,
        generate_s3_keys=True,
    )
    if storage.credentials and storage.credentials.s3:
        print(f"Generated new S3 keys for storage {s3_storage_id}")
        print(f"Access Key: {storage.credentials.s3.access_key}")
        print(f"Secret Key: {storage.credentials.s3.secret_key}")
    print("========================")


def generate_sftp_password(*, client: Gcore, sftp_storage_id: int) -> None:
    print("\n=== GENERATE SFTP PASSWORD ===")
    storage = client.storage.credentials.recreate(
        storage_id=sftp_storage_id,
        generate_sftp_password=True,
    )
    if storage.credentials and storage.credentials.sftp_password:
        print(f"Generated SFTP password for storage {sftp_storage_id}: {storage.credentials.sftp_password}")
    print("==============================")


def set_custom_sftp_password(*, client: Gcore, sftp_storage_id: int) -> None:
    print("\n=== SET CUSTOM SFTP PASSWORD ===")
    custom_password = "MyNewSecurePassword456!"
    client.storage.credentials.recreate(
        storage_id=sftp_storage_id,
        sftp_password=custom_password,
    )
    print(f"Set custom SFTP password for storage {sftp_storage_id}: {custom_password}")
    print("================================")


def delete_sftp_password(*, client: Gcore, sftp_storage_id: int) -> None:
    print("\n=== DELETE SFTP PASSWORD ===")
    client.storage.credentials.recreate(
        storage_id=sftp_storage_id,
        delete_sftp_password=True,
    )
    print(f"Deleted SFTP password for storage {sftp_storage_id}")
    print("============================")


def delete_storage(*, client: Gcore, storage_id: int) -> None:
    """Delete a single storage"""
    print("\n=== DELETE STORAGE ===")
    client.storage.delete(storage_id=storage_id)
    print(f"Storage {storage_id} deleted successfully")
    print("======================")


if __name__ == "__main__":
    main()
