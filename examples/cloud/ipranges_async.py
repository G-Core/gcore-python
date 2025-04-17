import os
import asyncio

from gcore import AsyncGcore
from gcore.types.cloud import IPRanges


async def list_all_ipranges() -> IPRanges:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = AsyncGcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_ipranges = await gcore.cloud.ip_ranges.list()

    print("\n=== LIST ALL IP RANGES ===")
    count = 1
    for iprange in all_ipranges.ranges:
        print(f"  {count}. IP Range: {iprange}")
        count += 1
    print("===========================")
    return all_ipranges


async def main() -> None:
    await list_all_ipranges()


if __name__ == "__main__":
    asyncio.run(main())
