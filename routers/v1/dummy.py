"""
Dummy Router
-------------
"""
from fastapi import APIRouter
from src.common import dummy
from routers.v1.api_models import Dummy, DummyResponse

router = APIRouter(prefix="/dummy")


@router.get("/")
def get_dummy() -> DummyResponse:
    return {"response": "dummy"}


@router.post("/")
def post_dummy(payload: Dummy) -> DummyResponse:
    data = payload.model_dump()
    res = dummy(**data)
    return {"response": res}
