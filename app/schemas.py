from pydantic import BaseModel, Field
from random import randint

def generate_random_destination() -> int:
    return randint(60000, 699999)

class Shipment(BaseModel):
    content : str = Field(
        max_length=100,
        description="Description of the shipment content"
    )
    weight : float = Field(
        description="Weight of the shipment in kilograms",
        ge=1,
        le=25)
    destination : int | None = Field(
        description="Destination postal code",
        default_factory=generate_random_destination
    )