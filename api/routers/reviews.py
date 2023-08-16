from fastapi import APIRouter
from queries.reviews import ReviewIn


router = APIRouter()


@router.post("/reviews")
def create_profile(review: ReviewIn):
    return review
