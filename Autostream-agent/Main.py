import json

# Load knowledge base (RAG)
with open("data.json") as f:
    data = json.load(f)

# -------- Intent Detection --------
def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in user_input for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"
    elif any(word in user_input for word in ["buy", "try", "subscribe", "start", "pro plan"]):
        return "high_intent"
    else:
        return "other"

# -------- RAG Response --------
def get_pricing():
    basic = data["pricing"]["basic"]
    pro = data["pricing"]["pro"]

    return f"""
📦 Basic Plan:
- Price: {basic['price']}
- Videos: {basic['videos']}
- Resolution: {basic['resolution']}

🚀 Pro Plan:
- Price: {pro['price']}
- Videos: {pro['videos']}
- Resolution: {pro['resolution']}
- Feature: {pro['features']}
"""

# -------- Tool (Lead Capture) --------
def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured successfully!")
    print(f"Name: {name}, Email: {email}, Platform: {platform}")

# -------- Chat Agent --------
def chat():
    print("🤖 AutoStream Agent: Hi! How can I help you today?")

    memory = {"name": None, "email": None, "platform": None}

    while True:
        user = input("\nUser: ")

        intent = detect_intent(user)

        # Greeting
        if intent == "greeting":
            print("Agent: Hello! Ask me about pricing or plans 😊")

        # Pricing (RAG)
        elif intent == "pricing":
            print("Agent:", get_pricing())

        # High Intent → Lead Capture Flow
        elif intent == "high_intent":
            print("Agent: Awesome! Let's get you started 🚀")

            # Ask for Name
            if not memory["name"]:
                memory["name"] = input("Agent: What's your name? ")

            # Ask for Email
            if not memory["email"]:
                memory["email"] = input("Agent: Your email? ")

            # Ask for Platform
            if not memory["platform"]:
                memory["platform"] = input("Agent: Which platform do you create on? (YouTube/Instagram): ")

            # Call Tool ONLY after all details
            if all(memory.values()):
                mock_lead_capture(
                    memory["name"],
                    memory["email"],
                    memory["platform"]
                )
                print("Agent: Our team will contact you soon! 🎉")
                break

        # Other
        else:
            print("Agent: I can help with pricing or getting started. What would you like to know?")

# -------- Run Program --------
if __name__ == "__main__":
    chat()
