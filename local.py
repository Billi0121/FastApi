from enum import Enum, StrEnum, IntEnum

class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование' 


# print(Fruit(256).name)

for fr in EducationLevel:
    print(fr.value)