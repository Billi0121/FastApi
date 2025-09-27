import uvicorn
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.get('/')
def hello():
    return {'Hello': 'Hello world'}
@app.post('/login')
def login(
    username: str = Form(),
    password: str = Form(),
    some_file: UploadFile = File(),
):
    some = some_file.file.read().splitlines()
    return {'username': username, 'some': some}
if __name__ == '__main__':
    uvicorn.run('form:app', reload=True, port=8001) 