from pydantic import BaseModel
from datetime import datetime

class Video(BaseModel):
    publishedAt : datetime
    title : str
    videoId : str
    description : str
    thumb_url : str
