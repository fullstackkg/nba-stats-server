from typing import Union

import nba_api
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def test():
    return {"Hello": "World"}


@app.get("/{id}")
async def getPlayerStats():
    return {}
