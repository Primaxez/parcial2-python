from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_artist_repo, get_album_repo, get_track_repo, get_db
from repositories.album_repository import AlbumRepo
from repositories.track_repository import TrackRepo
from schemas.album_schemas import AlbumInDB
from schemas.track_schemas import TrackInDB
from schemas.artist_schemas import ArtistInDB

router = APIRouter(
    prefix="/singer",
    tags=["Artists"]
)

@router.get("s/",
    response_model=List[ArtistInDB],
    status_code=status.HTTP_200_OK)
# obtener todos los artistas
async def get_all_artists(
    db: Session = Depends(get_db),
    artist_repo: AlbumRepo = Depends(get_artist_repo),
) -> List[ArtistInDB]:
    artists = await artist_repo.get_all_artists(db=db)
    if not artists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return artists

@router.get("s/{id}/",
    response_model=List[AlbumInDB],
    status_code=status.HTTP_200_OK)
# obtener los albums de un artista
async def get_albums_by_artist_id(
    id: int,
    db: Session = Depends(get_db),
    album_repo: AlbumRepo = Depends(get_album_repo),
) -> List[AlbumInDB]:
    albums = await album_repo.get_albums_by_artist_id(artist_id=id, db=db)
    if not albums:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return albums

@router.get("/{id}/",
    response_model=List[TrackInDB],
    status_code=status.HTTP_200_OK)
# obtener los tracks de un artista
async def get_tracks_by_artist_id(
    id: int,
    db: Session = Depends(get_db),
    track_repo: TrackRepo = Depends(get_track_repo),
) -> List[TrackInDB]:
    tracks = await track_repo.get_tracks_by_artist_id(artist_id=id, db=db)
    if not tracks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return tracks