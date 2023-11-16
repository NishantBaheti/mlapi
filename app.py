"""
Application Module
--------------------
"""
from fastapi import FastAPI, Depends
from git import Repo

from routers import v1

try:
    __version__ = Repo(".").tags[-1]
except IndexError as e:
    __version__ = "0.0.1"

app = FastAPI(
    title="ML Api",
    summary="This is a demo api template for Machine Learning Model.",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redocs",
)

@app.get("/")
def home():
    """Home Route"""
    return {"status": "active"}

app.mount('/v1', v1.subapi)
