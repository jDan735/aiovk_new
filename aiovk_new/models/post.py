import datetime
from typing import Optional

from pydantic import BaseModel

from .attachments import Photo, Link


class Attachment(BaseModel):
    type: str
    photo: Optional[Photo]
    link: Optional[Link]


class Post(BaseModel):
    id: int
    from_id: int
    owner_id: int

    date: datetime.datetime

    marked_as_ads: bool
    is_pinned: bool = None

    post_type: str

    text: str

    attachments: list[Attachment] = []

    # TODO Add stats
