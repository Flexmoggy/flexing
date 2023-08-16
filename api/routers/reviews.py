from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.reviews import ReviewIn, ReviewRepository, ReviewOut, Error

router = APIRouter()

@router.post("/reviews", response_model=Union[ReviewOut, Error])
def create_review(
    review: ReviewIn,
    response: Response,
    repo: ReviewRepository = Depends()
    ):
    created_review = repo.create(review)
    if isinstance(created_review, ReviewOut):
        response.status_code = 201
    else:
        response.status_code = 400
    return created_review


@router.get("/reviews", response_model=Union[Error, List[ReviewOut]])
def get_reviews(repo: ReviewRepository = Depends()):
    return repo.get_all()

@router.put("/reviews/{review_id}", response_model=Union[ReviewOut, Error])
def update_review(
    review_id: int,
    review: ReviewIn,
    repo: ReviewRepository = Depends(),
    ) -> Union[ReviewOut, Error]:
    return repo.update(review_id, review)
