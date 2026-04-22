import os
import time
from typing import List

from gcore import Gcore
from gcore.types.cloud.baremetal_flavor import BaremetalFlavor
from gcore.types.cloud.k8s_cluster_version import K8SClusterVersion
from gcore.types.cloud.k8s.cluster_create_params import Pool


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]
    # TODO set a pre-existing SSH keypair name before running. The K8s cluster
    # create endpoint requires a keypair to bootstrap nodes.
    keypair_name = os.environ["GCORE_CLOUD_K8S_KEYPAIR_NAME"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    # Look up a small non-GPU flavor and the latest version to use for cluster creation.
    flavors = list_flavors(client=gcore)
    pool_flavor_id = _pick_pool_flavor(flavors)

    versions = list_versions(client=gcore)
    cluster_version = _pick_create_version(versions)

    # Cluster lifecycle.
    cluster_name = create_cluster(
        client=gcore,
        flavor_id=pool_flavor_id,
        version=cluster_version,
        keypair_name=keypair_name,
    )

    get_cluster(client=gcore, cluster_name=cluster_name)
    list_clusters(client=gcore)
    update_cluster(client=gcore, cluster_name=cluster_name)

    # Upgrade the cluster to the newest available version, if one exists.
    upgrade_versions = list_upgrade_versions(client=gcore, cluster_name=cluster_name)
    if upgrade_versions:
        upgrade_cluster(client=gcore, cluster_name=cluster_name, target_version=upgrade_versions[-1].version)
        # The upgrade task finishes before the cluster itself settles back to
        # Provisioned, so subsequent mutations (e.g. creating a new pool) can
        # be rejected with "Cluster or pool is not ready". Wait it out.
        wait_for_cluster_ready(client=gcore, cluster_name=cluster_name)
    else:
        print(f"No upgrade versions available for cluster {cluster_name}; skipping upgrade")

    get_certificate(client=gcore, cluster_name=cluster_name)
    get_kubeconfig(client=gcore, cluster_name=cluster_name)

    # Pool operations.
    list_pools(client=gcore, cluster_name=cluster_name)
    first_pool = _get_first_pool(client=gcore, cluster_name=cluster_name)

    check_pool_quota(client=gcore, flavor_id=pool_flavor_id)
    second_pool = create_pool(client=gcore, cluster_name=cluster_name, flavor_id=pool_flavor_id)
    update_pool(client=gcore, cluster_name=cluster_name, pool_name=second_pool)
    resize_pool(client=gcore, cluster_name=cluster_name, pool_name=second_pool)
    list_pool_nodes(client=gcore, cluster_name=cluster_name, pool_name=second_pool)
    delete_pool(client=gcore, cluster_name=cluster_name, pool_name=second_pool)

    # Ensure the initial pool is still reachable after the second pool is gone.
    get_pool(client=gcore, cluster_name=cluster_name, pool_name=first_pool)

    list_cluster_nodes(client=gcore, cluster_name=cluster_name)

    # Final cleanup.
    delete_cluster(client=gcore, cluster_name=cluster_name)


def create_cluster(*, client: Gcore, flavor_id: str, version: str, keypair_name: str) -> str:
    print("\n=== CREATE K8S CLUSTER ===")
    cluster = client.cloud.k8s.clusters.create_and_poll(
        name="gcore-py-example-k8s",
        keypair=keypair_name,
        version=version,
        pools=[
            Pool(
                name="gcore-python-pool",
                flavor_id=flavor_id,
                min_node_count=1,
                max_node_count=2,
                boot_volume_size=50,
                boot_volume_type="standard",
                auto_healing_enabled=True,
                is_public_ipv4=True,
                servergroup_policy="soft-anti-affinity",
                labels={"pool": "gcore-python-example"},
            ),
        ],
    )
    print(f"Created K8s cluster: name={cluster.name}, version={cluster.version}, status={cluster.status}")
    print("==========================")
    return cluster.name


def get_cluster(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== GET K8S CLUSTER ===")
    cluster = client.cloud.k8s.clusters.get(cluster_name=cluster_name)
    print(
        f"K8s cluster: name={cluster.name}, version={cluster.version}, "
        f"status={cluster.status}, pools={len(cluster.pools)}"
    )
    print("=======================")


def list_clusters(*, client: Gcore) -> None:
    print("\n=== LIST K8S CLUSTERS ===")
    clusters = client.cloud.k8s.clusters.list()
    if not clusters.results:
        print("  No k8s clusters found.")
    for count, cluster in enumerate(clusters.results, 1):
        print(f"  {count}. K8s cluster: name={cluster.name}, version={cluster.version}, status={cluster.status}")
    print("=========================")


def update_cluster(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== UPDATE K8S CLUSTER ===")
    # Override a cluster-autoscaler parameter — a safe, idempotent change that
    # exercises update_and_poll.
    cluster = client.cloud.k8s.clusters.update_and_poll(
        cluster_name=cluster_name,
        autoscaler_config={"scale-down-unneeded-time": "5m"},
    )
    print(f"Updated K8s cluster: name={cluster.name}, autoscaler_config={cluster.autoscaler_config}")
    print("==========================")


def list_upgrade_versions(*, client: Gcore, cluster_name: str) -> List[K8SClusterVersion]:
    print("\n=== LIST K8S CLUSTER UPGRADE VERSIONS ===")
    versions = client.cloud.k8s.clusters.list_versions_for_upgrade(cluster_name=cluster_name)
    for count, version in enumerate(versions.results, 1):
        print(f"  {count}. Upgrade version: {version.version}")
    if not versions.results:
        print("  Cluster is already on the latest available version.")
    print("==========================================")
    return versions.results


def upgrade_cluster(*, client: Gcore, cluster_name: str, target_version: str) -> None:
    print("\n=== UPGRADE K8S CLUSTER ===")
    cluster = client.cloud.k8s.clusters.upgrade_and_poll(cluster_name=cluster_name, version=target_version)
    print(f"Upgraded K8s cluster: name={cluster.name}, version={cluster.version}")
    print("===========================")


def get_certificate(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== GET K8S CLUSTER CERTIFICATE ===")
    cert = client.cloud.k8s.clusters.get_certificate(cluster_name=cluster_name)
    print(f"Certificate bytes={len(cert.certificate)}, Key bytes={len(cert.key)}")
    print("===================================")


def wait_for_cluster_ready(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== WAIT FOR K8S CLUSTER READY ===")
    poll_interval = 10
    max_attempts = 60
    for attempt in range(1, max_attempts + 1):
        cluster = client.cloud.k8s.clusters.get(cluster_name=cluster_name)
        pending: List[str] = []
        if cluster.status != "Provisioned":
            pending.append(f"cluster={cluster.status}")
        for pool in cluster.pools:
            if pool.status != "Running":
                pending.append(f"pool[{pool.name}]={pool.status}")
        if not pending:
            print(f"Cluster {cluster_name} is ready (all pools Running)")
            print("==================================")
            return
        print(f"  attempt {attempt}: waiting on {' '.join(pending)}")
        time.sleep(poll_interval)
    raise TimeoutError(f"Cluster {cluster_name} did not become ready after {max_attempts} attempts")


def get_kubeconfig(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== GET K8S KUBECONFIG ===")
    kubeconfig = client.cloud.k8s.clusters.kubeconfig.get(cluster_name=cluster_name)
    print(
        f"Kubeconfig: host={kubeconfig.host}, created_at={kubeconfig.created_at}, "
        f"expires_at={kubeconfig.expires_at}, bytes={len(kubeconfig.config)}"
    )
    print("==========================")


def list_pools(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== LIST K8S CLUSTER POOLS ===")
    pools = client.cloud.k8s.clusters.pools.list(cluster_name=cluster_name)
    if not pools.results:
        print("  No pools found.")
    for count, pool in enumerate(pools.results, 1):
        print(
            f"  {count}. Pool: name={pool.name}, flavor={pool.flavor_id}, "
            f"node_count={pool.node_count}, status={pool.status}"
        )
    print("==============================")


def get_pool(*, client: Gcore, cluster_name: str, pool_name: str) -> None:
    print("\n=== GET K8S CLUSTER POOL ===")
    pool = client.cloud.k8s.clusters.pools.get(pool_name=pool_name, cluster_name=cluster_name)
    print(
        f"Pool: name={pool.name}, flavor={pool.flavor_id}, node_count={pool.node_count}, "
        f"min={pool.min_node_count}, max={pool.max_node_count}, status={pool.status}"
    )
    print("============================")


def check_pool_quota(*, client: Gcore, flavor_id: str) -> None:
    print("\n=== CHECK K8S POOL QUOTA ===")
    quota = client.cloud.k8s.clusters.pools.check_quota(
        flavor_id=flavor_id,
        name="gcore-python-pool-2",
        min_node_count=1,
        max_node_count=2,
        boot_volume_size=50,
        servergroup_policy="soft-anti-affinity",
    )
    print(f"CPU: limit={quota.cpu_count_limit}, requested={quota.cpu_count_requested}, usage={quota.cpu_count_usage}")
    print(f"RAM (MiB): limit={quota.ram_limit}, requested={quota.ram_requested}, usage={quota.ram_usage}")
    print(
        f"Volumes: count_limit={quota.volume_count_limit}, count_usage={quota.volume_count_usage}, "
        f"size_limit={quota.volume_size_limit} GiB"
    )
    print("============================")


def create_pool(*, client: Gcore, cluster_name: str, flavor_id: str) -> str:
    print("\n=== CREATE K8S CLUSTER POOL ===")
    pool = client.cloud.k8s.clusters.pools.create_and_poll(
        cluster_name=cluster_name,
        name="gcore-python-pool-2",
        flavor_id=flavor_id,
        min_node_count=1,
        max_node_count=2,
        boot_volume_size=50,
        boot_volume_type="standard",
        auto_healing_enabled=True,
        is_public_ipv4=True,
        servergroup_policy="soft-anti-affinity",
        labels={"pool": "gcore-python-example-2"},
    )
    print(f"Created pool: name={pool.name}, flavor={pool.flavor_id}, node_count={pool.node_count}")
    print("===============================")
    return pool.name


def update_pool(*, client: Gcore, cluster_name: str, pool_name: str) -> None:
    print("\n=== UPDATE K8S CLUSTER POOL ===")
    pool = client.cloud.k8s.clusters.pools.update(
        pool_name=pool_name,
        cluster_name=cluster_name,
        labels={"pool": "gcore-python-example-2", "stage": "updated"},
    )
    print(f"Updated pool: name={pool.name}, labels={pool.labels}")
    print("===============================")


def resize_pool(*, client: Gcore, cluster_name: str, pool_name: str) -> None:
    print("\n=== RESIZE K8S CLUSTER POOL ===")
    pool = client.cloud.k8s.clusters.pools.resize_and_poll(
        pool_name=pool_name,
        cluster_name=cluster_name,
        node_count=2,
    )
    print(f"Resized pool: name={pool.name}, node_count={pool.node_count}")
    print("===============================")


def delete_pool(*, client: Gcore, cluster_name: str, pool_name: str) -> None:
    print("\n=== DELETE K8S CLUSTER POOL ===")
    client.cloud.k8s.clusters.pools.delete_and_poll(pool_name=pool_name, cluster_name=cluster_name)
    print(f"Deleted pool: name={pool_name}")
    print("===============================")


def list_cluster_nodes(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== LIST K8S CLUSTER NODES ===")
    nodes = client.cloud.k8s.clusters.nodes.list(cluster_name=cluster_name)
    if not nodes.results:
        print("  No nodes found.")
    for count, node in enumerate(nodes.results, 1):
        print(f"  {count}. Node: ID={node.id}, name={node.name}, status={node.status}")
    print("==============================")


def list_pool_nodes(*, client: Gcore, cluster_name: str, pool_name: str) -> None:
    print("\n=== LIST K8S POOL NODES ===")
    nodes = client.cloud.k8s.clusters.pools.nodes.list(pool_name=pool_name, cluster_name=cluster_name)
    if not nodes.results:
        print("  No pool nodes found.")
    for count, node in enumerate(nodes.results, 1):
        print(f"  {count}. Node: ID={node.id}, name={node.name}, status={node.status}")
    print("===========================")


def delete_cluster(*, client: Gcore, cluster_name: str) -> None:
    print("\n=== DELETE K8S CLUSTER ===")
    client.cloud.k8s.clusters.delete_and_poll(cluster_name=cluster_name)
    print(f"Deleted K8s cluster: name={cluster_name}")
    print("==========================")


def list_flavors(*, client: Gcore) -> List[BaremetalFlavor]:
    print("\n=== LIST K8S FLAVORS ===")
    flavors = client.cloud.k8s.flavors.list(exclude_gpu=True, include_capacity=True)

    display_count = min(3, len(flavors.results))
    for i in range(display_count):
        flavor = flavors.results[i]
        print(
            f"  {i + 1}. Flavor: ID={flavor.flavor_id}, name={flavor.flavor_name}, "
            f"RAM={flavor.ram} MB, VCPUs={flavor.vcpus}"
        )

    if len(flavors.results) > display_count:
        print(f"  ... and {len(flavors.results) - display_count} more flavors")

    print(f"Total k8s flavors: {len(flavors.results)}")
    print("========================")
    return flavors.results


def list_versions(*, client: Gcore) -> List[K8SClusterVersion]:
    print("\n=== LIST K8S VERSIONS ===")
    versions = client.cloud.k8s.list_versions()
    for count, version in enumerate(versions.results, 1):
        print(f"  {count}. Version: {version.version}")
    print(f"Total k8s versions: {len(versions.results)}")
    print("=========================")
    return versions.results


def _pick_pool_flavor(flavors: List[BaremetalFlavor]) -> str:
    # Prefer the smallest g1-standard VM flavor with capacity; skip disabled,
    # zero-capacity, and test/fake flavors.
    candidates = [
        f
        for f in flavors
        if not f.disabled
        and (f.capacity or 0) > 0
        and "test" not in f.flavor_name
        and "fake" not in f.flavor_name
        and f.flavor_name.startswith("g1-standard-")
    ]
    if not candidates:
        raise ValueError("No suitable g1-standard k8s flavor with capacity found")

    pick = min(candidates, key=lambda f: f.ram)
    print(f"Selected k8s pool flavor: {pick.flavor_name} (RAM: {pick.ram} MB, VCPUs: {pick.vcpus})")
    return pick.flavor_id


def _pick_create_version(versions: List[K8SClusterVersion]) -> str:
    if not versions:
        raise ValueError("No k8s versions available for cluster creation")
    # The API returns versions in ascending order. Pick the penultimate
    # version when possible so the example always has a newer version to
    # upgrade to later. Fall back to the only available version otherwise.
    idx = max(len(versions) - 2, 0)
    picked = versions[idx].version
    print(f"Selected k8s version for creation: {picked}")
    return picked


def _get_first_pool(*, client: Gcore, cluster_name: str) -> str:
    pools = client.cloud.k8s.clusters.pools.list(cluster_name=cluster_name)
    if not pools.results:
        raise ValueError(f"Cluster {cluster_name} has no pools")
    return pools.results[0].name


if __name__ == "__main__":
    main()
