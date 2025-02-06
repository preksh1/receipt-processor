from typing import Dict
from app.models import Receipt

# Simulated in-memory database
receipt_db: Dict[str, Receipt] = {}
points_db: Dict[str, int] = {}
