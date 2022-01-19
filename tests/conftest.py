import pytest
from aiovk_new import AioVK


@pytest.fixture(scope="function")
def aiovk():
    return AioVK(access_token="80f76354d97fdb2efc9811073065e12279266428374048b03db27299b47c45b93dce1cda085c2afaa85c4")
