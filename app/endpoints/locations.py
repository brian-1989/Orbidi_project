from app.crud.locations import create_location_in_db
from app.models.base import SessionLocal
from app.schemas.locations import LocationSchema
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_location")
def create_location(location: LocationSchema, db: Session = Depends(get_db)):
    return JSONResponse(
        jsonable_encoder(create_location_in_db(location=location, db=db)),
        status_code=status.HTTP_201_CREATED)

