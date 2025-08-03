from fastapi import APIRouter
import requests
from config import settings
from db import neo4jService
from entities.video import Video
import json


router = APIRouter()

@router.get("/video/search",tags=["video"])
async def search_video_by_name(channelId: str,max_results : int = 5):
    params = {
    "part": "snippet,id",
    "channelId":channelId,
    "maxResults":max_results,
    "order":"date",
    "type": "video",
    "key": settings.API_KEY_YOUTUBE_DEV
    }
    url = "https://www.googleapis.com/youtube/v3/search"
    try:
        response = requests.get(url, params=params)
        videos=[]
        video={}
        for item in response.json()["items"]:
            video["videoId"] = item["id"]["videoId"]
            video["publishedAt"] = item["snippet"]["publishedAt"]
            video["title"] = item["snippet"]["title"]
            video["description"]  = item["snippet"]["description"]
            video["thumb_url"]  = item["snippet"]["thumbnails"]["high"]["url"]
            videos.append(video)
            video={}
        return [Video(**item) for item in videos]
    except Exception as e:
        raise e

@router.post("/video/insert",tags=["video"])
def insert_video(video: Video):
    try:
        neo4jService.run_query("""
        MERGE (c:Video {
            publishedAt: $publishedAt,
            videoId: $videoId,
            title: $title,
            description: $description,
            thumb_url: $thumb_url
        })
        """,video.model_dump())
        return {"msg": "Video node created", "video": video}
    except Exception as e:
        raise e