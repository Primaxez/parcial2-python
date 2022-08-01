from config_db import SessionLocal
from repositories.album_repository import AlbumRepo
from repositories.artist_repository import ArtistRepo
from repositories.track_repository import TrackRepo
from tests.config_test_db import TestingSessionLocal

# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_album_repo():
    return AlbumRepo()

def get_artist_repo():
    return ArtistRepo()

def get_track_repo():
    return TrackRepo()

# nuestra instancia de db para pruebas
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()