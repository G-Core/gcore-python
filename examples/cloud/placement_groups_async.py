import os
import time
import asyncio

from gcore import AsyncGcore


async def main() -> None:
    # set GCORE_CLOUD_PROJECT_ID, GCORE_CLOUD_REGION_ID, and GCORE_INSTANCE_ID
    region_id = int(os.environ["GCORE_CLOUD_REGION_ID"])
    instance_id = os.environ["GCORE_INSTANCE_ID"]
    async with AsyncGcore() as client:
        instance = await client.cloud.instances.get(instance_id)
        if instance.region_id != region_id or instance.status != "active" or instance.placement_group_id is not None:
            raise ValueError("Choose an active test VM in that region with no placement group")

        groups = client.cloud.placement_groups
        name = f"sdk-placement-{time.time_ns()}"
        group = await groups.create_and_poll(name=name, policy="anti-affinity", region_id=region_id)
        try:
            async for match in groups.list(region_ids=[region_id], name={"exact": [name]}):
                print(f"Found group {match.id}")
            details = await groups.get(group.id)
            print(f"Group {details.name} uses policy {details.policy}")

            await client.cloud.instances.update_and_poll(instance_id, placement_group_id=group.id)
            print(f"Member IDs: {(await groups.get(group.id)).member_ids}")
            await client.cloud.instances.update_and_poll(instance_id, placement_group_id=None)
        finally:
            await groups.delete_and_poll(group.id)
            print(f"Deleted group {group.id}")


if __name__ == "__main__":
    asyncio.run(main())
