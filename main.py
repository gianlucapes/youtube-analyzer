from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from routes.channel_retriever import router as channel_search_router

app = FastAPI()
app.include_router(channel_search_router)