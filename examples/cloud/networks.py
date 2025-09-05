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

    network_id = create_network(client=gcore)
    list_networks(client=gcore)
    get_network(client=gcore, network_id=network_id)
    update_network(client=gcore, network_id=network_id)

    # Subnets
    subnet_id = create_subnet(client=gcore, network_id=network_id)
    list_subnets(client=gcore, network_id=network_id)
    get_subnet(client=gcore, subnet_id=subnet_id)
    update_subnet(client=gcore, subnet_id=subnet_id)

    # Routers
    router_id = create_router(client=gcore)
    list_routers(client=gcore)
    get_router(client=gcore, router_id=router_id)
    update_router(client=gcore, router_id=router_id)
    attach_subnet_to_router(client=gcore, router_id=router_id, subnet_id=subnet_id)
    detach_subnet_from_router(client=gcore, router_id=router_id, subnet_id=subnet_id)

    delete_router(client=gcore, router_id=router_id)
    delete_subnet(client=gcore, subnet_id=subnet_id)
    delete_network(client=gcore, network_id=network_id)


def create_network(*, client: Gcore) -> str:
    print("\n=== CREATE NETWORK ===")
    network = client.cloud.networks.create_and_poll(name="gcore-go-example", create_router=True, type="vxlan")
    print(f"Created network: ID={network.id}, name={network.name}, type={network.type}")
    print("========================")
    return network.id


def list_networks(*, client: Gcore) -> None:
    print("\n=== LIST NETWORKS ===")
    networks = client.cloud.networks.list()
    for count, network in enumerate(networks, 1):
        print(f"{count}. Network: ID={network.id}, name={network.name}, type={network.type}")
    print("========================")


def get_network(*, client: Gcore, network_id: str) -> None:
    print("\n=== GET NETWORK ===")
    network = client.cloud.networks.get(network_id=network_id)
    print(f"Network: ID={network.id}, name={network.name}, type={network.type}")
    print("========================")


def update_network(*, client: Gcore, network_id: str) -> None:
    print("\n=== UPDATE NETWORK ===")
    network = client.cloud.networks.update(network_id=network_id, name="gcore-go-example-updated")
    print(f"Updated network: ID={network.id}, name={network.name}")
    print("========================")


def create_subnet(*, client: Gcore, network_id: str) -> str:
    print("\n=== CREATE SUBNET ===")
    subnet = client.cloud.networks.subnets.create_and_poll(
        network_id=network_id,
        cidr="192.168.1.0/24",
        name="gcore-go-example",
        enable_dhcp=True,
        ip_version=4,
    )
    print(f"Created subnet: ID={subnet.id}, CIDR={subnet.cidr}, name={subnet.name}")
    print("========================")
    return subnet.id or ""


def list_subnets(*, client: Gcore, network_id: str) -> None:
    print("\n=== LIST SUBNETS ===")
    subnets = client.cloud.networks.subnets.list(network_id=network_id)
    for count, subnet in enumerate(subnets, 1):
        print(f"{count}. Subnet: ID={subnet.id}, CIDR={subnet.cidr}, name={subnet.name}")
    print("========================")


def get_subnet(*, client: Gcore, subnet_id: str) -> None:
    print("\n=== GET SUBNET ===")
    subnet = client.cloud.networks.subnets.get(subnet_id=subnet_id)
    print(f"Subnet: ID={subnet.id}, CIDR={subnet.cidr}, name={subnet.name}")
    print("========================")


def update_subnet(*, client: Gcore, subnet_id: str) -> None:
    print("\n=== UPDATE SUBNET ===")
    subnet = client.cloud.networks.subnets.update(subnet_id=subnet_id, name="gcore-go-example-updated")
    print(f"Updated subnet: ID={subnet.id}, name={subnet.name}")
    print("========================")


def create_router(*, client: Gcore) -> str:
    print("\n=== CREATE ROUTER ===")
    response = client.cloud.networks.routers.create(name="gcore-go-example")
    task_id = response.tasks[0]
    task = client.cloud.tasks.poll(task_id=task_id)
    if task.created_resources is None or task.created_resources.routers is None:
        raise RuntimeError("Task completed but created_resources or routers is missing")
    router_id: str = task.created_resources.routers[0]
    print(f"Created router: ID={router_id}")
    print("========================")
    return router_id


def list_routers(*, client: Gcore) -> None:
    print("\n=== LIST ROUTERS ===")
    routers = client.cloud.networks.routers.list()
    for count, router in enumerate(routers, 1):
        print(f"{count}. Router: ID={router.id}, name={router.name}, status={router.status}")
    print("========================")


def get_router(*, client: Gcore, router_id: str) -> None:
    print("\n=== GET ROUTER ===")
    router = client.cloud.networks.routers.get(router_id=router_id)
    print(f"Router: ID={router.id}, name={router.name}, status={router.status}")
    print("========================")


def update_router(*, client: Gcore, router_id: str) -> None:
    print("\n=== UPDATE ROUTER ===")
    router = client.cloud.networks.routers.update(router_id=router_id, name="gcore-go-example-updated")
    print(f"Updated router: ID={router.id}, name={router.name}")
    print("========================")


def attach_subnet_to_router(*, client: Gcore, router_id: str, subnet_id: str) -> None:
    print("\n=== ATTACH SUBNET TO ROUTER ===")
    router = client.cloud.networks.routers.attach_subnet(router_id=router_id, subnet_id=subnet_id)
    print(f"Attached subnet {subnet_id} to router: ID={router.id}")
    print("========================")


def detach_subnet_from_router(*, client: Gcore, router_id: str, subnet_id: str) -> None:
    print("\n=== DETACH SUBNET FROM ROUTER ===")
    router = client.cloud.networks.routers.detach_subnet(router_id=router_id, subnet_id=subnet_id)
    print(f"Detached subnet {subnet_id} from router: ID={router.id}")
    print("========================")


def delete_router(*, client: Gcore, router_id: str) -> None:
    print("\n=== DELETE ROUTER ===")
    response = client.cloud.networks.routers.delete(router_id=router_id)
    task_id = response.tasks[0]
    client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted router: ID={router_id}")
    print("========================")


def delete_subnet(*, client: Gcore, subnet_id: str) -> None:
    print("\n=== DELETE SUBNET ===")
    client.cloud.networks.subnets.delete(subnet_id=subnet_id)
    print(f"Deleted subnet: ID={subnet_id}")
    print("========================")


def delete_network(*, client: Gcore, network_id: str) -> None:
    print("\n=== DELETE NETWORK ===")
    client.cloud.networks.delete_and_poll(network_id=network_id)
    print(f"Deleted network: ID={network_id}")
    print("========================")


if __name__ == "__main__":
    main()
