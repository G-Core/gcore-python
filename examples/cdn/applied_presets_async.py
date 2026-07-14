import os
import time
import asyncio
from typing import Tuple, Optional

from gcore import AsyncGcore
from gcore.types.cdn import CDNResource, PresetDetail
from gcore.types.cdn.presets import AppliedPresetFields
from gcore.types.cdn.cdn_resources import CDNResourceRule
from gcore.types.cdn.presets.applied_preset import AppliedObjects


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    # Origin group ID is required to create the CDN resource that presets are applied to.
    origin_group_id = int(os.environ["GCORE_CDN_ORIGIN_GROUP_ID"])

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    # Pick a preset for each object type from the catalog.
    resource_preset, rule_preset = await find_presets(client=gcore)
    if resource_preset is None or resource_preset.id is None:
        print("No CDN resource preset found to apply in this example")
        return

    # Create a CDN resource to apply presets to.
    resource = await create_cdn_resource(client=gcore, origin_group_id=origin_group_id)
    assert resource.id is not None
    try:
        # --- Applied preset lifecycle for a CDN resource ---
        await apply_preset(client=gcore, preset_id=resource_preset.id, object_id=resource.id)
        await get_applied_objects(client=gcore, preset_id=resource_preset.id)
        await get_resource_preset(client=gcore, resource_id=resource.id)
        await unapply_preset(client=gcore, preset_id=resource_preset.id, object_id=resource.id)

        # --- Applied preset lifecycle for a rule ---
        # A Rule-type preset is required to demonstrate the rule flow. It may not be
        # available on every account, so skip gracefully when it is missing.
        if rule_preset is None or rule_preset.id is None:
            print("\nNo Rule preset available, skipping the rule-preset flow")
            return

        rule = await create_rule(client=gcore, resource_id=resource.id)
        assert rule.id is not None
        await apply_preset(client=gcore, preset_id=rule_preset.id, object_id=rule.id)
        await get_rule_preset(client=gcore, resource_id=resource.id, rule_id=rule.id)
        await unapply_preset(client=gcore, preset_id=rule_preset.id, object_id=rule.id)
    finally:
        await deactivate_and_delete_cdn_resource(client=gcore, resource_id=resource.id)


async def find_presets(*, client: AsyncGcore) -> Tuple[Optional[PresetDetail], Optional[PresetDetail]]:
    print("\n=== LIST PRESETS ===")
    resource_preset: Optional[PresetDetail] = None
    rule_preset: Optional[PresetDetail] = None
    count = 0
    async for preset in client.cdn.presets.list():
        count += 1
        print(f"  {count}. Preset: ID={preset.id}, name={preset.name}, object_type={preset.object_type}")
        # Remember the first preset found for each object type.
        if preset.object_type == "CDNResource" and resource_preset is None:
            resource_preset = preset
        elif preset.object_type == "Rule" and rule_preset is None:
            rule_preset = preset
    print("====================")
    return resource_preset, rule_preset


async def create_cdn_resource(*, client: AsyncGcore, origin_group_id: int) -> CDNResource:
    print("\n=== CREATE CDN RESOURCE ===")
    # Use a unique CNAME to avoid conflicts.
    cname = f"cdn-applied-preset-example-{int(time.time())}.example.com"
    resource = await client.cdn.cdn_resources.create(cname=cname, origin_group=origin_group_id, active=True)
    print(f"Created CDN Resource: ID={resource.id}, cname={resource.cname}, active={resource.active}")
    print("===========================")
    return resource


async def create_rule(*, client: AsyncGcore, resource_id: int) -> CDNResourceRule:
    print("\n=== CREATE RULE ===")
    rule = await client.cdn.cdn_resources.rules.create(
        resource_id, name="applied-preset-example", rule="/static", rule_type=0
    )
    print(f"Created Rule: ID={rule.id}, name={rule.name}")
    print("===================")
    return rule


async def apply_preset(*, client: AsyncGcore, preset_id: int, object_id: int) -> None:
    print("\n=== APPLY PRESET ===")
    result = await client.cdn.presets.applied.apply(preset_id, object_id=object_id)
    print(f"Applied preset {preset_id} to object {object_id}: {result.message}")
    print("====================")


async def get_applied_objects(*, client: AsyncGcore, preset_id: int) -> None:
    print("\n=== GET APPLIED OBJECTS ===")
    result = await client.cdn.presets.applied.get_objects(preset_id)
    if isinstance(result, AppliedObjects) and result.object_ids:
        print(f"Preset {preset_id} is applied to {result.object_type} objects: {result.object_ids}")
    else:
        message = getattr(result, "message", None)
        print(f"Preset {preset_id} is not applied to any objects: {message}")
    print("===========================")


async def get_resource_preset(*, client: AsyncGcore, resource_id: int) -> AppliedPresetFields:
    print("\n=== GET RESOURCE PRESET ===")
    applied = await client.cdn.presets.applied.get_resource_preset(resource_id)
    print(
        f"CDN resource {resource_id} has preset: ID={applied.id}, name={applied.name}, "
        f"deletable={applied.deletable}, managed_fields={applied.fields}"
    )
    print("===========================")
    return applied


async def get_rule_preset(*, client: AsyncGcore, resource_id: int, rule_id: int) -> AppliedPresetFields:
    print("\n=== GET RULE PRESET ===")
    applied = await client.cdn.presets.applied.get_rule_preset(rule_id, resource_id=resource_id)
    print(
        f"Rule {rule_id} has preset: ID={applied.id}, name={applied.name}, "
        f"deletable={applied.deletable}, managed_fields={applied.fields}"
    )
    print("=======================")
    return applied


async def unapply_preset(*, client: AsyncGcore, preset_id: int, object_id: int) -> None:
    print("\n=== UNAPPLY PRESET ===")
    await client.cdn.presets.applied.unapply(object_id, preset_id=preset_id)
    print(f"Unapplied preset {preset_id} from object {object_id}")
    print("======================")


async def deactivate_and_delete_cdn_resource(*, client: AsyncGcore, resource_id: int) -> None:
    print("\n=== DEACTIVATE AND DELETE CDN RESOURCE ===")
    # The delete operation requires the CDN resource to be deactivated first.
    await client.cdn.cdn_resources.update(resource_id, active=False)
    await client.cdn.cdn_resources.delete(resource_id)
    print(f"CDN Resource with ID {resource_id} successfully deactivated and deleted")
    print("==========================================")


if __name__ == "__main__":
    asyncio.run(main())
