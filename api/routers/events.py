from fastapi import APIRouter, Depends, Response
from queries.events import EventIn, EventOut, EventRepository, Error
from typing import Union, List


router = APIRouter()

#/event --> /events
@router.post("/events", response_model=Union[EventOut, Error])
def create_event(
    event: EventIn,
    response: Response,
    repo: EventRepository = Depends()
):
    created_event = repo.create(event)
    if isinstance(created_event, EventOut):
        response.status_code = 201
    else:
        response.status_code = 400
    return created_event


@router.get("/events", response_model=List[EventOut])
def get_all(
    repo: EventRepository = Depends(),
):
    return repo.get_all()
