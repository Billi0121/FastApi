from enum import Enum, StrEnum, IntEnum

class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование' 


# print(Fruit(256).name)

# for fr in EducationLevel:
#     print(fr.value)


class Fruits(Enum):
    APPLE = 256
    PEAR = 156
    BANAN = 240

print(Fruits.APPLE)
