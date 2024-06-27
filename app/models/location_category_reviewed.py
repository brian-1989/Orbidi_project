from app.models.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import pytz

class LocationCategoryReviewed(Base):
    __tablename__ = "location_category_reviewed"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    location_id = Column(Integer, ForeignKey("public.locations.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("public.categories.id"), nullable=False)
    last_reviewed = Column(DateTime, nullable=False)

    location = relationship("Location")
    category = relationship("Category")

