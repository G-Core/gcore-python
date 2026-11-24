import os
import time

from gcore import Gcore


def main() -> None:
    # set GCORE_CLOUD_PROJECT_ID, GCORE_CLOUD_REGION_ID, and GCORE_INSTANCE_ID
    region_id = int(os.environ["GCORE_CLOUD_REGION_ID"])
    instance_id = os.environ["GCORE_INSTANCE_ID"]
    with Gcore() as client:
        instance = client.cloud.instances.get(instance_id)
        if instance.region_id != region_id or instance.status != "active" or instance.placement_group_id is not None:
            raise ValueError("Choose an active test VM in that region with no placement group")

        groups = client.cloud.placement_groups
        name = f"sdk-placement-{time.time_ns()}"
        group = groups.create_and_poll(name=name, policy="anti-affinity", region_id=region_id)
        try:
            for match in groups.list(region_ids=[region_id], name={"exact": [name]}):
                print(f"Found group {match.id}")
            details = groups.get(group.id)
            print(f"Group {details.name} uses policy {details.policy}")

            client.cloud.instances.update_and_poll(instance_id, placement_group_id=group.id)
            print(f"Member IDs: {groups.get(group.id).member_ids}")
            client.cloud.instances.update_and_poll(instance_id, placement_group_id=None)
        finally:
            groups.delete_and_poll(group.id)
            print(f"Deleted group {group.id}")


if __name__ == "__main__":
    main()
