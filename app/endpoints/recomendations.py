from app.models.base import SessionLocal
from app.crud.recomendations import get_recomendations_from_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get_recomendations", response_model=list[dict])
def get_recomendations(db: Session = Depends(get_db)):
    return JSONResponse(
        jsonable_encoder(get_recomendations_from_db(db=db)),
        status_code=status.HTTP_200_OK)
