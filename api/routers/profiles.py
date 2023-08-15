from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.profiles import ProfileIn, ProfileRepository, ProfileOut, Error


router = APIRouter()


@router.post("/profile", response_model=Union[ProfileOut, Error])
def create_profile(profile: ProfileIn,
                   response: Response,
                   repo: ProfileRepository = Depends()):
    response.status_code = 400
    return repo.create(profile)


@router.get("/profiles", response_model=Union[Error, List[ProfileOut]])
def get_profiles(repo: ProfileRepository = Depends()):
    return repo.get_all()
