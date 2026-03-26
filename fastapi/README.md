# 🚀 AI Event Booking Backend (FastAPI)

## 📌 Overview

This is a FastAPI-based backend that simulates a **BookMyShow-like event booking system**.
It allows users to:

* View events
* Book tickets (date, time, number of people)
* Proceed to checkout

---

## 🎯 Features

* 🎟️ Event listing (Music Concert, Tech Conference)
* 📅 Date & time selection
* 👥 Number of people selection
* 💰 Dynamic pricing calculation
* 🔐 Booking ID generation
* 💳 Checkout simulation

---

## 🛠️ Tech Stack

* FastAPI
* Python 3.10+
* Uvicorn

---

## 📁 Project Structure

```
project/
│── main.py
```

---

## ▶️ Run the Server

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### 1. Get Events

```
GET /events
```

---

### 2. Book Ticket

```
POST /book
```

**Request Body:**

```json
{
  "event_id": "1",
  "date": "2026-04-01",
  "time": "18:00",
  "location": "Bangalore",
  "persons": 2,
  "user_name": "Rahul",
  "email": "rahul@email.com"
}
```

---

### 3. Checkout

```
POST /checkout/{booking_id}
```

---

## 💡 Future Improvements

* Razorpay integration
* Seat selection UI
* Email ticket (PDF)
* QR code ticket

---

## 🚀 Use Case

This backend can be used for:

* Movie booking apps
* Event ticket platforms
* AI automation agents

---

## 📄 License

For learning and development purposes.
