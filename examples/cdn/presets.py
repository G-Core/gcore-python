from gcore import Gcore
from gcore.types.cdn import PresetDetail
from gcore.pagination import SyncOffsetPage


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
    )

    presets = list_presets(client=gcore)
    for preset in presets:
        if preset.id is not None:
            get_preset(client=gcore, preset_id=preset.id)
            break


def list_presets(*, client: Gcore) -> SyncOffsetPage[PresetDetail]:
    print("\n=== LIST PRESETS ===")
    result = client.cdn.presets.list()
    for count, preset in enumerate(result, 1):
        print(f"  {count}. Preset: ID={preset.id}, name={preset.name}, object_type={preset.object_type}")
    print("====================")
    return result


def get_preset(*, client: Gcore, preset_id: int) -> PresetDetail:
    print("\n=== GET PRESET ===")
    preset = client.cdn.presets.get(preset_id)
    settings = preset.preset_settings or {}
    print(
        f"Preset: ID={preset.id}, name={preset.name}, object_type={preset.object_type}, "
        f"service={preset.service}, settings={len(settings)} field(s)"
    )
    print("==================")
    return preset


if __name__ == "__main__":
    main()
