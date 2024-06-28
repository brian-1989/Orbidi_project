from pydantic import BaseModel


class CategorySchema(BaseModel):
    place_name: str
