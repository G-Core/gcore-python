import asyncio

from gcore import AsyncGcore
from gcore.types.cloud import IPRanges


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    await list_all_ip_ranges(client=gcore)


async def list_all_ip_ranges(*, client: AsyncGcore) -> IPRanges:
    print("\n=== LIST ALL IP RANGES ===")
    all_ip_ranges = await client.cloud.ip_ranges.list()
    for count, iprange in enumerate(all_ip_ranges.ranges, 1):
        print(f"  {count}. IP Range: {iprange}")
    print("===========================")
    return all_ip_ranges


if __name__ == "__main__":
    asyncio.run(main())
