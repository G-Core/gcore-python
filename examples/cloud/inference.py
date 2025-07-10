import os

from gcore import Gcore
from gcore.types.cloud.inference.deployment_create_params import (
    Container,
    ContainerScale,
    ContainerScaleTriggers,
    ContainerScaleTriggersCPU,
)


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]
    # TODO set flavor name before running
    cloud_inference_flavor_name = os.environ["GCORE_CLOUD_INFERENCE_FLAVOR_NAME"]
    # TODO set model ID before running
    cloud_inference_model_id = os.environ["GCORE_CLOUD_INFERENCE_MODEL_ID"]

    gcore = Gcore(
        timeout=180.0,
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
    )

    # Capacity
    get_capacity_by_region(client=gcore)

    # Flavors
    list_flavors(client=gcore)
    get_flavor(client=gcore, flavor_name=cloud_inference_flavor_name)

    # Models
    list_models(client=gcore)
    get_model(client=gcore, model_id=cloud_inference_model_id)

    # Registry Credentials
    credential_name = create_registry_credential(client=gcore)
    list_registry_credentials(client=gcore)
    get_registry_credential(client=gcore, credential_name=credential_name)
    replace_registry_credential(client=gcore, credential_name=credential_name)
    delete_registry_credential(client=gcore, credential_name=credential_name)

    # Secrets
    secret_name = create_secret(client=gcore)
    list_secrets(client=gcore)
    get_secret(client=gcore, secret_name=secret_name)
    replace_secret(client=gcore, secret_name=secret_name)
    delete_secret(client=gcore, secret_name=secret_name)

    # Deployments
    deployment_name = create_deployment(
        client=gcore, flavor_name=cloud_inference_flavor_name, region_id=int(cloud_region_id)
    )
    list_deployments(client=gcore)
    get_deployment(client=gcore, deployment_name=deployment_name)
    update_deployment(client=gcore, deployment_name=deployment_name)
    stop_deployment(client=gcore, deployment_name=deployment_name)
    start_deployment(client=gcore, deployment_name=deployment_name)
    delete_deployment(client=gcore, deployment_name=deployment_name)


def get_capacity_by_region(*, client: Gcore) -> None:
    print("\n=== GET CAPACITY BY REGION ===")
    capacities = client.cloud.inference.get_capacity_by_region()

    # Display first few regions
    display_count = min(3, len(capacities.results))

    for i in range(display_count):
        region_capacity = capacities.results[i]
        print(f"{i + 1}. Region ID: {region_capacity.region_id}, available flavors: {len(region_capacity.capacity)}")

        # Display first few flavors per region
        flavor_display_count = min(3, len(region_capacity.capacity))

        for j in range(flavor_display_count):
            flavor = region_capacity.capacity[j]
            print(f"   - {flavor.flavor_name}: {flavor.capacity} capacity")

        if len(region_capacity.capacity) > flavor_display_count:
            print(f"   ... and {len(region_capacity.capacity) - flavor_display_count} more flavors")

    if len(capacities.results) > display_count:
        print(f"... and {len(capacities.results) - display_count} more regions")

    print("========================")


def list_flavors(*, client: Gcore) -> None:
    print("\n=== LIST FLAVORS ===")
    flavors = client.cloud.inference.flavors.list()

    # Convert to list to get all flavors
    flavor_list = list(flavors)

    # Display first few flavors
    display_count = min(3, len(flavor_list))

    for i in range(display_count):
        flavor = flavor_list[i]
        print(f"{i + 1}. Flavor: {flavor.name}, CPU: {flavor.cpu}, Memory: {flavor.memory} Gi")

    if len(flavor_list) > display_count:
        print(f"... and {len(flavor_list) - display_count} more flavors")

    print("========================")


def get_flavor(*, client: Gcore, flavor_name: str) -> None:
    print("\n=== GET FLAVOR ===")
    flavor = client.cloud.inference.flavors.get(flavor_name=flavor_name)
    print(f"Flavor: {flavor.name}, CPU: {flavor.cpu}, Memory: {flavor.memory} Gi")
    print("========================")


def list_models(*, client: Gcore) -> None:
    print("\n=== LIST MODELS ===")
    models = client.cloud.inference.models.list()

    # Convert to list to get all models
    model_list = list(models)

    # Display first few models
    display_count = min(3, len(model_list))

    for i in range(display_count):
        model = model_list[i]
        print(f"{i + 1}. Model: {model.name}, ID: {model.id}")

    if len(model_list) > display_count:
        print(f"... and {len(model_list) - display_count} more models")

    print("========================")


def get_model(*, client: Gcore, model_id: str) -> None:
    print("\n=== GET MODEL ===")
    model = client.cloud.inference.models.get(model_id=model_id)
    print(f"Model: {model.name}, ID: {model.id}")
    print("========================")


def create_registry_credential(*, client: Gcore) -> str:
    print("\n=== CREATE REGISTRY CREDENTIAL ===")
    credential = client.cloud.inference.registry_credentials.create(
        name="gcore-go-example",
        username="example-user",
        password="example-password",
        registry_url="https://registry.example.com",
    )
    print(f"Created registry credential: {credential.name}")
    print("========================")
    return credential.name


def list_registry_credentials(*, client: Gcore) -> None:
    print("\n=== LIST REGISTRY CREDENTIALS ===")
    credentials = client.cloud.inference.registry_credentials.list()
    for count, credential in enumerate(credentials, 1):
        print(f"{count}. Registry credential: {credential.name}, URL: {credential.registry_url}")
    print("========================")


def get_registry_credential(*, client: Gcore, credential_name: str) -> None:
    print("\n=== GET REGISTRY CREDENTIAL ===")
    credential = client.cloud.inference.registry_credentials.get(credential_name=credential_name)
    print(f"Registry credential: {credential.name}, URL: {credential.registry_url}")
    print("========================")


def replace_registry_credential(*, client: Gcore, credential_name: str) -> None:
    print("\n=== REPLACE REGISTRY CREDENTIAL ===")
    client.cloud.inference.registry_credentials.replace(
        credential_name=credential_name,
        username="updated-user",
        password="updated-password",
        registry_url="https://updated-registry.example.com",
    )
    print(f"Replaced registry credential: {credential_name}")
    print("========================")


def delete_registry_credential(*, client: Gcore, credential_name: str) -> None:
    print("\n=== DELETE REGISTRY CREDENTIAL ===")
    client.cloud.inference.registry_credentials.delete(credential_name=credential_name)
    print(f"Deleted registry credential: {credential_name}")
    print("========================")


def create_secret(*, client: Gcore) -> str:
    print("\n=== CREATE SECRET ===")
    secret = client.cloud.inference.secrets.create(
        name="gcore-go-example",
        type="aws-iam",
        data={"aws_access_key_id": "example-key", "aws_secret_access_key": "example-secret"},
    )
    print(f"Created secret: {secret.name}")
    print("========================")
    return secret.name


def list_secrets(*, client: Gcore) -> None:
    print("\n=== LIST SECRETS ===")
    secrets = client.cloud.inference.secrets.list()
    for count, secret in enumerate(secrets, 1):
        print(f"{count}. Secret: {secret.name}, type: {secret.type}")
    print("========================")


def get_secret(*, client: Gcore, secret_name: str) -> None:
    print("\n=== GET SECRET ===")
    secret = client.cloud.inference.secrets.get(secret_name=secret_name)
    print(f"Secret: {secret.name}, type: {secret.type}")
    print("========================")


def replace_secret(*, client: Gcore, secret_name: str) -> None:
    print("\n=== REPLACE SECRET ===")
    secret = client.cloud.inference.secrets.replace(
        secret_name=secret_name,
        type="aws-iam",
        data={"aws_access_key_id": "updated-key", "aws_secret_access_key": "updated-secret"},
    )
    print(f"Replaced secret: {secret.name}")
    print("========================")


def delete_secret(*, client: Gcore, secret_name: str) -> None:
    print("\n=== DELETE SECRET ===")
    client.cloud.inference.secrets.delete(secret_name=secret_name)
    print(f"Deleted secret: {secret_name}")
    print("========================")


def create_deployment(*, client: Gcore, flavor_name: str, region_id: int) -> str:
    print("\n=== CREATE DEPLOYMENT ===")

    container = Container(
        region_id=region_id,
        scale=ContainerScale(
            min=1,
            max=3,
            triggers=ContainerScaleTriggers(cpu=ContainerScaleTriggersCPU(threshold=80)),
        ),
    )

    deployment = client.cloud.inference.deployments.create_and_poll(
        name="gcore-go-example",
        image="nginx:latest",
        flavor_name=flavor_name,
        listening_port=80,
        containers=[container],
    )
    print(f"Created deployment: {deployment.name}, status: {deployment.status}")
    print("========================")
    return deployment.name


def list_deployments(*, client: Gcore) -> None:
    print("\n=== LIST DEPLOYMENTS ===")
    deployments = client.cloud.inference.deployments.list()
    for count, deployment in enumerate(deployments, 1):
        print(f"{count}. Deployment: {deployment.name}, status: {deployment.status}")
    print("========================")


def get_deployment(*, client: Gcore, deployment_name: str) -> None:
    print("\n=== GET DEPLOYMENT ===")
    deployment = client.cloud.inference.deployments.get(deployment_name=deployment_name)
    print(f"Deployment: {deployment.name}, status: {deployment.status}")
    print("========================")


def update_deployment(*, client: Gcore, deployment_name: str) -> None:
    print("\n=== UPDATE DEPLOYMENT ===")
    deployment = client.cloud.inference.deployments.update_and_poll(
        deployment_name=deployment_name,
        description="Updated description",
    )
    print(f"Updated deployment: {deployment.name}")
    print("========================")


def start_deployment(*, client: Gcore, deployment_name: str) -> None:
    print("\n=== START DEPLOYMENT ===")
    client.cloud.inference.deployments.start(deployment_name=deployment_name)
    print(f"Started deployment: {deployment_name}")
    print("========================")


def stop_deployment(*, client: Gcore, deployment_name: str) -> None:
    print("\n=== STOP DEPLOYMENT ===")
    client.cloud.inference.deployments.stop(deployment_name=deployment_name)
    print(f"Stopped deployment: {deployment_name}")
    print("========================")


def delete_deployment(*, client: Gcore, deployment_name: str) -> None:
    print("\n=== DELETE DEPLOYMENT ===")
    client.cloud.inference.deployments.delete_and_poll(deployment_name=deployment_name)
    print(f"Deleted deployment: {deployment_name}")
    print("========================")


if __name__ == "__main__":
    main()
