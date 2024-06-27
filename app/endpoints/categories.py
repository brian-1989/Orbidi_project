from app.crud.categories import create_category_in_db
from app.models.base import SessionLocal
from app.schemas.categories import CategorySchema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_category")
def create_category(category: CategorySchema, db: Session = Depends(get_db)):
    return create_category_in_db(category=category, db=db)