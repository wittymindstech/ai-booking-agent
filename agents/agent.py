from google.adk.agents import LlmAgent
import requests

# 🔧 Tool: Calls FastAPI backend
def book_event(event_name: str, persons: int, date: str, time: str):
    try:
        payload = {
            "event_name": event_name,
            "persons": persons,
            "date": date,
            "time": time
        }

        response = requests.post(
            "http://127.0.0.1:8080/book",
            json=payload,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "error": f"Backend error: {response.status_code}"
            }

        data = response.json()

        return {
            "message": "✅ Booking successful!",
            "booking_details": data
        }

    except Exception as e:
        return {
            "error": f"Failed to connect to booking service: {str(e)}"
        }


# 🤖 ADK Agent (IMPORTANT: root_agent name)
root_agent = LlmAgent(
    name="booking-agent",
    model="gemini-2.0-flash",  # or switch to OpenAI later
    description="AI agent to book event tickets via backend API",
    instruction="""
You are a smart booking assistant.

Your job:
1. Understand user request
2. Extract:
   - event_name (music concert or tech conference)
   - number of persons
   - date
   - time
3. Call the function `book_event`

Rules:
- If user input is incomplete, ask follow-up questions
- Always confirm booking details
- Always return the payment link from response
- Keep responses clear and user-friendly
""",
    tools=[book_event]
)
