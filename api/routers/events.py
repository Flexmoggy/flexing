from fastapi import APIRouter, Depends, Response
from queries.events import EventIn, EventOut, EventRepository, Error
from typing import Union, List, Optional


router = APIRouter()


@router.post("/events", response_model=Union[EventOut, Error])
def create_event(
    event: EventIn, response: Response, repo: EventRepository = Depends()
):
    created_event = repo.create(event)
    if isinstance(created_event, EventOut):
        response.status_code = 201
    else:
        response.status_code = 400
    return created_event


@router.get("/events", response_model=Union[Error, List[EventOut]])
def get_all(
    repo: EventRepository = Depends(),
):
    return repo.get_all()


@router.put("/events/{event_id}", response_model=Union[EventOut, Error])
def update_event(
    event_id: int,
    event: EventIn,
    repo: EventRepository = Depends(),
) -> Union[EventOut, Error]:
    return repo.update(event_id, event)


@router.delete("/events/{event_id}", response_model=bool)
def delete_event(
    event_id: int,
    repo: EventRepository = Depends(),
) -> bool:
    return repo.delete(event_id)


@router.get("/events/{event_id}", response_model=Optional[EventOut])
def get_one_event(
    event_id: int,
    response: Response,
    repo: EventRepository = Depends(),
) -> EventOut:
    found_event = repo.get_one(event_id)
    if isinstance(found_event, EventOut):
        response.status_code = 201
    else:
        response.status_code = 404
    return found_event

