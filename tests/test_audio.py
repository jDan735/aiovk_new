import pytest
from aiovk_new import AioVK


@pytest.mark.asyncio
async def test_audio_get(aiovk: AioVK):
    USER_ID = 521255536

    song, *_ = await aiovk.audio.get(USER_ID)

    assert song.owner_id == USER_ID


@pytest.mark.asyncio
async def test_audio_search(aiovk: AioVK):
    songs = await aiovk.audio.search("Rick Astley - Never Gonna Give You Up")
    common_info = [(song.artist, song.title) for song in songs]

    assert any([song == ("Rick Astley", "Never Gonna Give You Up") for song in common_info])
