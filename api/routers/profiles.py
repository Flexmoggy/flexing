from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.profiles import ProfileIn, ProfileRepository, ProfileOut, Error


router = APIRouter()


@router.post("/profiles", response_model=Union[ProfileOut, Error])
def create_profile(
    profile: ProfileIn, response: Response, repo: ProfileRepository = Depends()
):
    created_profile = repo.create(profile)
    if isinstance(created_profile, ProfileOut):
        response.status_code = 201
    else:
        response.status_code = 400
    return created_profile


@router.get("/profiles", response_model=Union[Error, List[ProfileOut]])
def get_profiles(repo: ProfileRepository = Depends()):
    return repo.get_all()


@router.get("/profiles/{profile_id}", response_model=Union[ProfileOut, Error])
def get_one_profile(
    profile_id: int,
    repo: ProfileRepository = Depends(),
) -> ProfileOut:
    return repo.get_one(profile_id)


@router.put("/profiles/{profile_id}", response_model=Union[ProfileOut, Error])
def update_profile(
    profile_id: int,
    profile: ProfileIn,
    repo: ProfileRepository = Depends(),
) -> Union[ProfileOut, Error]:
    return repo.update(profile_id, profile)


@router.delete("/profiles/{profile_id}", response_model=bool)
def delete_profile(
    profile_id: int,
    repo: ProfileRepository = Depends(),
) -> bool:
    return repo.delete(profile_id)
