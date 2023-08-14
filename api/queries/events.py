from pydantic import BaseModel
from datetime import datetime


class EventIn(BaseModel):
    topic: str
    author: str
    partner: str
    paired: bool
    expired: bool
    created_at: datetime
    zoom_link: str
    category: str
    
