from sqlalchemy import Column, Integer, String, Float

from src.application.database import Base


class GeoPosOrm(Base):
    __tablename__ = "geoposition"

    id = Column(Integer, primary_key=True)
    longitude = Column(Float)
    latitude = Column(Float)
    description = Column(String, nullable=True)
