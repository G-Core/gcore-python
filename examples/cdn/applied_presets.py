import os
import time
from typing import Tuple, Optional

from gcore import Gcore
from gcore.types.cdn import CDNResource, PresetDetail
from gcore.types.cdn.presets import AppliedPresetFields
from gcore.types.cdn.cdn_resources import CDNResourceRule
from gcore.types.cdn.presets.applied_preset import AppliedObjects


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    # Origin group ID is required to create the CDN resource that presets are applied to.
    origin_group_id = int(os.environ["GCORE_CDN_ORIGIN_GROUP_ID"])

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    # Pick a preset for each object type from the catalog.
    resource_preset, rule_preset = find_presets(client=gcore)
    if resource_preset is None or resource_preset.id is None:
        print("No CDN resource preset found to apply in this example")
        return

    # Create a CDN resource to apply presets to.
    resource = create_cdn_resource(client=gcore, origin_group_id=origin_group_id)
    assert resource.id is not None
    try:
        # --- Applied preset lifecycle for a CDN resource ---
        apply_preset(client=gcore, preset_id=resource_preset.id, object_id=resource.id)
        get_applied_objects(client=gcore, preset_id=resource_preset.id)
        get_resource_preset(client=gcore, resource_id=resource.id)
        unapply_preset(client=gcore, preset_id=resource_preset.id, object_id=resource.id)

        # --- Applied preset lifecycle for a rule ---
        # A Rule-type preset is required to demonstrate the rule flow. It may not be
        # available on every account, so skip gracefully when it is missing.
        if rule_preset is None or rule_preset.id is None:
            print("\nNo Rule preset available, skipping the rule-preset flow")
            return

        rule = create_rule(client=gcore, resource_id=resource.id)
        assert rule.id is not None
        apply_preset(client=gcore, preset_id=rule_preset.id, object_id=rule.id)
        get_rule_preset(client=gcore, resource_id=resource.id, rule_id=rule.id)
        unapply_preset(client=gcore, preset_id=rule_preset.id, object_id=rule.id)
    finally:
        deactivate_and_delete_cdn_resource(client=gcore, resource_id=resource.id)


def find_presets(*, client: Gcore) -> Tuple[Optional[PresetDetail], Optional[PresetDetail]]:
    print("\n=== LIST PRESETS ===")
    resource_preset: Optional[PresetDetail] = None
    rule_preset: Optional[PresetDetail] = None
    for count, preset in enumerate(client.cdn.presets.list(), 1):
        print(f"  {count}. Preset: ID={preset.id}, name={preset.name}, object_type={preset.object_type}")
        # Remember the first preset found for each object type.
        if preset.object_type == "CDNResource" and resource_preset is None:
            resource_preset = preset
        elif preset.object_type == "Rule" and rule_preset is None:
            rule_preset = preset
    print("====================")
    return resource_preset, rule_preset


def create_cdn_resource(*, client: Gcore, origin_group_id: int) -> CDNResource:
    print("\n=== CREATE CDN RESOURCE ===")
    # Use a unique CNAME to avoid conflicts.
    cname = f"cdn-applied-preset-example-{int(time.time())}.example.com"
    resource = client.cdn.cdn_resources.create(cname=cname, origin_group=origin_group_id, active=True)
    print(f"Created CDN Resource: ID={resource.id}, cname={resource.cname}, active={resource.active}")
    print("===========================")
    return resource


def create_rule(*, client: Gcore, resource_id: int) -> CDNResourceRule:
    print("\n=== CREATE RULE ===")
    rule = client.cdn.cdn_resources.rules.create(
        resource_id, name="applied-preset-example", rule="/static", rule_type=0
    )
    print(f"Created Rule: ID={rule.id}, name={rule.name}")
    print("===================")
    return rule


def apply_preset(*, client: Gcore, preset_id: int, object_id: int) -> None:
    print("\n=== APPLY PRESET ===")
    result = client.cdn.presets.applied.apply(preset_id, object_id=object_id)
    print(f"Applied preset {preset_id} to object {object_id}: {result.message}")
    print("====================")


def get_applied_objects(*, client: Gcore, preset_id: int) -> None:
    print("\n=== GET APPLIED OBJECTS ===")
    result = client.cdn.presets.applied.get_objects(preset_id)
    if isinstance(result, AppliedObjects) and result.object_ids:
        print(f"Preset {preset_id} is applied to {result.object_type} objects: {result.object_ids}")
    else:
        message = getattr(result, "message", None)
        print(f"Preset {preset_id} is not applied to any objects: {message}")
    print("===========================")


def get_resource_preset(*, client: Gcore, resource_id: int) -> AppliedPresetFields:
    print("\n=== GET RESOURCE PRESET ===")
    applied = client.cdn.presets.applied.get_resource_preset(resource_id)
    print(
        f"CDN resource {resource_id} has preset: ID={applied.id}, name={applied.name}, "
        f"deletable={applied.deletable}, managed_fields={applied.fields}"
    )
    print("===========================")
    return applied


def get_rule_preset(*, client: Gcore, resource_id: int, rule_id: int) -> AppliedPresetFields:
    print("\n=== GET RULE PRESET ===")
    applied = client.cdn.presets.applied.get_rule_preset(rule_id, resource_id=resource_id)
    print(
        f"Rule {rule_id} has preset: ID={applied.id}, name={applied.name}, "
        f"deletable={applied.deletable}, managed_fields={applied.fields}"
    )
    print("=======================")
    return applied


def unapply_preset(*, client: Gcore, preset_id: int, object_id: int) -> None:
    print("\n=== UNAPPLY PRESET ===")
    client.cdn.presets.applied.unapply(object_id, preset_id=preset_id)
    print(f"Unapplied preset {preset_id} from object {object_id}")
    print("======================")


def deactivate_and_delete_cdn_resource(*, client: Gcore, resource_id: int) -> None:
    print("\n=== DEACTIVATE AND DELETE CDN RESOURCE ===")
    # The delete operation requires the CDN resource to be deactivated first.
    client.cdn.cdn_resources.update(resource_id, active=False)
    client.cdn.cdn_resources.delete(resource_id)
    print(f"CDN Resource with ID {resource_id} successfully deactivated and deleted")
    print("==========================================")


if __name__ == "__main__":
    main()
