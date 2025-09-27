from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, root_validator

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]

app = FastAPI()

class Person(BaseModel):
    name: str
    surname: str

    @root_validator(skip_on_failure=True)
    def cheking_name(cls, values):
        surname = values['surname'].capitalize()
        checked_value = values['name'].capitalize() +' ' + surname
        if checked_value in FORBIDDEN_NAMES:
                raise ValueError('You are not that warrior!')
        return values

@app.post('/hi')
def person( character: Person ):
    result = ''.join(character.name,)
    return result

if __name__ =='__main__':
    uvicorn.run('task3:app', reload=True)