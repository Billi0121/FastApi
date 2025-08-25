from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
from enum import Enum
import uvicorn


app = FastAPI()


class EducationLevel(str, Enum):    
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'

class Post(BaseModel):
    title: str
    description: str | None = None
    tags: float | None = None

@app.post(
    "/post/",
    tags=[EducationLevel.SECONDARY],
    summary=['Post Someting']
    )
def create_post(post: Post):
    return post

@app.get(
    "/", 
    tags=['Greetings'],
    summary='Hello!'
    )
def home_page():
    return {"Hello": "World"}
 

@app.get(
        "/{name}", 
        tags=['Greetings'], 
        summary='Welcome!',
        response_description='Full Greetings'
        )
def greetings(
        *,
        surname: str,        
        age: Optional[int] = None,
        is_staff: bool = False,
        education_level: Optional[EducationLevel] = None,
        name: str,
    ) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    # return {"Hello": name.capitalize()}
    result = ' '.join([name, surname])
    result = result.title( )
    if age is not None:
        result += ', ' + str(age)
    if is_staff:
        result += ', employee '
    if education_level:
        result += str(education_level.name)
    return {"Hello": result}


if __name__ == '__main__':
    uvicorn.run('main:app' ,reload=True)