from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_track_repo, get_db
from repositories.track_repository import TrackRepo
from schemas.track_schemas import TrackInDB

router = APIRouter(
    prefix="/song",
    tags=["Tracks"]
)

@router.get("/{id}/",
    response_model=TrackInDB,
    status_code=status.HTTP_200_OK)
# obtener un track
async def get_track(
    id: int,
    db: Session = Depends(get_db),
    track_repo: TrackRepo = Depends(get_track_repo),
) -> TrackInDB:
    track = await track_repo.get_track_by_id(id=id, db=db)
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return track