from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY not found.")
    print("Create a .env file or set the environment variable.")
    exit()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

print("===== Gemini Chatbot =====")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    try:
        response = model.generate_content(user)
        print("Bot:", response.text)

    except Exception as e:
        print("Error:", e)