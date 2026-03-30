from __future__ import annotations

import time
import asyncio

from gcore import AsyncGcore, NotFoundError


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    # Create SSH keys
    ts = int(time.time())
    key1_id = await create_ssh_key(client=gcore, name=f"example-key-1-{ts}")
    key2_id = await create_ssh_key(client=gcore, name=f"example-key-2-{ts}")
    await list_ssh_keys(client=gcore)
    await get_ssh_key(client=gcore, key_id=key1_id)

    # Create an SFTP storage associated with the SSH keys
    sftp_storage_id = await create_sftp_storage_with_keys(client=gcore, ssh_key_ids=[key1_id, key2_id])
    await wait_for_storage_provisioning(client=gcore, storage_id=sftp_storage_id)

    # Update the storage to only use the first key
    await update_storage_ssh_keys(client=gcore, storage_id=sftp_storage_id, ssh_key_ids=[key1_id])

    # Cleanup
    await cleanup(client=gcore, storage_id=sftp_storage_id, key_ids=[key1_id, key2_id])


async def create_ssh_key(*, client: AsyncGcore, name: str) -> int:
    print(f"\n=== CREATE SSH KEY: {name} ===")
    key = await client.storage.ssh_keys.create(
        name=name,
        public_key=_generate_temp_ssh_key(),
    )
    print(f"Created SSH Key: ID={key.id}, Name={key.name}")
    print("==========================")
    return key.id


async def list_ssh_keys(*, client: AsyncGcore) -> None:
    print("\n=== LIST SSH KEYS ===")
    count = 1
    async for key in client.storage.ssh_keys.list():
        print(f"  {count}. ID={key.id}, Name={key.name}, Created={key.created_at}")
        count += 1
    print("=====================")


async def get_ssh_key(*, client: AsyncGcore, key_id: int) -> None:
    print("\n=== GET SSH KEY ===")
    key = await client.storage.ssh_keys.get(ssh_key_id=key_id)
    print(f"SSH Key: ID={key.id}, Name={key.name}, Created={key.created_at}")
    print(f"Public Key: {key.public_key[:50]}...")
    print("==================")


async def create_sftp_storage_with_keys(*, client: AsyncGcore, ssh_key_ids: list[int]) -> int:
    print("\n=== CREATE SFTP STORAGE WITH SSH KEYS ===")
    name = f"sftp-ssh-{int(time.time())}"
    storage = await client.storage.sftp_storages.create(
        name=name,
        location_name="ams",
        password_mode="none",
        ssh_key_ids=ssh_key_ids,
    )
    print(f"Created Storage: ID={storage.id}, Name={storage.name}, Location={storage.location_name}")
    print(f"SSH Key IDs: {storage.ssh_key_ids}")
    print(f"Has Password: {storage.has_password} (SSH-key-only access)")
    print("=========================================")
    return storage.id


async def wait_for_storage_provisioning(*, client: AsyncGcore, storage_id: int) -> None:
    print("\n=== WAIT FOR STORAGE PROVISIONING ===")
    max_wait = 30
    wait_interval = 2
    elapsed = 0
    while elapsed < max_wait:
        storage = await client.storage.sftp_storages.get(storage_id=storage_id)
        if storage.provisioning_status == "active":
            print(f"Storage {storage_id} is ready")
            print("=====================================")
            return
        print(f"Storage {storage_id} status: {storage.provisioning_status}, waiting...")
        await asyncio.sleep(wait_interval)
        elapsed += wait_interval
    print(f"Storage {storage_id} not ready, proceeding anyway...")
    print("=====================================")


async def update_storage_ssh_keys(*, client: AsyncGcore, storage_id: int, ssh_key_ids: list[int]) -> None:
    print("\n=== UPDATE STORAGE SSH KEYS ===")
    storage = await client.storage.sftp_storages.update(
        storage_id=storage_id,
        ssh_key_ids=ssh_key_ids,
    )
    print(f"Updated storage {storage_id} SSH keys: {storage.ssh_key_ids}")
    print("==============================")


async def cleanup(*, client: AsyncGcore, storage_id: int, key_ids: list[int]) -> None:
    print("\n=== CLEANUP ===")

    # Delete the SFTP storage
    await client.storage.sftp_storages.delete(storage_id=storage_id)
    print(f"Storage {storage_id} delete requested, waiting for completion...")

    # Poll until the storage is fully deleted
    for _ in range(30):
        await asyncio.sleep(2)
        try:
            await client.storage.sftp_storages.get(storage_id=storage_id)
        except NotFoundError:
            print(f"Storage {storage_id} deleted successfully")
            break

    # Delete the SSH keys
    for key_id in key_ids:
        await client.storage.ssh_keys.delete(ssh_key_id=key_id)
        print(f"SSH key {key_id} deleted successfully")

    print("===============")


def _generate_temp_ssh_key() -> str:
    """Generate a temporary ed25519 SSH public key for the example.

    In production, you would use your own pre-existing SSH public key.
    """
    import os
    import base64
    import struct

    # Generate a random 32-byte ed25519 public key (for demo purposes only)
    key_type = b"ssh-ed25519"
    raw_key = os.urandom(32)
    blob = struct.pack(">I", len(key_type)) + key_type + struct.pack(">I", len(raw_key)) + raw_key
    return f"ssh-ed25519 {base64.b64encode(blob).decode()} example@demo"


if __name__ == "__main__":
    asyncio.run(main())
