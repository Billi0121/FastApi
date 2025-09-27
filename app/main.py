import uvicorn
from api.routers import router
from fastapi import FastAPI


app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)