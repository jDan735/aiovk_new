from dataclasses import dataclass, field
from os import access

from .audio import Audio
from .wall import Wall


@dataclass
class AioVK:
    access_token: str = field(repr=None)
    api_version: str = "5.131"

    def __post_init__(self):
        self.audio = Audio(self.access_token, self.api_version)
        self.wall = Wall(self.access_token, self.api_version)
