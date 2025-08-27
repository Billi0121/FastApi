from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/math_sum/", tags=['Float Numbers 🧠'], summary='Numbers')
def math_sum(
    add : float = Query(gt=0, lt=9.99, description='You can add Float Number', title='Sum of Num'),  
):
    result = round(add, 1)
    return result

@app.get("/{name}", tags=["Greetings"])
def greetings(
    name: str
):  
    result = ' '.join([name])
    return f'Hello {result}'

if __name__ == '__main__':
    uvicorn.run('task6:app', reload=True)
