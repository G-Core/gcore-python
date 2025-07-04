import asyncio

from gcore import AsyncGcore
from gcore.types.cloud.security_group_create_params import SecurityGroup


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    security_group_id = await create_security_group(client=gcore)
    await list_security_groups(client=gcore)
    await get_security_group(client=gcore, security_group_id=security_group_id)
    await update_security_group(client=gcore, security_group_id=security_group_id)

    # Rules
    rule_id = await create_security_group_rule(client=gcore, security_group_id=security_group_id)
    rule_id = await replace_security_group_rule(client=gcore, rule_id=rule_id, security_group_id=security_group_id)
    await delete_security_group_rule(client=gcore, rule_id=rule_id)

    await delete_security_group(client=gcore, security_group_id=security_group_id)


async def create_security_group(client: AsyncGcore) -> str:
    print("\n=== CREATE SECURITY GROUP ===")
    security_group = await client.cloud.security_groups.create(security_group=SecurityGroup(name="gcore-go-example"))
    print(f"Created security group: ID={security_group.id}, name={security_group.name}")
    print("========================")
    return security_group.id


async def list_security_groups(*, client: AsyncGcore) -> None:
    print("\n=== LIST SECURITY GROUPS ===")
    security_groups = await client.cloud.security_groups.list()
    count = 0
    async for security_group in security_groups:
        count += 1
        print(f"{count}. Security group: ID={security_group.id}, name={security_group.name}")
    print("========================")


async def get_security_group(*, client: AsyncGcore, security_group_id: str) -> None:
    print("\n=== GET SECURITY GROUP ===")
    security_group = await client.cloud.security_groups.get(group_id=security_group_id)
    print(
        f"Security group: ID={security_group.id}, name={security_group.name}, description={security_group.description}"
    )
    print("========================")


async def update_security_group(*, client: AsyncGcore, security_group_id: str) -> None:
    print("\n=== UPDATE SECURITY GROUP ===")
    security_group = await client.cloud.security_groups.update(
        group_id=security_group_id,
        name="gcore-go-example-updated",
    )
    print(f"Updated security group: ID={security_group.id}, name={security_group.name}")
    print("========================")


async def delete_security_group(*, client: AsyncGcore, security_group_id: str) -> None:
    print("\n=== DELETE SECURITY GROUP ===")
    await client.cloud.security_groups.delete(group_id=security_group_id)
    print(f"Deleted security group: ID={security_group_id}")
    print("========================")


async def create_security_group_rule(*, client: AsyncGcore, security_group_id: str) -> str:
    print("\n=== CREATE SECURITY GROUP RULE ===")
    rule = await client.cloud.security_groups.rules.create(
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


async def replace_security_group_rule(*, client: AsyncGcore, rule_id: str, security_group_id: str) -> str:
    print("\n=== REPLACE SECURITY GROUP RULE ===")
    rule = await client.cloud.security_groups.rules.replace(
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


async def delete_security_group_rule(*, client: AsyncGcore, rule_id: str) -> None:
    print("\n=== DELETE SECURITY GROUP RULE ===")
    await client.cloud.security_groups.rules.delete(rule_id=rule_id)
    print(f"Deleted security group rule: ID={rule_id}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
