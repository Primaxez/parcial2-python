from typing import Optional
from pydantic import BaseModel


class MediaTypeBase(BaseModel):
    MediaTypeId: int
    Name: Optional[str]

# usado para entregar un tipo de multimedia
class MediaTypeInDB(MediaTypeBase):
    MediaTypeId: int
    Name: str
    
    class Config:
        orm_mode = True