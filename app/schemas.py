from pydantic import BaseModel, Field
from enum import Enum

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

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
        default=None
    )
    placed : ShipmentStatus | None = Field(
        description="Current status of the shipment",
        default=ShipmentStatus.placed
    )