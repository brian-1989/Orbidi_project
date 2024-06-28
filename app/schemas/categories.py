from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    place_name: str = Field(max_length=100)
