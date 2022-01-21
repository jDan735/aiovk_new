import os
from re import ASCII
import yaml

import pytest
from aiovk_new import AioVK


@pytest.fixture(scope="function")
def aiovk():
    with open("test_config.yml", "r") as config_file:
        ACCESS_TOKEN = yaml.safe_load(config_file.read())["ACCESS_TOKEN"]

    return AioVK(access_token=ACCESS_TOKEN)
