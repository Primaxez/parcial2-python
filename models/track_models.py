from sqlalchemy import Column, ForeignKey, Integer, String, Numeric

from config_db import Base

class Track(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'), index=True)
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'), index=True)
    GenreId = Column(Integer, ForeignKey('genres.GenreId'), index=True)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(String) # Se usa String porque pytest lanza una advertencia sobre la conversión errónes de decimales