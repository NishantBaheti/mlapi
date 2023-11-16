"""
v1 Router
----------
"""

from fastapi import FastAPI
from routers.v1 import dummy
from middleware import ApiKeyAuthentication

subapi = FastAPI()
subapi.add_middleware(ApiKeyAuthentication)


subapi.include_router(router=dummy.router)
