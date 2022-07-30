from typing import List

from sqlalchemy.orm import Session

from models.artist_models import Artist
from schemas.artist_schemas import ArtistInDB

class ArtistRepo:

    # get all artists
    async def get_all_artists(self, db: Session) -> List[ArtistInDB]:
        artist_list: List[ArtistInDB] = db.query(Artist).all()
        return artist_list

    # get artist by id
    async def get_artist_by_id(self, *, id: int, db: Session) -> ArtistInDB:
        artist: ArtistInDB = db.query(Artist).get(id)
        return artist