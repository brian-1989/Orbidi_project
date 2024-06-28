from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Location(Base):
    __tablename__ = "locations"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    latitude = Column(String(15), nullable=False)
    longitude = Column(String(15), nullable=False)
