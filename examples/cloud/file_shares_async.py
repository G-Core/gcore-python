import os
import asyncio

from gcore import AsyncGcore
from gcore.types.cloud.file_share_create_params import CreateStandardFileShareSerializerNetwork


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set cloud network ID before running
    cloud_network_id = os.environ["GCORE_CLOUD_NETWORK_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    fs_id = await create_file_share(client=gcore, network_id=cloud_network_id)
    await list_file_shares(client=gcore)
    await get_file_share(client=gcore, file_share_id=fs_id)
    await update_file_share(client=gcore, file_share_id=fs_id)
    await resize_file_share(client=gcore, file_share_id=fs_id)

    # Access rules
    access_rule_id = await create_file_share_access_rule(client=gcore, file_share_id=fs_id)
    await list_file_share_access_rules(client=gcore, file_share_id=fs_id)
    await delete_file_share_access_rule(client=gcore, file_share_id=fs_id, access_rule_id=access_rule_id)

    await delete_file_share(client=gcore, file_share_id=fs_id)


async def create_file_share(client: AsyncGcore, *, network_id: str) -> str:
    print("\n=== CREATE FILE SHARE ===")
    network = CreateStandardFileShareSerializerNetwork(network_id=network_id)
    response = await client.cloud.file_shares.create(
        name="gcore-go-example",
        network=network,
        protocol="NFS",
        size=1,
    )
    task = await client.cloud.tasks.poll(task_id=response.tasks[0])
    if task.created_resources is None or task.created_resources.file_shares is None:
        raise RuntimeError("Task completed but created_resources or file_shares is missing")
    file_share_id: str = task.created_resources.file_shares[0]
    print(f"Created file share: ID={file_share_id}")
    print("========================")
    return file_share_id


async def list_file_shares(*, client: AsyncGcore) -> None:
    print("\n=== LIST FILE SHARES ===")
    file_shares = await client.cloud.file_shares.list()
    count = 0
    async for file_share in file_shares:
        count += 1
        print(f"{count}. File share: ID={file_share.id}, name={file_share.name}, size={file_share.size} GiB")
    print("========================")


async def get_file_share(*, client: AsyncGcore, file_share_id: str) -> None:
    print("\n=== GET FILE SHARE ===")
    file_share = await client.cloud.file_shares.get(file_share_id=file_share_id)
    print(f"File share: ID={file_share.id}, name={file_share.name}, size={file_share.size} GiB")
    print("========================")


async def update_file_share(*, client: AsyncGcore, file_share_id: str) -> None:
    print("\n=== UPDATE FILE SHARE ===")
    file_share = await client.cloud.file_shares.update_and_poll(
        file_share_id=file_share_id,
        name="gcore-go-example-updated",
    )
    print(f"Updated file share: ID={file_share.id}, name={file_share.name}")
    print("========================")


async def resize_file_share(*, client: AsyncGcore, file_share_id: str) -> None:
    print("\n=== RESIZE FILE SHARE ===")
    response = await client.cloud.file_shares.resize(file_share_id=file_share_id, size=2)
    task_id = response.tasks[0]
    await client.cloud.tasks.poll(task_id=task_id)
    print(f"Resized file share: ID={file_share_id}, size=2 GiB")
    print("========================")


async def create_file_share_access_rule(*, client: AsyncGcore, file_share_id: str) -> str:
    print("\n=== CREATE FILE SHARE ACCESS RULE ===")
    access_rule = await client.cloud.file_shares.access_rules.create(
        file_share_id=file_share_id,
        access_mode="ro",
        ip_address="192.168.1.0/24",
    )
    print(
        f"Created access rule: ID={access_rule.id}, access level={access_rule.access_level}, access to={access_rule.access_to}, state={access_rule.state}"
    )
    print("========================")
    return access_rule.id


async def list_file_share_access_rules(*, client: AsyncGcore, file_share_id: str) -> None:
    print("\n=== LIST FILE SHARE ACCESS RULES ===")
    access_rules = await client.cloud.file_shares.access_rules.list(file_share_id=file_share_id)
    for count, rule in enumerate(access_rules.results, 1):
        print(
            f"{count}. Access rule: ID={rule.id}, access level={rule.access_level}, access to={rule.access_to}, state={rule.state}"
        )
    print("========================")


async def delete_file_share_access_rule(*, client: AsyncGcore, file_share_id: str, access_rule_id: str) -> None:
    print("\n=== DELETE FILE SHARE ACCESS RULE ===")
    await client.cloud.file_shares.access_rules.delete(
        access_rule_id=access_rule_id,
        file_share_id=file_share_id,
    )
    print(f"Deleted access rule: ID={access_rule_id}")
    print("========================")


async def delete_file_share(*, client: AsyncGcore, file_share_id: str) -> None:
    print("\n=== DELETE FILE SHARE ===")
    response = await client.cloud.file_shares.delete(file_share_id=file_share_id)
    task_id = response.tasks[0]
    await client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted file share: ID={file_share_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
