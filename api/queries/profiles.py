from pydantic import BaseModel
from typing import Optional


class ProfileIn(BaseModel):
    username: str
    picture_url: Optional[str]
    first_name: str
    last_name: str
    email: str
    skills: Optional[str]
    interests: Optional[str]
    bio: Optional[str]
