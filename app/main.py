from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Any

from app.schemas import Shipment # or from .schemas import Shipment

app = FastAPI()

db = {
    101 : {
        "content": "smartphone",
        "weight": 0.5,
        "status": "placed"
    },
    102 : {
        "content": "laptop",
        "weight": 2.1,
        "status": "delivered"
    },
    103 : {
        "content": "tablet",
        "weight": 0.8,
        "status": "in transit"
    }
}

@app.get("/shipment")
def get_shipment(shipment_id: int | None = None) -> dict[str, Any]:
    if shipment_id is None:
        max_id = max(db.keys())
        return db[max_id]
    
    if shipment_id in db:
        return db[shipment_id]
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Shipmet ID does not exist!"
    )

@app.post("/shipment")
def submit_shipment(body : Shipment) -> dict[str, int]:
    if body.weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight exceeds the maximum limit of 25 kg."
        )
    new_id = max(db.keys()) + 1
    db[new_id] = {
        "content": body.content,
        "weight": body.weight,
        "destination": body.destination,
        "status": "placed"
    }
    return {"shipment_id": new_id}
    

@app.put("/shipment")
def update_shipment(
    id : int, content : str, weight : float, shipment_status : str
    ) -> dict[str, Any]:
    if id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment ID does not exist!"
        )
    db[id] = {
        "content": content,
        "weight": weight,
        "status": shipment_status
    }
    return db[id]

@app.patch("/shipment")
def patch_shipment(
    id : int,
    body : dict[str, Any]
    ) -> dict[str, Any]:
    if id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment ID does not exist!"
        )
    db[id].update(body)
    return db[id]

@app.delete("/shipment")
def delete_shipment(id : int) -> dict[str, str]:
    if id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment ID does not exist!"
        )
    db.pop(id)
    return {"detail": f"Shipment with id # {id} is deleted successfully."}

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar Docs"
    )