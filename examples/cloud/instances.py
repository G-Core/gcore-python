import os
from typing import List, Optional
from typing_extensions import Literal

from gcore import Gcore, omit
from gcore.types.cloud import Port, Volume, Instance


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # instances and ports take the region from their parameters. Volumes, images and metrics are regional
    # and take it from the client when you omit it
    cloud_region_id = int(os.environ["GCORE_CLOUD_REGION_ID"])

    # TODO set cloud network ID before running
    cloud_network_id = os.environ["GCORE_CLOUD_NETWORK_ID"]
    # TODO set cloud subnet ID of the network before running
    cloud_subnet_id = os.environ["GCORE_CLOUD_SUBNET_ID"]
    # TODO set cloud image ID before running, or leave it empty to upload an Ubuntu image
    cloud_image_id = os.environ.get("GCORE_CLOUD_IMAGE_ID")
    # TODO set cloud flavor name before running, or leave it empty to use the smallest flavor that can boot the volume
    cloud_flavor_name = os.environ.get("GCORE_CLOUD_FLAVOR_NAME")
    # TODO set cloud SSH key ID before running, or leave it empty to create the instance without a key
    cloud_ssh_key_id = os.environ.get("GCORE_CLOUD_SSH_KEY_ID")

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    image_id = cloud_image_id or upload_image(client=gcore)

    # an instance boots from a volume and connects to networks through ports, so create them first
    boot_volume = create_boot_volume(client=gcore, region_id=cloud_region_id, image_id=image_id)
    port = create_port(client=gcore, region_id=cloud_region_id, network_id=cloud_network_id, subnet_id=cloud_subnet_id)
    flavor_name = cloud_flavor_name or pick_flavor(
        client=gcore, region_id=cloud_region_id, boot_volume_id=boot_volume.id
    )

    instance = create_instance(
        client=gcore,
        region_id=cloud_region_id,
        flavor_name=flavor_name,
        boot_volume_id=boot_volume.id,
        port_id=port.id,
        ssh_key_id=cloud_ssh_key_id,
    )
    get_instance(client=gcore, instance_id=instance.id)
    list_instances(client=gcore, region_id=cloud_region_id)

    resize_flavor_name = pick_resize_flavor(client=gcore, instance_id=instance.id)
    if resize_flavor_name:
        resize_instance(client=gcore, instance_id=instance.id, flavor_name=resize_flavor_name)

    get_console(client=gcore, instance_id=instance.id)
    list_metrics(client=gcore, instance_id=instance.id)
    run_action(client=gcore, instance_id=instance.id, action="stop")
    run_action(client=gcore, instance_id=instance.id, action="start")

    delete_instance(client=gcore, instance_id=instance.id, volume_ids=[boot_volume.id], port_ids=[port.id])
    if not cloud_image_id:
        delete_image(client=gcore, image_id=image_id)


def create_boot_volume(*, client: Gcore, region_id: int, image_id: str) -> Volume:
    print("\n=== CREATE BOOT VOLUME ===")
    # the size must be at least the minimum disk size of the image
    volume = client.cloud.volumes.create_and_poll(
        region_id=region_id,
        source="image",
        image_id=image_id,
        name="gcore-python-example-boot-volume",
        size=10,
        type_name="standard",
        tags={"name": "gcore-python-example"},
    )
    print(f"Created boot volume: ID={volume.id}, name={volume.name}, size={volume.size} GiB, status={volume.status}")
    print("========================")
    return volume


def create_port(*, client: Gcore, region_id: int, network_id: str, subnet_id: str) -> Port:
    print("\n=== CREATE PORT ===")
    port = client.cloud.ports.create_and_poll(
        region_id=region_id,
        network_id=network_id,
        ip_assignments=[{"subnet_id": subnet_id}],
        tags={"name": "gcore-python-example"},
    )
    print(f"Created port: ID={port.id}, network ID={port.network_id}")
    for assignment in port.ip_assignments:
        print(f"  IP assignment: IP address={assignment.ip_address}, subnet ID={assignment.subnet_id}")
    print("========================")
    return port


def pick_flavor(*, client: Gcore, region_id: int, boot_volume_id: str) -> str:
    """Return the smallest available flavor that can boot the volume."""
    print("\n=== LIST FLAVORS ===")
    # without region_ids the list holds the flavors of all regions
    flavors = client.cloud.instances.flavors.list(
        region_ids=[region_id],
        compatible_with_boot_volume_id=boot_volume_id,
        available=True,
        order_by="vcpus.asc",
        limit=1,
    )
    if not flavors.results:
        raise RuntimeError(f"No available flavor in region {region_id} can boot volume {boot_volume_id}")
    flavor = flavors.results[0]
    print(f"Picked flavor: name={flavor.name}, vCPUs={flavor.vcpus}, RAM={flavor.ram_mib} MiB")
    print("========================")
    return flavor.name


def create_instance(
    *,
    client: Gcore,
    region_id: int,
    flavor_name: str,
    boot_volume_id: str,
    port_id: str,
    ssh_key_id: Optional[str],
) -> Instance:
    print("\n=== CREATE INSTANCE ===")
    instance = client.cloud.instances.create_and_poll(
        region_id=region_id,
        flavor_name=flavor_name,
        boot_volume_id=boot_volume_id,
        # the order of the ports is the order of the network interfaces
        interfaces=[{"port_id": port_id}],
        name="gcore-python-example-instance",
        ssh_key_id=ssh_key_id or omit,
        tags={"name": "gcore-python-example"},
    )
    print("Created instance:")
    _print_instance_details(instance)
    print("========================")
    return instance


def get_instance(*, client: Gcore, instance_id: str) -> None:
    print("\n=== GET INSTANCE ===")
    instance = client.cloud.instances.get(instance_id=instance_id)
    print("Instance:")
    _print_instance_details(instance)
    print("========================")


def list_instances(*, client: Gcore, region_id: int) -> None:
    print("\n=== LIST INSTANCES ===")
    # without region_ids the list holds the instances of all regions. Iterating the page fetches the
    # following pages automatically
    instances = client.cloud.instances.list(region_ids=[region_id], order_by="created_at.desc", limit=10)
    for count, instance in enumerate(instances, 1):
        print(
            f"  {count}. Instance: ID={instance.id}, name={instance.name}, region ID={instance.region_id}, "
            f"status={instance.status}"
        )
    print("========================")


def pick_resize_flavor(*, client: Gcore, instance_id: str) -> Optional[str]:
    """Return the smallest available flavor that the instance can resize to, or None."""
    print("\n=== LIST RESIZE FLAVORS ===")
    # the list holds the flavors of the instance region that the instance can resize to, without its
    # current flavor
    resize_flavor_name: Optional[str] = None
    flavors = client.cloud.instances.resize_flavors.list(instance_id=instance_id, order_by="vcpus.asc")
    for count, flavor in enumerate(flavors, 1):
        print(
            f"  {count}. Flavor: name={flavor.name}, vCPUs={flavor.vcpus}, RAM={flavor.ram_mib} MiB, "
            f"available={flavor.available}"
        )
        if resize_flavor_name is None and flavor.available:
            resize_flavor_name = flavor.name
    if resize_flavor_name is None:
        print("No available flavor to resize to")
    print("========================")
    return resize_flavor_name


def resize_instance(*, client: Gcore, instance_id: str, flavor_name: str) -> None:
    print("\n=== RESIZE INSTANCE ===")
    # a resize restarts the instance. The same call can also rename the instance, change its ports and
    # data volumes, or move it to a placement group with placement_group_id
    instance = client.cloud.instances.update_and_poll(instance_id=instance_id, flavor_name=flavor_name)
    print(f"Resized instance: ID={instance.id}, flavor name={instance.flavor_name}, status={instance.status}")
    print("========================")


def get_console(*, client: Gcore, instance_id: str) -> None:
    print("\n=== GET CONSOLE ===")
    console = client.cloud.instances.console.get(instance_id=instance_id, console_type="novnc")
    remote_console = console.remote_console
    print(f"Console: protocol={remote_console.protocol}, type={remote_console.type}, url={remote_console.url}")
    print("========================")


def run_action(*, client: Gcore, instance_id: str, action: Literal["start", "stop"]) -> None:
    print(f"\n=== {action.upper()} INSTANCE ===")
    instance = client.cloud.instances.action_and_poll(instance_id=instance_id, action=action)
    print(f"Ran action {action}: ID={instance.id}, status={instance.status}")
    print("========================")


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


def delete_instance(*, client: Gcore, instance_id: str, volume_ids: List[str], port_ids: List[str]) -> None:
    print("\n=== DELETE INSTANCE ===")
    # by default the delete keeps the volumes, ports and floating IPs of the instance. The cascade
    # options name the resources to delete with it
    client.cloud.instances.delete_and_poll(instance_id=instance_id, volume_ids=volume_ids, port_ids=port_ids)
    print(f"Deleted instance: ID={instance_id}, volume IDs={volume_ids}, port IDs={port_ids}")
    print("========================")


def upload_image(*, client: Gcore) -> str:
    print("\n=== UPLOAD IMAGE ===")

    image = client.cloud.instances.images.upload_and_poll(
        name="gcore-go-example-uploaded",
        url="https://cloud-images.ubuntu.com/releases/24.04/release/ubuntu-24.04-server-cloudimg-amd64.img",
        os_type="linux",
        architecture="x86_64",
        ssh_key="allow",
        os_distro="Ubuntu",
        os_version="24.04",
    )

    print(
        f"Uploaded image: ID={image.id}, name={image.name}, OS type={image.os_type}, arch={image.architecture}, status={image.status}, size={image.size}"
    )
    print("========================")
    return image.id


def create_image_from_volume(*, client: Gcore, volume_id: str) -> str:
    print("\n=== CREATE IMAGE FROM VOLUME ===")

    image = client.cloud.instances.images.create_from_volume_and_poll(
        volume_id=volume_id, name="gcore-go-example", os_type="linux"
    )

    print(f"Created image ID: {image.id}")
    print("========================")
    return image.id


def list_images(*, client: Gcore) -> None:
    print("\n=== LIST ALL IMAGES ===")

    images = client.cloud.instances.images.list()

    display_count = 3
    if len(images.results) < display_count:
        display_count = len(images.results)

    for i in range(display_count):
        img = images.results[i]
        print(f"  {i + 1}. Image ID: {img.id}, name: {img.name}, OS type: {img.os_type}, status: {img.status}")

    if len(images.results) > display_count:
        print(f"  ... and {len(images.results) - display_count} more images")

    print("========================")


def get_image(*, client: Gcore, image_id: str) -> None:
    print("\n=== GET IMAGE BY ID ===")

    image = client.cloud.instances.images.get(image_id=image_id)

    print(f"Image ID: {image.id}, name: {image.name}, OS type: {image.os_type}, status: {image.status}")
    print("========================")


def update_image(*, client: Gcore, image_id: str) -> None:
    print("\n=== UPDATE IMAGE ===")

    updated_image = client.cloud.instances.images.update(image_id=image_id, name="gcore-go-example-updated")

    print(f"Updated image ID: {updated_image.id}, name: {updated_image.name}")
    print("========================")


def delete_image(*, client: Gcore, image_id: str) -> None:
    print("\n=== DELETE IMAGE ===")

    client.cloud.instances.images.delete_and_poll(image_id=image_id)

    print(f"Image with ID {image_id} successfully deleted")
    print("========================")


def _print_instance_details(instance: Instance) -> None:
    print(f"  ID={instance.id}, name={instance.name}, status={instance.status}, region ID={instance.region_id}")
    print(f"  Flavor name={instance.flavor_name}, boot volume ID={instance.boot_volume_id}")
    for interface in instance.interfaces:
        print(f"  Interface: port ID={interface.port_id}, network ID={interface.network_id}")
        for assignment in interface.ip_assignments:
            print(f"    IP assignment: IP address={assignment.ip_address}, subnet ID={assignment.subnet_id}")


if __name__ == "__main__":
    main()
