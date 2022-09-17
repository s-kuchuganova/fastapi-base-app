from fastapi import FastAPI

from app.routers import router

app = FastAPI()
@app.get('/')
def hello():
    return {'hello': 'Sveta'}
# app.include_router(router)
