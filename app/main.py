from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Any

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

# @app.get("/shipment/latest")
# def get_latest_shipment() -> dict[str, Any]:
#     latest_id = max(db.keys())
#     shipment = db[latest_id]
#     return shipment

# @app.get("/shipment/{id}")
# def get_shipment_by_id(id: int) -> dict[str, Any]:
#     if id in db:
#         return db[id]
#     return {"error": "Shipment not found"}

#query parameter example
@app.get("/shipment")
def get_shipment(id: int | None = None) -> dict[str, Any]:
    if id is None or id not in db:
        latest_id = max(db.keys())
        return db[latest_id]
    return db[id]

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar Docs"
    )