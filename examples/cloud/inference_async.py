import os
import asyncio

from gcore import AsyncGcore
from gcore.types.cloud.inference.deployment_create_params import (
    Container,
    ContainerScale,
    ContainerScaleTriggers,
    ContainerScaleTriggersCPU,
)


async def main() -> None:
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

    gcore = AsyncGcore(
        timeout=180.0,
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
    )

    # Capacity
    await get_capacity_by_region(client=gcore)

    # Flavors
    await list_flavors(client=gcore)
    await get_flavor(client=gcore, flavor_name=cloud_inference_flavor_name)

    # Models
    await list_models(client=gcore)
    await get_model(client=gcore, model_id=cloud_inference_model_id)

    # Registry Credentials
    credential_name = await create_registry_credential(client=gcore)
    await list_registry_credentials(client=gcore)
    await get_registry_credential(client=gcore, credential_name=credential_name)
    await replace_registry_credential(client=gcore, credential_name=credential_name)
    await delete_registry_credential(client=gcore, credential_name=credential_name)

    # Secrets
    secret_name = await create_secret(client=gcore)
    await list_secrets(client=gcore)
    await get_secret(client=gcore, secret_name=secret_name)
    await replace_secret(client=gcore, secret_name=secret_name)
    await delete_secret(client=gcore, secret_name=secret_name)

    # Deployments
    deployment_name = await create_deployment(
        client=gcore, flavor_name=cloud_inference_flavor_name, region_id=int(cloud_region_id)
    )
    await list_deployments(client=gcore)
    await get_deployment(client=gcore, deployment_name=deployment_name)
    await update_deployment(client=gcore, deployment_name=deployment_name)
    await stop_deployment(client=gcore, deployment_name=deployment_name)
    await start_deployment(client=gcore, deployment_name=deployment_name)
    await delete_deployment(client=gcore, deployment_name=deployment_name)


async def get_capacity_by_region(*, client: AsyncGcore) -> None:
    print("\n=== GET CAPACITY BY REGION ===")
    capacities = await client.cloud.inference.get_capacity_by_region()

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


async def list_flavors(*, client: AsyncGcore) -> None:
    print("\n=== LIST FLAVORS ===")
    flavors = await client.cloud.inference.flavors.list()

    # Display first few flavors
    count = 0
    async for flavor in flavors:
        count += 1
        print(f"{count}. Flavor: {flavor.name}, CPU: {flavor.cpu}, Memory: {flavor.memory} Gi")
        if count >= 3:
            break

    # Note: We can't easily determine the total count with async iteration
    # without consuming the entire iterator
    print("========================")


async def get_flavor(*, client: AsyncGcore, flavor_name: str) -> None:
    print("\n=== GET FLAVOR ===")
    flavor = await client.cloud.inference.flavors.get(flavor_name=flavor_name)
    print(f"Flavor: {flavor.name}, CPU: {flavor.cpu}, Memory: {flavor.memory} Gi")
    print("========================")


async def list_models(*, client: AsyncGcore) -> None:
    print("\n=== LIST MODELS ===")
    models = await client.cloud.inference.models.list()

    # Display first few models
    count = 0
    async for model in models:
        count += 1
        print(f"{count}. Model: {model.name}, ID: {model.id}")
        if count >= 3:
            break

    # Note: We can't easily determine the total count with async iteration
    # without consuming the entire iterator
    print("========================")


async def get_model(*, client: AsyncGcore, model_id: str) -> None:
    print("\n=== GET MODEL ===")
    model = await client.cloud.inference.models.get(model_id=model_id)
    print(f"Model: {model.name}, ID: {model.id}")
    print("========================")


async def create_registry_credential(*, client: AsyncGcore) -> str:
    print("\n=== CREATE REGISTRY CREDENTIAL ===")
    credential = await client.cloud.inference.registry_credentials.create(
        name="gcore-go-example",
        username="example-user",
        password="example-password",
        registry_url="https://registry.example.com",
    )
    print(f"Created registry credential: {credential.name}")
    print("========================")
    return credential.name


async def list_registry_credentials(*, client: AsyncGcore) -> None:
    print("\n=== LIST REGISTRY CREDENTIALS ===")
    credentials = await client.cloud.inference.registry_credentials.list()
    count = 0
    async for credential in credentials:
        count += 1
        print(f"{count}. Registry credential: {credential.name}, URL: {credential.registry_url}")
    print("========================")


async def get_registry_credential(*, client: AsyncGcore, credential_name: str) -> None:
    print("\n=== GET REGISTRY CREDENTIAL ===")
    credential = await client.cloud.inference.registry_credentials.get(credential_name=credential_name)
    print(f"Registry credential: {credential.name}, URL: {credential.registry_url}")
    print("========================")


async def replace_registry_credential(*, client: AsyncGcore, credential_name: str) -> None:
    print("\n=== REPLACE REGISTRY CREDENTIAL ===")
    await client.cloud.inference.registry_credentials.replace(
        credential_name=credential_name,
        username="updated-user",
        password="updated-password",
        registry_url="https://updated-registry.example.com",
    )
    print(f"Replaced registry credential: {credential_name}")
    print("========================")


async def delete_registry_credential(*, client: AsyncGcore, credential_name: str) -> None:
    print("\n=== DELETE REGISTRY CREDENTIAL ===")
    await client.cloud.inference.registry_credentials.delete(credential_name=credential_name)
    print(f"Deleted registry credential: {credential_name}")
    print("========================")


async def create_secret(*, client: AsyncGcore) -> str:
    print("\n=== CREATE SECRET ===")
    secret = await client.cloud.inference.secrets.create(
        name="gcore-go-example",
        type="aws-iam",
        data={"aws_access_key_id": "example-key", "aws_secret_access_key": "example-secret"},
    )
    print(f"Created secret: {secret.name}")
    print("========================")
    return secret.name


async def list_secrets(*, client: AsyncGcore) -> None:
    print("\n=== LIST SECRETS ===")
    secrets = await client.cloud.inference.secrets.list()
    count = 0
    async for secret in secrets:
        count += 1
        print(f"{count}. Secret: {secret.name}, type: {secret.type}")
    print("========================")


async def get_secret(*, client: AsyncGcore, secret_name: str) -> None:
    print("\n=== GET SECRET ===")
    secret = await client.cloud.inference.secrets.get(secret_name=secret_name)
    print(f"Secret: {secret.name}, type: {secret.type}")
    print("========================")


async def replace_secret(*, client: AsyncGcore, secret_name: str) -> None:
    print("\n=== REPLACE SECRET ===")
    secret = await client.cloud.inference.secrets.replace(
        secret_name=secret_name,
        type="aws-iam",
        data={"aws_access_key_id": "updated-key", "aws_secret_access_key": "updated-secret"},
    )
    print(f"Replaced secret: {secret.name}")
    print("========================")


async def delete_secret(*, client: AsyncGcore, secret_name: str) -> None:
    print("\n=== DELETE SECRET ===")
    await client.cloud.inference.secrets.delete(secret_name=secret_name)
    print(f"Deleted secret: {secret_name}")
    print("========================")


async def create_deployment(*, client: AsyncGcore, flavor_name: str, region_id: int) -> str:
    print("\n=== CREATE DEPLOYMENT ===")

    container = Container(
        region_id=region_id,
        scale=ContainerScale(
            min=1,
            max=3,
            triggers=ContainerScaleTriggers(cpu=ContainerScaleTriggersCPU(threshold=80)),
        ),
    )

    deployment = await client.cloud.inference.deployments.create_and_poll(
        name="gcore-go-example",
        image="nginx:latest",
        flavor_name=flavor_name,
        listening_port=80,
        containers=[container],
    )
    print(f"Created deployment: {deployment.name}, status: {deployment.status}")
    print("========================")
    return deployment.name


async def list_deployments(*, client: AsyncGcore) -> None:
    print("\n=== LIST DEPLOYMENTS ===")
    deployments = await client.cloud.inference.deployments.list()
    count = 0
    async for deployment in deployments:
        count += 1
        print(f"{count}. Deployment: {deployment.name}, status: {deployment.status}")
    print("========================")


async def get_deployment(*, client: AsyncGcore, deployment_name: str) -> None:
    print("\n=== GET DEPLOYMENT ===")
    deployment = await client.cloud.inference.deployments.get(deployment_name=deployment_name)
    print(f"Deployment: {deployment.name}, status: {deployment.status}")
    print("========================")


async def update_deployment(*, client: AsyncGcore, deployment_name: str) -> None:
    print("\n=== UPDATE DEPLOYMENT ===")
    deployment = await client.cloud.inference.deployments.update_and_poll(
        deployment_name=deployment_name,
        description="Updated description",
    )
    print(f"Updated deployment: {deployment.name}")
    print("========================")


async def start_deployment(*, client: AsyncGcore, deployment_name: str) -> None:
    print("\n=== START DEPLOYMENT ===")
    await client.cloud.inference.deployments.start(deployment_name=deployment_name)
    print(f"Started deployment: {deployment_name}")
    print("========================")


async def stop_deployment(*, client: AsyncGcore, deployment_name: str) -> None:
    print("\n=== STOP DEPLOYMENT ===")
    await client.cloud.inference.deployments.stop(deployment_name=deployment_name)
    print(f"Stopped deployment: {deployment_name}")
    print("========================")


async def delete_deployment(*, client: AsyncGcore, deployment_name: str) -> None:
    print("\n=== DELETE DEPLOYMENT ===")
    await client.cloud.inference.deployments.delete_and_poll(deployment_name=deployment_name)
    print(f"Deleted deployment: {deployment_name}")
    print("========================")


if __name__ == "__main__":
    asyncio.run(main())
