from gcore import Gcore
from gcore.types.cloud.pricing import GPUCurrency, GPUPriceCatalog, GPUDeploymentType


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    catalog = list_gpu_prices(client=gcore)
    filter_gpu_prices(catalog=catalog, currency="EUR", deployment_type="virtual")


def list_gpu_prices(*, client: Gcore) -> GPUPriceCatalog:
    print("\n=== LIST GPU PRICES ===")
    catalog = client.cloud.pricing.gpu.list()
    print(f"Catalog generated at {catalog.generated_at}, {catalog.count} prices")
    for count, price in enumerate(catalog.results, 1):
        print(
            f"  {count}. {price.gpu_count}x {price.gpu_model} ({price.deployment_type}) in {price.region_name}: "
            f"{price.price_per_hour} {price.currency}/hour, {price.price_per_gpu_hour} {price.currency}/GPU/hour, "
            f"SKU {price.pricing_detail.sku}"
        )
    print("=======================")
    return catalog


def filter_gpu_prices(*, catalog: GPUPriceCatalog, currency: GPUCurrency, deployment_type: GPUDeploymentType) -> None:
    print(f"\n=== {deployment_type} GPU PRICES IN {currency} ===")
    # the API has no filters, so filter the catalog on the client
    prices = [p for p in catalog.results if p.currency == currency and p.deployment_type == deployment_type]
    for count, price in enumerate(prices, 1):
        # prices are decimal strings; use Decimal, not float, to compare or sum them
        print(
            f"  {count}. {price.gpu_count}x {price.gpu_model} in {price.region_name}: {price.price_per_hour}/hour, "
            f"flavors {', '.join(price.pricing_detail.flavor_names)}"
        )
    print("=======================")


if __name__ == "__main__":
    main()
