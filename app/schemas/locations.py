from pydantic import BaseModel, Field


class LocationSchema(BaseModel):
    latitude: str = Field(max_length=15)
    longitude: str = Field(max_length=15)
