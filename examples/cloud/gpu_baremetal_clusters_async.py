import asyncio
from typing import List

from gcore import AsyncGcore
from gcore.types.cloud.gpu_image import GPUImage
from gcore.types.cloud.network_interface import NetworkInterface
from gcore.types.cloud.gpu_baremetal.cluster_create_params import (
    ServersSettings,
    ServersSettingsInterfaceExternalInterfaceInputSerializer,
)
from gcore.types.cloud.gpu_baremetal.gpu_baremetal_cluster import GPUBaremetalCluster
from gcore.types.cloud.gpu_baremetal.clusters.gpu_baremetal_flavor import GPUBaremetalFlavor


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

    # Flavors
    flavors = await list_flavors(client=gcore)

    # Images
    images = await list_images(client=gcore)

    # Clusters
    flavor_name = _get_first_available_flavor(flavors)
    image_id = _get_first_image(images)
    cluster = await create_cluster(client=gcore, flavor=flavor_name, image_id=image_id)
    await get_cluster(client=gcore, cluster_id=cluster.id)
    await list_clusters(client=gcore)
    await update_cluster(client=gcore, cluster_id=cluster.id)

    # Interfaces
    await list_interfaces(client=gcore, cluster_id=cluster.id)

    # Servers
    await list_servers(client=gcore, cluster_id=cluster.id)

    # Delete
    await delete_cluster(client=gcore, cluster_id=cluster.id)


async def create_cluster(*, client: AsyncGcore, flavor: str, image_id: str) -> GPUBaremetalCluster:
    print("\n=== CREATE GPU BAREMETAL CLUSTER ===")
    cluster = await client.cloud.gpu_baremetal.clusters.create_and_poll(
        name="gcore-python-example-gpu-baremetal",
        flavor=flavor,
        image_id=image_id,
        servers_count=1,
        servers_settings=ServersSettings(
            interfaces=[
                ServersSettingsInterfaceExternalInterfaceInputSerializer(type="external"),
            ],
        ),
        tags={"name": "gcore-python-example"},
    )
    print(f"Created cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")
    return cluster


async def get_cluster(*, client: AsyncGcore, cluster_id: str) -> GPUBaremetalCluster:
    print("\n=== GET GPU BAREMETAL CLUSTER ===")
    cluster = await client.cloud.gpu_baremetal.clusters.get(cluster_id=cluster_id)
    print(f"Cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")
    return cluster


async def list_clusters(*, client: AsyncGcore) -> None:
    print("\n=== LIST GPU BAREMETAL CLUSTERS ===")
    clusters = await client.cloud.gpu_baremetal.clusters.list()
    count = 0
    async for cluster in clusters:
        count += 1
        print(f"  {count}. Cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")


async def update_cluster(*, client: AsyncGcore, cluster_id: str) -> None:
    print("\n=== UPDATE GPU BAREMETAL CLUSTER ===")
    cluster = await client.cloud.gpu_baremetal.clusters.update(
        cluster_id=cluster_id, name="gcore-python-example-gpu-baremetal-updated"
    )
    print(f"Updated cluster: ID={cluster.id}, name={cluster.name}")
    print("========================")


async def delete_cluster(*, client: AsyncGcore, cluster_id: str) -> None:
    print("\n=== DELETE GPU BAREMETAL CLUSTER ===")
    await client.cloud.gpu_baremetal.clusters.delete_and_poll(
        cluster_id=cluster_id,
        all_floating_ips=True,
    )
    print(f"Deleted cluster: ID={cluster_id}")
    print("========================")


async def list_interfaces(*, client: AsyncGcore, cluster_id: str) -> List[NetworkInterface]:
    print("\n=== LIST GPU BAREMETAL CLUSTER INTERFACES ===")
    interfaces = await client.cloud.gpu_baremetal.clusters.interfaces.list(cluster_id=cluster_id)
    for count, interface in enumerate(interfaces.results, 1):
        print(f"  {count}. Interface: PortID={interface.port_id}, NetworkID={interface.network_id}")
    print("========================")
    return interfaces.results


async def list_servers(*, client: AsyncGcore, cluster_id: str) -> None:
    print("\n=== LIST GPU BAREMETAL CLUSTER SERVERS ===")
    servers = await client.cloud.gpu_baremetal.clusters.servers.list(cluster_id=cluster_id)
    for count, server in enumerate(servers.results, 1):
        print(f"  {count}. Server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")


async def list_flavors(*, client: AsyncGcore) -> List[GPUBaremetalFlavor]:
    print("\n=== LIST GPU BAREMETAL FLAVORS ===")
    flavors = await client.cloud.gpu_baremetal.clusters.flavors.list()
    _print_flavor_details(flavors.results)
    print("========================")
    return flavors.results


async def list_images(*, client: AsyncGcore) -> List[GPUImage]:
    print("\n=== LIST GPU BAREMETAL IMAGES ===")
    images = await client.cloud.gpu_baremetal.clusters.images.list()
    _print_image_details(images.results)
    print("========================")
    return images.results


def _print_flavor_details(flavors: List[GPUBaremetalFlavor]) -> None:
    display_count = 3
    if len(flavors) < display_count:
        display_count = len(flavors)

    for i in range(display_count):
        flavor = flavors[i]
        print(f"  {i + 1}. Flavor: name={flavor.name}")
        print(f"     Capacity: {flavor.capacity}")
        status = "AVAILABLE"
        if flavor.disabled:
            status = "DISABLED"
        print(f"     Status: {status}")
        print()

    if len(flavors) > display_count:
        print(f"  ... and {len(flavors) - display_count} more flavors")


def _print_image_details(images: List[GPUImage]) -> None:
    display_count = 3
    if len(images) < display_count:
        display_count = len(images)

    for i in range(display_count):
        img = images[i]
        print(f"  {i + 1}. Image ID: {img.id}, name: {img.name}, OS type: {img.os_type}, status: {img.status}")

    if len(images) > display_count:
        print(f"  ... and {len(images) - display_count} more images")


def _get_first_available_flavor(flavors: List[GPUBaremetalFlavor]) -> str:
    available_flavors = [f for f in flavors if not f.disabled and f.capacity > 0]
    if not available_flavors:
        raise ValueError("No available flavors with capacity found")
    selected = available_flavors[0]
    print(f"Selected flavor: {selected.name} (Capacity: {selected.capacity})")
    return selected.name


def _get_first_image(images: List[GPUImage]) -> str:
    if not images:
        raise ValueError("No images found")
    selected = images[0]
    print(f"Selected image: {selected.name} (ID: {selected.id})")
    return selected.id


if __name__ == "__main__":
    asyncio.run(main())
