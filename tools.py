from uuid import uuid4

def book_event(event_name: str, persons: int, date: str, time: str):
    booking_id = str(uuid4())

    prices = {
        "music concert": 500,
        "tech conference": 1200
    }

    event_name = event_name.lower()

    if event_name not in prices:
        return {"error": "Invalid event"}

    total = prices[event_name] * persons

    payment_link = f"https://rzp.io/l/YOUR_PAYMENT_LINK?booking_id={booking_id}"

    return {
        "booking_id": booking_id,
        "event": event_name,
        "persons": persons,
        "date": date,
        "time": time,
        "total": total,
        "payment_link": payment_link
    }
