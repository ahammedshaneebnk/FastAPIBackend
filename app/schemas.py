from pydantic import BaseModel, Field
from random import randint

def generate_random_destination() -> int:
    return randint(60000, 699999)

class Shipment(BaseModel):
    content : str = Field(max_length=100)
    weight : float = Field(ge=1, le=25)
    destination : int | None = Field(
        default_factory=generate_random_destination
    )