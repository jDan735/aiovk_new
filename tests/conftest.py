import os

import pytest
from aiovk_new import AioVK


@pytest.fixture(scope="function")
def aiovk():
    return AioVK(access_token=os.environ["ACCESS_TOKEN"])
