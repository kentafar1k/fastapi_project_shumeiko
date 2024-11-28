from fastapi import FastAPI, Query, Depends
from typing import Optional, List, Dict
import uvicorn
from datetime import date, datetime
from pydantic import BaseModel

app = FastAPI()


class HotelsSearchArgs:  # чтобы не засорять функцию гет запроса
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

class SHotel(BaseModel):
    address: str
    name: str
    stars: int
    

@app.get("/hotels")
async def get_hotels(
    search_args: HotelsSearchArgs = Depends(),
) -> list[SHotel]:  # добавление валидации
    hotels = [
        {
            "address": "ул. Ленинградская 10",
            "name": "best hotel",
            "stars": 5,
        },
    ]
    return hotels

class SBooking(BaseModel):
    hotel_id: int
    date_from: date
    date_to: date

@app.post("/booking")
def add_booking(booking: SBooking):
    pass

