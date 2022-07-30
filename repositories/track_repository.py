from typing import List

from sqlalchemy.orm import Session

from models.track_models import Track
from models.album_models import Album
from schemas.track_schemas import TrackInDB

class TrackRepo:

    # get all tracks
    async def get_all_tracks(self, db: Session) -> List[TrackInDB]:
        track_list: List[TrackInDB] = db.query(Track).all()
        return track_list

    # get track by id
    async def get_track_by_id(self, *, id: int, db: Session) -> TrackInDB:
        track: TrackInDB = db.query(Track).get(id)
        return track

    # get tracks by album id
    async def get_tracks_by_album_id(self, *, album_id: int, db: Session) -> List[TrackInDB]:
        track_list: List[TrackInDB] = db.query(Track).filter(Track.AlbumId == album_id).all()
        return track_list

    # get track by artist id
    async def get_tracks_by_artist_id(self, *, artist_id: int, db: Session) -> List[TrackInDB]:
        track_list: List[TrackInDB] = db.query(Track).join(Album).filter(Album.ArtistId == artist_id).all()
        return track_list