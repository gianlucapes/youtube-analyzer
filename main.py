from fastapi import FastAPI,APIRouter
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
router = APIRouter()