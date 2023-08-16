from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReviewIn(BaseModel):
    reviewer: int
    reviewee: int
    datetime: date
    rating: int
    review: str

class ReviewRepository:
    def create(review: ReviewIn):
        pass
