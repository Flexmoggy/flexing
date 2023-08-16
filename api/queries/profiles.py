from pydantic import BaseModel
from typing import Optional, List, Union
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
    def update(self, profile_id: int, profile: ProfileIn) -> Union[ProfileOut, Error]:
        pass

    def get_all(self) -> Union[Error, List[ProfileOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, username, picture_url, skills, interests, bio
                        FROM profile
                        ORDER BY id;
                        """
                    )
                    result = []
                    for record in db:
                        profile = ProfileOut(
                            id=record[0],
                            username=record[1],
                            picture_url=record[2],
                            first_name=record[3],
                            last_name=record[4],
                            email=record[5],
                            skills=record[6],
                            interests=record[7],
                            bio=record[8],
                            )
                        result.append(profile)
                    return result

        except Exception as e:
            print(e)
            return {"message": "Failed to retrieve profiles"}

    def create(self, profile: ProfileIn) -> ProfileOut:
        try:
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
                    return ProfileOut(id=id, **data)
        except Exception:
            return {"message": "Looks like something went wrong. Check the input Data and try again."}
