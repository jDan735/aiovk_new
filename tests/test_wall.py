import pytest
from aiovk_new import AioVK


@pytest.mark.asyncio
async def test_wall_get(aiovk: AioVK):
    post, *_ = await aiovk.wall.get("nii_rap")

    assert post.from_id == -71794920
    assert post.owner_id == -71794920
