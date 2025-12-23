from datetime import datetime, timezone, timedelta

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

    # Example: list the last 10 user actions of type 'create' in the 'instance' api_group from the last 7 days
    from_time = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    logs = gcore.cloud.audit_logs.list(
        # action_type=["create"],
        # api_group=["instance"],
        from_timestamp=from_time,
        limit=10,
        order_by="desc",
    )
    print("\n=== AUDIT LOGS ===")
    for count, log in enumerate(logs, 1):
        print(
            f"{count}. ID={log.id}, time={log.timestamp}, action={log.action_type}, api_group={log.api_group}, user_id={log.user_id}, email={log.email}"
        )
    print("==================")


if __name__ == "__main__":
    main()
