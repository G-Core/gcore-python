from typing import List

from gcore import Gcore
from gcore.types.cloud.gpu_image import GPUImage
from gcore.types.cloud.gpu_virtual.gpu_virtual_cluster import GPUVirtualCluster
from gcore.types.cloud.gpu_virtual.cluster_create_params import (
    ServersSettings,
    ServersSettingsVolumeImageVolumeInputSerializer,
    ServersSettingsInterfaceExternalInterfaceInputSerializer,
)
from gcore.types.cloud.gpu_virtual.clusters.gpu_virtual_flavor import GPUVirtualFlavor


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

    # Servers
    list_servers(client=gcore, cluster_id=cluster.id)

    # Delete
    delete_cluster(client=gcore, cluster_id=cluster.id)


def create_cluster(*, client: Gcore, flavor: str, image_id: str) -> GPUVirtualCluster:
    print("\n=== CREATE GPU VIRTUAL CLUSTER ===")
    cluster = client.cloud.gpu_virtual.clusters.create_and_poll(
        name="gcore-python-example-gpu-virtual",
        flavor=flavor,
        servers_count=1,
        servers_settings=ServersSettings(
            interfaces=[
                ServersSettingsInterfaceExternalInterfaceInputSerializer(type="external"),
            ],
            volumes=[
                ServersSettingsVolumeImageVolumeInputSerializer(
                    name="gcore-python-example-volume",
                    size=50,
                    type="standard",
                    source="image",
                    image_id=image_id,
                    boot_index=0,
                ),
            ],
        ),
        tags={"name": "gcore-python-example"},
    )
    print(f"Created cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")
    return cluster


def get_cluster(*, client: Gcore, cluster_id: str) -> GPUVirtualCluster:
    print("\n=== GET GPU VIRTUAL CLUSTER ===")
    cluster = client.cloud.gpu_virtual.clusters.get(cluster_id=cluster_id)
    print(f"Cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")
    return cluster


def list_clusters(*, client: Gcore) -> None:
    print("\n=== LIST GPU VIRTUAL CLUSTERS ===")
    clusters = client.cloud.gpu_virtual.clusters.list()
    for count, cluster in enumerate(clusters, 1):
        print(f"  {count}. Cluster: ID={cluster.id}, name={cluster.name}, status={cluster.status}")
    print("========================")


def update_cluster(*, client: Gcore, cluster_id: str) -> None:
    print("\n=== UPDATE GPU VIRTUAL CLUSTER ===")
    cluster = client.cloud.gpu_virtual.clusters.update(
        cluster_id=cluster_id, name="gcore-python-example-gpu-virtual-updated"
    )
    print(f"Updated cluster: ID={cluster.id}, name={cluster.name}")
    print("========================")


def delete_cluster(*, client: Gcore, cluster_id: str) -> None:
    print("\n=== DELETE GPU VIRTUAL CLUSTER ===")
    client.cloud.gpu_virtual.clusters.delete_and_poll(
        cluster_id=cluster_id,
        all_volumes=True,
        all_floating_ips=True,
    )
    print(f"Deleted cluster: ID={cluster_id}")
    print("========================")


def list_servers(*, client: Gcore, cluster_id: str) -> None:
    print("\n=== LIST GPU VIRTUAL CLUSTER SERVERS ===")
    servers = client.cloud.gpu_virtual.clusters.servers.list(cluster_id=cluster_id)
    for count, server in enumerate(servers.results, 1):
        print(f"  {count}. Server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")


def list_flavors(*, client: Gcore) -> List[GPUVirtualFlavor]:
    print("\n=== LIST GPU VIRTUAL FLAVORS ===")
    flavors = client.cloud.gpu_virtual.clusters.flavors.list()
    _print_flavor_details(flavors.results)
    print("========================")
    return flavors.results


def list_images(*, client: Gcore) -> List[GPUImage]:
    print("\n=== LIST GPU VIRTUAL IMAGES ===")
    images = client.cloud.gpu_virtual.clusters.images.list()
    _print_image_details(images.results)
    print("========================")
    return images.results


def _print_flavor_details(flavors: List[GPUVirtualFlavor]) -> None:
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


def _get_first_available_flavor(flavors: List[GPUVirtualFlavor]) -> str:
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
