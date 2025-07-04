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
        timeout=180.0,
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    lb_id = await create_load_balancer(client=gcore)
    await list_load_balancers(client=gcore)
    await get_load_balancer(client=gcore, loadbalancer_id=lb_id)
    await update_load_balancer(client=gcore, loadbalancer_id=lb_id)
    await resize_load_balancer(client=gcore, loadbalancer_id=lb_id)
    await failover_load_balancer(client=gcore, loadbalancer_id=lb_id)

    # Statuses
    await list_load_balancer_statuses(client=gcore)
    await get_load_balancer_status(client=gcore, loadbalancer_id=lb_id)

    # Metrics
    await get_load_balancer_metrics(client=gcore, loadbalancer_id=lb_id)

    await delete_load_balancer(client=gcore, loadbalancer_id=lb_id)


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


async def get_load_balancer(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.get(loadbalancer_id=loadbalancer_id)
    flavor_name = lb.flavor.flavor_name if lb.flavor else "Unknown"
    print(f"Load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}, flavor={flavor_name}")
    print("========================")


async def update_load_balancer(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== UPDATE LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.update(loadbalancer_id=loadbalancer_id, name="gcore-go-example-updated")
    print(f"Updated load balancer: ID={lb.id}, name={lb.name}")
    print("========================")


async def resize_load_balancer(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== RESIZE LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.resize_and_poll(loadbalancer_id=loadbalancer_id, flavor="lb1-2-4")
    print(f"Resized load balancer: ID={lb.id}, flavor=lb1-2-4")
    print("========================")


async def failover_load_balancer(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== FAILOVER LOAD BALANCER ===")
    lb = await client.cloud.load_balancers.failover_and_poll(loadbalancer_id=loadbalancer_id)
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


async def get_load_balancer_status(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER STATUS ===")
    status = await client.cloud.load_balancers.statuses.get(loadbalancer_id=loadbalancer_id)
    print(
        f"Load balancer status: ID={status.id}, operating status={status.operating_status}, provisioning status={status.provisioning_status}"
    )
    print("========================")


async def get_load_balancer_metrics(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER METRICS ===")
    metrics = await client.cloud.load_balancers.metrics.list(
        loadbalancer_id=loadbalancer_id,
        time_interval=1,
        time_unit="hour",
    )
    print(f"Load balancer metrics: ID={loadbalancer_id}")
    if metrics.results:
        metric = metrics.results[0]
        print(f"CPU: {metric.cpu_util}%, memory: {metric.memory_util}%, time: {metric.time}")
    print("========================")


async def delete_load_balancer(*, client: AsyncGcore, loadbalancer_id: str) -> None:
    print("\n=== DELETE LOAD BALANCER ===")
    await client.cloud.load_balancers.delete_and_poll(loadbalancer_id=loadbalancer_id)
    print(f"Deleted load balancer: ID={loadbalancer_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
