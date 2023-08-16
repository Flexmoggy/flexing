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
    skills: Optional[str]
    interests: Optional[str]
    bio: Optional[str]


class ProfileOut(BaseModel):
    id: int
    username: str
    picture_url: Optional[str]
    first_name: str
    last_name: str
    skills: Optional[str]
    interests: Optional[str]
    bio: Optional[str]


class ProfileRepository:
    def delete(self, profile_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM profile
                        WHERE id = %s
                        """,
                        [profile_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(
        self, profile_id: int, profile: ProfileIn
    ) -> Union[ProfileOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE profile
                        SET username = %s,
                        picture_url = %s,
                        first_name = %s,
                        last_name = %s,
                        skills = %s,
                        interests = %s,
                        bio = %s

                        WHERE id = %s
                        """,
                        [
                            profile.username,
                            profile.picture_url,
                            profile.first_name,
                            profile.last_name,
                            profile.skills,
                            profile.interests,
                            profile.bio,
                            profile_id,
                        ],
                    )
                    data = profile.dict()
                    return ProfileOut(id=profile_id, **data)
        except Exception as e:
            print(e)
            return {
                "message": "Update Failed, Check the input Data and try again."
            }

    def get_all(self) -> Union[Error, List[ProfileOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                                SELECT id,
                                username,
                                picture_url,
                                first_name,
                                last_name,
                                skills,
                                interests,
                                bio

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
                            skills=record[5],
                            interests=record[6],
                            bio=record[7],
                        )
                        result.append(profile)
                    return result

        except Exception as e:
            print(e)
            return {"message": "Failed to retrieve profiles"}

    def get_one(self, profile_id: int) -> Optional[ProfileOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """SELECT id,
                            username,
                            picture_url,
                            first_name,
                            last_name,
                            skills,
                            interests,
                            bio

                            FROM profile
                            WHERE id = %s
                            """,
                        [profile_id],
                    )
                    record = result.fetchone()
                    return ProfileOut(
                        id=record[0],
                        username=record[1],
                        picture_url=record[2],
                        first_name=record[3],
                        last_name=record[4],
                        skills=record[5],
                        interests=record[6],
                        bio=record[7],
                    )
        except Exception as e:
            print(e)
            return {"message": "Sorry Couldnt Get that Profile"}

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
                                skills,
                                interests,
                                bio
                            )
                            VALUES
                                (%s, %s, %s, %s, %s, %s, %s)
                            RETURNING id;
                            """,
                        [
                            profile.username,
                            profile.picture_url,
                            profile.first_name,
                            profile.last_name,
                            profile.skills,
                            profile.interests,
                            profile.bio,
                        ],
                    )

                    id = result.fetchone()[0]
                    data = profile.dict()
                    return ProfileOut(id=id, **data)

        except Exception as e:
            print(e)
            return {
                "message": "Looks like something went wrong. Check the input Data and try again."
            }

    # def record_to_profileout(self, record):
    #     return ProfileOut(
    #         id=record[0],
    #         username=record[1],
    #         picture_url=record[2],
    #         first_name=record[3],
    #         last_name=record[4],
    #         skills=record[5],
    #         interests=record[6],
    #         bio=record[7],
    #     )
