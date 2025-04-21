import os

from gcore import Gcore
from gcore.pagination import SyncOffsetPage
from gcore.types.cloud import SSHKey, SSHKeyCreated


def get_ssh_key_by_id(ssh_key_id: str) -> SSHKey:
    # No need to pass the API key explicitly — it will automatically be read from the GCORE_API_KEY environment variable if omitted
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    ssh_key = gcore.cloud.ssh_keys.get(ssh_key_id=ssh_key_id)

    print("\n=== GET SSH KEY BY ID ===")
    print(f"SSH Key ID: {ssh_key.id}, Name: {ssh_key.name}, Fingerprint: {ssh_key.fingerprint}")
    print("==========================")
    return ssh_key


def list_all_ssh_keys() -> SyncOffsetPage[SSHKey]:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    all_ssh_keys = gcore.cloud.ssh_keys.list()

    print("\n=== LIST ALL SSH KEYS ===")
    for count, ssh_key in enumerate(all_ssh_keys, 1):
        print(f"  {count}. SSH Key ID: {ssh_key.id}, Name: {ssh_key.name}")
    print("==========================")
    return all_ssh_keys


def create_new_ssh_key() -> SSHKeyCreated:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    # Sample SSH key values
    ssh_key_name = "Example SSH Key"
    new_ssh_key = gcore.cloud.ssh_keys.create(name=ssh_key_name)

    print("\n=== CREATE NEW SSH KEY ===")
    print(f"SSH Key ID: {new_ssh_key.id}, Name: {new_ssh_key.name}")
    print("===========================")
    return new_ssh_key


def update_ssh_key(ssh_key_id: str) -> SSHKey:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    updated_ssh_key = gcore.cloud.ssh_keys.update(ssh_key_id=ssh_key_id, shared_in_project=True)

    print("\n=== UPDATE SSH KEY ===")
    print(f"SSH Key ID: {updated_ssh_key.id}, Updated Name: {updated_ssh_key.name}")
    print("=======================")
    return updated_ssh_key


def delete_ssh_key(ssh_key_id: str) -> None:
    gcore = Gcore(api_key=os.environ.get("GCORE_API_KEY"), base_url=os.environ.get("GCORE_API_URL"))
    gcore.cloud.ssh_keys.delete(ssh_key_id=ssh_key_id)

    print("\n=== DELETE SSH KEY ===")
    print(f"SSH Key ID: {ssh_key_id} has been deleted")
    print("=======================")


if __name__ == "__main__":
    # Follow the order: create, list, get, update, delete
    new_ssh_key = create_new_ssh_key()
    list_all_ssh_keys()
    get_ssh_key_by_id(new_ssh_key.id)
    update_ssh_key(ssh_key_id=new_ssh_key.id)
    delete_ssh_key(ssh_key_id=new_ssh_key.id)
