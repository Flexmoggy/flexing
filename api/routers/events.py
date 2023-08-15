from fastapi import APIRouter, Depends
from queries.events import EventIn, EventRepository


router = APIRouter()


@router.post("/event")
def create_event(event: EventIn):
    pass

# @router.post("/event")
# def create_event(
#     event: EventIn,
#     repo: EventRepository = Depends()
# ):
#     repo.create(event)
#     return event
