from app.models import Receipt
import math

def calculate_points(receipt: Receipt) -> int:
    points = 0
    points += sum(c.isalnum() for c in receipt.retailer)

    total_amount = float(receipt.total)
    if total_amount.is_integer():
        points += 50


    if total_amount % 0.25 == 0:
        points += 25

    points += (len(receipt.items) // 2) * 5

    for item in receipt.items:
        desc_length = len(item.shortDescription.strip())
        if desc_length % 3 == 0:
            item_points = math.ceil(float(item.price) * 0.2)
            points += item_points

    purchase_day = int(receipt.purchaseDate.split("-")[-1])
    if purchase_day % 2 == 1:
        points += 6

    purchase_hour = int(receipt.purchaseTime.split(":")[0])
    # purchase_minute = int(receipt.purchaseTime.split(":")[1])
    if 14 <= purchase_hour < 16:
        points += 10

    return points
