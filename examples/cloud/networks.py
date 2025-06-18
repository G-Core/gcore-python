from gcore import Gcore


def main() -> None:
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = Gcore()

    network_id = create_network(client=gcore)
    list_networks(client=gcore)
    get_network(client=gcore, network_id=network_id)
    update_network(client=gcore, network_id=network_id)

    # Subnets
    subnet_id = create_subnet(client=gcore, network_id=network_id)
    list_subnets(client=gcore, network_id=network_id)
    get_subnet(client=gcore, subnet_id=subnet_id)
    update_subnet(client=gcore, subnet_id=subnet_id)
    delete_subnet(client=gcore, subnet_id=subnet_id)

    delete_network(client=gcore, network_id=network_id)


def create_network(*, client: Gcore) -> str:
    print("\n=== CREATE NETWORK ===")
    response = client.cloud.networks.create(name="gcore-go-example", create_router=True, type="vxlan")
    task_id = response.tasks[0]
    task = client.cloud.tasks.poll(task_id=task_id)
    if task.created_resources is None or task.created_resources.networks is None:
        raise RuntimeError("Task completed but created_resources or networks is missing")
    network_id: str = task.created_resources.networks[0]
    print(f"Created network: ID={network_id}")
    print("========================")
    return network_id


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
    response = client.cloud.networks.subnets.create(
        network_id=network_id,
        cidr="192.168.1.0/24",
        name="gcore-go-example",
        enable_dhcp=True,
        ip_version=4,
    )
    task_id = response.tasks[0]
    task = client.cloud.tasks.poll(task_id=task_id)
    if task.created_resources is None or task.created_resources.subnets is None:
        raise RuntimeError("Task completed but created_resources or subnets is missing")
    subnet_id: str = task.created_resources.subnets[0]
    print(f"Created subnet: ID={subnet_id}")
    print("========================")
    return subnet_id


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


def delete_subnet(*, client: Gcore, subnet_id: str) -> None:
    print("\n=== DELETE SUBNET ===")
    client.cloud.networks.subnets.delete(subnet_id=subnet_id)
    print(f"Deleted subnet: ID={subnet_id}")
    print("========================")


def delete_network(*, client: Gcore, network_id: str) -> None:
    print("\n=== DELETE NETWORK ===")
    response = client.cloud.networks.delete(network_id=network_id)
    if response.tasks:
        task_id = response.tasks[0]
        client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted network: ID={network_id}")
    print("========================")


if __name__ == "__main__":
    main()
