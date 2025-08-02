from fastapi import APIRouter
import requests
from config import settings
from db import neo4jService
from entities.video import Video
import json

router=APIRouter()

@router.post("/relationships/upload_by",tags=["relationships"])
def associate_channel_video(channelId : str, videoId:str):
    try:
        kwargs={"videoId":videoId,"channelId":channelId}
        neo4jService.run_query(
            """MATCH (a:Video {videoId: $videoId})
            MATCH (b:YoutubeChannel {channelId: $channelId})
            MERGE (a)-[:UPLOADED_BY]->(b)""",
            kwargs=kwargs
        )
    except Exception as e:
        raise e