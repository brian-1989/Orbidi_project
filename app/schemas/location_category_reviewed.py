from pydantic import BaseModel

class LocationCategoryReviewedSchema(BaseModel):
    location_id: int
    category_id: int