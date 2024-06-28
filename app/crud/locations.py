from app.models.locations import Location
from app.schemas.locations import LocationSchema
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_location_in_db(location: LocationSchema, db: Session):
    try:
        # Validate if latitude and longitude are recorded in the DB
        validate = db.query(Location).filter(
            and_(
                Location.latitude == location.latitude,
                Location.longitude == location.longitude
            )
        ).all()
        if len(validate) > 0:
            raise IntegrityError("", "", "", "")
        # Insert latitude and longitude data into the database.
        db_location = Location(latitude=location.latitude,
                               longitude=location.longitude)
        db.add(db_location)
        db.commit()
        db.refresh(db_location)
        return db_location
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Latitude and longitude are already registered.")
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=jsonable_encoder(str(error)))
