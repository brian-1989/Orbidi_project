from app.models.locations import Location
from app.schemas.locations import LocationSchema
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def create_location_in_db(location: LocationSchema, db: Session):
    try:
        db_location = Location(latitude=location.latitude, longitude=location.longitude)
        db.add(db_location)
        db.commit()
        db.refresh(db_location)
        return db_location
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=jsonable_encoder(str(error)))