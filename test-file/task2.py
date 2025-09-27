from typing import Optional
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    surname: str
    age: Optional[int]
    is_staff: bool = False

class CategoryLot(str, Enum):
    PRINTER = 'Принтеры'
    MONITOR = 'Мониторы'
    ADD_EQUIP = 'Доп. оборудование'
    INPUT_DEVICE = 'Устройства ввода'

class AuctionLot(BaseModel):
    category: CategoryLot
    name: str
    model: Optional[str]
    start_price: int = 1000
    # TODO подумать, как вложенный объект отправить.
    seller: Person

@app.post('new-lot')
def register_lot(lot: AuctionLot):
    return {'result': 'Ваша заявка зарегистрирована!'}