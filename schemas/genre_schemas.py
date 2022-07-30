from typing import Optional
from pydantic import BaseModel


class GenreBase(BaseModel):
    GenreId: int
    Name: Optional[str]

# usado para entregar un género musical
class GenreInDB(GenreBase):
    GenreId: int
    Name: str
    
    class Config:
        orm_mode = True