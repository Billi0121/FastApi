import re
from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, Field, validator, root_validator, ConfigDict

class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'

class Person(BaseModel):
    name: str = Field(
        min_length=2, max_length=20,
        title='Full name', description='You can write in any register'
    )
    surname: Union[str, list[str]] = Field(min_length=2, max_length=50)
    age: Optional[int] = Field(None, gt=4, le=99)
    is_staff: bool = Field(False, alias='is-staff')
    educational_level: Optional[EducationLevel]
    
    @validator('name')

    def name_is_not_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError('Name cant be only with numbers')
        return value
    
    @root_validator(skip_on_failure=True)

    def cheking_utf(cls, values):
        surname = ''.join(values['surname'])
        cheked_value = values['name'] + surname
        if (re.search('[а-я]', cheked_value , re.IGNORECASE)
                and re.search('[a-z]', cheked_value, re.IGNORECASE)):
            raise ValueError(
                'Pls Do not use different languages!'
            )
        return values

Person_examples = {
        "Surname": {
            "summary": "Surname example",
            "description": "One surname request",
            "value": {
                "name": "Ali",
                "surname": "Karimov",
                "age": 16,
                "is-staff": False,
                "educational_level": "Высшее образование"
            },
        },
        "Surnames": {
            "summary": "Surnames example",
            "description": "Many surname example",
            "value": {
                "name": "Bilol",
                "surname": {"Gafa", 'Andrey'},
                "age": 35,
                "is-staff": True,
                "educational_level": "Среднее специальное образование"
            },
        },
    }   