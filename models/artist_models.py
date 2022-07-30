from sqlalchemy import Column, Integer, String 

from config_db import Base

class Artist(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)