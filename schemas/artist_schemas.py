from typing import Optional
from pydantic import BaseModel


class ArtistBase(BaseModel):
    ArtistId: int
    Name: Optional[str]

# usado para entregar un artista
class ArtistInDB(ArtistBase):
    ArtistId: int
    Name: str
    
    class Config:
        orm_mode = True
