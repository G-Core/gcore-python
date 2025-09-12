from __future__ import annotations

import os
import asyncio

from gcore import AsyncGcore


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set cloud port ID before running
    cloud_port_id = os.environ["GCORE_CLOUD_PORT_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    floating_ip_id = await create_floating_ip(client=gcore)
    await list_floating_ips(client=gcore)
    await get_floating_ip(client=gcore, floating_ip_id=floating_ip_id)
    await assign_floating_ip(client=gcore, floating_ip_id=floating_ip_id, port_id=cloud_port_id)
    await unassign_floating_ip(client=gcore, floating_ip_id=floating_ip_id)
    await delete_floating_ip(client=gcore, floating_ip_id=floating_ip_id)


async def create_floating_ip(*, client: AsyncGcore) -> str:
    print("\n=== CREATE FLOATING IP ===")
    floating_ip = await client.cloud.floating_ips.create_and_poll(tags={"name": "gcore-go-example"})
    print(f"Created floating IP: ID={floating_ip.id}")
    print("========================")
    return floating_ip.id


async def list_floating_ips(*, client: AsyncGcore) -> None:
    print("\n=== LIST FLOATING IPS ===")
    count = 0
    async for ip in client.cloud.floating_ips.list():
        count += 1
        print(f"{count}. Floating IP: ID={ip.id}, status={ip.status}, floating IP address={ip.floating_ip_address}")
    print("========================")


async def get_floating_ip(*, client: AsyncGcore, floating_ip_id: str) -> None:
    print("\n=== GET FLOATING IP ===")
    floating_ip = await client.cloud.floating_ips.get(floating_ip_id=floating_ip_id)
    print(
        f"Floating IP: ID={floating_ip.id}, status={floating_ip.status}, floating IP address={floating_ip.floating_ip_address}"
    )
    print("========================")


async def assign_floating_ip(*, client: AsyncGcore, floating_ip_id: str, port_id: str) -> None:
    print("\n=== ASSIGN FLOATING IP ===")
    floating_ip = await client.cloud.floating_ips.assign(
        floating_ip_id=floating_ip_id,
        port_id=port_id,
    )
    print(f"Assigned floating IP: ID={floating_ip.id}, port ID={floating_ip.port_id}")
    print("========================")


async def unassign_floating_ip(*, client: AsyncGcore, floating_ip_id: str) -> None:
    print("\n=== UNASSIGN FLOATING IP ===")
    floating_ip = await client.cloud.floating_ips.unassign(floating_ip_id=floating_ip_id)
    print(f"Unassigned floating IP: ID={floating_ip.id}")
    print("========================")


async def delete_floating_ip(*, client: AsyncGcore, floating_ip_id: str) -> None:
    print("\n=== DELETE FLOATING IP ===")
    await client.cloud.floating_ips.delete_and_poll(floating_ip_id=floating_ip_id)
    print(f"Deleted floating IP: ID={floating_ip_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
