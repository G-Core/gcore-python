from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import ReservedFixedIP


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    fixed_ip = create_reserved_fixed_ip(client=gcore)
    list_reserved_fixed_ips(client=gcore)
    get_reserved_fixed_ip(client=gcore, port_id=fixed_ip.port_id)

    # VIP
    toggle_reserved_fixed_ip_vip(client=gcore, port_id=fixed_ip.port_id, is_vip=True)
    list_candidate_ports(client=gcore, port_id=fixed_ip.port_id)
    list_connected_ports(client=gcore, port_id=fixed_ip.port_id)
    # is_vip needs to be false to delete the reserved fixed IP
    toggle_reserved_fixed_ip_vip(client=gcore, port_id=fixed_ip.port_id, is_vip=False)

    delete_reserved_fixed_ip(client=gcore, port_id=fixed_ip.port_id)


def create_reserved_fixed_ip(*, client: Gcore) -> ReservedFixedIP:
    print("\n=== CREATE RESERVED FIXED IP ===")
    task_list = client.cloud.reserved_fixed_ips.create(
        type="external",
        ip_family="ipv4",
        is_vip=False,
    )
    task = client.cloud.tasks.poll(task_list.tasks[0])
    if not task.created_resources or not task.created_resources.ports or len(task.created_resources.ports) != 1:
        raise RuntimeError("Expected exactly one port created in the task result")
    port = client.cloud.reserved_fixed_ips.get(task.created_resources.ports[0])
    print(f"Created reserved fixed IP: ID={port.port_id}, name={port.name}, IP={port.fixed_ip_address}")
    print("========================")
    return port


def list_reserved_fixed_ips(*, client: Gcore) -> SyncOffsetPage[ReservedFixedIP]:
    print("\n=== LIST RESERVED FIXED IPS ===")
    reserved_ips = client.cloud.reserved_fixed_ips.list()
    for count, ip in enumerate(reserved_ips, 1):
        print(f"{count}. Reserved fixed IP: ID={ip.port_id}, name={ip.name}, status={ip.status}")
    print("========================")
    return reserved_ips


def get_reserved_fixed_ip(*, client: Gcore, port_id: str) -> ReservedFixedIP:
    print("\n=== GET RESERVED FIXED IP ===")
    reserved_ip = client.cloud.reserved_fixed_ips.get(port_id)
    print(f"Reserved fixed IP: ID={reserved_ip.port_id}, name={reserved_ip.name}, status={reserved_ip.status}")
    print("========================")
    return reserved_ip


def toggle_reserved_fixed_ip_vip(*, client: Gcore, port_id: str, is_vip: bool) -> ReservedFixedIP:
    print("\n=== TOGGLE RESERVED FIXED IP VIP ===")
    reserved_ip = client.cloud.reserved_fixed_ips.vip.toggle(port_id, is_vip=is_vip)
    print(
        f"Toggled reserved fixed IP VIP: ID={reserved_ip.port_id}, name={reserved_ip.name}, is_vip={reserved_ip.is_vip}"
    )
    print("========================")
    return reserved_ip


def list_candidate_ports(*, client: Gcore, port_id: str) -> None:
    print("\n=== LIST CANDIDATE PORTS ===")
    candidate_ports = client.cloud.reserved_fixed_ips.vip.list_candidate_ports(port_id)
    for count, port in enumerate(candidate_ports.results, 1):
        print(f"{count}. Candidate port: ID={port.port_id}, instance name={port.instance_name}")
    print("========================")


def list_connected_ports(*, client: Gcore, port_id: str) -> None:
    print("\n=== LIST CONNECTED PORTS ===")
    connected_ports = client.cloud.reserved_fixed_ips.vip.list_connected_ports(port_id)
    for count, port in enumerate(connected_ports.results, 1):
        print(f"{count}. Connected port: ID={port.port_id}, instance name={port.instance_name}")
    print("========================")


def delete_reserved_fixed_ip(*, client: Gcore, port_id: str) -> None:
    print("\n=== DELETE RESERVED FIXED IP ===")
    task_list = client.cloud.reserved_fixed_ips.delete(port_id)
    client.cloud.tasks.poll(task_list.tasks[0])
    print(f"Deleted reserved fixed IP: ID={port_id}")
    print("========================")


if __name__ == "__main__":
    main()
