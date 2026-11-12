from fastapi import APIRouter
from app.schemas.event import EventRequest

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)

@router.post("/events")
def receive_event(event: EventRequest):
    return{
        "message" : "Event received succeddfully",
        "event_id": event.event_id,
        "event_type": event.event_type,
        "status": "accepted"
    }