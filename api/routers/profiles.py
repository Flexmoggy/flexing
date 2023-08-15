from fastapi import APIRouter
from queries.profiles import ProfileIn


router = APIRouter()


@router.post("/profile")
def create_profile(profile: ProfileIn):
    pass
