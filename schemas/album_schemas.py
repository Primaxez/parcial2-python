from typing import Optional
from pydantic import BaseModel


class AlbumBase(BaseModel):
    AlbumId: int
    Title: Optional[str]
    ArtistId: Optional[int]

# usado para entregar un album
class AlbumInDB(AlbumBase):
    AlbumId: int
    Title: str
    ArtistId: int

    class Config:
        orm_mode = True
