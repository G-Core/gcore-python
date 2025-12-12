import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import ReservedFixedIP


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
    port = await client.cloud.reserved_fixed_ips.create_and_poll(
        type="external",
        ip_family="ipv4",
        is_vip=False,
    )
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
    candidate_ports = await client.cloud.reserved_fixed_ips.vip.candidate_ports.list(port_id)
    for count, port in enumerate(candidate_ports.results, 1):
        print(f"{count}. Candidate port: ID={port.port_id}, instance name={port.instance_name}")
    print("========================")


async def list_connected_ports(*, client: AsyncGcore, port_id: str) -> None:
    print("\n=== LIST CONNECTED PORTS ===")
    connected_ports = await client.cloud.reserved_fixed_ips.vip.connected_ports.list(port_id)
    for count, port in enumerate(connected_ports.results, 1):
        print(f"{count}. Connected port: ID={port.port_id}, instance name={port.instance_name}")
    print("========================")


async def delete_reserved_fixed_ip(*, client: AsyncGcore, port_id: str) -> None:
    print("\n=== DELETE RESERVED FIXED IP ===")
    await client.cloud.reserved_fixed_ips.delete_and_poll(port_id)
    print(f"Deleted reserved fixed IP: ID={port_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
