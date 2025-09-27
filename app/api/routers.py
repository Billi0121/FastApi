import uvicorn
from enum import Enum
from typing import Optional
from fastapi import APIRouter, Body
from schemas.schemas import Person, Person_examples

router = APIRouter()


@router.post('/hello',tags=["Greetings"], summary="Welcome to my first Fast API work!")
def greetings(person: Person = Body(openapi_examples=Person_examples)) -> dict[str, str]:
    surnames = ' '.join(person.surname)
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()    
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.educational_level is not None:
        result += ', ' + person.educational_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result} 


@router.post('/post', tags=["Greetings"], summary="Posting")
def post():
    pass
