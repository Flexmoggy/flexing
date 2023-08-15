from pydantic import BaseModel
from datetime import datetime
from queries.pool import pool


class EventIn(BaseModel):
    topic: str
    author: str
    partner: str
    paired: bool
    expired: bool
    created_at: datetime
    zoom_link: str
    category: str


class EventRepository:
    def create(self, event: EventIn):
        # connect the database
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
                            category,
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
                        event.category
                    ],
                )
                print(result)
                # return new data
