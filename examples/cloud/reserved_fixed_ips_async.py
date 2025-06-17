"""
Example demonstrating full lifecycle of Reserved Fixed IPs resource using async client.
Includes create, get, list, update (i.e. toggle VIP), and delete operations.
"""

import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import ReservedFixedIP


async def main() -> None:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    # api_key = os.environ.get("GCORE_API_KEY")
    # Will use Production API URL if omitted
    # base_url = os.environ.get("GCORE_BASE_URL")

    gcore = AsyncGcore(
        # api_key=api_key,
        # base_url=base_url,
    )

    fixed_ip = await create_reserved_fixed_ip(client=gcore)
    await list_reserved_fixed_ips(client=gcore)
    await get_reserved_fixed_ip(client=gcore, port_id=fixed_ip.port_id)

    # VIP
    await toggle_reserved_fixed_ip_vip(client=gcore, port_id=fixed_ip.port_id, is_vip=True)
    await list_candidate_ports(client=gcore, port_id=fixed_ip.port_id)
    await list_connected_ports(client=gcore, port_id=fixed_ip.port_id)
    # is_vip needs to be false to delete the reserved fixed IP
    await toggle_reserved_fixed_ip_vip(client=gcore, port_id=fixed_ip.port_id, is_vip=False)

    await delete_reserved_fixed_ip(client=gcore, port_id=fixed_ip.port_id)


async def create_reserved_fixed_ip(*, client: AsyncGcore) -> ReservedFixedIP:
    print("\n=== CREATE RESERVED FIXED IP ===")
    task_list = await client.cloud.reserved_fixed_ips.create(
        type="external",
        ip_family="ipv4",
        is_vip=False,
    )
    task = await client.cloud.tasks.poll(task_list.tasks[0])
    if not task.created_resources or not task.created_resources.ports or len(task.created_resources.ports) != 1:
        raise RuntimeError("Expected exactly one port created in the task result")
    port = await client.cloud.reserved_fixed_ips.get(task.created_resources.ports[0])
    print(f"Created reserved fixed IP: ID={port.port_id}, name={port.name}, IP={port.fixed_ip_address}")
    print("========================")
    return port


async def list_reserved_fixed_ips(*, client: AsyncGcore) -> AsyncOffsetPage[ReservedFixedIP]:
    print("\n=== LIST RESERVED FIXED IPS ===")
    reserved_ips = await client.cloud.reserved_fixed_ips.list()
    count = 1
    async for ip in reserved_ips:
        print(f"{count}. Reserved fixed IP: ID={ip.port_id}, name={ip.name}, status={ip.status}")
        count += 1
    print("========================")
    return reserved_ips


async def get_reserved_fixed_ip(*, client: AsyncGcore, port_id: str) -> ReservedFixedIP:
    print("\n=== GET RESERVED FIXED IP ===")
    reserved_ip = await client.cloud.reserved_fixed_ips.get(port_id)
    print(f"Reserved fixed IP: ID={reserved_ip.port_id}, name={reserved_ip.name}, status={reserved_ip.status}")
    print("========================")
    return reserved_ip


async def toggle_reserved_fixed_ip_vip(*, client: AsyncGcore, port_id: str, is_vip: bool) -> ReservedFixedIP:
    print("\n=== TOGGLE RESERVED FIXED IP VIP ===")
    reserved_ip = await client.cloud.reserved_fixed_ips.vip.toggle(port_id, is_vip=is_vip)
    print(
        f"Toggled reserved fixed IP VIP: ID={reserved_ip.port_id}, name={reserved_ip.name}, is_vip={reserved_ip.is_vip}"
    )
    print("========================")
    return reserved_ip


async def list_candidate_ports(*, client: AsyncGcore, port_id: str) -> None:
    print("\n=== LIST CANDIDATE PORTS ===")
    candidate_ports = await client.cloud.reserved_fixed_ips.vip.list_candidate_ports(port_id)
    for count, port in enumerate(candidate_ports.results, 1):
        print(f"{count}. Candidate port: ID={port.port_id}, instance name={port.instance_name}")
    print("========================")


async def list_connected_ports(*, client: AsyncGcore, port_id: str) -> None:
    print("\n=== LIST CONNECTED PORTS ===")
    connected_ports = await client.cloud.reserved_fixed_ips.vip.list_connected_ports(port_id)
    for count, port in enumerate(connected_ports.results, 1):
        print(f"{count}. Connected port: ID={port.port_id}, instance name={port.instance_name}")
    print("========================")


async def delete_reserved_fixed_ip(*, client: AsyncGcore, port_id: str) -> None:
    print("\n=== DELETE RESERVED FIXED IP ===")
    task_list = await client.cloud.reserved_fixed_ips.delete(port_id)
    await client.cloud.tasks.poll(task_list.tasks[0])
    print(f"Deleted reserved fixed IP: ID={port_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
