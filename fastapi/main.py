from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from uuid import uuid4

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mock DB
events_db = [
    {
        "id": "1",
        "name": "Music Concert",
        "location": "Bangalore",
        "dates": ["2026-04-01", "2026-04-02"],
        "times": ["18:00", "21:00"],
        "price": 500
    },
    {
        "id": "2",
        "name": "Tech Conference",
        "location": "Hyderabad",
        "dates": ["2026-04-05"],
        "times": ["10:00", "14:00"],
        "price": 1200
    }
]

bookings_db = []


# 🏠 Home Page UI
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "events": events_db
    })


# 🎟️ Book Ticket
@app.post("/book", response_class=HTMLResponse)
def book(
    request: Request,
    event_id: str = Form(...),
    date: str = Form(...),
    time: str = Form(...),
    persons: int = Form(...),
    name: str = Form(...),
    email: str = Form(...)
):
    event = next((e for e in events_db if e["id"] == event_id), None)

    total = event["price"] * persons
    booking_id = str(uuid4())

    booking = {
        "booking_id": booking_id,
        "event": event["name"],
        "date": date,
        "time": time,
        "persons": persons,
        "total": total,
        "status": "CONFIRMED"
    }

    bookings_db.append(booking)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "events": events_db,
        "message": f"✅ Booking Confirmed! ID: {booking_id}",
        "booking": booking
    })
