import os
from typing import List

from gcore import Gcore
from gcore.types.cloud.instance import Volume, Instance
from gcore.types.cloud.network_interface import NetworkInterface
from gcore.types.cloud.instance_create_params import (
    InterfaceNewInterfaceExternalSerializerPydantic,
    VolumeCreateInstanceCreateVolumeFromImageSerializer,
)
from gcore.types.cloud.instances.instance_flavor import InstanceFlavor


def main() -> None:
    # TODO set placement group ID before running
    placement_group_id = os.environ.get("GCORE_CLOUD_PLACEMENT_GROUP_ID")

    gcore = Gcore(timeout=180.0)

    instance_id = create_instance(client=gcore)
    instance = get_instance(client=gcore, instance_id=instance_id)
    get_console(client=gcore, instance_id=instance_id)
    list_instances(client=gcore)
    update_instance(client=gcore, instance_id=instance_id)
    reboot_instance(client=gcore, instance_id=instance_id)
    resize_instance(client=gcore, instance_id=instance_id)

    # Flavors
    list_flavors(client=gcore)

    # Interfaces
    interfaces = list_interfaces(client=gcore, instance_id=instance_id)
    if interfaces:
        ip_address = interfaces[0].ip_assignments[0].ip_address
        port_id = interfaces[0].port_id
        network_id = interfaces[0].network_id
        detach_interface(client=gcore, instance_id=instance_id, ip_address=ip_address, port_id=port_id)
        attach_interface(client=gcore, instance_id=instance_id, network_id=network_id)

    # Metrics
    list_metrics(client=gcore, instance_id=instance_id)

    # Placement groups
    if placement_group_id:
        add_to_placement_group(client=gcore, instance_id=instance_id, placement_group_id=placement_group_id)
        remove_from_placement_group(client=gcore, instance_id=instance_id)

    # Security groups
    unassign_security_group(client=gcore, instance_id=instance_id)
    assign_security_group(client=gcore, instance_id=instance_id)

    delete_instance(client=gcore, instance_id=instance_id, volumes=instance.volumes if instance else [])


def create_instance(*, client: Gcore) -> str:
    print("\n=== CREATE INSTANCE ===")
    image_id, vsize = _find_image(client=client)

    instance = client.cloud.instances.create_and_poll(
        name_template="gcore-go-example-{ip_octets}",
        flavor="g1-standard-1-2",
        interfaces=[
            InterfaceNewInterfaceExternalSerializerPydantic(type="external"),
        ],
        volumes=[
            VolumeCreateInstanceCreateVolumeFromImageSerializer(
                source="image",
                image_id=image_id,
                size=vsize,
                boot_index=0,
            ),
        ],
        password="Gcore123!",
    )
    print(f"Created instance: ID={instance.id}, name={instance.name}, status={instance.status}")
    print("========================")
    return instance.id


def get_instance(*, client: Gcore, instance_id: str) -> Instance:
    print("\n=== GET INSTANCE ===")
    instance = client.cloud.instances.get(instance_id=instance_id)
    print(f"Instance: ID={instance.id}, name={instance.name}, status={instance.status}")
    print("========================")
    return instance


def get_console(*, client: Gcore, instance_id: str) -> None:
    print("\n=== GET CONSOLE ===")
    console = client.cloud.instances.get_console(instance_id=instance_id)
    print(
        f"Console: protocol={console.remote_console.protocol}, type={console.remote_console.type}, url={console.remote_console.url}"
    )
    print("========================")


def list_instances(*, client: Gcore) -> None:
    print("\n=== LIST INSTANCES ===")
    instances = client.cloud.instances.list()
    for count, instance in enumerate(instances, 1):
        print(f"  {count}. Instance: ID={instance.id}, name={instance.name}, status={instance.status}")
    print("========================")


def update_instance(*, client: Gcore, instance_id: str) -> None:
    print("\n=== UPDATE INSTANCE ===")
    instance = client.cloud.instances.update(instance_id=instance_id, name="gcore-go-example-updated")
    print(f"Instance updated: ID={instance.id}, name changed to {instance.name}")
    print("========================")


def reboot_instance(*, client: Gcore, instance_id: str) -> None:
    print("\n=== REBOOT INSTANCE ===")
    response = client.cloud.instances.action(instance_id=instance_id, action="reboot")
    client.cloud.tasks.poll(task_id=response.tasks[0])
    print(f"Rebooted instance: {instance_id}")
    print("========================")


def resize_instance(*, client: Gcore, instance_id: str) -> None:
    print("\n=== RESIZE INSTANCE ===")
    instance = client.cloud.instances.resize_and_poll(instance_id=instance_id, flavor_id="g1-standard-2-4")
    print(f"Instance resized: ID={instance.id}, new flavor=g1-standard-2-4")
    print("========================")


def list_flavors(*, client: Gcore) -> None:
    print("\n=== LIST FLAVORS ===")
    flavors = client.cloud.instances.flavors.list()
    _print_flavor_details(flavors.results)
    print("========================")


def list_interfaces(*, client: Gcore, instance_id: str) -> List[NetworkInterface]:
    print("\n=== LIST INTERFACES ===")
    interfaces = client.cloud.instances.interfaces.list(instance_id=instance_id)
    for count, interface in enumerate(interfaces.results, 1):
        print(f"  {count}. Interface: PortID={interface.port_id}, NetworkID={interface.network_id}")
    print("========================")
    return interfaces.results


def list_metrics(*, client: Gcore, instance_id: str) -> None:
    print("\n=== LIST METRICS ===")
    metrics = client.cloud.instances.metrics.list(instance_id=instance_id, time_interval=1, time_unit="hour")
    print(f"Metrics for instance: {len(metrics.results)} entries")

    # Display first few metrics
    display_count = min(3, len(metrics.results))

    for i in range(display_count):
        metric = metrics.results[i]
        cpu = getattr(metric, "cpu_util", "N/A")
        memory = getattr(metric, "memory_util", "N/A")
        timestamp = getattr(metric, "timestamp", "N/A")

        print(f"  {i + 1}. Metric: CPU={cpu}%, Memory={memory}%, Time={timestamp}")

    if len(metrics.results) > display_count:
        print(f"  ... and {len(metrics.results) - display_count} more metrics")
    print("========================")


def assign_security_group(*, client: Gcore, instance_id: str) -> None:
    print("\n=== ASSIGN SECURITY GROUP ===")
    client.cloud.instances.assign_security_group(instance_id=instance_id, name="default")
    print("Assigned security group: default")
    print("========================")


def unassign_security_group(*, client: Gcore, instance_id: str) -> None:
    print("\n=== UNASSIGN SECURITY GROUP ===")
    client.cloud.instances.unassign_security_group(instance_id=instance_id, name="default")
    print("Unassigned security group: default")
    print("========================")


def add_to_placement_group(*, client: Gcore, instance_id: str, placement_group_id: str) -> None:
    print("\n=== ADD TO PLACEMENT GROUP ===")
    client.cloud.instances.add_to_placement_group_and_poll(instance_id=instance_id, servergroup_id=placement_group_id)
    print(f"Added instance {instance_id} to placement group: {placement_group_id}")
    print("========================")


def remove_from_placement_group(*, client: Gcore, instance_id: str) -> None:
    print("\n=== REMOVE FROM PLACEMENT GROUP ===")
    client.cloud.instances.remove_from_placement_group_and_poll(instance_id=instance_id)
    print(f"Removed instance {instance_id} from placement group")
    print("========================")


def detach_interface(*, client: Gcore, instance_id: str, ip_address: str, port_id: str) -> None:
    print("\n=== DETACH INTERFACE ===")
    response = client.cloud.instances.interfaces.detach(instance_id=instance_id, ip_address=ip_address, port_id=port_id)
    client.cloud.tasks.poll(task_id=response.tasks[0])

    print(f"Detached interface (IP: {ip_address}, Port: {port_id}) from instance: {instance_id}")
    print("========================")


def attach_interface(*, client: Gcore, instance_id: str, network_id: str) -> None:
    print("\n=== ATTACH INTERFACE ===")
    response = client.cloud.instances.interfaces.attach(
        instance_id=instance_id, type="any_subnet", network_id=network_id
    )
    client.cloud.tasks.poll(task_id=response.tasks[0])

    print(f"Attached interface to any available subnet in network {network_id} (instance: {instance_id})")
    print("========================")


def delete_instance(*, client: Gcore, instance_id: str, volumes: List[Volume]) -> None:
    print("\n=== DELETE INSTANCE ===")
    volumes_str = ""
    if volumes:
        volumes_str = ",".join([vol.id for vol in volumes])

    client.cloud.instances.delete_and_poll(
        instance_id=instance_id,
        delete_floatings=True,
        volumes=volumes_str,
    )
    print(f"Deleted instance and related resources: ID={instance_id}, Volumes={volumes_str}")
    print("========================")


def _print_flavor_details(flavors: List[InstanceFlavor]) -> None:
    display_count = 3
    if len(flavors) < display_count:
        display_count = len(flavors)

    for i in range(display_count):
        flavor = flavors[i]
        print(f"  {i + 1}. Flavor: ID={flavor.flavor_id}, name={flavor.flavor_name}")
        print(f"     RAM: {flavor.ram} MB, VCPUs: {flavor.vcpus}")
        status = "AVAILABLE"
        if flavor.disabled:
            status = "DISABLED"
        print(f"     Status: {status}")
        print()

    if len(flavors) > display_count:
        print(f"  ... and {len(flavors) - display_count} more flavors")


def _find_image(*, client: Gcore) -> "tuple[str, int]":
    images = client.cloud.instances.images.list()
    if not images.results:
        raise RuntimeError("No available images")
    image = images.results[0]
    vsize = getattr(image, "min_disk", 40) or 40
    return image.id, vsize


if __name__ == "__main__":
    main()
