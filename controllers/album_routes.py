from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_track_repo, get_db
from repositories.album_repository import AlbumRepo
from repositories.track_repository import TrackRepo
from schemas.track_schemas import TrackInDB

router = APIRouter(
    prefix="/albums",
    tags=["Albums"]
)

@router.get("/{id}",
    response_model=List[TrackInDB],
    status_code=status.HTTP_200_OK,
    name="albums:get-tracks-in-album"
)
# obtener los tracks de un album
async def get_tracks_in_album(
    id: int,
    db: Session = Depends(get_db),
    track_repo: TrackRepo = Depends(get_track_repo),
) -> List[TrackInDB]:
    tracks = await track_repo.get_tracks_by_album_id(album_id=id, db=db)
    if not tracks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return tracks

