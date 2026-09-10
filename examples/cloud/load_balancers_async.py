from __future__ import annotations

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

    lb_id = await create_load_balancer(client=gcore)
    await list_load_balancers(client=gcore)
    await get_load_balancer(client=gcore, load_balancer_id=lb_id)
    await update_load_balancer(client=gcore, load_balancer_id=lb_id)
    await resize_load_balancer(client=gcore, load_balancer_id=lb_id)
    await failover_load_balancer(client=gcore, load_balancer_id=lb_id)

    # Pools and members
    pool_id = await create_pool(client=gcore, load_balancer_id=lb_id)
    await list_pools(client=gcore)
    member_id = await create_pool_member(client=gcore, pool_id=pool_id)
    await list_pool_members(client=gcore, pool_id=pool_id)
    await get_pool_member(client=gcore, pool_id=pool_id, member_id=member_id)
    await update_pool_member(client=gcore, pool_id=pool_id, member_id=member_id)
    await delete_pool_member(client=gcore, pool_id=pool_id, member_id=member_id)
    await delete_pool(client=gcore, pool_id=pool_id)

    # Statuses
    await list_load_balancer_statuses(client=gcore)
    await get_load_balancer_status(client=gcore, load_balancer_id=lb_id)

    # Metrics
    await get_load_balancer_metrics(client=gcore, load_balancer_id=lb_id)

    await delete_load_balancer(client=gcore, load_balancer_id=lb_id)


async def create_load_balancer(*, client: AsyncGcore) -> str:
    print("\n=== CREATE LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.create_and_poll(flavor="lb1-1-2", name="gcore-go-example")
    print(f"Created load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}")
    print("========================")
    return lb.id


async def list_load_balancers(*, client: AsyncGcore) -> None:
    print("\n=== LIST LOAD BALANCERS ===")
    load_balancers = await client.cloud.load_balancers.list()
    count = 1
    async for lb in load_balancers:
        print(f"{count}. Load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}")
        count += 1
    print("========================")


async def get_load_balancer(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.get(load_balancer_id=load_balancer_id)
    flavor_name = lb.flavor.flavor_name if lb.flavor else "Unknown"
    print(f"Load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}, flavor={flavor_name}")
    print("========================")


async def update_load_balancer(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== UPDATE LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.update(load_balancer_id=load_balancer_id, name="gcore-go-example-updated")  # pyright: ignore[reportDeprecated]
    print(f"Updated load balancer: ID={lb.id}, name={lb.name}")
    print("========================")


async def resize_load_balancer(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== RESIZE LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.resize_and_poll(load_balancer_id=load_balancer_id, flavor="lb1-2-4")
    print(f"Resized load balancer: ID={lb.id}, flavor=lb1-2-4")
    print("========================")


async def failover_load_balancer(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== FAILOVER LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.failover_and_poll(load_balancer_id=load_balancer_id)
    print(f"Failed over load balancer: ID={lb.id}")
    print("========================")


async def list_load_balancer_statuses(*, client: AsyncGcore) -> None:
    print("\n=== LIST LOAD BALANCER STATUSES ===")
    statuses = await client.cloud.load_balancers.statuses.list()
    for count, status in enumerate(statuses.results, 1):
        print(
            f"{count}. Load balancer status: ID={status.id}, operating status={status.operating_status}, provisioning status={status.provisioning_status}"
        )
    print("========================")


async def get_load_balancer_status(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER STATUS ===")
    status = await client.cloud.load_balancers.statuses.get(load_balancer_id=load_balancer_id)
    print(
        f"Load balancer status: ID={status.id}, operating status={status.operating_status}, provisioning status={status.provisioning_status}"
    )
    print("========================")


async def get_load_balancer_metrics(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER METRICS ===")
    metrics = await client.cloud.load_balancers.metrics.list(
        load_balancer_id=load_balancer_id,
        time_interval=1,
        time_unit="hour",
    )
    print(f"Load balancer metrics: ID={load_balancer_id}")
    if metrics.results:
        metric = metrics.results[0]
        print(f"CPU: {metric.cpu_util}%, memory: {metric.memory_util}%, time: {metric.time}")
    print("========================")


async def delete_load_balancer(*, client: AsyncGcore, load_balancer_id: str) -> None:
    print("\n=== DELETE LOAD BALANCER ===")
    await client.cloud.load_balancers.delete_and_poll(load_balancer_id=load_balancer_id)
    print(f"Deleted load balancer: ID={load_balancer_id}")
    print("========================")


async def create_pool(*, client: AsyncGcore, load_balancer_id: str) -> str:
    print("\n=== CREATE POOL ===")
    pool = await client.cloud.load_balancers.pools.create_and_poll(
        name="gcore-python-example-pool",
        lb_algorithm="ROUND_ROBIN",
        protocol="HTTP",
        load_balancer_id=load_balancer_id,
    )
    print(f"Created pool: ID={pool.id}, name={pool.name}, protocol={pool.protocol}, algorithm={pool.lb_algorithm}")
    print("========================")
    return pool.id


async def list_pools(*, client: AsyncGcore) -> None:
    print("\n=== LIST POOLS ===")
    count = 0
    async for pool in client.cloud.load_balancers.pools.list():
        count += 1
        print(f"{count}. Pool: ID={pool.id}, name={pool.name}, protocol={pool.protocol}")
    print("========================")


async def create_pool_member(*, client: AsyncGcore, pool_id: str) -> str:
    print("\n=== CREATE POOL MEMBER ===")
    member = await client.cloud.load_balancers.pools.members.create_and_poll(
        pool_id=pool_id,
        address="192.168.1.10",
        protocol_port=80,
    )
    print(
        f"Created member: ID={member.id}, address={member.address}, "
        f"port={member.protocol_port}, status={member.operating_status}"
    )
    print("========================")
    return member.id


async def list_pool_members(*, client: AsyncGcore, pool_id: str) -> None:
    print("\n=== LIST POOL MEMBERS ===")
    count = 0
    async for member in client.cloud.load_balancers.pools.members.list(pool_id=pool_id):
        count += 1
        print(
            f"{count}. Member: ID={member.id}, address={member.address}, "
            f"port={member.protocol_port}, status={member.operating_status}"
        )
    print("========================")


async def get_pool_member(*, client: AsyncGcore, pool_id: str, member_id: str) -> None:
    print("\n=== GET POOL MEMBER ===")
    member = await client.cloud.load_balancers.pools.members.get(member_id=member_id, pool_id=pool_id)
    print(
        f"Member: ID={member.id}, address={member.address}, port={member.protocol_port}, "
        f"weight={member.weight}, status={member.provisioning_status}"
    )
    print("========================")


async def update_pool_member(*, client: AsyncGcore, pool_id: str, member_id: str) -> None:
    print("\n=== UPDATE POOL MEMBER ===")
    member = await client.cloud.load_balancers.pools.members.update_and_poll(
        member_id=member_id,
        pool_id=pool_id,
        weight=2,
    )
    print(f"Updated member: ID={member.id}, weight={member.weight}, status={member.operating_status}")
    print("========================")


async def delete_pool_member(*, client: AsyncGcore, pool_id: str, member_id: str) -> None:
    print("\n=== DELETE POOL MEMBER ===")
    await client.cloud.load_balancers.pools.members.delete_and_poll(member_id=member_id, pool_id=pool_id)
    print(f"Deleted member: ID={member_id}")
    print("========================")


async def delete_pool(*, client: AsyncGcore, pool_id: str) -> None:
    print("\n=== DELETE POOL ===")
    await client.cloud.load_balancers.pools.delete_and_poll(pool_id=pool_id)
    print(f"Deleted pool: ID={pool_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
