from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Any

app = FastAPI()

@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    return {
        "id": 101,
        "content": "smartphone",
        "weight": 0.5,
        "status": "placed"
    }

@app.get("/shipment/{id}")
def get_shipment_by_id(id: int) -> dict[str, Any]:
    return {
        "id": id,
        "content": "laptop",
        "weight": 2.1,
        "status": "delivered"
    }

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar Docs"
    )