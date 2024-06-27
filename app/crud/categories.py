from app.models.categories import Category
from app.schemas.categories import CategorySchema
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def create_category_in_db(db: Session, category: CategorySchema):
    try:
        db_category = Category(place_name=category.place_name)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=jsonable_encoder(str(error)))