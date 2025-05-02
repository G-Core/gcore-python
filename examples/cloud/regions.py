import os

from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import Region


def get_region_by_id() -> Region:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"))
    # Region ID can also be omitted — it defaults to the GCORE_CLOUD_REGION_ID environment variable
    region = gcore.cloud.regions.get(region_id=int(os.environ.get("GCORE_CLOUD_REGION_ID", "76")))

    print("\n=== GET REGION BY ID ===")
    print(f"Region ID: {region.id}, Display Name: {region.display_name}")
    print("========================")
    return region


def list_all_regions() -> SyncOffsetPage[Region]:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"))
    all_regions = gcore.cloud.regions.list()

    print("\n=== LIST ALL REGIONS ===")
    for count, region in enumerate(all_regions, 1):
        print(f"  {count}. Region ID: {region.id}, Display Name: {region.display_name}")
    print("========================")
    return all_regions


def list_regions_with_filters() -> SyncOffsetPage[Region]:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"))
    filtered_regions = gcore.cloud.regions.list(product="containers")

    print("\n=== LIST REGIONS WITH FILTERS ===")
    for count, region in enumerate(filtered_regions, 1):
        print(f"  {count}. Region ID: {region.id}, Display Name: {region.display_name}")
    print("=================================")
    return filtered_regions


if __name__ == "__main__":
    get_region_by_id()
    list_all_regions()
    list_regions_with_filters()
