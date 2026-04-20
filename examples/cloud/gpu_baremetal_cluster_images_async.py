import asyncio
from typing import List

from gcore import AsyncGcore
from gcore.types.cloud.gpu_image import GPUImage


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

    # List existing images
    await list_images(client=gcore)

    # Upload a new image
    image = await upload_image(client=gcore)

    # Get the newly uploaded image
    await get_image(client=gcore, image_id=image.id)

    # Delete the image
    await delete_image(client=gcore, image_id=image.id)


async def list_images(*, client: AsyncGcore) -> List[GPUImage]:
    print("\n=== LIST GPU BAREMETAL CLUSTER IMAGES ===")
    images = await client.cloud.gpu_baremetal.clusters.images.list()
    _print_image_details(images.results)
    print(f"Total GPU baremetal cluster images: {len(images.results)}")
    print("========================")
    return images.results


async def upload_image(*, client: AsyncGcore) -> GPUImage:
    print("\n=== UPLOAD GPU BAREMETAL CLUSTER IMAGE ===")
    image = await client.cloud.gpu_baremetal.clusters.images.upload_and_poll(
        name="gcore-python-example-gpu-baremetal-image",
        url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        architecture="x86_64",
        os_type="linux",
        ssh_key="allow",
        tags={"name": "gcore-python-example"},
    )
    print(f"Uploaded image: ID={image.id}, name={image.name}, status={image.status}")
    print("========================")
    return image


async def get_image(*, client: AsyncGcore, image_id: str) -> GPUImage:
    print("\n=== GET GPU BAREMETAL CLUSTER IMAGE ===")
    image = await client.cloud.gpu_baremetal.clusters.images.get(image_id=image_id)
    print(f"Image: ID={image.id}, name={image.name}, status={image.status}")
    print(f"OS type: {image.os_type}, architecture: {image.architecture}")
    print(f"Min RAM: {image.min_ram} MB, Min Disk: {image.min_disk} GB")
    print(f"Visibility: {image.visibility}")
    print("========================")
    return image


async def delete_image(*, client: AsyncGcore, image_id: str) -> None:
    print("\n=== DELETE GPU BAREMETAL CLUSTER IMAGE ===")
    await client.cloud.gpu_baremetal.clusters.images.delete_and_poll(image_id=image_id)
    print(f"Deleted image: ID={image_id}")
    print("========================")


def _print_image_details(images: List[GPUImage]) -> None:
    display_count = 3
    if len(images) < display_count:
        display_count = len(images)

    for i in range(display_count):
        img = images[i]
        print(f"  {i + 1}. Image ID: {img.id}, name: {img.name}, OS type: {img.os_type}, status: {img.status}")

    if len(images) > display_count:
        print(f"  ... and {len(images) - display_count} more images")


if __name__ == "__main__":
    asyncio.run(main())
