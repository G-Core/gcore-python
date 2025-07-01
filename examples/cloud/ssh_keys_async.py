import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import SSHKey, SSHKeyCreated


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    ssh_key = await create_ssh_key(client=gcore)
    await list_ssh_keys(client=gcore)
    await get_ssh_key(client=gcore, ssh_key_id=ssh_key.id)
    await update_ssh_key(client=gcore, ssh_key_id=ssh_key.id)
    await delete_ssh_key(client=gcore, ssh_key_id=ssh_key.id)


async def create_ssh_key(*, client: AsyncGcore) -> SSHKeyCreated:
    print("\n=== CREATE SSH KEY ===")
    ssh_key = await client.cloud.ssh_keys.create(name="gcore-go-example")
    print(f"Created SSH key: ID={ssh_key.id}, name={ssh_key.name}")
    print("========================")
    return ssh_key


async def list_ssh_keys(*, client: AsyncGcore) -> AsyncOffsetPage[SSHKey]:
    print("\n=== LIST SSH KEYS ===")
    ssh_keys = await client.cloud.ssh_keys.list()
    count = 1
    async for ssh_key in ssh_keys:
        print(f"  {count}. SSH key: ID={ssh_key.id}, name={ssh_key.name}")
        count += 1
    print("========================")
    return ssh_keys


async def get_ssh_key(*, client: AsyncGcore, ssh_key_id: str) -> SSHKey:
    print("\n=== GET SSH KEY ===")
    ssh_key = await client.cloud.ssh_keys.get(ssh_key_id=ssh_key_id)
    print(f"SSH key: ID={ssh_key.id}, name={ssh_key.name}, fingerprint={ssh_key.fingerprint}")
    print("========================")
    return ssh_key


async def update_ssh_key(*, client: AsyncGcore, ssh_key_id: str) -> SSHKey:
    print("\n=== UPDATE SSH KEY ===")
    updated_ssh_key = await client.cloud.ssh_keys.update(ssh_key_id=ssh_key_id, shared_in_project=True)
    print(f"Updated SSH key: ID={updated_ssh_key.id}, name={updated_ssh_key.name}")
    print("========================")
    return updated_ssh_key


async def delete_ssh_key(*, client: AsyncGcore, ssh_key_id: str) -> None:
    print("\n=== DELETE SSH KEY ===")
    await client.cloud.ssh_keys.delete(ssh_key_id=ssh_key_id)
    print(f"Deleted SSH key: ID={ssh_key_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
