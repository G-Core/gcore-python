import asyncio

from gcore import AsyncGcore
from gcore.types.cdn import PresetDetail
from gcore.pagination import AsyncOffsetPage


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    presets = await list_presets(client=gcore)
    async for preset in presets:
        if preset.id is not None:
            await get_preset(client=gcore, preset_id=preset.id)
            break


async def list_presets(*, client: AsyncGcore) -> AsyncOffsetPage[PresetDetail]:
    print("\n=== LIST PRESETS ===")
    result = await client.cdn.presets.list()
    count = 0
    async for preset in result:
        count += 1
        print(f"  {count}. Preset: ID={preset.id}, name={preset.name}, object_type={preset.object_type}")
    print("====================")
    return result


async def get_preset(*, client: AsyncGcore, preset_id: int) -> PresetDetail:
    print("\n=== GET PRESET ===")
    preset = await client.cdn.presets.get(preset_id)
    settings = preset.preset_settings or {}
    print(
        f"Preset: ID={preset.id}, name={preset.name}, object_type={preset.object_type}, "
        f"service={preset.service}, settings={len(settings)} field(s)"
    )
    print("==================")
    return preset


if __name__ == "__main__":
    asyncio.run(main())
