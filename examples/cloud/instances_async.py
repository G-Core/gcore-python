import os
import asyncio
from typing import List

from gcore import AsyncGcore
from gcore.types.cloud.instance import Volume, Instance
from gcore.types.cloud.network_interface import NetworkInterface
from gcore.types.cloud.instance_create_params import (
    InterfaceNewInterfaceExternalSerializerPydantic,
    VolumeCreateInstanceCreateVolumeFromImageSerializer,
)
from gcore.types.cloud.instances.instance_flavor import InstanceFlavor


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set placement group ID before running
    placement_group_id = os.environ.get("GCORE_CLOUD_PLACEMENT_GROUP_ID")

    gcore = AsyncGcore(
        timeout=180.0,
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    uploaded_image_id = await upload_image(client=gcore)

    instance_id = await create_instance(client=gcore, image_id=uploaded_image_id)
    instance = await get_instance(client=gcore, instance_id=instance_id)
    await get_console(client=gcore, instance_id=instance_id)
    await list_instances(client=gcore)
    await update_instance(client=gcore, instance_id=instance_id)
    await reboot_instance(client=gcore, instance_id=instance_id)
    await resize_instance(client=gcore, instance_id=instance_id)

    # Flavors
    await list_flavors(client=gcore)

    # Images
    await list_images(client=gcore)
    await get_image(client=gcore, image_id=uploaded_image_id)
    await update_image(client=gcore, image_id=uploaded_image_id)
    await delete_image(client=gcore, image_id=uploaded_image_id)
    # volume_image_id = await create_image_from_volume(client=gcore, volume_id=instance.volumes[0].id)
    # await delete_image(client=gcore, image_id=volume_image_id)

    # Interfaces
    interfaces = await list_interfaces(client=gcore, instance_id=instance_id)
    if interfaces:
        ip_address = interfaces[0].ip_assignments[0].ip_address
        port_id = interfaces[0].port_id
        network_id = interfaces[0].network_id
        await detach_interface(client=gcore, instance_id=instance_id, ip_address=ip_address, port_id=port_id)
        await attach_interface(client=gcore, instance_id=instance_id, network_id=network_id)

    # Metrics
    await list_metrics(client=gcore, instance_id=instance_id)

    # Placement groups
    if placement_group_id:
        await add_to_placement_group(client=gcore, instance_id=instance_id, placement_group_id=placement_group_id)
        await remove_from_placement_group(client=gcore, instance_id=instance_id)

    # Security groups
    await unassign_security_group(client=gcore, instance_id=instance_id)
    await assign_security_group(client=gcore, instance_id=instance_id)

    await delete_instance(client=gcore, instance_id=instance_id, volumes=instance.volumes)


async def create_instance(*, client: AsyncGcore, image_id: str) -> str:
    print("\n=== CREATE INSTANCE ===")

    instance = await client.cloud.instances.create_and_poll(
        name="gcore-go-example-instance",
        flavor="g1-standard-1-2",
        interfaces=[
            InterfaceNewInterfaceExternalSerializerPydantic(type="external"),
        ],
        volumes=[
            VolumeCreateInstanceCreateVolumeFromImageSerializer(
                name="gcore-go-example-volume",
                size=10,
                type_name="standard",
                source="image",
                image_id=image_id,
                boot_index=0,
            ),
        ],
        password="Gcore123!",
        tags={"name": "gcore-go-example"},
    )
    print(f"Created instance: ID={instance.id}, name={instance.name}, status={instance.status}")
    print("========================")
    return instance.id


async def get_instance(*, client: AsyncGcore, instance_id: str) -> Instance:
    print("\n=== GET INSTANCE ===")
    instance = await client.cloud.instances.get(instance_id=instance_id)
    print(f"Instance: ID={instance.id}, name={instance.name}, status={instance.status}")
    print("========================")
    return instance


async def get_console(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== GET CONSOLE ===")
    console = await client.cloud.instances.get_console(instance_id=instance_id)
    print(
        f"Console: protocol={console.remote_console.protocol}, type={console.remote_console.type}, url={console.remote_console.url}"
    )
    print("========================")


async def list_instances(*, client: AsyncGcore) -> None:
    print("\n=== LIST INSTANCES ===")
    instances = await client.cloud.instances.list()
    count = 0
    async for instance in instances:
        count += 1
        print(f"  {count}. Instance: ID={instance.id}, name={instance.name}, status={instance.status}")
    print("========================")


async def update_instance(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== UPDATE INSTANCE ===")
    instance = await client.cloud.instances.update(instance_id=instance_id, name="gcore-go-example-updated")
    print(f"Instance updated: ID={instance.id}, name changed to {instance.name}")
    print("========================")


async def reboot_instance(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== REBOOT INSTANCE ===")
    response = await client.cloud.instances.action(instance_id=instance_id, action="reboot")
    await client.cloud.tasks.poll(task_id=response.tasks[0])
    print(f"Rebooted instance: {instance_id}")
    print("========================")


async def resize_instance(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== RESIZE INSTANCE ===")
    instance = await client.cloud.instances.resize_and_poll(instance_id=instance_id, flavor_id="g1-standard-2-4")
    print(f"Instance resized: ID={instance.id}, new flavor=g1-standard-2-4")
    print("========================")


async def list_flavors(*, client: AsyncGcore) -> None:
    print("\n=== LIST FLAVORS ===")
    flavors = await client.cloud.instances.flavors.list()
    await _print_flavor_details(flavors.results)
    print("========================")


async def list_interfaces(*, client: AsyncGcore, instance_id: str) -> List[NetworkInterface]:
    print("\n=== LIST INTERFACES ===")
    interfaces = await client.cloud.instances.interfaces.list(instance_id=instance_id)
    for count, interface in enumerate(interfaces.results, 1):
        print(f"  {count}. Interface: PortID={interface.port_id}, NetworkID={interface.network_id}")
    print("========================")
    return interfaces.results


async def list_metrics(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== LIST METRICS ===")
    metrics = await client.cloud.instances.metrics.list(instance_id=instance_id, time_interval=1, time_unit="hour")
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


async def assign_security_group(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== ASSIGN SECURITY GROUP ===")
    await client.cloud.instances.assign_security_group(instance_id=instance_id, name="default")
    print("Assigned security group: default")
    print("========================")


async def unassign_security_group(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== UNASSIGN SECURITY GROUP ===")
    await client.cloud.instances.unassign_security_group(instance_id=instance_id, name="default")
    print("Unassigned security group: default")
    print("========================")


async def add_to_placement_group(*, client: AsyncGcore, instance_id: str, placement_group_id: str) -> None:
    print("\n=== ADD TO PLACEMENT GROUP ===")
    await client.cloud.instances.add_to_placement_group_and_poll(
        instance_id=instance_id, servergroup_id=placement_group_id
    )
    print(f"Added instance {instance_id} to placement group: {placement_group_id}")
    print("========================")


async def remove_from_placement_group(*, client: AsyncGcore, instance_id: str) -> None:
    print("\n=== REMOVE FROM PLACEMENT GROUP ===")
    await client.cloud.instances.remove_from_placement_group_and_poll(instance_id=instance_id)
    print(f"Removed instance {instance_id} from placement group")
    print("========================")


async def detach_interface(*, client: AsyncGcore, instance_id: str, ip_address: str, port_id: str) -> None:
    print("\n=== DETACH INTERFACE ===")
    response = await client.cloud.instances.interfaces.detach(
        instance_id=instance_id, ip_address=ip_address, port_id=port_id
    )
    await client.cloud.tasks.poll(task_id=response.tasks[0])

    print(f"Detached interface (IP: {ip_address}, Port: {port_id}) from instance: {instance_id}")
    print("========================")


async def attach_interface(*, client: AsyncGcore, instance_id: str, network_id: str) -> None:
    print("\n=== ATTACH INTERFACE ===")
    response = await client.cloud.instances.interfaces.attach(
        instance_id=instance_id, type="any_subnet", network_id=network_id
    )
    await client.cloud.tasks.poll(task_id=response.tasks[0])

    print(f"Attached interface to any available subnet in network {network_id} (instance: {instance_id})")
    print("========================")


async def delete_instance(*, client: AsyncGcore, instance_id: str, volumes: List[Volume]) -> None:
    print("\n=== DELETE INSTANCE ===")
    volumes_str = ""
    if volumes:
        volumes_str = ",".join([vol.id for vol in volumes])

    await client.cloud.instances.delete_and_poll(
        instance_id=instance_id,
        delete_floatings=True,
        volumes=volumes_str,
    )
    print(f"Deleted instance and related resources: ID={instance_id}, Volumes={volumes_str}")
    print("========================")


async def upload_image(*, client: AsyncGcore) -> str:
    print("\n=== UPLOAD IMAGE ===")

    image = await client.cloud.instances.images.upload_and_poll(
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


async def create_image_from_volume(*, client: AsyncGcore, volume_id: str) -> str:
    print("\n=== CREATE IMAGE FROM VOLUME ===")

    image = await client.cloud.instances.images.create_from_volume_and_poll(
        volume_id=volume_id, name="gcore-go-example", os_type="linux"
    )

    print(f"Created image ID: {image.id}")
    print("========================")
    return image.id


async def list_images(*, client: AsyncGcore) -> None:
    print("\n=== LIST ALL IMAGES ===")

    images = await client.cloud.instances.images.list()

    display_count = 3
    if len(images.results) < display_count:
        display_count = len(images.results)

    for i in range(display_count):
        img = images.results[i]
        print(f"  {i + 1}. Image ID: {img.id}, name: {img.name}, OS type: {img.os_type}, status: {img.status}")

    if len(images.results) > display_count:
        print(f"  ... and {len(images.results) - display_count} more images")

    print("========================")


async def get_image(*, client: AsyncGcore, image_id: str) -> None:
    print("\n=== GET IMAGE BY ID ===")

    image = await client.cloud.instances.images.get(image_id=image_id)

    print(f"Image ID: {image.id}, name: {image.name}, OS type: {image.os_type}, status: {image.status}")
    print("========================")


async def update_image(*, client: AsyncGcore, image_id: str) -> None:
    print("\n=== UPDATE IMAGE ===")

    updated_image = await client.cloud.instances.images.update(image_id=image_id, name="gcore-go-example-updated")

    print(f"Updated image ID: {updated_image.id}, name: {updated_image.name}")
    print("========================")


async def delete_image(*, client: AsyncGcore, image_id: str) -> None:
    print("\n=== DELETE IMAGE ===")

    await client.cloud.instances.images.delete_and_poll(image_id=image_id)

    print(f"Image with ID {image_id} successfully deleted")
    print("========================")


async def _print_flavor_details(flavors: List[InstanceFlavor]) -> None:
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


if __name__ == "__main__":
    asyncio.run(main())
