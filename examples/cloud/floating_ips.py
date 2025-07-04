from __future__ import annotations

import os

from gcore import Gcore


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    # TODO set cloud port ID before running
    cloud_port_id = os.environ["GCORE_CLOUD_PORT_ID"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    floating_ip_id = create_floating_ip(client=gcore)
    list_floating_ips(client=gcore)
    get_floating_ip(client=gcore, floating_ip_id=floating_ip_id)
    assign_floating_ip(client=gcore, floating_ip_id=floating_ip_id, port_id=cloud_port_id)
    unassign_floating_ip(client=gcore, floating_ip_id=floating_ip_id)
    delete_floating_ip(client=gcore, floating_ip_id=floating_ip_id)


def create_floating_ip(*, client: Gcore) -> str:
    print("\n=== CREATE FLOATING IP ===")
    response = client.cloud.floating_ips.create(tags={"name": "gcore-go-example"})
    task = client.cloud.tasks.poll(task_id=response.tasks[0])
    if task.created_resources is None or task.created_resources.floatingips is None:
        raise RuntimeError("Task completed but created_resources or floatingips is missing")
    floating_ip_id: str = task.created_resources.floatingips[0]
    print(f"Created Floating IP: ID={floating_ip_id}")
    print("========================")
    return floating_ip_id


def list_floating_ips(*, client: Gcore) -> None:
    print("\n=== LIST FLOATING IPS ===")
    floating_ips = client.cloud.floating_ips.list()
    for count, ip in enumerate(floating_ips, 1):
        print(f"{count}. Floating IP: ID={ip.id}, status={ip.status}, floating IP address={ip.floating_ip_address}")
    if not floating_ips:
        print("No floating IPs found.")
    print("========================")


def get_floating_ip(*, client: Gcore, floating_ip_id: str) -> None:
    print("\n=== GET FLOATING IP ===")
    floating_ip = client.cloud.floating_ips.get(floating_ip_id=floating_ip_id)
    print(
        f"Floating IP: ID={floating_ip.id}, status={floating_ip.status}, floating IP address={floating_ip.floating_ip_address}"
    )
    print("========================")


def assign_floating_ip(*, client: Gcore, floating_ip_id: str, port_id: str) -> None:
    print("\n=== ASSIGN FLOATING IP ===")
    floating_ip = client.cloud.floating_ips.assign(
        floating_ip_id=floating_ip_id,
        port_id=port_id,
    )
    print(f"Assigned floating IP: ID={floating_ip.id}, port ID={floating_ip.port_id}")
    print("========================")


def unassign_floating_ip(*, client: Gcore, floating_ip_id: str) -> None:
    print("\n=== UNASSIGN FLOATING IP ===")
    floating_ip = client.cloud.floating_ips.unassign(floating_ip_id=floating_ip_id)
    print(f"Unassigned floating IP: ID={floating_ip.id}")
    print("========================")


def delete_floating_ip(*, client: Gcore, floating_ip_id: str) -> None:
    print("\n=== DELETE FLOATING IP ===")
    response = client.cloud.floating_ips.delete(floating_ip_id=floating_ip_id)
    task_id = response.tasks[0]
    client.cloud.tasks.poll(task_id=task_id)
    print(f"Deleted floating IP: ID={floating_ip_id}")
    print("========================")


if __name__ == "__main__":
    main()
