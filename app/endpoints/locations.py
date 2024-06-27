from app.crud.locations import create_location_in_db
from app.schemas.locations import LocationSchema
from app.models.base import SessionLocal
from fastapi import APIRouter, Depends
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
    return create_location_in_db(location=location, db=db)

