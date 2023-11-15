"""
Dummy Router
-------------
"""
from fastapi import APIRouter
from src.common import dummy
from routers.v1.api_models import Dummy, DummyResponse

router = APIRouter(prefix="/dummy", tags=["dummy endpoint"])


@router.post("/dummy")
def post_dummy(payload: Dummy) -> DummyResponse:
    data = payload.model_dump()
    res = dummy(**data)
    return {"response": res}
