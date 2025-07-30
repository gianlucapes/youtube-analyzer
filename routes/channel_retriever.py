from fastapi import APIRouter
import requests
import os

router = APIRouter()

@router.get("/")
async def search_channel_by_name(name: str):
    params = {
    "part": "snippet",
    "q": name,
    "type": "channel",
    "key": os.environ.get("API_KEY_YOUTUBE_DEV")
    }
    url = "https://www.googleapis.com/youtube/v3/search"
    try:
        response = requests.get(url, params=params)
        return {"message": response.json()["items"]}
    except Exception as e:
        raise e

