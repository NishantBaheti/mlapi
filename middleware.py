"""
Middleware Module
-----------------

Middleware can be created 2 ways
    - decorator (https://fastapi.tiangolo.com/tutorial/middleware/) 
    - custom (https://www.starlette.io/middleware/#basehttpmiddleware)
"""
from typing import Optional
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from config import config

class ApiKeyAuthentication(BaseHTTPMiddleware):
    """Api Key Authentication middleware

    References
    ----------
        - https://www.starlette.io/middleware/#basehttpmiddleware
    """
    def __init__(self, app: ASGIApp, dispatch: Optional[DispatchFunction] = None) -> None:
        super().__init__(app, dispatch)
        self.api_key = config["server.auth"]["ApiKey"]

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        req_header_key = request.headers.get("X-API-Key")
        if req_header_key is None:
            return Response("Unauthorized - Missing X-API-Key in request header", 401)
        if self.api_key == req_header_key:
            response = await call_next(request)
            return response
        return Response("Unauthorization Failed", 401)
    
        

