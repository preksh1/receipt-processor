import uuid

def generate_receipt_id() -> str:
    return str(uuid.uuid4())
