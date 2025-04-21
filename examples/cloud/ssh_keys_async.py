import os
import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import SSHKey, SSHKeyCreated


async def get_ssh_key_by_id(ssh_key_id: str) -> SSHKey:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    ssh_key = await gcore.cloud.ssh_keys.get(ssh_key_id=ssh_key_id)

    print("\n=== GET SSH KEY BY ID ===")
    print(f"SSH Key ID: {ssh_key.id}, Name: {ssh_key.name}, Fingerprint: {ssh_key.fingerprint}")
    print("==========================")
    return ssh_key


async def list_all_ssh_keys() -> AsyncOffsetPage[SSHKey]:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_ssh_keys = await gcore.cloud.ssh_keys.list()

    print("\n=== LIST ALL SSH KEYS ===")
    count = 1
    async for ssh_key in all_ssh_keys:
        print(f"  {count}. SSH Key ID: {ssh_key.id}, Name: {ssh_key.name}")
        count += 1
    print("==========================")
    return all_ssh_keys


async def create_new_ssh_key() -> SSHKeyCreated:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Sample SSH key values
    ssh_key_name = "Example SSH Key"
    
    new_ssh_key = await gcore.cloud.ssh_keys.create(name=ssh_key_name)

    print("\n=== CREATE NEW SSH KEY ===")
    print(f"SSH Key ID: {new_ssh_key.id}, Name: {new_ssh_key.name}")
    print("===========================")
    return new_ssh_key


async def update_ssh_key(ssh_key_id: str) -> SSHKey:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    updated_ssh_key = await gcore.cloud.ssh_keys.update(ssh_key_id=ssh_key_id, shared_in_project=True)

    print("\n=== UPDATE SSH KEY ===")
    print(f"SSH Key ID: {updated_ssh_key.id}, SharedInProject: {updated_ssh_key.shared_in_project}")
    print("=======================")
    return updated_ssh_key


async def delete_ssh_key(ssh_key_id: str) -> None:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    await gcore.cloud.ssh_keys.delete(ssh_key_id=ssh_key_id)

    print("\n=== DELETE SSH KEY ===")
    print(f"SSH Key ID: {ssh_key_id} has been deleted")
    print("=======================")


async def main() -> None:
    # Follow the order: create, list, get, update, delete
    new_ssh_key = await create_new_ssh_key()
    await list_all_ssh_keys()
    await get_ssh_key_by_id(new_ssh_key.id)
    await update_ssh_key(ssh_key_id=new_ssh_key.id)
    await delete_ssh_key(ssh_key_id=new_ssh_key.id)


if __name__ == "__main__":
    asyncio.run(main())
