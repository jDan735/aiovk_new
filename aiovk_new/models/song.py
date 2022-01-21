import datetime

from pydantic import BaseModel


class Song(BaseModel):
    id: int
    owner_id: int

    title: str
    artist: str
    album_name: str = None

    url: str = None

    is_explicit: bool
    is_focus_track: bool
    is_licensed: bool

    date: datetime.date

    track_code: str
