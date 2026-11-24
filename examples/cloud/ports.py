import os
from typing import List

from gcore import Gcore
from gcore.types.cloud import Port


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # ports use the global view: the requests take the region from their parameters, not from the client
    cloud_region_id = int(os.environ["GCORE_CLOUD_REGION_ID"])

    # TODO set cloud network ID before running
    # use a private network: the public network does not allow port security changes
    cloud_network_id = os.environ["GCORE_CLOUD_NETWORK_ID"]
    # TODO set cloud subnet ID of the network before running
    cloud_subnet_id = os.environ["GCORE_CLOUD_SUBNET_ID"]
    # TODO set cloud security group ID before running
    cloud_security_group_id = os.environ["GCORE_CLOUD_SECURITY_GROUP_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
    )

    port = create_port(client=gcore, region_id=cloud_region_id, network_id=cloud_network_id, subnet_id=cloud_subnet_id)
    # the second port owns the shared address that the first port holds as an allowed address pair
    vip_port = create_port(
        client=gcore, region_id=cloud_region_id, network_id=cloud_network_id, subnet_id=cloud_subnet_id
    )

    get_port(client=gcore, port_id=port.id)
    update_port_tag(client=gcore, port_id=port.id, key="env", value="example")
    update_port_security_groups(client=gcore, port_id=port.id, security_group_ids=[cloud_security_group_id])
    disable_port_security(client=gcore, port_id=port.id)
    enable_port_security(client=gcore, port_id=port.id, security_group_ids=[cloud_security_group_id])
    update_port_allowed_address_pairs(client=gcore, port_id=port.id, ip_address=vip_port.ip_assignments[0].ip_address)
    list_ports_with_filters(
        client=gcore, region_id=cloud_region_id, network_id=cloud_network_id, tag_key="env", tag_value="example"
    )

    # delete the first port before the VIP port, because its allowed address pairs refer to the VIP address
    delete_port(client=gcore, port_id=port.id)
    delete_port(client=gcore, port_id=vip_port.id)

    convert_port_to_floating_ip(client=gcore, region_id=cloud_region_id)


def create_port(*, client: Gcore, region_id: int, network_id: str, subnet_id: str) -> Port:
    print("\n=== CREATE PORT ===")
    port = client.cloud.ports.create_and_poll(
        region_id=region_id,
        network_id=network_id,
        ip_assignments=[{"subnet_id": subnet_id}],
        tags={"name": "gcore-python-example"},
    )
    print("Created port:")
    _print_port_details(port)
    print("========================")
    return port


def get_port(*, client: Gcore, port_id: str) -> None:
    print("\n=== GET PORT ===")
    port = client.cloud.ports.get(port_id=port_id)
    print("Port:")
    _print_port_details(port)
    print("========================")


def update_port_tag(*, client: Gcore, port_id: str, key: str, value: str) -> None:
    print("\n=== UPDATE PORT TAGS ===")
    # the sent tags merge into the existing tags. A tag with the value None removes the tag
    port = client.cloud.ports.update_and_poll(port_id=port_id, tags={key: value})
    print("Updated port:")
    _print_port_details(port)
    print("========================")


def update_port_security_groups(*, client: Gcore, port_id: str, security_group_ids: List[str]) -> None:
    print("\n=== UPDATE PORT SECURITY GROUPS ===")
    # the list replaces all security groups of the port
    port = client.cloud.ports.update_and_poll(port_id=port_id, security_group_ids=security_group_ids)
    print("Updated port:")
    _print_port_details(port)
    print("========================")


def disable_port_security(*, client: Gcore, port_id: str) -> None:
    print("\n=== DISABLE PORT SECURITY ===")
    # a port without port security must have no security groups. `[]` detaches all groups, while an
    # omitted field leaves them unchanged
    port = client.cloud.ports.update_and_poll(port_id=port_id, port_security_enabled=False, security_group_ids=[])
    print("Updated port:")
    _print_port_details(port)
    print("========================")


def enable_port_security(*, client: Gcore, port_id: str, security_group_ids: List[str]) -> None:
    print("\n=== ENABLE PORT SECURITY ===")
    # with port security and no security groups the port permits no traffic, so attach the groups again
    port = client.cloud.ports.update_and_poll(
        port_id=port_id, port_security_enabled=True, security_group_ids=security_group_ids
    )
    print("Updated port:")
    _print_port_details(port)
    print("========================")


def update_port_allowed_address_pairs(*, client: Gcore, port_id: str, ip_address: str) -> None:
    print("\n=== UPDATE PORT ALLOWED ADDRESS PAIRS ===")
    # allowed address pairs need port security on the port
    port = client.cloud.ports.update_and_poll(port_id=port_id, allowed_address_pairs=[{"ip_address": ip_address}])
    print("Updated port:")
    _print_port_details(port)
    print("========================")


def list_ports_with_filters(*, client: Gcore, region_id: int, network_id: str, tag_key: str, tag_value: str) -> None:
    print("\n=== LIST PORTS WITH FILTERS ===")
    # without region_ids the list holds the ports of all regions. A tag key can list several values, and
    # the port must have one of them. Iterating the page fetches the following pages automatically
    ports = client.cloud.ports.list(
        network_ids=[network_id], region_ids=[region_id], tags={tag_key: [tag_value]}, limit=10
    )
    for count, port in enumerate(ports, 1):
        print(
            f"  {count}. Port: ID={port.id}, region ID={port.region_id}, network ID={port.network_id}, tags={port.tags}"
        )
    print("========================")


def delete_port(*, client: Gcore, port_id: str) -> None:
    print("\n=== DELETE PORT ===")
    client.cloud.ports.delete_and_poll(port_id=port_id)
    print(f"Deleted port: ID={port_id}")
    print("========================")


def convert_port_to_floating_ip(*, client: Gcore, region_id: int) -> None:
    print("\n=== CONVERT PORT TO FLOATING IP ===")
    # a port without a network gets one public IPv4 address. Only an unattached port with one public
    # IPv4 address can become a floating IP
    port = client.cloud.ports.create_and_poll(region_id=region_id, tags={"name": "gcore-python-example"})
    print("Created public port:")
    _print_port_details(port)
    # the task deletes the port and creates a floating IP with the same address
    floating_ip = client.cloud.ports.convert_and_poll(port_id=port.id, target_type="floating_ip")
    print(
        f"Converted port {port.id} to floating IP: ID={floating_ip.id}, "
        f"address={floating_ip.floating_ip_address}, region ID={floating_ip.region_id}"
    )
    client.cloud.floating_ips.delete_and_poll(floating_ip_id=floating_ip.id, region_id=floating_ip.region_id)
    print(f"Deleted floating IP: ID={floating_ip.id}")
    print("========================")


def _print_port_details(port: Port) -> None:
    print(f"  ID={port.id}, region ID={port.region_id}, network ID={port.network_id}")
    for assignment in port.ip_assignments:
        print(f"  IP assignment: IP address={assignment.ip_address}, subnet ID={assignment.subnet_id}")
    print(f"  Security group IDs={port.security_group_ids}")
    print(f"  Port security enabled={port.port_security_enabled}")
    for pair in port.allowed_address_pairs:
        print(f"  Allowed address pair: IP address={pair.ip_address}")
    print(f"  Tags={port.tags}")


if __name__ == "__main__":
    main()
