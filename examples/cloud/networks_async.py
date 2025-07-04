import asyncio

from gcore import AsyncGcore


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

    network_id = await create_network(client=gcore)
    await list_networks(client=gcore)
    await get_network(client=gcore, network_id=network_id)
    await update_network(client=gcore, network_id=network_id)

    # Subnets
    subnet_id = await create_subnet(client=gcore, network_id=network_id)
    await list_subnets(client=gcore, network_id=network_id)
    await get_subnet(client=gcore, subnet_id=subnet_id)
    await update_subnet(client=gcore, subnet_id=subnet_id)

    # Routers
    router_id = await create_router(client=gcore)
    await list_routers(client=gcore)
    await get_router(client=gcore, router_id=router_id)
    await update_router(client=gcore, router_id=router_id)
    await attach_subnet_to_router(client=gcore, router_id=router_id, subnet_id=subnet_id)
    await detach_subnet_from_router(client=gcore, router_id=router_id, subnet_id=subnet_id)

    await delete_router(client=gcore, router_id=router_id)
    await delete_subnet(client=gcore, subnet_id=subnet_id)
    await delete_network(client=gcore, network_id=network_id)


async def create_network(*, client: AsyncGcore) -> str:
    print("\n=== CREATE NETWORK ===")
    response = await client.cloud.networks.create(name="gcore-go-example", create_router=True, type="vxlan")
    task_id = response.tasks[0]
    task = await client.cloud.tasks.poll(task_id=task_id)
    if task.created_resources is None or task.created_resources.networks is None:
        raise RuntimeError("Task completed but created_resources or networks is missing")
    network_id: str = task.created_resources.networks[0]
    print(f"Created network: ID={network_id}")
    print("========================")
    return network_id


async def list_networks(*, client: AsyncGcore) -> None:
    print("\n=== LIST NETWORKS ===")
    networks = await client.cloud.networks.list()
    count = 0
    async for network in networks:
        count += 1
        print(f"{count}. Network: ID={network.id}, name={network.name}, type={network.type}")
    print("========================")


async def get_network(*, client: AsyncGcore, network_id: str) -> None:
    print("\n=== GET NETWORK ===")
    network = await client.cloud.networks.get(network_id=network_id)
    print(f"Network: ID={network.id}, name={network.name}, type={network.type}")
    print("========================")


async def update_network(*, client: AsyncGcore, network_id: str) -> None:
    print("\n=== UPDATE NETWORK ===")
    network = await client.cloud.networks.update(network_id=network_id, name="gcore-go-example-updated")
    print(f"Updated network: ID={network.id}, name={network.name}")
    print("========================")


async def create_subnet(*, client: AsyncGcore, network_id: str) -> str:
    print("\n=== CREATE SUBNET ===")
    response = await client.cloud.networks.subnets.create(
        network_id=network_id,
        cidr="192.168.1.0/24",
        name="gcore-go-example",
        enable_dhcp=True,
        ip_version=4,
    )
    task_id = response.tasks[0]
    task = await client.cloud.tasks.poll(task_id=task_id)
    if task.created_resources is None or task.created_resources.subnets is None:
        raise RuntimeError("Task completed but created_resources or subnets is missing")
    subnet_id: str = task.created_resources.subnets[0]
    print(f"Created subnet: ID={subnet_id}")
    print("========================")
    return subnet_id


async def list_subnets(*, client: AsyncGcore, network_id: str) -> None:
    print("\n=== LIST SUBNETS ===")
    subnets = await client.cloud.networks.subnets.list(network_id=network_id)
    count = 0
    async for subnet in subnets:
        count += 1
        print(f"{count}. Subnet: ID={subnet.id}, CIDR={subnet.cidr}, name={subnet.name}")
    print("========================")


async def get_subnet(*, client: AsyncGcore, subnet_id: str) -> None:
    print("\n=== GET SUBNET ===")
    subnet = await client.cloud.networks.subnets.get(subnet_id=subnet_id)
    print(f"Subnet: ID={subnet.id}, CIDR={subnet.cidr}, name={subnet.name}")
    print("========================")


async def update_subnet(*, client: AsyncGcore, subnet_id: str) -> None:
    print("\n=== UPDATE SUBNET ===")
    subnet = await client.cloud.networks.subnets.update(subnet_id=subnet_id, name="gcore-go-example-updated")
    print(f"Updated subnet: ID={subnet.id}, name={subnet.name}")
    print("========================")


async def create_router(*, client: AsyncGcore) -> str:
    print("\n=== CREATE ROUTER ===")
    response = await client.cloud.networks.routers.create(name="gcore-go-example")
    task_id = response.tasks[0]
    task = await client.cloud.tasks.poll(task_id=task_id)
    if task.created_resources is None or task.created_resources.routers is None:
        raise RuntimeError("Task completed but created_resources or routers is missing")
    router_id: str = task.created_resources.routers[0]
    print(f"Created router: ID={router_id}")
    print("========================")
    return router_id


async def list_routers(*, client: AsyncGcore) -> None:
    print("\n=== LIST ROUTERS ===")
    routers = await client.cloud.networks.routers.list()
    count = 0
    async for router in routers:
        count += 1
        print(f"{count}. Router: ID={router.id}, name={router.name}, status={router.status}")
    print("========================")


async def get_router(*, client: AsyncGcore, router_id: str) -> None:
    print("\n=== GET ROUTER ===")
    router = await client.cloud.networks.routers.get(router_id=router_id)
    print(f"Router: ID={router.id}, name={router.name}, status={router.status}")
    print("========================")


async def update_router(*, client: AsyncGcore, router_id: str) -> None:
    print("\n=== UPDATE ROUTER ===")
    router = await client.cloud.networks.routers.update(router_id=router_id, name="gcore-go-example-updated")
    print(f"Updated router: ID={router.id}, name={router.name}")
    print("========================")


async def attach_subnet_to_router(*, client: AsyncGcore, router_id: str, subnet_id: str) -> None:
    print("\n=== ATTACH SUBNET TO ROUTER ===")
    router = await client.cloud.networks.routers.attach_subnet(router_id=router_id, subnet_id=subnet_id)
    print(f"Attached subnet {subnet_id} to router: ID={router.id}")
    print("========================")


async def detach_subnet_from_router(*, client: AsyncGcore, router_id: str, subnet_id: str) -> None:
    print("\n=== DETACH SUBNET FROM ROUTER ===")
    router = await client.cloud.networks.routers.detach_subnet(router_id=router_id, subnet_id=subnet_id)
    print(f"Detached subnet {subnet_id} from router: ID={router.id}")
    print("========================")


async def delete_router(*, client: AsyncGcore, router_id: str) -> None:
    print("\n=== DELETE ROUTER ===")
    response = await client.cloud.networks.routers.delete(router_id=router_id)
    task_id = response.tasks[0]
    await client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted router: ID={router_id}")
    print("========================")


async def delete_subnet(*, client: AsyncGcore, subnet_id: str) -> None:
    print("\n=== DELETE SUBNET ===")
    await client.cloud.networks.subnets.delete(subnet_id=subnet_id)
    print(f"Deleted subnet: ID={subnet_id}")
    print("========================")


async def delete_network(*, client: AsyncGcore, network_id: str) -> None:
    print("\n=== DELETE NETWORK ===")
    response = await client.cloud.networks.delete(network_id=network_id)
    task_id = response.tasks[0]
    await client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted network: ID={network_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
