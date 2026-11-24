import os
from typing import List, Optional

from gcore import Gcore, omit
from gcore.types.cloud import Port
from gcore.types.cloud.baremetal import BaremetalImage, BaremetalFlavor, BaremetalServer, server_update_params


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # servers, flavors and ports take the region from their parameters. Images and rebuild are regional
    # and take it from the client when you omit it
    cloud_region_id = int(os.environ["GCORE_CLOUD_REGION_ID"])

    # TODO set cloud network ID before running. The example adds a second port in this network
    cloud_network_id = os.environ["GCORE_CLOUD_NETWORK_ID"]
    # TODO set cloud SSH key ID before running, or leave it empty to create the server without a key
    cloud_ssh_key_id = os.environ.get("GCORE_CLOUD_SSH_KEY_ID")

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    image = pick_image(list_images(client=gcore, region_id=cloud_region_id))
    flavor = pick_flavor(client=gcore, region_id=cloud_region_id, image_id=image.id)

    # a bare metal server connects to networks through ports. The ports live on after the server,
    # so delete them at the end, also when a step fails
    port_ids: List[str] = []
    try:
        public_port = create_port(client=gcore, region_id=cloud_region_id, flavor=flavor)
        port_ids.append(public_port.id)
        server = create_server(
            client=gcore,
            region_id=cloud_region_id,
            flavor_name=flavor.name,
            image_id=image.id,
            port_id=public_port.id,
            ssh_key_id=cloud_ssh_key_id,
        )
        try:
            list_servers(client=gcore, region_id=cloud_region_id)
            get_server(client=gcore, server_id=server.id)
            update_tags(client=gcore, server_id=server.id)

            private_port = create_port(
                client=gcore, region_id=cloud_region_id, flavor=flavor, network_id=cloud_network_id
            )
            port_ids.append(private_port.id)
            add_interface(client=gcore, server_id=server.id, port_id=private_port.id)

            get_console(client=gcore, server_id=server.id)
            reboot_server(client=gcore, server_id=server.id)
            rebuild_server(client=gcore, server_id=server.id, region_id=cloud_region_id, image_id=image.id)
        finally:
            delete_server(client=gcore, server_id=server.id)
    finally:
        delete_ports(client=gcore, port_ids=port_ids)


def list_images(*, client: Gcore, region_id: int) -> List[BaremetalImage]:
    print("\n=== LIST BAREMETAL IMAGES ===")
    images = client.cloud.baremetal.images.list(region_id=region_id)
    display_count = min(3, len(images.results))
    for i in range(display_count):
        img = images.results[i]
        print(f"  {i + 1}. Image ID: {img.id}, name: {img.name}, OS type: {img.os_type}, status: {img.status}")
    if len(images.results) > display_count:
        print(f"  ... and {len(images.results) - display_count} more images")
    print("========================")
    return images.results


def pick_image(images: List[BaremetalImage]) -> BaremetalImage:
    """Return an Ubuntu image, or else the first Linux image."""
    linux_images = [img for img in images if img.os_type == "linux"]
    ubuntu_images = [img for img in linux_images if "ubuntu" in img.name.lower()]
    if not linux_images:
        raise RuntimeError("No Linux bare metal image found")
    image = (ubuntu_images or linux_images)[0]
    print(f"Picked image: ID={image.id}, name={image.name}")
    return image


def pick_flavor(*, client: Gcore, region_id: int, image_id: str) -> BaremetalFlavor:
    """Return the smallest flavor that can boot the image and has free servers in the region."""
    print("\n=== LIST BAREMETAL FLAVORS ===")
    # without region_ids the list holds the flavors of all regions. Iterating the page fetches the
    # following pages automatically
    flavors = client.cloud.baremetal.flavors.list(
        region_ids=[region_id], compatible_with_image_id=image_id, order_by="cpu_threads.asc"
    )
    for flavor in flavors:
        print(
            f"  Flavor: name={flavor.name}, CPU threads={flavor.cpu_threads}, RAM={flavor.ram_mib} MiB, "
            f"capacity={flavor.capacity}"
        )
        if flavor.capacity > 0:
            capabilities = flavor.networking_capabilities
            print(
                f"Picked flavor: name={flavor.name}, security groups={capabilities.security_groups}, "
                f"port security={capabilities.port_security}, "
                f"allowed address pairs={capabilities.allowed_address_pairs}"
            )
            print("========================")
            return flavor
    raise RuntimeError(f"No bare metal flavor in region {region_id} can boot image {image_id} now")


def create_port(*, client: Gcore, region_id: int, flavor: BaremetalFlavor, network_id: Optional[str] = None) -> Port:
    print("\n=== CREATE PORT ===")
    # without network_id the port gets one IPv4 address in the public network of the region.
    # Ports of a flavor without security group support must have no security groups, so send an
    # empty list. Do not enable port security or allowed address pairs that the flavor does not support
    port = client.cloud.ports.create_and_poll(
        region_id=region_id,
        network_id=network_id or omit,
        security_group_ids=omit if flavor.networking_capabilities.security_groups else [],
        tags={"name": "gcore-python-example"},
    )
    print(f"Created port: ID={port.id}, network ID={port.network_id}")
    for assignment in port.ip_assignments:
        print(f"  IP assignment: IP address={assignment.ip_address}, subnet ID={assignment.subnet_id}")
    print("========================")
    return port


def create_server(
    *,
    client: Gcore,
    region_id: int,
    flavor_name: str,
    image_id: str,
    port_id: str,
    ssh_key_id: Optional[str],
) -> BaremetalServer:
    print("\n=== CREATE BAREMETAL SERVER ===")
    server = client.cloud.baremetal.servers.create_and_poll(
        region_id=region_id,
        flavor_name=flavor_name,
        image_id=image_id,
        # the order of the ports is the NIC order and the boot order. Omit port_group: the API puts
        # the ports in the first bond, and DPU hardware rejects an explicit group
        interfaces=[{"port_id": port_id}],
        name="gcore-python-example-baremetal",
        ssh_key_id=ssh_key_id or omit,
        tags={"name": "gcore-python-example"},
    )
    print("Created baremetal server:")
    _print_server_details(server)
    print("========================")
    return server


def list_servers(*, client: Gcore, region_id: int) -> None:
    print("\n=== LIST BAREMETAL SERVERS ===")
    # without region_ids the list holds the servers of all regions. Iterating the page fetches the
    # following pages automatically
    servers = client.cloud.baremetal.servers.list(region_ids=[region_id], order_by="created_at.desc", limit=10)
    for count, server in enumerate(servers, 1):
        print(f"  {count}. Server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")


def get_server(*, client: Gcore, server_id: str) -> None:
    print("\n=== GET BAREMETAL SERVER ===")
    server = client.cloud.baremetal.servers.get(server_id=server_id)
    _print_server_details(server)
    print("========================")


def update_tags(*, client: Gcore, server_id: str) -> None:
    print("\n=== UPDATE BAREMETAL SERVER TAGS ===")
    # tags is a JSON Merge Patch: a value adds or changes a tag, None removes it
    server = client.cloud.baremetal.servers.update_and_poll(
        server_id=server_id, tags={"stage": "example", "name": None}
    )
    # the server can show the old tags for a few seconds after the task
    print(f"Updated tags: ID={server.id}, tags={server.tags}")
    print("========================")


def add_interface(*, client: Gcore, server_id: str, port_id: str) -> None:
    print("\n=== ADD BAREMETAL SERVER INTERFACE ===")
    # interfaces is the full list: keep the current interfaces in their order and add the new port at the end
    server = client.cloud.baremetal.servers.get(server_id=server_id)
    interfaces: List[server_update_params.Interface] = []
    for interface in server.interfaces:
        current: server_update_params.Interface = {"port_id": interface.port_id}
        if interface.port_group is not None:
            current["port_group"] = interface.port_group
        interfaces.append(current)
    interfaces.append({"port_id": port_id})
    server = client.cloud.baremetal.servers.update_and_poll(server_id=server_id, interfaces=interfaces)
    print(f"Added interface: server ID={server.id}, port ID={port_id}")
    print("========================")


def get_console(*, client: Gcore, server_id: str) -> None:
    print("\n=== GET BAREMETAL SERVER CONSOLE ===")
    # without console_type the hardware selects the console type
    console = client.cloud.baremetal.servers.console.get(server_id=server_id)
    remote_console = console.remote_console
    print(f"Console: protocol={remote_console.protocol}, type={remote_console.type}, url={remote_console.url}")
    print("========================")


def reboot_server(*, client: Gcore, server_id: str) -> None:
    print("\n=== REBOOT BAREMETAL SERVER ===")
    server = client.cloud.baremetal.servers.action_and_poll(server_id=server_id, action="reboot")
    # the status can show the old state for a few seconds after the task
    print(f"Rebooted baremetal server: ID={server.id}, status={server.status}")
    print("========================")


def rebuild_server(*, client: Gcore, server_id: str, region_id: int, image_id: str) -> None:
    print("\n=== REBUILD BAREMETAL SERVER ===")
    # rebuild keeps its regional route. The helper returns the legacy BaremetalRegionalServer model
    server = client.cloud.baremetal.servers.rebuild_and_poll(
        server_id=server_id, region_id=region_id, image_id=image_id
    )
    print(f"Rebuilt baremetal server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")


def delete_server(*, client: Gcore, server_id: str) -> None:
    print("\n=== DELETE BAREMETAL SERVER ===")
    # by default the delete keeps the ports and floating IPs of the server
    client.cloud.baremetal.servers.delete_and_poll(server_id=server_id)
    print(f"Deleted baremetal server: ID={server_id}")
    print("========================")


def delete_ports(*, client: Gcore, port_ids: List[str]) -> None:
    print("\n=== DELETE PORTS ===")
    for port_id in port_ids:
        client.cloud.ports.delete_and_poll(port_id=port_id)
        print(f"Deleted port: ID={port_id}")
    print("========================")


def _print_server_details(server: BaremetalServer) -> None:
    print(f"  ID={server.id}, name={server.name}, status={server.status}, region ID={server.region_id}")
    print(f"  Flavor name={server.flavor_name}, image ID={server.image_id}")
    for interface in server.interfaces:
        print(
            f"  Interface: port ID={interface.port_id}, network ID={interface.network_id}, "
            f"port group={interface.port_group}"
        )
        for assignment in interface.ip_assignments:
            print(f"    IP assignment: IP address={assignment.ip_address}, subnet ID={assignment.subnet_id}")


if __name__ == "__main__":
    main()
