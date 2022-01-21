from dataclasses import dataclass, field
from ..base import BaseMethod


@dataclass
class Wall(BaseMethod):
    access_token: str = field(repr=None)
    api_version: str = "5.131"

    from .get import get
