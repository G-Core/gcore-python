import os

from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import Region


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud region ID before running
    cloud_region_id = int(os.environ.get("GCORE_CLOUD_REGION_ID", 76))

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    get_region_by_id(client=gcore, region_id=cloud_region_id)
    list_all_regions(client=gcore)
    list_regions_with_filters(client=gcore)


def get_region_by_id(*, client: Gcore, region_id: int) -> Region:
    print("\n=== GET REGION BY ID ===")
    region = client.cloud.regions.get(region_id=region_id)
    print(f"Region ID: {region.id}, display name: {region.display_name}")
    print("========================")
    return region


def list_all_regions(*, client: Gcore) -> SyncOffsetPage[Region]:
    print("\n=== LIST ALL REGIONS ===")
    all_regions = client.cloud.regions.list()
    for count, region in enumerate(all_regions, 1):
        print(f"  {count}. Region ID: {region.id}, display name: {region.display_name}")
    print("========================")
    return all_regions


def list_regions_with_filters(*, client: Gcore) -> SyncOffsetPage[Region]:
    print("\n=== LIST REGIONS WITH FILTERS ===")
    filtered_regions = client.cloud.regions.list(product="inference")
    for count, region in enumerate(filtered_regions, 1):
        print(f"  {count}. Region ID: {region.id}, display name: {region.display_name}")
    print("=================================")
    return filtered_regions


if __name__ == "__main__":
    main()
