import uvicorn
from enum import Enum
from typing import Optional
from fastapi import FastAPI, Body
from schemas import Person

app = FastAPI()


@app.post('/hello')
async def greetings(
    person: Person = Body(
        ...,
        openapi_examples={   # ⚠️ this is the key in FastAPI
            "student": {
                "summary": "Student example",
                "description": "Highschool student",
                "value": {
                    "name": "Ali",
                    "surname": "Karimov",
                    "age": 16,
                    "is_staff": False,
                    "educational_level": "highschool"
                },
            },
            "professor": {
                "summary": "Professor example",
                "description": "Adult teacher",
                "value": {
                    "name": "Bilol",
                    "surname": "Gafarov",
                    "age": 35,
                    "is_staff": True,
                    "educational_level": "master"
                },
            },
        },
    )
)-> dict [str, str]:
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

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)