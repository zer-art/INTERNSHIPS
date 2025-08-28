from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from Rule_based_chatbot import simple_chatbot

app = FastAPI()

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Read and return the HTML file
    html_path = os.path.join(os.path.dirname(__file__), "chatbot.html")
    with open(html_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.post("/chat")
async def chat_endpoint(chat_message: ChatMessage):
    try:
        # Process the message using your rule-based chatbot
        response = simple_chatbot(chat_message.message)
        return {"response": response}
    except Exception as e:
        return {"response": "Sorry, I encountered an error processing your request. Please try again."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 