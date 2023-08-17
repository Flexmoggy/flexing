from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool
from datetime import datetime

class Error(BaseModel):
    message: str

class ReviewIn(BaseModel):
    author: int
    reviewee: int
    date: datetime
    rating: int
    review_text: Optional[str]

class ReviewOut(BaseModel):
    id: int
    author: int
    reviewee: int
    date: datetime
    rating: int
    review_text: Optional[str]


class ReviewRepository:
    def update(self, review_id: int, review: ReviewIn) -> Union[ReviewOut, Error]:
        pass

    def get_all(self) -> Union[Error, List[ReviewOut]]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT 
                    id,
                    author,
                    reviewee,
                    date,
                    rating,
                    review_text
                    FROM review
                    ORDER BY id;
                    """
                )
                result = []
                for record in db:
                    review = ReviewOut(
                        id=record[0],
                        author=record[1],
                        reviewee=record[2],
                        date=record[3],
                        rating=record[4],
                        review_text=record[5],
                        )
                    result.append(review)
                return result

    def create(self, review: ReviewIn) -> ReviewOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO review
                    (
                        author,
                        reviewee,
                        date,
                        rating,
                        review_text
                    )
                    VALUES
                        (%s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        review.author,
                        review.reviewee,
                        review.date,
                        review.rating,
                        review.review_text
                    ],
                )

                id = result.fetchone()[0]
                data = review.dict()
                return ReviewOut(id=id, **data)



    def create(review: ReviewIn):
        pass
