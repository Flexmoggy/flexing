from fastapi import APIRouter
from queries.events import EventIn


router = APIRouter()


@router.post("/event")
def create_event(event: EventIn):
    print('event', event)
    return event
