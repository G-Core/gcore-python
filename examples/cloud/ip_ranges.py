from gcore import Gcore
from gcore.types.cloud import IPRanges


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    list_all_ip_ranges(client=gcore)


def list_all_ip_ranges(*, client: Gcore) -> IPRanges:
    print("\n=== LIST ALL IP RANGES ===")
    all_ip_ranges = client.cloud.ip_ranges.list()
    for count, iprange in enumerate(all_ip_ranges.ranges, 1):
        print(f"  {count}. IP Range: {iprange}")
    print("===========================")
    return all_ip_ranges


if __name__ == "__main__":
    main()
