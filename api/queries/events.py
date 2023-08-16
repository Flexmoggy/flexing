from pydantic import BaseModel
from datetime import datetime
from queries.pool import pool


class Error(BaseModel):
    message: str


class EventIn(BaseModel):
    topic: str
    author: str
    partner: str
    paired: bool
    expired: bool
    created_at: datetime
    zoom_link: str
    category: str


class EventOut(BaseModel):
    id: int
    topic: str
    author: str
    partner: str
    paired: bool
    expired: bool
    created_at: datetime
    zoom_link: str
    category: str


class EventRepository:
    def get_all(self):
        

    def create(self, event: EventIn) -> EventOut:
        # connect the database
        try:
            with pool.connection() as conn:
                # get a cursor
                with conn.cursor() as db:
                    # run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO event
                            (
                                topic,
                                author,
                                partner,
                                paired,
                                expired,
                                created_at,
                                zoom_link,
                                category
                            )
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            event.topic,
                            event.author,
                            event.partner,
                            event.paired,
                            event.expired,
                            event.created_at,
                            event.zoom_link,
                            event.category,
                        ],
                    )
                    id = result.fetchone()[0]
                    # return new data
                    old_data = event.dict()
                    return EventOut(id=id, **old_data)
        except Exception as e:
            return Error(
                message=f"Error occurred while creating 'event': {str(e)}"
            )
