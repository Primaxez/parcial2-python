from typing import List

from sqlalchemy.orm import Session

from models.album_models import Album
from schemas.album_schemas import AlbumInDB

class AlbumRepo:

    # get all albums
    async def get_all_albums(self, db: Session) -> List[AlbumInDB]:
        album_list: List[AlbumInDB] = db.query(Album).all()
        return album_list

    # get album by id
    async def get_album_by_id(self, *, id: int, db: Session) -> AlbumInDB:
        album: AlbumInDB = db.query(Album).get(id)
        return album

    # get albums by artist id
    async def get_albums_by_artist_id(self, *, artist_id: int, db: Session) -> List[AlbumInDB]:
        album_list: List[AlbumInDB] = db.query(Album).filter(Album.ArtistId == artist_id).all()
        return album_list