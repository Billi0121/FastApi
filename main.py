from fastapi import FastAPI

app = FastAPI(docs_url='/gg')


@app.get("/")
def home_page():
    return {"Hello": "World"}

@app.get("/{name}")
def user_name(name: str):
    return {"Hello": name.capitalize()}