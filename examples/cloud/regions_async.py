import os
import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import Region


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud region ID before running
    cloud_region_id = int(os.environ.get("GCORE_CLOUD_REGION_ID", 76))

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    await get_region_by_id(client=gcore, region_id=cloud_region_id)
    await list_all_regions(client=gcore)
    await list_regions_with_filters(client=gcore)


async def get_region_by_id(*, client: AsyncGcore, region_id: int) -> Region:
    print("\n=== GET REGION BY ID ===")
    region = await client.cloud.regions.get(region_id=region_id)
    print(f"Region ID: {region.id}, display name: {region.display_name}")
    print("========================")
    return region


async def list_all_regions(*, client: AsyncGcore) -> AsyncOffsetPage[Region]:
    print("\n=== LIST ALL REGIONS ===")
    all_regions = await client.cloud.regions.list()
    count = 1
    async for region in all_regions:
        print(f"  {count}. Region ID: {region.id}, display name: {region.display_name}")
        count += 1
    print("========================")
    return all_regions


async def list_regions_with_filters(*, client: AsyncGcore) -> AsyncOffsetPage[Region]:
    print("\n=== LIST REGIONS WITH FILTERS ===")
    filtered_regions = await client.cloud.regions.list(product="inference")
    count = 1
    async for region in filtered_regions:
        print(f"  {count}. Region ID: {region.id}, display name: {region.display_name}")
        count += 1
    print("=================================")
    return filtered_regions


if __name__ == "__main__":
    asyncio.run(main())
