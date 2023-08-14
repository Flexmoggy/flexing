from pydantic import BaseModel
from typing import Optional
from queries.pool import pool


class Error(BaseModel):
    message: str


class ProfileIn(BaseModel):
    username: str
    picture_url: Optional[str]
    first_name: str
    last_name: str
    email: str
    skills: Optional[str]
    interests: Optional[str]
    bio: Optional[str]


class ProfileOut(BaseModel):
    id: int
    username: str
    picture_url: Optional[str]
    first_name: str
    last_name: str
    email: str
    skills: Optional[str]
    interests: Optional[str]
    bio: Optional[str]


class ProfileRepository:
    def create(self, profile: ProfileIn) -> ProfileOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO profile
                    (
                        username,
                        picture_url,
                        first_name,
                        last_name,
                        email,
                        skills,
                        interests,
                        bio
                    )
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                     profile.username,
                     profile.picture_url,
                     profile.first_name,
                     profile.last_name,
                     profile.email,
                     profile.skills,
                     profile.interests,
                     profile.bio,
                     ]
                )

                id = result.fetchone()[0]
                data = profile.dict()
                #return {"message": "Looks like something went wrong. Check the input Data and try again."}
                return ProfileOut(id=id, **data)
