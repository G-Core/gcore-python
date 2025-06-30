import os
import asyncio

from gcore import AsyncGcore
from gcore.types.cloud import IPRanges


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    await list_all_ip_ranges()


async def list_all_ip_ranges() -> IPRanges:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_ip_ranges = await gcore.cloud.ip_ranges.list()

    print("\n=== LIST ALL IP RANGES ===")
    count = 1
    for iprange in all_ip_ranges.ranges:
        print(f"  {count}. IP Range: {iprange}")
        count += 1
    print("===========================")
    return all_ip_ranges


if __name__ == "__main__":
    asyncio.run(main())
