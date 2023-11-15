"""
v1 Router
----------
"""

from fastapi import APIRouter
from routers.v1 import dummy



router = APIRouter(
    prefix="/v1",
    tags=["v1"]
)

router.include_router(router=dummy.router)