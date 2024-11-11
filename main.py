from fastapi import FastAPI, Request, WebSocket, HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from rag_service import handle_query

import os
import logging

WEBSOCKET_BASE_URL = os.getenv("WEBSOCKET_URL")
# APP_BASE_URL = os.getenv("APP_BASE_URL", "ws://127.0.0.1:8000")

# Initialize FastAPI app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@app.get("/")
def index_get(request: Request):
    """Controller serving the UI"""
    return templates.TemplateResponse("base.html", {"request": request, "websocket_url": WEBSOCKET_BASE_URL})

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    """Controller for HTTP chat communication"""
    try:
        response_text = handle_query(request.query)
        return QueryResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/ws/query")
async def websocketChannel(websocket: WebSocket):
    """Controller for webocket chat communication"""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"Received query: {data}")

            try:
                response = handle_query(data)
            except Exception as e:
                logging.error(f"Error processing query: {e}")
                response = "I'm sorry, I think there was a break in communication."

            await websocket.send_json({"response": response})

    except WebSocketDisconnect:
        logging.info("Client disconnected from WebSocket.")
    except Exception as e:
        logging.error(f"Unexpected WebSocket error: {e}")
    finally:
        await websocket.close()
        logging.info("WebSocket connection closed.")
