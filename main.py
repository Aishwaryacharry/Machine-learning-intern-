import json

# -------- Load knowledge base (RAG) --------
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ Error: data.json file not found!")
    data = {
        "pricing": {
            "basic": {
                "price": "₹0",
                "videos": "5/month",
                "resolution": "720p"
            },
            "pro": {
                "price": "₹499",
                "videos": "Unlimited",
                "resolution": "1080p",
                "features": "AI Editing"
            }
        }
    }

# -------- Intent Detection --------
def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in user_input for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"
    elif any(word in user_input for word in ["buy", "try", "subscribe", "start", "pro"]):
        return "high_intent"
    else:
        return "other"

# -------- RAG Response --------
def get_pricing():
    basic = data["pricing"]["basic"]
    pro = data["pricing"]["pro"]

    return f"""
📦 Basic Plan:
- Price: {basic.get('price', 'N/A')}
- Videos: {basic.get('videos', 'N/A')}
- Resolution: {basic.get('resolution', 'N/A')}

🚀 Pro Plan:
- Price: {pro.get('price', 'N/A')}
- Videos: {pro.get('videos', 'N/A')}
- Resolution: {pro.get('resolution', 'N/A')}
- Feature: {pro.get('features', 'Not Available')}
"""

# -------- Lead Capture Tool --------
def mock_lead_capture(name, email, platform):
    print("\n✅ Lead captured successfully!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")

# -------- Chat Flow --------
def chat():
    print("🤖 AutoStream Agent: Hi! How can I help you today?")

    memory = {
        "name": None,
        "email": None,
        "platform": None
    }

    while True:
        user = input("\nUser: ")
        intent = detect_intent(user)

        if intent == "greeting":
            print("Agent: Hello! You can ask about pricing or plans 😊")

        elif intent == "pricing":
            print("Agent:", get_pricing())

        elif intent == "high_intent":
            print("Agent: Great choice! Let's get you started 🚀")

            if not memory["name"]:
                memory["name"] = input("Agent: What's your name? ")

            if not memory["email"]:
                memory["email"] = input("Agent: Your email? ")

            if not memory["platform"]:
                memory["platform"] = input("Agent: Which platform do you use? (YouTube/Instagram): ")

            if all(memory.values()):
                mock_lead_capture(
                    memory["name"],
                    memory["email"],
                    memory["platform"]
                )
                print("Agent: Thank you! Our team will contact you soon 🎉")
                break

        else:
            print("Agent: I can help with pricing or getting started. Please ask 😊")

# -------- Run Program --------
if __name__ == "__main__":
    chat()
