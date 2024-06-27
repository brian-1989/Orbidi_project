from pydantic import BaseModel, Field

class locations(BaseModel):
    length: str = Field(default="") 
