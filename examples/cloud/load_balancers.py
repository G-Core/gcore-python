from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    lb_id = create_load_balancer(client=gcore)
    list_load_balancers(client=gcore)
    get_load_balancer(client=gcore, load_balancer_id=lb_id)
    update_load_balancer(client=gcore, load_balancer_id=lb_id)
    resize_load_balancer(client=gcore, load_balancer_id=lb_id)
    failover_load_balancer(client=gcore, load_balancer_id=lb_id)

    # Statuses
    list_load_balancer_statuses(client=gcore)
    get_load_balancer_status(client=gcore, load_balancer_id=lb_id)

    # Metrics
    get_load_balancer_metrics(client=gcore, load_balancer_id=lb_id)

    delete_load_balancer(client=gcore, load_balancer_id=lb_id)


def create_load_balancer(*, client: Gcore) -> str:
    print("\n=== CREATE LOAD BALANCER ===")
    lb = client.cloud.load_balancers.create_and_poll(flavor="lb1-1-2", name="gcore-go-example")
    print(f"Created load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}")
    print("========================")
    return lb.id


def list_load_balancers(*, client: Gcore) -> None:
    print("\n=== LIST LOAD BALANCERS ===")
    load_balancers = client.cloud.load_balancers.list()
    for count, lb in enumerate(load_balancers, 1):
        print(f"{count}. Load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}")
    print("========================")


def get_load_balancer(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER ===")
    lb = client.cloud.load_balancers.get(load_balancer_id=load_balancer_id)
    flavor_name = lb.flavor.flavor_name if lb.flavor else "Unknown"
    print(f"Load balancer: ID={lb.id}, name={lb.name}, status={lb.provisioning_status}, flavor={flavor_name}")
    print("========================")


def update_load_balancer(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== UPDATE LOAD BALANCER ===")
    lb = client.cloud.load_balancers.update(load_balancer_id=load_balancer_id, name="gcore-go-example-updated")
    print(f"Updated load balancer: ID={lb.id}, name={lb.name}")
    print("========================")


def resize_load_balancer(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== RESIZE LOAD BALANCER ===")
    lb = client.cloud.load_balancers.resize_and_poll(load_balancer_id=load_balancer_id, flavor="lb1-2-4")
    print(f"Resized load balancer: ID={lb.id}, flavor=lb1-2-4")
    print("========================")


def failover_load_balancer(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== FAILOVER LOAD BALANCER ===")
    lb = client.cloud.load_balancers.failover_and_poll(load_balancer_id=load_balancer_id)
    print(f"Failed over load balancer: ID={lb.id}")
    print("========================")


def list_load_balancer_statuses(*, client: Gcore) -> None:
    print("\n=== LIST LOAD BALANCER STATUSES ===")
    statuses = client.cloud.load_balancers.statuses.list()
    for count, status in enumerate(statuses.results, 1):
        print(
            f"{count}. Load balancer status: ID={status.id}, operating status={status.operating_status}, provisioning status={status.provisioning_status}"
        )
    print("========================")


def get_load_balancer_status(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER STATUS ===")
    status = client.cloud.load_balancers.statuses.get(load_balancer_id=load_balancer_id)
    print(
        f"Load balancer status: ID={status.id}, operating status={status.operating_status}, provisioning status={status.provisioning_status}"
    )
    print("========================")


def get_load_balancer_metrics(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== GET LOAD BALANCER METRICS ===")
    metrics = client.cloud.load_balancers.metrics.list(
        load_balancer_id=load_balancer_id,
        time_interval=1,
        time_unit="hour",
    )
    print(f"Load balancer metrics: ID={load_balancer_id}")
    if metrics.results:
        metric = metrics.results[0]
        print(f"CPU: {metric.cpu_util}%, memory: {metric.memory_util}%, time: {metric.time}")
    print("========================")


def delete_load_balancer(*, client: Gcore, load_balancer_id: str) -> None:
    print("\n=== DELETE LOAD BALANCER ===")
    client.cloud.load_balancers.delete_and_poll(load_balancer_id=load_balancer_id)
    print(f"Deleted load balancer: ID={load_balancer_id}")
    print("========================")


if __name__ == "__main__":
    main()
