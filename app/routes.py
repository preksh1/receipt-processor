from fastapi import APIRouter, HTTPException
from app.models import Receipt, ReceiptResponse, PointsResponse
from app.database import receipt_db, points_db
from app.utils import generate_receipt_id
from app.services import calculate_points

router = APIRouter()

@router.post("/receipts/process", response_model=ReceiptResponse)
async def process_receipt(receipt: Receipt):
    receipt_id = generate_receipt_id()
    points = calculate_points(receipt)
    receipt_db[receipt_id] = receipt
    points_db[receipt_id] = points
    return {"id": receipt_id}


@router.get("/receipts/{id}/points", response_model=PointsResponse)
async def get_points(id: str):
    if id not in points_db:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    return {"points": points_db[id]}
