from typing import List

from gcore import Gcore
from gcore.types.cloud.image import Image
from gcore.types.cloud.baremetal_flavor import BaremetalFlavor
from gcore.types.cloud.baremetal.server_create_params import (
    InterfaceCreateBareMetalExternalInterfaceSerializer,
)


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

    # Servers
    server_id = create_server(client=gcore, flavor_id=_get_smallest_flavor(flavors), image_id=_get_ubuntu_image(images))
    list_servers(client=gcore)
    rebuild_server(client=gcore, server_id=server_id, image_id=_get_debian_image(images))


def create_server(*, client: Gcore, flavor_id: str, image_id: str) -> str:
    print("\n=== CREATE BAREMETAL SERVER ===")

    server = client.cloud.baremetal.servers.create_and_poll(
        name="gcore-go-example-baremetal",
        flavor=flavor_id,
        interfaces=[
            InterfaceCreateBareMetalExternalInterfaceSerializer(type="external"),
        ],
        image_id=image_id,
        password="Gcore123!",
        tags={"name": "gcore-go-example"},
    )
    print(f"Created baremetal server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")
    return server.id


def list_servers(*, client: Gcore) -> None:
    print("\n=== LIST BAREMETAL SERVERS ===")
    servers = client.cloud.baremetal.servers.list()
    for count, server in enumerate(servers.results, 1):
        print(f"  {count}. Server: ID={server.id}, name={server.name}, status={server.status}")
    print("========================")
    print()


def rebuild_server(*, client: Gcore, server_id: str, image_id: str) -> None:
    print("\n=== REBUILD BAREMETAL SERVER ===")
    server = client.cloud.baremetal.servers.rebuild_and_poll(
        server_id=server_id,
        image_id=image_id,
    )
    print(f"Rebuilt baremetal server: ID={server.id}, name={server.name}")
    print("========================")


def list_flavors(*, client: Gcore) -> List[BaremetalFlavor]:
    print("\n=== LIST BAREMETAL FLAVORS ===")
    flavors = client.cloud.baremetal.flavors.list(include_capacity=True)
    _print_flavor_details(flavors.results)
    print("========================")
    return flavors.results


def list_images(*, client: Gcore) -> List[Image]:
    print("\n=== LIST BAREMETAL IMAGES ===")
    images = client.cloud.baremetal.images.list()
    _print_image_details(images.results)
    print("========================")
    return images.results


def _print_flavor_details(flavors: List[BaremetalFlavor]) -> None:
    display_count = 3
    if len(flavors) < display_count:
        display_count = len(flavors)

    for i in range(display_count):
        flavor = flavors[i]
        print(f"  {i + 1}. Flavor: ID={flavor.flavor_id}, name={flavor.flavor_name}")
        print(f"     RAM: {flavor.ram} MB, VCPUs: {flavor.vcpus}")
        print(f"     Architecture: {flavor.architecture}, OS: {flavor.os_type}")
        status = "AVAILABLE"
        if flavor.disabled:
            status = "DISABLED"
        print(f"     Status: {status}")
        print()

    if len(flavors) > display_count:
        print(f"  ... and {len(flavors) - display_count} more flavors")


def _print_image_details(images: List[Image]) -> None:
    display_count = 3
    if len(images) < display_count:
        display_count = len(images)

    for i in range(display_count):
        img = images[i]
        print(f"  {i + 1}. Image ID: {img.id}, name: {img.name}, OS type: {img.os_type}, status: {img.status}")

    if len(images) > display_count:
        print(f"  ... and {len(images) - display_count} more images")


def _get_smallest_flavor(flavors: List[BaremetalFlavor]) -> str:
    available_flavors = [f for f in flavors if not f.disabled and f.capacity is not None and f.capacity > 0]
    if not available_flavors:
        raise ValueError("No available flavors with capacity found")

    smallest_flavor = min(available_flavors, key=lambda f: f.ram)
    print(
        f"Selected smallest flavor: {smallest_flavor.flavor_name} (RAM: {smallest_flavor.ram} MB, Capacity: {smallest_flavor.capacity})"
    )
    return smallest_flavor.flavor_id


def _get_ubuntu_image(images: List[Image]) -> str:
    return _get_os_image(images, "ubuntu")


def _get_debian_image(images: List[Image]) -> str:
    return _get_os_image(images, "debian")


def _get_os_image(images: List[Image], os_name: str) -> str:
    os_images = [img for img in images if os_name.lower() in img.name.lower()]
    if not os_images:
        linux_images = [img for img in images if img.os_type.lower() == "linux"]
        if not linux_images:
            if images:
                selected_image = images[0]
                print(f"No {os_name.title()}/Linux images found, using first available: {selected_image.name}")
            else:
                raise ValueError("No images found")
        else:
            selected_image = linux_images[0]
            print(f"No {os_name.title()} images found, using first Linux image: {selected_image.name}")
    else:
        selected_image = os_images[0]
        print(f"Selected {os_name.title()} image: {selected_image.name}")

    return selected_image.id


if __name__ == "__main__":
    main()
