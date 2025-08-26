from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
from enum import Enum
import uvicorn

app = FastAPI()


@app.get("/math_sum/")
def math_sum(
    add : list[float] = Query(gt=0, lt=9.99) 
) -> dict[str, str]:
    result = round(sum(add), 2)
    return result

if __name__ == '__main__':
    uvicorn.run('task6:app', reload=True)