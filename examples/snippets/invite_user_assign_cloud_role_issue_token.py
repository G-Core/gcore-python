import os
from datetime import datetime, timezone, timedelta

from gcore import Gcore
from gcore.types.iam.user_invite_params import UserRole
from gcore.types.iam.api_token_create_params import ClientUser


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set client ID before running
    client_id = int(os.environ["GCORE_CLIENT_ID"])
    # TODO set client ID before running
    cloud_project_id = int(os.environ["GCORE_CLOUD_PROJECT_ID"])

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    user_email = "john.doe@example.com"
    user_name = "John Doe"
    user_role = UserRole(id=5, name="Engineers")

    # Step 1: Invite user via IAM
    invited_user = gcore.iam.users.invite(
        client_id=client_id,
        email=user_email,
        name=user_name,
        user_role=user_role,
        lang="en",
    )

    # Step 2: Create role in cloud for the invited user
    if not invited_user.user_id:
        raise RuntimeError("User invitation succeeded, but no user_id was returned")

    gcore.cloud.users.role_assignments.create(
        user_id=invited_user.user_id,
        role="ProjectAdministrator",
        project_id=cloud_project_id,
        client_id=client_id,
    )

    # Step 3: Create API token for the invited user (expires in 1 month)
    expires_in_days = 30
    exp_date = (datetime.now(timezone.utc) + timedelta(days=expires_in_days)).isoformat()
    gcore.iam.api_tokens.create(
        client_id=client_id,
        client_user=ClientUser(role=user_role),
        exp_date=exp_date,
        name=f"Token for {user_email}",
        description=f"API token for invited user {user_name}",
    )


if __name__ == "__main__":
    main()
