from pydantic import BaseModel
from datetime import datetime
from queries.pool import pool
from typing import List, Union, Optional


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
    def get_one(self, event_id: int) -> Optional[EventOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , topic
                        , author
                        , partner
                        , paired
                        , expired
                        , created_at
                        , zoom_link
                        , category
                        FROM event
                        WHERE id = %s
                        """,
                        [event_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_event_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not find event."}

    def delete(self, event_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM event
                        WHERE id = %s
                        """,
                        [event_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(self, event_id, event: EventIn) -> Union[EventIn, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE event
                        SET topic = %s
                          , author = %s
                          , partner = %s
                          , paired = %s
                          , expired = %s
                          , created_at = %s
                          , zoom_link = %s
                          , category = %s
                        WHERE id = %s
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
                            event_id,
                        ],
                    )
                    return self.event_in_to_out(event_id, event)
        except Exception as e:
            return Error(
                message=f"Error occurred while updating 'event': {str(e)}"
            )

    def get_all(self) -> Union[Error, List[EventOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id
                        , topic
                        , author
                        , partner
                        , paired
                        , expired
                        , created_at
                        , zoom_link
                        , category
                        FROM event
                        ORDER BY created_at;
                        """
                    )
                    return [
                        self.record_to_event_out(record)
                        for record in db
                    ]
        except Exception as e:
            return Error(
                message=f"Error occurred while retrieving 'events': {str(e)}"
            )

    def create(self, event: EventIn) -> EventOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
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
                    return self.event_in_to_out(id, event)
        except Exception as e:
            return Error(
                message=f"Error occurred while creating 'event': {str(e)}"
            )

    def event_in_to_out(self, id: int, event: EventIn):
        old_data = event.dict()
        return EventOut(id=id, **old_data)

    def record_to_event_out(self, record):
        return EventOut(
            id=record[0],
            topic=record[1],
            author=record[2],
            partner=record[3],
            paired=record[4],
            expired=record[5],
            created_at=record[6],
            zoom_link=record[7],
            category=record[8],
        )
