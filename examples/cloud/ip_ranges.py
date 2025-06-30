import os

from gcore import Gcore
from gcore.types.cloud import IPRanges


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    list_all_ip_ranges()


def list_all_ip_ranges() -> IPRanges:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_ip_ranges = gcore.cloud.ip_ranges.list()

    print("\n=== LIST ALL IP RANGES ===")
    for count, iprange in enumerate(all_ip_ranges.ranges, 1):
        print(f"  {count}. IP Range: {iprange}")
    print("===========================")
    return all_ip_ranges


if __name__ == "__main__":
    main()
