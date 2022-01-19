import pytest
from aiovk_new import AioVK


@pytest.mark.asyncio
async def test_audio_get(aiovk: AioVK):
    USER_ID = 521255536

    song, *_ = await aiovk.audio.get(USER_ID)

    assert song.owner_id == USER_ID


@pytest.mark.asyncio
async def test_audio_search(aiovk: AioVK):
    song, *_ = await aiovk.audio.search("Rick Astley - Never Gonna Give You Up")

    assert song.artist == "Rick Astley"
    assert song.title == "Never Gonna Give You Up"
