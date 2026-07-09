from typing import List

from gcore import Gcore
from gcore.types.cloud.gpu_image import GPUImage
from gcore.types.cloud.gpu_baremetal.cluster_create_params import (
    ServersSettings,
    ServersSettingsInterfaceExternalInterfaceInputSerializer,
)
from gcore.types.cloud.gpu_baremetal.gpu_baremetal_cluster import GPUBaremetalCluster
from gcore.types.cloud.gpu_baremetal.clusters.gpu_baremetal_flavor import GPUBaremetalFlavor
from gcore.types.cloud.gpu_baremetal.clusters.interface_list_response import Result
from gcore.types.cloud.gpu_baremetal.clusters.gpu_baremetal_cluster_server import GPUBaremetalClusterServer


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

    # Flavors
    flavors = list_flavors(client=gcore)

    # Images
    images = list_images(client=gcore)

    # Clusters
    flavor_name = _get_first_available_flavor(flavors)
    image_id = _get_first_image(images)
    cluster = create_cluster(client=gcore, flavor=flavor_name, image_id=image_id)
    get_cluster(client=gcore, cluster_id=cluster.id)
    list_clusters(client=gcore)
    update_cluster(client=gcore, cluster_id=cluster.id)

    # Interfaces
    list_interfaces(client=gcore, cluster_id=cluster.id)

    # Servers
    servers = list_servers(client=gcore, cluster_id=cluster.id)
    if servers:
        rebuild_server(client=gcore, cluster_id=cluster.id, server_id=servers[0].id)
        replace_server(client=gcore, cluster_id=cluster.id, server_id=servers[0].id)

    # Delete
    delete_cluster(client=gcore, cluster_id=cluster.id)


def create_cluster(*, client: Gcore, flavor: str, image_id: str) -> GPUBaremetalCluster:
    print("\n=== CREATE GPU BAREMETAL CLUSTER ===")
    cluster = client.cloud.gpu_baremetal.clusters.create_and_poll(
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


def get_cluster(*, client: Gcore, cluster_id: str) -> GPUBaremetalCluster:
    print("\n=== GET GPU BAREMETAL CLUSTER ===")
    cluster = client.cloud.gpu_baremetal.clusters.get(cluster_id=cluster_id)
    print(f"Cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")
    return cluster


def list_clusters(*, client: Gcore) -> None:
    print("\n=== LIST GPU BAREMETAL CLUSTERS ===")
    clusters = client.cloud.gpu_baremetal.clusters.list()
    for count, cluster in enumerate(clusters, 1):
        print(f"  {count}. Cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")


def update_cluster(*, client: Gcore, cluster_id: str) -> None:
    print("\n=== UPDATE GPU BAREMETAL CLUSTER ===")
    cluster = client.cloud.gpu_baremetal.clusters.update(
        cluster_id=cluster_id, name="gcore-python-example-gpu-baremetal-updated"
    )
    print(f"Updated cluster: ID={cluster.id}, name={cluster.name}")
    print("========================")


def delete_cluster(*, client: Gcore, cluster_id: str) -> None:
    print("\n=== DELETE GPU BAREMETAL CLUSTER ===")
    client.cloud.gpu_baremetal.clusters.delete_and_poll(
        cluster_id=cluster_id,
        all_floating_ips=True,
    )
    print(f"Deleted cluster: ID={cluster_id}")
    print("========================")


def list_interfaces(*, client: Gcore, cluster_id: str) -> List[Result]:
    print("\n=== LIST GPU BAREMETAL CLUSTER INTERFACES ===")
    interfaces = client.cloud.gpu_baremetal.clusters.interfaces.list(cluster_id=cluster_id)
    for count, interface in enumerate(interfaces.results, 1):
        print(f"  {count}. Interface: PortID={interface.port_id}, NetworkID={interface.network_id}")
    print("========================")
    return interfaces.results


def list_servers(*, client: Gcore, cluster_id: str) -> List[GPUBaremetalClusterServer]:
    print("\n=== LIST GPU BAREMETAL CLUSTER SERVERS ===")
    servers = client.cloud.gpu_baremetal.clusters.servers.list(cluster_id=cluster_id)
    for count, server in enumerate(servers.results, 1):
        print(f"  {count}. Server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")
    return servers.results


def rebuild_server(*, client: Gcore, cluster_id: str, server_id: str) -> GPUBaremetalClusterServer:
    print("\n=== REBUILD GPU BAREMETAL CLUSTER SERVER ===")
    server = client.cloud.gpu_baremetal.clusters.servers.rebuild_and_poll(
        server_id=server_id,
        cluster_id=cluster_id,
    )
    print(f"Rebuilt server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")
    return server


def replace_server(*, client: Gcore, cluster_id: str, server_id: str) -> GPUBaremetalClusterServer:
    print("\n=== REPLACE GPU BAREMETAL CLUSTER SERVER ===")
    server = client.cloud.gpu_baremetal.clusters.servers.replace_and_poll(
        server_id=server_id,
        cluster_id=cluster_id,
    )
    print(f"Replaced server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")
    return server


def list_flavors(*, client: Gcore) -> List[GPUBaremetalFlavor]:
    print("\n=== LIST GPU BAREMETAL FLAVORS ===")
    flavors = client.cloud.gpu_baremetal.clusters.flavors.list()
    _print_flavor_details(flavors.results)
    print("========================")
    return flavors.results


def list_images(*, client: Gcore) -> List[GPUImage]:
    print("\n=== LIST GPU BAREMETAL IMAGES ===")
    images = client.cloud.gpu_baremetal.clusters.images.list()
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
    main()
