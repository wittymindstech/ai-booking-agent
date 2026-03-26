from google.adk.agents import LlmAgent
#from google.adk.tools import tool
from uuid import uuid4

# Tool
#@tool
def book_event(event_name: str, persons: int, date: str, time: str):
    prices = {
        "music concert": 500,
        "tech conference": 1200
    }

    event_name = event_name.lower()

    if event_name not in prices:
        return {"error": "Invalid event"}

    booking_id = str(uuid4())
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


# Agent (THIS IS WHAT ADK LOOKS FOR)
root_agent = LlmAgent(
    name="booking_agent",
    model="gemini-2.0-flash",
    description="Books tickets for music concerts and tech conferences",
    instruction="""
You are a smart booking assistant.

Collect:
- event (music concert or tech conference)
- number of persons
- date
- time

Then call the tool book_event.

Always respond with booking details and payment link.
""",
    tools=[book_event]
)
