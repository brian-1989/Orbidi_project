from pydantic import BaseModel

class LocationSchema(BaseModel):
    latitude: float
    longitude: float