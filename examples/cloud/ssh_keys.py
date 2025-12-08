from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import SSHKey, SSHKeyCreate


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

    ssh_key = create_ssh_key(client=gcore)
    list_ssh_keys(client=gcore)
    get_ssh_key(client=gcore, ssh_key_id=ssh_key.id)
    update_ssh_key(client=gcore, ssh_key_id=ssh_key.id)
    delete_ssh_key(client=gcore, ssh_key_id=ssh_key.id)


def create_ssh_key(*, client: Gcore) -> SSHKeyCreate:
    print("\n=== CREATE SSH KEY ===")
    ssh_key = client.cloud.ssh_keys.create(name="gcore-go-example")
    print(f"Created SSH key: ID={ssh_key.id}, name={ssh_key.name}")
    print("========================")
    return ssh_key


def list_ssh_keys(*, client: Gcore) -> SyncOffsetPage[SSHKey]:
    print("\n=== LIST SSH KEYS ===")
    ssh_keys = client.cloud.ssh_keys.list()
    for count, ssh_key in enumerate(ssh_keys, 1):
        print(f"  {count}. SSH key: ID={ssh_key.id}, name={ssh_key.name}")
    print("========================")
    return ssh_keys


def get_ssh_key(*, client: Gcore, ssh_key_id: str) -> SSHKey:
    print("\n=== GET SSH KEY ===")
    ssh_key = client.cloud.ssh_keys.get(ssh_key_id=ssh_key_id)
    print(f"SSH key: ID={ssh_key.id}, name={ssh_key.name}, fingerprint={ssh_key.fingerprint}")
    print("========================")
    return ssh_key


def update_ssh_key(*, client: Gcore, ssh_key_id: str) -> SSHKey:
    print("\n=== UPDATE SSH KEY ===")
    updated_ssh_key = client.cloud.ssh_keys.update(ssh_key_id=ssh_key_id, shared_in_project=True)
    print(f"Updated SSH key: ID={updated_ssh_key.id}, name={updated_ssh_key.name}")
    print("========================")
    return updated_ssh_key


def delete_ssh_key(*, client: Gcore, ssh_key_id: str) -> None:
    print("\n=== DELETE SSH KEY ===")
    client.cloud.ssh_keys.delete(ssh_key_id=ssh_key_id)
    print(f"Deleted SSH key: ID={ssh_key_id}")
    print("========================")


if __name__ == "__main__":
    main()
