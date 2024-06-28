from app.crud.location_category_reviewed import (
    create_location_category_reviewed_in_db
)
from app.endpoints.description import (
    create_location_category_reviewed_description as description
)
from app.models.base import SessionLocal
from app.schemas.location_category_reviewed import (
    LocationCategoryReviewedSchema as ReviewedSchema
)
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


@router.post("/create_location_category_reviewed", description=description)
def create_location_category_reviewed(
        review_schema: ReviewedSchema, db: Session = Depends(get_db)):
    return JSONResponse(
        jsonable_encoder(create_location_category_reviewed_in_db(
            reviewed_schema=review_schema, db=db)),
        status_code=status.HTTP_201_CREATED)
