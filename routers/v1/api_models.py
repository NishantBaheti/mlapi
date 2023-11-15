"""
API Models
-----------
"""
from typing import Any
from pydantic import BaseModel


class Dummy(BaseModel):
    first_arg: Any
    second_arg: Any

class DummyResponse(BaseModel):
    response: str