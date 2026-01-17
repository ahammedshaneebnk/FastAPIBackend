from pydantic import BaseModel, Field
from enum import Enum

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

class BaseShipment(BaseModel):
    content: str = Field(description="Description of the shipment content")
    weight: float = Field(gt=0, description="Weight of the shipment in kilograms")
    destination: int | None = Field(description="Destination ZIP code", default=None)

class ShipmentCreate(BaseShipment):
    pass

class ShipmentRead(BaseShipment):
    status: ShipmentStatus

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus