from sqlalchemy import Column, Integer, String 

from config_db import Base

class MediaType(Base):
    __tablename__ = 'media_types'

    MediaTypeId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)