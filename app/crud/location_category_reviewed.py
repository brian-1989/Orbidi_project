from app.models.location_category_reviewed import LocationCategoryReviewed as ReviewedModel
from app.schemas.location_category_reviewed import LocationCategoryReviewedSchema as ReviewedSchema
from datetime import datetime
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def create_location_category_reviewed_in_db(reviewed_schema: ReviewedSchema, db: Session):
    try:
        db_reviewed = ReviewedModel(
            location_id=reviewed_schema.location_id, category_id=reviewed_schema.category_id,
            last_reviewed=datetime.now())
        db.add(db_reviewed)
        db.commit()
        db.refresh(db_reviewed)
        return db_reviewed
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=jsonable_encoder(str(error)))
