from app.crud.location_category_reviewed import create_location_category_reviewed_in_db
from app.models.base import SessionLocal
from app.schemas.location_category_reviewed import LocationCategoryReviewedSchema as ReviewedSchema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_location_category_reviewed")
def create_location_category_reviewed(review_schema: ReviewedSchema, db: Session = Depends(get_db)):
    return create_location_category_reviewed_in_db(reviewed_schema=review_schema, db=db)
