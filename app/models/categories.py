from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    place_name = Column(String(20), unique=True, nullable=False)
