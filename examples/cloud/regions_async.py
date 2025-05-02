import os
import asyncio

from gcore import AsyncGcore
from gcore.pagination import AsyncOffsetPage
from gcore.types.cloud import Region


async def get_region_by_id() -> Region:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"))
    # Region ID can also be omitted — it defaults to the GCORE_CLOUD_REGION_ID environment variable
    region = await gcore.cloud.regions.get(region_id=int(os.environ.get("GCORE_CLOUD_REGION_ID", "76")))

    print("\n=== GET REGION BY ID ===")
    print(f"Region ID: {region.id}, Display Name: {region.display_name}")
    print("========================")
    return region


async def list_all_regions() -> AsyncOffsetPage[Region]:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"))
    all_regions = await gcore.cloud.regions.list()

    print("\n=== LIST ALL REGIONS ===")
    count = 1
    async for region in all_regions:
        print(f"  {count}. Region ID: {region.id}, Display Name: {region.display_name}")
        count += 1
    print("========================")
    return all_regions


async def list_regions_with_filters() -> AsyncOffsetPage[Region]:
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"))
    filtered_regions = await gcore.cloud.regions.list(product="containers")

    print("\n=== LIST REGIONS WITH FILTERS ===")
    count = 1
    async for region in filtered_regions:
        print(f"  {count}. Region ID: {region.id}, Display Name: {region.display_name}")
        count += 1
    print("=================================")
    return filtered_regions


async def main() -> None:
    await get_region_by_id()
    await list_all_regions()
    await list_regions_with_filters()


if __name__ == "__main__":
    asyncio.run(main())
