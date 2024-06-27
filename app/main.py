from app.endpoints.categories import router as category_router
from app.endpoints.locations import router as location_router
from app.endpoints.location_category_reviewed import router as reviwed_router
from app.endpoints.recomendations import router as recomendations_router
from app.models.base import Base, engine
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(location_router, prefix="/api/v1")
app.include_router(category_router, prefix="/api/v1")
app.include_router(reviwed_router, prefix="/api/v1")
app.include_router(recomendations_router, prefix="/api/v1")
