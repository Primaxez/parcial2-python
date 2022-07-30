from typing import Optional
from pydantic import BaseModel


class TrackBase(BaseModel):
    TrackId: int
    Name: Optional[str]
    AlbumId: Optional[int]
    MediaTypeId: Optional[int]
    GenreId: Optional[int]
    Composer: Optional[str]
    Milliseconds: Optional[int]
    Bytes: Optional[int]
    UnitPrice: Optional[float]

# usado para entregar una pista
class TrackInDB(TrackBase):
    TrackId: int
    Name: str
    AlbumId: int
    MediaTypeId: int
    GenreId: int
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: float
    
    class Config:
        orm_mode = True