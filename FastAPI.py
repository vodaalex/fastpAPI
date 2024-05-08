import asyncio
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import requests

app = FastAPI()


# Класс для валидации входящего JSON
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# GET route
@app.get("/index")
async def read_index():
    return {"Hello": "World"}


# POST route для обработки строк
@app.post("/string")
async def read_string(string: str):
    return {"received_string": string}


# POST route для обработки JSON
@app.post("/json")
async def read_json(item: Item):
    response = {
        "name": item.name,
        "price": item.price
    }
    if item.description:
        response["description"] = item.description
    if item.tax:
        response["total_price"] = item.price + item.tax
    return response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

