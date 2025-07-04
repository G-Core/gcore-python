from gcore import Gcore
from gcore.types.cloud.security_group_create_params import SecurityGroup


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

    security_group_id = create_security_group(client=gcore)
    list_security_groups(client=gcore)
    get_security_group(client=gcore, security_group_id=security_group_id)
    update_security_group(client=gcore, security_group_id=security_group_id)

    # Rules
    rule_id = create_security_group_rule(client=gcore, security_group_id=security_group_id)
    rule_id = replace_security_group_rule(client=gcore, rule_id=rule_id, security_group_id=security_group_id)
    delete_security_group_rule(client=gcore, rule_id=rule_id)

    delete_security_group(client=gcore, security_group_id=security_group_id)


def create_security_group(*, client: Gcore) -> str:
    print("\n=== CREATE SECURITY GROUP ===")
    security_group = client.cloud.security_groups.create(security_group=SecurityGroup(name="gcore-go-example"))
    print(f"Created security group: ID={security_group.id}, name={security_group.name}")
    print("========================")
    return security_group.id


def list_security_groups(*, client: Gcore) -> None:
    print("\n=== LIST SECURITY GROUPS ===")
    security_groups = client.cloud.security_groups.list()
    for count, security_group in enumerate(security_groups, 1):
        print(f"{count}. Security group: ID={security_group.id}, name={security_group.name}")
    print("========================")


def get_security_group(*, client: Gcore, security_group_id: str) -> None:
    print("\n=== GET SECURITY GROUP ===")
    security_group = client.cloud.security_groups.get(group_id=security_group_id)
    print(
        f"Security group: ID={security_group.id}, name={security_group.name}, description={security_group.description}"
    )
    print("========================")


def update_security_group(*, client: Gcore, security_group_id: str) -> None:
    print("\n=== UPDATE SECURITY GROUP ===")
    security_group = client.cloud.security_groups.update(
        group_id=security_group_id,
        name="gcore-go-example-updated",
    )
    print(f"Updated security group: ID={security_group.id}, name={security_group.name}")
    print("========================")


def delete_security_group(*, client: Gcore, security_group_id: str) -> None:
    print("\n=== DELETE SECURITY GROUP ===")
    client.cloud.security_groups.delete(group_id=security_group_id)
    print(f"Deleted security group: ID={security_group_id}")
    print("========================")


def create_security_group_rule(*, client: Gcore, security_group_id: str) -> str:
    print("\n=== CREATE SECURITY GROUP RULE ===")
    rule = client.cloud.security_groups.rules.create(
        group_id=security_group_id,
        direction="ingress",
        protocol="tcp",
        ethertype="IPv4",
        port_range_min=80,
        port_range_max=80,
        remote_ip_prefix="0.0.0.0/0",
        description="Allow HTTP traffic",
    )
    print(f"Created security group rule: ID={rule.id}, protocol={rule.protocol}, port={rule.port_range_min}")
    print("========================")
    return rule.id


def replace_security_group_rule(*, client: Gcore, rule_id: str, security_group_id: str) -> str:
    print("\n=== REPLACE SECURITY GROUP RULE ===")
    rule = client.cloud.security_groups.rules.replace(
        rule_id=rule_id,
        direction="ingress",
        security_group_id=security_group_id,
        protocol="tcp",
        ethertype="IPv4",
        port_range_min=443,
        port_range_max=443,
        remote_ip_prefix="0.0.0.0/0",
        description="Allow HTTPS traffic",
    )
    print(f"Replaced security group rule: ID={rule.id}, protocol={rule.protocol}, port={rule.port_range_min}")
    print("========================")
    return rule.id


def delete_security_group_rule(*, client: Gcore, rule_id: str) -> None:
    print("\n=== DELETE SECURITY GROUP RULE ===")
    client.cloud.security_groups.rules.delete(rule_id=rule_id)
    print(f"Deleted security group rule: ID={rule_id}")
    print("========================")


if __name__ == "__main__":
    main()
